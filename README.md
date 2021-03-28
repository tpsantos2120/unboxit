# User Experience Design - UX

## Project Goal

This is **UNBOXIT** a website where it allows you to search for Movies and TV Series to add to a watchlist where you can use as a tracker, and once you have watched you can tick off your list. It also comes with Recommendations and Trending in the cinematography world, you will be able to watch trailers and also know more trivial information about your favourite Movies and TV Series. In addition, I will use IMDB endpoint from Rapid API to consume their huge database of Movies and TV Series. 

## Strategy

- **User Goals**

	- I will be able to easily navigate .
	- All images and texts will have no distractions.
	- It will allow me to search for a movies and tv series.
	- I will be able to see more details about a movie by navigating to that specific movie.
	- There will be a dashboard with a watchlist and recommendations in my profile.
	- The website will have a watchlist for their users.
	- It will be easy for me to remove / add movies and tv series to my watchlist.
	- The website will have a visually appealing look and feel.

- **User Stories**

	- As a user, I will have to sign up if they wish to be able to save movies or tv series to my watchlist.
	- As a user, I will be able to access a dashboard where I can view my watchlist and recommendations.
	- As a user, I will not have to sign up if they wish to search for a movie.
	- As a user, I will be able to add a movie or a tv series to my watchlist.
	- As a user, I will be able to remove a movie or a tv series from my watchlist.
	- As a user, I will be able to mark movies and tv series I have watched off of my watchlist.
	- As a user, I will be able to change my password.
	- As a user, I will be able to see trending movies and tv series.
	- As a user, I will be able to get recommended movies or tv series based on my watchlist.

## Scope

**Functional Specifications & Content Requirements**

The functional specification will be based on the [assessment criteria](https://drive.google.com/file/d/1GBoEwg5ODXp1Gg3oJJdXYpELdO7_s3MP/view?usp=sharing) and user stories. The content required to bring value to a product so I would say is crucial to have them set out. The written content has to be concise and to the point, relevant to the section of the game. It has to follow the same typography to maintain consistency throughout the website. The imagery has to be consistent throughout the website in terms of colours and sizes. The colours has to be consistent with the logo colours to bring a theme based to the visitors. The typography will have consistency between written content and logo. It is important that the game will have one typography for the logo and one for the content. The logo has to bring set the tone for the look and feel of the game so that the other parts can follow it nicely. All information to have the right amount of contrast between foreground and background to avoid distractions.

## Structure & Skeleton

**Wireframes**

- **[Home Page](https://github.com/tpsantos2120/unboxit/blob/main/wireframes/Home_Page.png)**
- **[Login Modal](https://github.com/tpsantos2120/unboxit/blob/main/wireframes/Login.png)**
- **[Sign Up Modal](https://github.com/tpsantos2120/unboxit/blob/main/wireframes/Sign_Up.png)**
- **[Dashboard Page](https://github.com/tpsantos2120/unboxit/blob/main/wireframes/Dashboard.png)**
- **[Search Page](https://en.wikipedia.org/wiki/Bootstrap_%28front-end_framework%29)**
- **[Settings](https://github.com/tpsantos2120/unboxit/blob/main/wireframes/Search.png)**
- **[Full Preview](https://github.com/tpsantos2120/unboxit/blob/main/wireframes/Movie_and_Series_Full_Preview.png)**
- **[Short Preview](https://github.com/tpsantos2120/unboxit/blob/main/wireframes/Movie_and_Series_Short_Preview.png)**

**Database Structure**

I have designed the database structure during the planning stage to help me structure better the database and to also have a better sense of what I am doing. Below you will see the structure I will be using.
 
 **Users**
| Key |  Value |
|:--:|:--:|
| _id |  ObjectId|
| firstname | String|
| lastname | String|
| username | String|
| password | String|

 **Watchlist**
| Key |  Value |
|:--:|:--:|
| _id |  ObjectId|
| user_id | String|
| imdb_id | Array|

 **Movie Details**
| Key |  Value |
|:--:|:--:|
| _id |  ObjectId|
| type | String|
| title | String|
| description | String|
| year | String|
| release_date | String|
| imdb_id | String|
| imdb_rating | String|
| vote_count | String|
| popularity | String|
| youtube_trailer_key | String|
| runtime | Number|
| rated | Array|
| genres | Array|
| stars | Array|
| directors | Array|
| countries | Array|
| language | Array|

 **TV Series Details**
| Key |  Value |
|:--:|:--:|
| _id |  ObjectId|
| type | String|
| title | String|
| description | String|
| release_date | String|
| imdb_id | String|
| imdb_rating | String|
| vote_count | String|
| popularity | String|
| youtube_trailer_key | String|
| rated | String|
| runtime | Number|
| year_started | String|
| stars | Array|
| creators | Array|
| countries | Array|
| language | Array|
| production_companies | Array|
| networks | Array|

**Proposed API Routes**

>     - GET	/
>     - GET	/dashboard
>     - GET	/dashboard/id
>     - GET	/search
>     - GET	/search/id
>     - GET	/api/watchlist
>     - GET	/api/watchlist/id
>     - POST  /api/watchlist/id
>     - GET   /api/users/id
>     - POST  /api/users

## Surface

-  **Design Choices**

	- **Colours** - you can view my colour palette. The palette was created based on the Netflix website. I believe it brings the right colours for movie and tv series enthusiasts.
	![Pallette](https://ik.imagekit.io/2a1in3cldn/Pallette_t2p3Xbrnuu2wL.png)
	
	- **Typography** - I will use Space Grotesk for headings and sub-headings and for the paragraphs it will be Jura. All these from [Google Fonts](https://fonts.google.com/).
	
	- **Images** - I will use images that are provided with the API Endpoints. Each movie or tv series will have their own poster image. 
	
	- **Logo** - I used [Canva](https://www.canva.com) to design logo and favicon. You can view this under **Resources** in this document.  The fonts used for the logo are Mont Thin and Alta which both are also from canva.
	
	- **Icons** - I will be using icons from Font Awesome. more in the **Resources** section in this document.

# Technologies Used

# Resources

# Implementation

# Testing

# Deployment
