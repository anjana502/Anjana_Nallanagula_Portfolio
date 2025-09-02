const hamburger = document.getElementById('hamburger');
const menu = document.querySelector('.menu');
hamburger.addEventListener('click', function () {
    const hamIcon = this.querySelector('.hamburger-icon');
    const crossIcon = this.querySelector('.cross-icon');
    if (hamIcon.style.display === "none") {
        hamIcon.style.display = "inline-block"
        menu.style.display = "none"
        crossIcon.style.display = "none"
    }
    else {
        crossIcon.style.display = "inline-block"
        hamIcon.style.display = "none"
        menu.style.display = "block"
    }
});

document.addEventListener("DOMContentLoaded", function() {
  var typed = new Typed("#typed", {
    strings: [
        "Computer Science Graduate Student",
        "Software Engineer",
        "AWS Certified Developer-Associate",
        "Machine Learning Practitioner"
    ],
    typeSpeed: 80,
    backSpeed: 50,
    backDelay: 1000,
    loop: true
  });
});