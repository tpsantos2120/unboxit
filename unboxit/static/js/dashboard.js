import Fetch from "./fetch.js";
import Spinner from "./userFeedback.js";


/**
 * load user feedback modal to let user know
 * we are searching.
 */
const handleDashboardLoading = () => {
  Spinner.userFeedback(
    "Please, wait whilst we load the truck.",
    "#dashboard-message"
  );
  Spinner.startSpinner("#dashboard-spinner");
  Spinner.showModal("#dashboard-feedback");
};


const dashboard = document.querySelector("#dashboard");
const dashboardSearch = document.querySelector("#dashboard-search");

if (dashboard && dashboardSearch) {
  dashboard.addEventListener("click", handleDashboardLoading);
  dashboardSearch.addEventListener("click", handleDashboardLoading);
}

/**
 * Listens for window when is fully loaded then hide feedback modal.
 */
const handleWindow = () => {
  Spinner.hideModal("#dashboard-feedback");
};

window.onload = handleWindow;


const handleDelete = async (e) => {
  e.target.setAttribute("disabled","");
  handleDashboardLoading();
  const id = e.target.getAttribute("imdb");
  const deleteResponse = await Fetch.remove("/api/watchlist/", id);
  if (deleteResponse.status === 200) {
    window.location.replace("/dashboard");
  } else {
    UIkit.notification({
      message: "Ops! It could not delete it.",
      status: "success",
      pos: "top-center",
      timeout: 5000,
    });
  }
};

document.querySelectorAll(".delete").forEach((item) => {
  item.onclick = handleDelete;
});

/**
 * Query DB for existing review if there is any append to form
 * Validate review form, once validation is ok perform submit.
 * 
 * @param {Event} e 
 */
const handleReview = async (e) => {
  const id = e.target.getAttribute("imdb");
  const review = document.querySelector("#reviewTextArea");
  const existReview = await Fetch.get("/api/watchlist/" + id);
  if (existReview.review) {
    review.value = existReview.review;
  }

  $("#review-form").validate({
    errorClass: "uk-form-danger",
    validClass: "uk-form-success",
    success: "uk-form-success",
    focusInvalid: false,
    focusCleanup: true,
    rules: {
      reviewTextArea: {
        required: true,
      },
    },
    messages: {
      reviewTextArea: {
        required: "Please write a review.",
      },
    },
    submitHandler: async function (form, event) {
      event.preventDefault();
      handleDashboardLoading();
      const reviewResponse = await Fetch.update("/api/watchlist/" + id, {
        review: review.value,
      });
      if (reviewResponse.status === 200) {
        window.location.replace("/dashboard");
        handleWindow();
      } else {
        UIkit.notification({
          message: "Ops! It could not update review.",
          status: "success",
          pos: "top-center",
          timeout: 5000,
        });
      }
      form.reset();
    },
  });
};

document.querySelectorAll(".review").forEach((item) => {
  item.onclick = handleReview;
});
