import Fetch from "./fetch.js";
/**
 * Validate password change form when logged in.
 */
$(document).ready(function () {
  $("#settings-form").validate({
    errorClass: "uk-form-danger",
    validClass: "uk-form-success",
    success: "uk-form-success",
    focusInvalid: false,
    focusCleanup: true,
    rules: {
      newPassword: {
        required: true,
        minlength: 8,
      },
      repeatPassword: {
        required: true,
        minlength: 8,
      },
    },
    messages: {
      newPassword: {
        required: "Please enter your new password.",
      },
      repeatPassword: {
        required: "Please enter your repeat password.",
      },
    },
    submitHandler: function (form, event) {
      event.preventDefault();
      const newPassword = document.querySelector("#newPassword");
      const repeatPassword = document.querySelector("#repeatPassword");
      if (newPassword.value == repeatPassword.value) {
        changePassword(newPassword.value);
        console.log("matches");
      } else {
        console.log("not matches");
        const validator = $("#settings-form").validate();
        validator.showErrors({
          repeatPassword: "Password does not match.",
        });
      }
    },
  });
});

const changePassword = async (password) => {
  const passwordResponse = await Fetch.create("/api/auth/reset", {
    password: password,
  });
  if (passwordResponse.status === 200) {
    UIkit.modal("#settings-modal").hide();
    UIkit.notification({
      message: "Your password has been changed successfully.",
      status: "success",
      pos: "top-center",
      timeout: 5000,
    });
  }
};
/**
 * Validate email to send password reset request, and
 * send email to user with a reset link, when logged out.
 */
$(document).ready(function () {
  $("#reset-modal-form").validate({
    errorClass: "uk-form-danger",
    validClass: "uk-form-success",
    success: "uk-form-success",
    focusInvalid: false,
    focusCleanup: true,
    rules: {
      resetEmail: {
        required: true,
        email: true,
      },
    },
    messages: {
      resetEmail: {
        required: "Please enter your email.",
      },
    },
    submitHandler: function (form, event) {
      event.preventDefault();
      const resetEmail = document.querySelector("#resetEmail");
      if (resetEmail.value) {
        sendResetEmail(resetEmail.value);
        console.log("matches");
      }
    },
  });
});

const sendResetEmail = async (email) => {
  const resetResponse = await Fetch.create("/api/auth/forgot", {
    email: email,
  });
  console.log(resetResponse);
  if (resetResponse === null) {
    UIkit.modal("#reset-modal").hide();
    UIkit.notification({
      message: "We have sent you a reset email.",
      status: "success",
      pos: "top-center",
      timeout: 5000,
    });
  } else if (resetResponse.status === 400) {
    const validator = $("#reset-modal-form").validate();
    validator.showErrors({
      resetEmail: "No user found with given email.",
    });
  }
};
/**
 * Email is sent to user to reset password, once clicked on reset
 * email link, a page with form will be loaded and the code below
 * will validate that form as well as perform password change.
 */
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
    "/api/auth/reset/password",
    resetPassword,
    authorization
  );
  
  if (passwordResponse === null) {
    UIkit.notification({
      message: "Your password has been changed successfully.",
      status: "success",
      pos: "top-center",
      timeout: 5000,
    });
    setTimeout(() => {
      window.location.replace("/");
    }, 5000);
  } else if (passwordResponse.status === 403) {
    const validator = $("#reset-form").validate();
    validator.showErrors({
      forgotRepeatPassword:
        "Token expired or invalid, request another reset password email.",
    });
  }
};
