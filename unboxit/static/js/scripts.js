/**
 * Handles search form.
 */

$(function () {
  let typingTimer,
    doneTypingInterval = 2000,
    $input = $("#search-input");

  $input.on("keyup", function () {
    clearTimeout(typingTimer);
    typingTimer = setTimeout(doneTyping, doneTypingInterval);
  });

  $input.on("keydown", function () {
    clearTimeout(typingTimer);
  });

  function doneTyping() {
    const userInput = getUserInput();
    if (userInput.type == "TV Shows") {
      searchTvShows(userInput);
    } else if (userInput.type == "Movies") {
      searchMovies(userInput);
    }
    $("#search-input").val("");
  }

  function getUserInput() {
    let query = $("#search-input").val();
    let type = $("#tabs").find("li.uk-active").text();
    query = query.replace(" ", "+");
    return (userInput = { type: type, query: query });
  }

  function searchMovies(userInput) {
    var url = "/search/movies/" + userInput.query;
    startSpinner();
    $.ajax({
      url: url,
      type: "get",
      success: function (response) {
        endSpinner();
        $("#result").html(response);
        getResultDetails();
        console.log(response);
      },
      error: function (error) {
        console.log(error);
      },
    });
  }

  function searchTvShows(userInput) {
    var url = "search/tv-shows/" + userInput.query;
    $.ajax({
      url: url,
      type: "get",
      success: function (response) {
        $("#result").html(response);
        endSpinner();
        console.log(response);
      },
      error: function (error) {
        endSpinner();
        console.log(error);
      },
    });
  }
  function startSpinner() {
    $("#spinner").attr("uk-spinner", "");
    $("#user-message").text(
      "Please, bear with us a moment whilst we are searching our books!"
    );
    UIkit.modal("#user-feedback").show();
  }
  function endSpinner() {
    UIkit.modal("#user-feedback").hide();
  }
});

// $("#result-full-details").append(response);
//           $(".uk-background-cover").css(
//             "background-image",
//             "url(" + image + ")"
//           );
//           UIkit.modal("#view-details-modal").show();
//           $(".close-details-modal").click(function () {
//             $("#view-details-modal").remove();
//             $("#modal-media-youtube").remove();
//           });
//           $(".close-video-modal").click(function () {
//             $("#view-details-modal").remove();
//             $("#modal-media-youtube").remove();
//           });
/**
 * Results Function to display movies details
 */
function getResultDetails() {
  $(".results").bind("click", function (e) {
    const imdbID = $(e.target).attr("imdb");
    const type = $(e.target).attr("type");
    const image = $(e.target).attr("data-src");
    if (type == "movies") {
      var url = "/search/movie-details/" + imdbID;
      $.ajax({
        url: url,
        type: "get",
        success: function (response) {
          $("#result-full-details").append(response);
          $(".uk-background-cover").css(
            "background-image",
            "url(" + image + ")"
          );
          UIkit.modal("#view-details-modal").show();
          $(".close-details-modal").click(function () {
            $("#view-details-modal").remove();
            $("#modal-media-youtube").remove();
          });
          $(".close-video-modal").click(function () {
            $("#view-details-modal").remove();
            $("#modal-media-youtube").remove();
          });
        },
        error: function (error) {
          console.log(error);
        },
      });
    } else if (type == "tvshows") {
      var url = "/search/show-details/" + imdbID;
      $.ajax({
        url: url,
        type: "get",
        success: function (response) {
          $("#result-full-details").append(response);
          $(".uk-background-cover").css(
            "background-image",
            "url(" + image + ")"
          );
          UIkit.modal("#view-details-modal").show();
          $(".close-details-modal").click(function () {
            $("#view-details-modal").remove();
            $("#modal-media-youtube").remove();
          });
          $(".close-video-modal").click(function () {
            $("#view-details-modal").remove();
            $("#modal-media-youtube").remove();
          });
        },
        error: function (error) {
          console.log(error);
        },
      });
    }
    function userFeedback(userFeedback) {
      UIkit.notification({
        message: userFeedback.message || userFeedback.responseJSON.message,
        status: userFeedback.message ? "success" : "warning",
        pos: "top-center",
        timeout: 5000,
      });
    }
  });
};
/**
 * Function to login user.
 */
$(function () {
  $('#login-button').bind('click', function() {
    const email = $("#login-email").val();
    const password = $("#login-password").val();
    const url = "/api/auth/login"
    $.ajax({
      url: url,
      type: "post",
      data: {email:email, password:password},
      success: function (response) {
        window.location.replace("/dashboard")
      },
      error: function (error) {
        if (error.status == 401){
          $("#login-email").addClass("uk-form-danger");
          $("#login-password").addClass("uk-form-danger");
        }
      },
    });
  });
  // function userFeedback(userFeedback){
  //   UIkit.notification({
  //         message: userFeedback.message || userFeedback.responseJSON.message,
  //         status: userFeedback.message ? "success" : "warning",
  //         pos: "top-center",
  //         timeout: 5000,
  //       });
  // }
});
/**
 * Registration Function
 */
$(function () {
  $('#register-button').bind('click', function() {
    const firstName = $("#firstname").val();
    const lastName = $("#lastname").val();
    const username = $("#username").val();
    const email = $("#email").val();
    const password = $("#password").val();
    const url = "/api/auth/register"

    console.log(username,lastName, email)
    $.ajax({
      url: url,
      type: "post",
      data: {email:email, password:password, first_name:firstName
        , last_name:lastName, username:username},
      success: function (response) {
        window.location.replace("/dashboard")
      },
      error: function (error) {
        if (error.status == 401){
          $("#firstname").addClass("uk-form-danger");
          $("#lastname").addClass("uk-form-danger");
          $("#username").addClass("uk-form-danger");
          $("#email").addClass("uk-form-danger");
          $("#password").addClass("uk-form-danger");
        }
      },
    });
  });
  // function userFeedback(userFeedback){
  //   UIkit.notification({
  //         message: userFeedback.message || userFeedback.responseJSON.message,
  //         status: userFeedback.message ? "success" : "warning",
  //         pos: "top-center",
  //         timeout: 5000,
  //       });
  // }
});