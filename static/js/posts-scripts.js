$('a.vote-link').on('click', function (e) {
  e.preventDefault();
  var direction = $(this).attr('data-direction');
  var id = $(this).attr('data-db-id');
  var votesSelector = $('h2[data-votes-id=' + id + ']');
  var request_url = "/post/" + id + "/vote/" + direction;

  $.ajax({
    type: "POST",
    url: request_url,
    dataType: "json",
    success: function (data) {
      if (data.success) {
        var votes = data.votes;
        votesSelector.text(votes);
      } else {
        alert("Something gone wrong.")
      }
    }
  });
});

function getCookie(name) {
    var cookieValue = null;
    var i = 0;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (i; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
