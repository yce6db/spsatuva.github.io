function clearToggledHeaders() {
    /* Deactivate toggled elements */
    $(".header__toggled").children(".header__links-wrapper").css("display", "none");
    $(".header__toggled").removeClass("header__toggled");

    /* Make all arrows down */
    $('.header__link').find('.arrow').removeClass("up down");
    $('.header__link').find('.arrow').addClass("down");
}

$('.header__item').click(function() {
    var is_toggled = this.className.includes("header__toggled");
    clearToggledHeaders();
    /* Compute child id */
    var child_id = this.id.replace("_parent", "_child");
    /* If child element exists */
    if ($("#" + child_id).length) {
        if (is_toggled) {
            /* Set parent as inactive */
            $(this).removeClass("header__toggled");
            /* Hide child */
            $("#" + child_id).css("display", "none");
            /* Flip indicator arrow */
            $(this).find(".arrow").removeClass("up down");
            $(this).find(".arrow").addClass("down");
        } else {
            /* Set parent as active */
            $(this).addClass("header__toggled");
            /* Show child */
            $("#" + child_id).css("display", "block");
            $("#" + child_id).css("height", "auto");
            /* Flip indicator arrow */
            $(this).find(".arrow").removeClass("up down");
            $(this).find(".arrow").addClass("up");
        }
    }
});

/* Click anywhere to close dropdowns */
$('html').click(function() {
    clearToggledHeaders()
});

/* If clicking on an actual dropdown, don't close */
$('.header__item').click(function(event) {
    event.stopPropagation();
});
