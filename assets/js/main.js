/* AgentEdge — minimal progressive enhancement. No storage, no dependencies. */
(function () {
  "use strict";

  // Footer year
  var year = document.getElementById("year");
  if (year) year.textContent = String(new Date().getFullYear());

  // Header shadow on scroll
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("is-scrolled", window.scrollY > 8);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  // Accessible mobile nav toggle
  var toggle = document.querySelector(".nav-toggle");
  var links = document.getElementById("nav-links");
  if (toggle && links) {
    var setOpen = function (open) {
      links.classList.toggle("is-open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    };
    toggle.addEventListener("click", function () {
      setOpen(toggle.getAttribute("aria-expanded") !== "true");
    });
    // Close when a link is chosen
    links.addEventListener("click", function (e) {
      if (e.target.closest("a")) setOpen(false);
    });
    // Close on Escape
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") setOpen(false);
    });
    // Close when clicking outside the nav
    document.addEventListener("click", function (e) {
      if (!e.target.closest(".nav")) setOpen(false);
    });
  }
})();
