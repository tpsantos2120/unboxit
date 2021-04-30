import Fetch from "./fetch.js";
import Spinner from "./userFeedback.js";

const handleDashboardLoading = () => {
  Spinner.userFeedback(
    "Please, wait whilst we load the truck.",
    "#dashboard-message"
  );
  Spinner.startSpinner("#dashboard-spinner");
  Spinner.showModal("#dashboard-feedback");
};

const dashboard = document.querySelector("#dashboard");
const dashboardSerch = document.querySelector("#dashboard-search");

if (dashboard) {
  dashboard.addEventListener("click", handleDashboardLoading);
  dashboardSerch.addEventListener("click", handleDashboardLoading);
}

const handleWindow = () => {
  Spinner.hideModal("#dashboard-feedback");
};

window.onload = handleWindow;

const handleDelete = async (e) => {
  handleDashboardLoading();
  const id = e.target.getAttribute("imdb");
  const deleteResponse = await Fetch.remove("/api/watchlist/", id);
  console.log(deleteResponse);
  if (deleteResponse.status === 200) {
    window.location.replace("/dashboard");
    handleWindow();
  }
};

document.querySelectorAll(".delete").forEach((item) => {
  item.onclick = handleDelete;
});

const handleReview = async (e) => {
  const id = e.target.getAttribute("imdb");
  const review = document.querySelector("#review");
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
      review: {
        required: true,
      },
    },
    messages: {
      review: {
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
      }
    },
  });
};

document.querySelectorAll(".review").forEach((item) => {
  item.onclick = handleReview;
});
