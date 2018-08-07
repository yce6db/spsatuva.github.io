function clearToggledHeaders() {
    /* Deactivate toggled elements */
    var toggled = document.querySelectorAll(".header_toggled");
    for (i = 0; i < toggled.length; i++) {
        toggled[i].className = toggled[i].className.replace(" header_toggled", "");
        /* Hide child */
        child = document.getElementById(toggled[i].id.replace("_parent", "_child"));
        child.style.display = 'none';
    }

    /* Make all arrows down */
    var arrows = document.querySelectorAll(".arrow");
    for (i = 0; i < arrows.length; i++) {
        arrows[i].className = arrows[i].className.replace("up", "down");
    }
}

function toggleHeader(e) {
    var e_toggled = e.className.includes("header_toggled");
    clearToggledHeaders();

    /* If selected header closed, open it */
    if (!e_toggled) {
        /* Show child */
        e.className += " header_toggled";
        child = document.getElementById(e.id.replace("_parent", "_child"));
        child.style.display = 'block';
        child.style.height = 'auto';
        /* Flip arrow */
        my_arrow.className = my_arrow.className.replace("down", "up");
    }
}

/* Click anywhere to close dropdowns */
$('html').click(function() {
    clearToggledHeaders()
});

/* If clicking on an actual dropdown, don't close */
$('.header__item').click(function(event) {
    event.stopPropagation();
});
