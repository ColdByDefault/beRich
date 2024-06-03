document.addEventListener("DOMContentLoaded", function() {
    var sections = document.querySelectorAll("h2");

    sections.forEach(function(section) {
        section.addEventListener("click", function() {
            var content = this.nextElementSibling;
            if (content.style.display === "block") {
                content.style.display = "none";
            } else {
                content.style.display = "block";
            }
        });
    });
});
