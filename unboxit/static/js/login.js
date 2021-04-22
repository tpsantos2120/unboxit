import Fetch from "./Fetch.js";
// const ready = (id) => {
//   let isIdExist = false;
//   // If the body element and the #main element exist
//   if (document.body && document.querySelector(id)) {
//     // Run your code here...
//     // Return so that we don't call requestAnimationFrame() again
//     isIdExist = true;
//     return isIdExist;
//   }

//   // If the body element isn't found, run ready() again at the next pain
//   window.requestAnimationFrame(ready);
// };

// // Initialize our ready() function
// window.requestAnimationFrame(ready);

const loginButton = document.querySelector("#login-button");

const handleLogin = (e) => {
  const email = document.querySelector("#login-email");
  const password = document.querySelector("#login-password");
  if (email && password) {
    loginUser(email, password);
  }
  e.preventDefault();
};

loginButton.onclick = handleLogin;

async function loginUser(email, password) {
  const response = await Fetch.create("/api/auth/login", {
    email: email.value,
    password: password.value,
  });
  console.log(response);
  if (response.status === 200) {
    window.location.replace("/dashboard");
  } else {
    const alert = document.querySelector("#alert");
    console.log(email, password);
    email.classList.add("uk-form-danger");
    password.classList.add("uk-form-danger");
    alert.removeAttribute("hidden");
  }
  
}
