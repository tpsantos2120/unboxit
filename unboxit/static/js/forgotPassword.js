import Fetch from "./fetch.js";

$(document).ready(function () {
  $("#reset-form").validate({
    errorClass: "uk-form-danger",
    validClass: "uk-form-success",
    success: "uk-form-success",
    focusInvalid: false,
    focusCleanup: true,
    rules: {
      forgotPassword: {
        required: true,
        minlength: 8,
      },
      forgotRepeatPassword: {
        required: true,
        minlength: 8,
      },
    },
    messages: {
      forgotPassword: {
        required: "Please enter your new password.",
      },
      forgotRepeatPassword: {
        required: "Please enter your repeat password.",
      },
    },
    submitHandler: function (form, event) {
      event.preventDefault();
      const newPassword = document.querySelector("#forgotPassword");
      const repeatPassword = document.querySelector("#forgotRepeatPassword");
      if (newPassword.value == repeatPassword.value) {
        const resetButton = document.querySelector("#resetButton");
        resetButton.setAttribute("disabled", "");
        const url = window.location.href;
        const token = url.split("/").pop();
        forgottenPassword(newPassword.value, token);
      } else {
        const validator = $("#reset-form").validate();
        validator.showErrors({
          forgotRepeatPassword: "Passwords do not match.",
        });
      }
    },
  });
});

const forgottenPassword = async (password, token) => {
  const resetPassword = {
    password: password,
  };
  const authorization = "Bearer " + token;
  const passwordResponse = await Fetch.create(
    "/api/auth/reset",
    resetPassword,
    authorization
  );
  if (passwordResponse.status === 200) {
    UIkit.notification({
      message: "Your password has been changed successfully.",
      status: "success",
      pos: "top-center",
      timeout: 5000,
    });
    setTimeout(() => {
      window.location.replace("/");
    }, 5000);
  } else {
    UIkit.notification({
      message: "Please try to reset the password again.",
      status: "warning",
      pos: "top-center",
      timeout: 5000,
    });
    setTimeout(() => {
      window.location.replace("/");
    }, 5000);
  }
};
