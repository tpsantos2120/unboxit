import Fetch from "./fetch.js";
import Spinner from "./userFeedback.js";

$(document).ready(function () {
  $("#login-form").validate({
    errorClass: "uk-form-danger",
    validClass: "uk-form-success",
    success: "uk-form-success",
    focusInvalid: false,
    focusCleanup: true,
    rules: {
      loginEmail: {
        required: true,
        email: true,
      },
      loginPassword: {
        required: true,
        minlength: 8,
      },
    },
    messages: {
      loginEmail: {
        required: "Please enter your email.",
      },
      loginPassword: {
        required: "Please enter your password.",
      },
    },
    submitHandler: function (form, event) {
      event.preventDefault();
      const email = document.querySelector("#loginEmail");
      const password = document.querySelector("#loginPassword");
      loginUser(email, password);
    },
  });
});

async function loginUser(email, password) {
  const loginResponse = await Fetch.create("/api/auth/login", {
    email: email.value,
    password: password.value,
  });
  if (loginResponse.status === 200) {
    Spinner.userFeedback(
      "Please, wait whilst we load the truck.",
      "#user-message"
    );
    Spinner.startSpinner("#spinner");
    Spinner.showModal("#user-feedback");
    window.location.replace("/dashboard");
    Spinner.hideModal("#user-feedback");
  } else {
    const validator = $("#login-form").validate();
    validator.showErrors({
      loginEmail: "Email is not valid.",
      loginPassword: "Password is not valid.",
    });
  }
}
