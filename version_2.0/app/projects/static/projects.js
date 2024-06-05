
function toggleSection(id) {
    var container = document.getElementById(id);
    var toggleButton = container.querySelector(".show-more i");
    if (container.classList.contains("preview")) {
        container.classList.remove("preview");
        container.classList.add("full");
        toggleButton.classList.remove("fa-circle-down");
        toggleButton.classList.add("fa-circle-up");
        toggleButton.innerHTML = ' Show Less';
    } else {
        container.classList.remove("full");
        container.classList.add("preview");
        toggleButton.classList.remove("fa-circle-up");
        toggleButton.classList.add("fa-circle-down");
        toggleButton.innerHTML = ' Show More';
    }
}



function showResultsSection() {
    document.getElementById('results-section').style.display = 'flex';
}







