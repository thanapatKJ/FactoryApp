$(document).ready(() => {
  $('.btn-collapse-table').on('click', function() {
    if ($(this).find('svg').hasClass('fa-caret-down')) {
      $(this).find('svg').addClass('fa-caret-right');
      $(this).find('svg').removeClass('fa-caret-down');
    } else {
      $(this).find('svg').addClass('fa-caret-down');
      $(this).find('svg').removeClass('fa-caret-right');
    }
  });
});
