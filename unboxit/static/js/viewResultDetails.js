import Fetch from "./Fetch.js";

const ready = () => {
  if (document.body && document.querySelector(".results")) {
    console.log("yessss")
    searchDetails();
    return;
  }

  window.requestAnimationFrame(ready);
};

window.requestAnimationFrame(ready);

const handleSearchDetails = (e) => {
  
  const id = e.target.getAttribute("imdb");
  const type = e.target.getAttribute("type");
  console.log(id);
  if (type === "movies") {
    findMovieDetails(id);
  } else {
    findShowDetails(id);
  }

  console.log(id, type);
};

const searchDetails = () => {
  const slider = document.querySelectorAll(".results");
  slider.forEach((element) => {
    element.onclick = handleSearchDetails;
  });
};

const findMovieDetails = async (id) => {
  const viewMovieDetails = document.querySelector("#view-result-details");
  const movieDetails = await Fetch.get("/search/movie/details/", id);
  console.log(movieDetails, viewMovieDetails);
  viewMovieDetails.classList.add("uk-margin-large")
  viewMovieDetails.innerHTML = movieDetails;
};

const findShowDetails = async (id) => {
  const viewShowDetails = document.querySelector("#view-result-details");
  const showDetails = await Fetch.get("/search/show/details/", id);
  console.log(showDetails, viewShowDetails);
  viewShowDetails.classList.add("uk-margin-large")
  viewShowDetails.innerHTML = showDetails;
};

const appendResultDetails = (showDetails) => {};
