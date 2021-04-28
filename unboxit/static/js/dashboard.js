import Fetch from "./fetch.js";

const userFeedback = (message) => {
  const userMessage = document.querySelector("#dashboard-message");
  if (userMessage) {
    userMessage.innerText = message;
  }
};
const startSpinner = () => {
  const spinner = document.querySelector("#dashboard-spinner");
  if (spinner) {
    spinner.setAttribute("uk-spinner", "");
  }
};
const stopSpinner = () => {
  const spinner = document.querySelector("#dashboard-spinner");
  if (spinner) {
    spinner.removeAttribute("uk-spinner", "");
  }
};

const showModal = () => {
  const dashboard = document.querySelector("#dashboard-feedback");
  if (dashboard) {
    UIkit.modal(dashboard, { bgClose: false }).show();
  }
};

const hideModal = () => {
  const dashboard = document.querySelector("#dashboard-feedback");
  if (dashboard) {
    UIkit.modal("#dashboard-feedback").hide();
  }
};

userFeedback("loading dashboard..");
startSpinner();
showModal();

const handleDelete = async (e) => {
  const id = e.target.getAttribute("imdb");
  const deleteResponse = await Fetch.remove("/api/movie/", id);
  console.log(deleteResponse);
  if (deleteResponse.status === 200) {
    window.location.replace("/dashboard");
  }
};

document.querySelectorAll(".delete").forEach((item) => {
  item.onclick = handleDelete;
});

const handleReview = async (e) => {
  const id = e.target.getAttribute("imdb");
  const review = document.querySelector("#review");
  const existReview = await Fetch.get("/api/movie/" + id);
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
      const reviewResponse = await Fetch.update("/api/movie/" + id, {
        review: review.value,
      });
      if (reviewResponse.status === 200) {
        window.location.replace("/dashboard");
      }
    },
  });
};

document.querySelectorAll(".review").forEach((item) => {
  item.onclick = handleReview;
});

const handleLoading = () => {
  hideModal();
};

window.onload = handleLoading;
