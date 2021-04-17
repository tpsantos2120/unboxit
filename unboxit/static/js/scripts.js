function form_submit() {
  document.getElementById("login-form").submit();
  document.getElementById("register-form").submit();
  document.getElementById("search-form").submit();

}

// const searchButton = document.querySelector("#search-button");

// const queryHandler = (e) => {
//   //e.preventDefault();
//   const searchInput = document.querySelector("#search-input");
//   console.log(searchInput.value)
// };

// searchButton.addEventListener("click", queryHandler);


// async function getData(url = '/get-movies-by-title', data = {}) {
//   // Default options are marked with *
//   const response = await fetch(url, {
//     method: 'GET', // *GET, POST, PUT, DELETE, etc.
//     mode: 'cors', // no-cors, *cors, same-origin
//     cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
//     credentials: 'same-origin', // include, *same-origin, omit
//     headers: {
//       'Content-Type': 'application/json'
//       // 'Content-Type': 'application/x-www-form-urlencoded',
//     },
//     redirect: 'follow', // manual, *follow, error
//     referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
//     params: JSON.stringify(data) // body data type must match "Content-Type" header
//   });
//   return response.json(); // parses JSON response into native JavaScript objects
// }