function getMediaCheck() {
    var test = $(".media-test").css("width");
    if (test == '1px') {
      return 'sm';
    }
    if (test == '2px') {
      return 'md';
    }
    if (test == '3px') {
      return 'lg';
    }
    if (test == '4px') {
      return 'xl';
    }
    return 'none';
}