import Fetch from "./fetch.js";

// const ready = () => {
//   if (document.body && document.querySelector(".results")) {
//     console.log("yessss");
//     searchDetails();
//     return;
//   }

//   window.requestAnimationFrame(ready);
// };

// window.requestAnimationFrame(ready);

const handleSearchDetails = (e) => {
  const id = e.target.getAttribute("imdb");
  const type = e.target.getAttribute("type");
  const image = e.target.getAttribute("data-src");

  console.log(id);
  if (type === "movies") {
    findMovieDetails(id, image, type);
  } else {
    findShowDetails(id, image, type);
  }
};

const searchDetails = () => {
  const slider = document.querySelectorAll(".results");
  slider.forEach((element) => {
    element.onclick = handleSearchDetails;
  });
};

const addlistener = (id, image, type, e) => {
  postData(id, image, type);
};

const postData = async (id, image, type) => {
  const title = document.querySelector("#title");
  const description = document.querySelector("#description");
  const year = document.querySelector("#year");
  const imdbRating = document.querySelector("#imdb-rating");
  const voteCount = document.querySelector("#vote-count");
  const releaseDate = document.querySelector("#release-date");
  const populatity = document.querySelector("#popularity");
  const runtime = document.querySelector("#runtime");
  const stars = document.querySelectorAll(".stars");
  const directors = document.querySelectorAll(".directors");
  const creators = document.querySelectorAll(".creators");
  const data = {
    imdb_id: id,
    poster: image,
    media_type: type,
    title: title.innerText,
    description: description.innerText,
    year: year.innerText,
    imdb_rating: imdbRating.innerText,
    vote_count: voteCount.innerText,
    release_date: releaseDate.innerText,
    popularity: populatity.innerText,
    runtime: parseInt(runtime.innerText, 10),
    stars: [],
    directors: [],
    creators: [],
  };
  stars.forEach((item) => {
    data.stars.push(item.innerText);
  });
  directors.forEach((item) => {
    data.directors.push(item.innerText);
  });
  creators.forEach((item) => {
    data.creators.push(item.innerText);
  });
  console.log(data);
  const saveDataResponse = await Fetch.create("/api/movies", data);
  if (saveDataResponse.status === 400) {
    UIkit.notification({
      message: 'It already exists in your watchlist.',
      status: 'danger',
      pos: 'top-center',
      timeout: 5000
  });
  } else {
    UIkit.notification({
      message: 'It has been added to your watchlist.',
      status: 'success',
      pos: 'top-center',
      timeout: 5000
  });
  }

};

const findMovieDetails = async (id, image, type) => {
  const viewMovieDetails = document.querySelector("#view-result-details");
  const movieDetails = await Fetch.get("/search/movie/details/", id);
  console.log(movieDetails, viewMovieDetails);
  viewMovieDetails.classList.add("uk-margin-large");
  viewMovieDetails.classList.add("uk-margin-bottom-large");
  removeChildrenEl(viewMovieDetails);
  viewMovieDetails.innerHTML = movieDetails;
  const addButton = document.querySelector("#add-button");
  if (addButton) {
    addButton.onclick = addlistener.bind(this, id, image, type);
  }
};
  
  

const findShowDetails = async (id, image, type) => {
  const viewShowDetails = document.querySelector("#view-result-details");
  const showDetails = await Fetch.get("/search/show/details/", id);
  console.log(showDetails, viewShowDetails);
  viewShowDetails.classList.add("uk-margin-large");
  viewShowDetails.classList.add("uk-margin-bottom-large");
  removeChildrenEl(viewShowDetails);
  viewShowDetails.innerHTML = showDetails;
  const addButton = document.querySelector("#add-button");
  if (addButton) {
    addButton.onclick = addlistener.bind(this, id, image, type);
  }
};

const removeChildrenEl = (node) => {
  while (node.firstChild) {
    node.removeChild(node.lastChild);
  }
};

export default {
  searchDetails,
};
