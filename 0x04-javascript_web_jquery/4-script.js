$('header').addClass('green');
$('DIV#toggle_header').on('click', function () {
  if ($('header').hasClass('green')) {
    $('header').removeClass('green');
  } else {
    $('header').addClass('green');
  }
  if ($('header').hasClass('red')) {
    $('header').removeClass('red');
  } else {
    $('header').addClass('red');
  }
});
