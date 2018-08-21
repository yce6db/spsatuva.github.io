function resizeImages() {
  var doc_width = $( document ).width();
  if ( getMediaCheck() === 'sm' ) {
    $(".full-width-img").each(function() {
      if ($(this).is(":visible") && $(this).parent().is(":visible")) {
        /* Reset width */
        $(this).parent().css("width", "100%");
        $(this).parent().css("margin-left", "0%");
        /* Compute required width to match screen width */
        var width = $(this).width();
        /* A little extra for no reason at all */
        var scale = 100. * doc_width / width + 2.;
        var margin = ( scale - 100. ) / 2. + 1;
        $(this).parent().css("width", scale.toString() + "%");
        $(this).parent().css("margin-left", "-" + margin.toString() + "%");
        $(this).css("max-height", "400px");
        $(this).css("object-fit", "cover");
        $('.site__content').css("overflow", "hidden");
      }
    });
  } else {
    $(".full-width-img").each(function() {
      /* Reset width */
      $(this).parent().css("width", "100%");
      $(this).parent().css("margin-left", "0%");
      $(this).css("max-height", "");
      $('.site__content').css("overflow", "");
    });
  }  
}

$( document ).ready(function() {
  resizeImages();
});

$( window ).resize(function() {
  resizeImages();
});

$('.collapse').on('shown.bs.collapse', function() {
    resizeImages();
});