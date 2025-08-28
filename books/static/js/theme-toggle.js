document.addEventListener("DOMContentLoaded", () => {
    const body = document.body;
    const nav = document.querySelector("nav");
    const toggleBtn = document.getElementById("themeToggle");

    // Load saved theme
    const savedTheme = localStorage.getItem("theme") || "light-mode";
    body.className = savedTheme;
    if (nav) nav.classList.add(savedTheme);
    if (toggleBtn) {
        toggleBtn.textContent = savedTheme === "dark-mode" ? "☀️" : "🌙";
        toggleBtn.addEventListener("click", () => {
            const newTheme = body.classList.contains("light-mode") ? "dark-mode" : "light-mode";
            body.className = newTheme;
            if (nav) nav.className = "navbar navbar-expand-lg navbar-dark " + newTheme;
            toggleBtn.textContent = newTheme === "dark-mode" ? "☀️" : "🌙";
            localStorage.setItem("theme", newTheme);
        });
    }
});
