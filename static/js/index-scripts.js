$('.category-list').hide();

$('.category-heading').on('click', function () {
  var this$ = $(this);
  var id = this$.attr('data-for');
  $('[data-id=' + id + ']').toggle();
});
