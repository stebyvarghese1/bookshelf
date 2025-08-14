// Show list of books under the form (for quick confirmation)
(async function(){
  const res = await fetch('/api/books');
  if (!res.ok) return;
  const books = await res.json();
  const el = document.getElementById('admin-books');
  if (!books.length) { el.textContent = 'No books uploaded yet.'; return; }
  el.innerHTML = books.map(b => `
    <div style="display:flex;align-items:center;gap:10px;margin:6px 0;">
      <img src="${b.cover}" alt="cover" style="width:40px;height:56px;border-radius:4px;object-fit:cover;">
      <div>
        <div><strong>${b.title}</strong></div>
        <div style="color:#9aa3b2;font-size:12px;">${b.author}</div>
      </div>
    </div>
  `).join('');
})();
