import Fetch from "./fetch.js";

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
      resetEmail: "There is a schema error problem, please contact support centre.",
    });
  } else if (resetResponse.status === 403) {
    const validator = $("#reset-modal-form").validate();
    validator.showErrors({
      resetEmail: "Token is invalid or expired, try re-sending the email.",
    });
  } else {
    const validator = $("#reset-modal-form").validate();
    validator.showErrors({
      resetEmail: "Email does not exist.",
    });
  }
};
