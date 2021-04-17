function form_submit() {
  document.getElementById("login-form").submit();
  document.getElementById("register-form").submit();
  document.getElementById("search-form").submit();
}

const searchButton = document.querySelector("#search-button");

const queryHandler = async (e) => {
  //e.preventDefault();
  const searchInput = document.querySelector("#search-input");
  console.log(searchInput.value);
  const response = await getData("/get-shows-by-title/" + searchInput.value);
  console.log(response);
};

searchButton.addEventListener("click", queryHandler);

async function getData(url) {
  // Default options are marked with *
  const response = await fetch(url, {
    method: "GET", // *GET, POST, PUT, DELETE, etc.
    headers: {
      "Content-Type": "application/json",
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
  });
  return response.json(); // parses JSON response into native JavaScript objects
}
