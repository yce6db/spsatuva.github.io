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

$('.collapse-list-heading').click(function() {
    var arrow_down = $(this).children('.arrow').attr('class').includes('down');
    /* Flip arrows down of self and siblings in same list */
    $(this).children('.arrow').removeClass('up down');
    $(this).children('.arrow').addClass('down');
    $(this).siblings('.collapse-list-heading').children('.arrow').removeClass('up down');
    $(this).siblings('.collapse-list-heading').children('.arrow').addClass('down');
    /* Flip own arrow if was already down */
    if (arrow_down) {
    $(this).children('.arrow').removeClass('up down');
    $(this).children('.arrow').addClass('up');
    }
});

$(document).ready(function() {
    $("body").removeClass("preload");
});