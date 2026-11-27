document.addEventListener("DOMContentLoaded", function() {
  const toggle = document.querySelector(".mobile-toggle");
  const drawer = document.querySelector(".mobile-menu-drawer");
  if (toggle && drawer) {
    toggle.addEventListener("click", function() {
      drawer.classList.toggle("is-open");
    });
    // Close drawer when any mobile link is clicked
    drawer.querySelectorAll("a").forEach(function(link) {
      link.addEventListener("click", function() {
        drawer.classList.remove("is-open");
      });
    });
  }
});
