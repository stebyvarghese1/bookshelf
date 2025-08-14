/* Minimal PDF.js viewer with page "turn" feel and AI emotion TTS via Web Speech API */
const pdfjsLib = window['pdfjs-dist/build/pdf'];
pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/4.5.136/pdf.worker.min.js';

const container = document.getElementById('viewerContainer');
let pdfDoc = null;

async function loadPdf(url) {
  const loadingTask = pdfjsLib.getDocument(url);
  pdfDoc = await loadingTask.promise;

  for (let pageNum = 1; pageNum <= pdfDoc.numPages; pageNum++) {
    const page = await pdfDoc.getPage(pageNum);
    const viewport = page.getViewport({scale: 1.2});
    const canvas = document.createElement('canvas');
    canvas.width = viewport.width;
    canvas.height = viewport.height;
    canvas.className = 'pdf-page';
    const ctx = canvas.getContext('2d');

    const renderContext = { canvasContext: ctx, viewport };
    await page.render(renderContext).promise;
    container.appendChild(canvas);

    // Simple page-turn effect on click/drag
    canvas.addEventListener('mousedown', () => canvas.classList.add('turning'));
    canvas.addEventListener('mouseup', () => canvas.classList.remove('turning'));
    canvas.addEventListener('mouseleave', () => canvas.classList.remove('turning'));
  }
}

function getSelectedText() {
  // Selection only works if text is selectable (canvas isn't selectable),
  // so fallback to extracted text from server.
  return window.getSelection().toString().trim();
}

// Emotion TTS
const emotionStatus = document.getElementById('emotionStatus');

function emotionToVoiceTweaks(emotion) {
  // Basic mapping to pitch/rate
  switch (emotion) {
    case 'joy':   return { pitch: 1.3, rate: 1.08 };
    case 'sad':   return { pitch: 0.8, rate: 0.9 };
    case 'anger': return { pitch: 0.9, rate: 1.1 };
    case 'fear':  return { pitch: 1.1, rate: 1.0 };
    default:      return { pitch: 1.0, rate: 1.0 };
  }
}

function speakSentencesWithEmotion(items) {
  window.speechSynthesis.cancel();
  for (const {sentence, emotion} of items) {
    const u = new SpeechSynthesisUtterance(sentence);
    const { pitch, rate } = emotionToVoiceTweaks(emotion);
    u.pitch = pitch;
    u.rate  = rate;
    u.onstart = () => emotionStatus.textContent = `Speaking (${emotion}) …`;
    u.onend   = () => emotionStatus.textContent = '';
    window.speechSynthesis.speak(u);
  }
}

async function analyzeAndSpeak(text) {
  if (!text) return;
  const res = await fetch('/api/analyze_emotions', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ text })
  });
  const data = await res.json();
  if (Array.isArray(data)) {
    speakSentencesWithEmotion(data);
  }
}

async function readSelection() {
  const sel = getSelectedText();
  if (sel) {
    analyzeAndSpeak(sel);
  } else {
    // fallback: grab extracted text from the server
    const r = await fetch(`/api/extract_text/${BOOK_ID}`);
    const j = await r.json();
    analyzeAndSpeak(j.text);
  }
}

async function readPage() {
  // For demo, just use the extracted doc text (first chunk)
  const r = await fetch(`/api/extract_text/${BOOK_ID}`);
  const j = await r.json();
  analyzeAndSpeak(j.text);
}

document.getElementById('btnReadSelection').addEventListener('click', readSelection);
document.getElementById('btnReadPage').addEventListener('click', readPage);
document.getElementById('btnStop').addEventListener('click', () => window.speechSynthesis.cancel());

loadPdf(PDF_URL);
