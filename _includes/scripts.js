function toggleHeader(e) {
    /* Deactivate toggled elements */
    var toggled = document.querySelectorAll(".header_toggled");
    var e_toggled = false;
    for (i = 0; i < toggled.length; i++) {
      if (toggled[i] == e) {
        e_toggled = toggled[i].className.includes("header_toggled");
      }
      toggled[i].className = toggled[i].className.replace(" header_toggled", "");
      /* Hide child */
      child = document.getElementById(toggled[i].id.replace("_parent", "_child"));
      child.style.display = 'none';
    }

    /* Make all arrows down */
    var arrows = document.querySelectorAll(".arrow");
    var my_arrow;
    for (i = 0; i < arrows.length; i++) {
      if (arrows[i].parentElement.parentElement == e) {
        my_arrow = arrows[i];
      }
      arrows[i].className = arrows[i].className.replace("up", "down");
    }

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