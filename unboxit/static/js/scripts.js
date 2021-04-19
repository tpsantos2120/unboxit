function form_submit() {
  document.getElementById("login-form").submit();
  document.getElementById("register-form").submit();
  document.getElementById("search-form").submit();
}

let typingTimer,
  doneTypingInterval = 2000,
  $input = $("#search-input");
const POST = "post",
  GET = "get",
  DELETE = "delete",
  PUT = "put",
  TV_SHOWS = "TV Shows",
  MOVIES = "Movies",
  QUERY_MOVIES = "/get-movies-by-title/",
  QUERY_TV_SHOWS = "/get-shows-by-title/";

$input.on("keyup", function () {
  clearTimeout(typingTimer);
  typingTimer = setTimeout(doneTyping, doneTypingInterval);
});

$input.on("keydown", function () {
  clearTimeout(typingTimer);
});

function doneTyping() {
  apiRequestHandler(urlBuilder(getUserInput()));
}

function getUserInput() {
  const searchInput = $("#search-input").val();
  const queryType = $("#tabs").find("li.uk-active").text();
  return (userInput = { queryType: queryType, searchInput: searchInput });
}

function urlBuilder(query) {
  if (query.queryType && query.searchInput) {
    query.searchInput = query.searchInput.replace(" ", "+");
    console.log(query.searchInput);
    if (query.queryType == TV_SHOWS) {
      return (url = { url: QUERY_TV_SHOWS + query.searchInput, method: GET, type:query.queryType });
    } else if (query.queryType == MOVIES) {
      return (url = { url: QUERY_MOVIES + query.searchInput, method: GET, type:query.queryType });
    }
  }
}

function apiRequestHandler(query) {
  console.log(query)

  startSpinner();
  $("#search-input").val("");
  $.ajax({
    url: query.url,
    type: query.method,
    success: function (response) {
      console.log(response)
      endSpinner();
      $("#result").html(response);
      handleEachResult(query.type);
    },
    error: function (error) {
      endSpinner();
      console.log(error);
    },
  });
}

function handleEachResult(query) {
  document.querySelectorAll(".results").forEach((item) => {
    item.addEventListener("click", (item) => {
      const id = $(item.target).attr("imdb");
      const image = $(item.target).attr("data-src");
      console.log(query)
      $.ajax({
        url: "/view-details/?id=" + id +"&type="+ query.type,
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
    });
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
