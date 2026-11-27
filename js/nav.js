document.addEventListener("DOMContentLoaded", function() {
  const toggle = document.querySelector(".mobile-toggle");
  const drawer = document.querySelector(".mobile-menu-drawer");
  if (toggle && drawer) {
    toggle.addEventListener("click", function(e) {
      e.stopPropagation();
      drawer.classList.toggle("is-open");
    });
    drawer.querySelectorAll("a").forEach(function(link) {
      link.addEventListener("click", function() {
        drawer.classList.remove("is-open");
      });
    });
    document.addEventListener("click", function(e) {
      if (!drawer.contains(e.target) && !toggle.contains(e.target)) {
        drawer.classList.remove("is-open");
      }
    });
  }
});
