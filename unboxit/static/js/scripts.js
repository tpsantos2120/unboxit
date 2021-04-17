function form_submit() {
  document.getElementById("login-form").submit();
  document.getElementById("register-form").submit();
  document.getElementById("search-form").submit();
}

// const searchButton = document.querySelector("#search-button");

// const queryHandler = async (e) => {
//   //e.preventDefault();
//   const searchInput = document.querySelector("#search-input");
//   console.log(searchInput.value);
//   const response = await getData("/get-shows-by-title/" + searchInput.value);
//   const movies = document.querySelector("#movies");

//   let output = "";
//   for (const movie of response) {
//     console.log(movie);
//     output += `<div class="card" style="width: 18rem;">`;
//     output += `<img src="${movies.poster}" class="card-img-top" alt="...">`;
//     output += `<div class="card-body">`;
//     output += `<h5 class="card-title">${movie.title}</h5>`;
//     output += `<a href="#" class="btn btn-primary">View Details</a>`;
//     output += `</div>`;
//     output += `</div>`;
//   }
//   movies.innerHTML = output;
// };

// searchButton.addEventListener("click", queryHandler);

// async function getData(url) {
//   // Default options are marked with *
//   const response = await fetch(url, {
//     method: "GET", // *GET, POST, PUT, DELETE, etc.
//     headers: {
//       "Content-Type": "application/json",
//       // 'Content-Type': 'application/x-www-form-urlencoded',
//     },
//   });
//   return response.json(); // parses JSON response into native JavaScript objects
// }

$("#search-button").click(function(){
  var text = $("#search-input").val();
  console.log(text)
  $.ajax({
    url: "/get-movies-by-title/"+ text,
    type: "get",
    success: function (response) {
      console.log(response)
      $("#movies").html(response);
    },
    error: function(xhr) {
      //Do Something to handle error
    }
  });
});