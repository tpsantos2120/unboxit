function form_submit() {
  document.getElementById("login-form").submit();
  document.getElementById("register-form").submit();
  document.getElementById("search-form").submit();
}

let typingTimer,
  doneTypingInterval = 3000,
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
  apiRequestHandler((urlBuilder(getUserInput())));
}

function getUserInput() {
  const searchInput = $("#search-input").val();
  const queryType = $("#tabs").find("li.uk-active").text();
  return (userInput = { queryType: queryType, searchInput: searchInput });
}

function urlBuilder(query) {
  if (query.queryType && query.searchInput) {
    query.searchInput = query.searchInput.replace(" ", "+");
    console.log(query.searchInput)
    if (query.queryType == TV_SHOWS) {
      return (url = { url: QUERY_TV_SHOWS + query.searchInput, method: GET });
    } else if (query.queryType == MOVIES) {
      return (url = { url: QUERY_MOVIES + query.searchInput, method: GET });
    }
  }
}

function apiRequestHandler(query) {
  startSpinner();
  $("#search-input").val("");
  $.ajax({
    url: query.url,
    type: query.method,
    success: function (response) {
      endSpinner();
      $("#result").html(response);
    },
    error: function (error) {
      endSpinner();
      console.log(error);
    },
  });
}

function startSpinner() {
  $("#spinner").attr("uk-spinner", "");
  $("#user-message").text("Please, bear with us a moment we are searching our books!");
  UIkit.modal("#user-feedback").show();
}
function endSpinner() {
  UIkit.modal("#user-feedback").hide();
}
