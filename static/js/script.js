window.addEventListener("scroll", () => {
    const nav = document.querySelector("header");
    if (window.scrollY > 10) {
      nav.style.boxShadow = "0 2px 10px rgba(0, 0, 0, 0.5)";
    } else {
      nav.style.boxShadow = "none";
    }
  });
  