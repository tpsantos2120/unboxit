import Fetch from "./fetch.js";
import Load from "./viewResultDetails.js";
import Spinner from "./userFeedback.js";

/**
 * Validate search form and perform search upon validation.
 */
$(document).ready(function () {
  $("#search-form").validate({
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
      form.reset();
      event.target.classList.remove("uk-position-center-right")
      event.target.classList.remove("uk-position-center-left")
      const type = document.querySelector("#tabs > li.uk-active > a");
      const query = document.querySelector("#search");
      if (type.innerText == "MOVIES") {
        Spinner.userFeedback("Please wait whilst we search our books!", "#user-message");
        Spinner.startSpinner("#spinner");
        Spinner.showModal("#user-feedback");
        searchMovie(query.value);
        query.value = "";
      } else {
        Spinner.userFeedback("Please wait whilst we search our books!", "#user-message");
        Spinner.startSpinner("#spinner");
        Spinner.showModal("#user-feedback");
        searchShow(query.value);
        query.value = "";
      }
      form.reset();
    },
  });
});
/**
 * Query for shows and execute modal spinner.
 * 
 * @param {String} query 
 */
async function searchShow(query) {
  const response = await Fetch.get("/search/shows/", query);
  if (response.status === 400) {
    Spinner.stopSpinner("#spinner");
    Spinner.userFeedback("Sorry we could not find what you searched!", "#user-message");
    setTimeout(() => {
      Spinner.hideModal("#user-feedback");
    }, 1000);
  } else {
    const viewResults = document.querySelector("#view-results");
    removeChildrenEl(viewResults);
    viewResults.classList.add("uk-margin-large-top");
    viewResults.innerHTML = response;
    Load.searchDetails();
    Spinner.hideModal("#user-feedback");
  }
}

/**
 * Query for shows and execute modal spinner
 * 
 * @param {String} query 
 */
async function searchMovie(query) {
  const response = await Fetch.get("/search/movies/", query);
  if (response.status === 400) {
    Spinner.stopSpinner("#spinner");
    Spinner.userFeedback("Sorry we could not find what you searched!", "#user-message");
    setTimeout(() => {
      Spinner.hideModal("#user-feedback");
    }, 1000);
  } else {
    const viewResults = document.querySelector("#view-results");
    removeChildrenEl(viewResults);
    viewResults.classList.add("uk-margin-large-top");
    viewResults.innerHTML = response;
    Load.searchDetails();
    Spinner.hideModal("#user-feedback");
  }
}

/**
 * Remove search results just before appending more results,
 * if the search happens again.
 * 
 * @param {Object} node 
 */
const removeChildrenEl = (node) => {
  while (node.firstChild) {
    node.removeChild(node.lastChild);
  }
};
/**
 * Perform modal spinner when clicking on dashbaord navbar link.
 */
const handleDashboardSearch = () => {
  Spinner.userFeedback("Please, wait whilst we load the truck.", "#user-message");
  Spinner.startSpinner("#spinner");
  Spinner.showModal("#user-feedback");
};

const dashboardEl = document.querySelector("#dashboard");
if (dashboardEl) {
  dashboardEl.addEventListener("click", handleDashboardSearch);
}

/**
 * Watch when window is ready, hide modal spinner.
 */
const handleWindow = () => {
  Spinner.hideModal("#spinner");
};

window.onload = handleWindow;
