const registerButton = document.querySelector("#register-button");

const handleRegister = (e) => {
  const firstName = document.querySelector("#firstname");
  const lastName = document.querySelector("#lastname");
  const userName = document.querySelector("#username");
  const email = document.querySelector("#email");
  const password = document.querySelector("#password");

  if (firstName && lastName && userName && email && password) {
    registerUser(firstName, lastName, userName, email, password);
  }
  e.preventDefault();
};

registerButton.onclick = handleRegister;

async function registerUser(firstName, lastName, userName, email, password) {
  const response = await Fetch.create("/api/auth/register", {
    firstname: firstName.value,
    lastname: lastName.value,
    username: userName.value,
    password: password.value,
    email: email.value,
  });
  console.log(response);
  if (response.status === 200) {
    window.location.replace("/dashboard");
  } else {
    const alert = document.querySelector("#register-alert");
    console.log(email, password);
    email.classList.add("uk-form-danger");
    password.classList.add("uk-form-danger");
    alert.removeAttribute("hidden");
  }
}
