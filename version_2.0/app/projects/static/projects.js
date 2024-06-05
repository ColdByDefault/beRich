
/* switch between languages is disabled */
/* document.addEventListener("DOMContentLoaded", function() {
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
}); */



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

/* function submitEdits() {
    const editableNotes = document.querySelectorAll('.editable-notes');
    let notesData = {};
    editableNotes.forEach(note => {
        notesData[note.dataset.day] = note.value;
    });

    fetch('/submit-edits', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(notesData),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        alert(data.message);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
} */

function showResultsSection() {
    document.getElementById('results-section').style.display = 'flex';
}







