import fetch from "./fetch.js";

$(document).ready(function () {
  $("#search-form").validate( {
    errorClass: "uk-form-danger",
    validClass: "uk-form-success",
    success: "uk-form-success",
    focusInvalid: false,
    focusCleanup: true,
    rules: {
      search: {
        required: true,
        minlength: 3,
      },
    },
    messages: {
      search: {
        required: "Please enter a movie or show...",
      },
    },
    submitHandler: function (form, event) {
      event.preventDefault();
      const type = document.querySelector("#tabs > li.uk-active > a");
      const query = document.querySelector("#search");

      if (type.innerText == "MOVIES") {
        userFeedback("Please wait whilst we search our books!");
        startSpinner();
        showModal();
        searchMovie(query.value);
        query.value = "";
      } else {
        userFeedback("Please wait whilst we search our books!");
        startSpinner();
        showModal();
        searchShow(query.value);
        query.value = "";
      }
    },
  });
});

async function searchShow(query) {
  const response = await fetch.get("/search/shows/", query);
  if (response.status === 400) {
    stopSpinner();
    userFeedback("Sorry we could not find what you searched!");
    setTimeout(() => {
      hideModal();
    }, 1000);
  } else {
    const viewResults = document.querySelector("#view-results");
    viewResults.classList.add("uk-margin-large-top")
    viewResults.innerHTML = response;
    hideModal();
  }
}

async function searchMovie(query) {
  const response = await fetch.get("/search/movies/", query);
  if (response.status === 400) {
    stopSpinner();
    userFeedback("Sorry we could not find what you searched!");
    setTimeout(() => {
      hideModal();
    }, 1000);
  } else {
    const viewResults = document.querySelector("#view-results");
    viewResults.classList.add("uk-margin-large-top")
    viewResults.innerHTML = response;
    hideModal();
  }
}
const userFeedback = (message) => {
  const userMessage = document.querySelector("#user-message");
  userMessage.innerText = message;
};
const startSpinner = () => {
  const spinner = document.querySelector("#spinner");
  spinner.setAttribute("uk-spinner", "");
};
const stopSpinner = () => {
  const spinner = document.querySelector("#spinner");
  spinner.removeAttribute("uk-spinner", "");
};

const showModal = () => {
  UIkit.modal("#user-feedback", { bgClose: false }).show();
};

const hideModal = () => {
  UIkit.modal("#user-feedback").hide();
};
