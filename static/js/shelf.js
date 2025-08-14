// Optional: little wiggle or keyboard navigation on the shelf
document.addEventListener('keydown', (e) => {
  if (e.key.toLowerCase() === 'r') {
    document.querySelectorAll('.book').forEach((b,i) => {
      b.style.transform = 'rotateY(-12deg)';
      setTimeout(()=> b.style.transform = '', 50*i);
    });
  }
});
