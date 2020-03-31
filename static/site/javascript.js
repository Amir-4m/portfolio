$(document).ready(function () {
  $('.send-button').attr('disabled', true);

  $('input[type="text"]').on('keyup', function () {
    var text_value = $('input[name="text"]').val();
    if (text_value !== '') {
      $('.send-button').attr('disabled', false);
    } else {
      $('.send-button').attr('disabled', true);
    }
  });
});