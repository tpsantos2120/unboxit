import Fetch from "../../static/js/fetch.js";

$(document).ready(function () {
  $("#register-form").validate({
    errorClass: "uk-form-danger",
    validClass: "uk-form-success",
    success: "uk-form-success",
    focusInvalid: false,
    focusCleanup: true,
    rules: {
      firstname: {
        required: true,
        maxlength: 30,
      },
      lastname: {
        required: true,
        maxlength: 30,
      },
      username: {
        required: true,
        minlength: 8,
      },
      email: {
        required: true,
        email: true,
      },
      password: {
        required: true,

        minlength: 8,
      },
    },
    messages: {
      firstname: {
        required: "Please enter first name.",
      },
      lastname: {
        required: "Please enter last name.",
      },
      username: {
        required: "Please enter a username.",
      },
      email: {
        required: "Please enter your email.",
      },
      password: {
        required: "Please enter your password.",
      },
    },
    submitHandler: function (form, event) {
      event.preventDefault();
      const firstName = document.querySelector("#firstname");
      const lastName = document.querySelector("#lastname");
      const userName = document.querySelector("#username");
      const email = document.querySelector("#email");
      const password = document.querySelector("#password");
      registerUser(firstName, lastName, userName, email, password);
    },
  });
});

async function registerUser(firstName, lastName, userName, email, password) {
  const response = await Fetch.create("/api/auth/register", {
    first_name: firstName.value,
    last_name: lastName.value,
    username: userName.value,
    password: password.value,
    email: email.value,
  });
  console.log(response);
  if (response.status === 200) {
    window.location.replace("/dashboard");
  } else {
    const validator = $("#register-form").validate();
    validator.showErrors({
      email: "Email is already taken.",
    });
  }
}
