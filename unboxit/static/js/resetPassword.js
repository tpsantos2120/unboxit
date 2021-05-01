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
        console.log("matches")
      } else {
        console.log("not matches")
        const validator = $("#settings-form").validate();
        validator.showErrors({
          repeatPassword: "Password does not match.",
        });
      }
    },
  });
});

const changePassword = async (password) => {
  const passwordResponse = await Fetch.update("/api/auth/reset", {
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
