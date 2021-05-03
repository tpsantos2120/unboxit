
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

**Languages**
- **[CSS](https://en.wikipedia.org/wiki/CSS)**
- **[HTML](https://en.wikipedia.org/wiki/HTML)**
- **[JavaScript](https://en.wikipedia.org/wiki/JavaScript)**
- **[Python](https://www.python.org/)**

**Libraries and Frameworks**
- **[Font Awesome](https://fontawesome.com/)**
- **[Bootstrap](https://en.wikipedia.org/wiki/Bootstrap_%28front-end_framework%29)**
- **[Google Fonts](https://fonts.google.com/)**

**Tools**

- **[VSCode](https://en.wikipedia.org/wiki/Visual_Studio_Code)**
- **[Git](https://git-scm.com/)**
- **[GitHub](https://en.wikipedia.org/wiki/GitHub)**
- **[MockFlow](https://mockflow.com/)**
- **[Heroku](https://www.heroku.com/)**
- **[W3C HTML Validation](https://validator.w3.org/)**
- **[W3C CSS Validation](https://jigsaw.w3.org/css-validator/)**
- **[MongoDB Atlas](https://www.mongodb.com/)**
- **[Flask](https://flask.palletsprojects.com/en/1.1.x/)**
- **[PyMongo](https://api.mongodb.com/python/current/tutorial.html)**

# Resources

- **Font Awesome & Iconify**
- **Canva** 
- **StackEdit**
- **Bootstrap**
- **Javascript**
- **HTML**
- **CSS**
- **ImageKit** 
- **Auto CSS Prefixer**

# Implementation

**Planning**

The implementation will start by the backend working through the frontend. I will be setting up Python and Flask folders and environment. Next, I will setup MongoDB using the database structure planned in the Structure & Skeleton section. Once I am happy with these setups I will configure my environment variables and connect to the database. Afterwards, all API routes would then be written whilst performing some tests along the way to check if it works. When I have all API routes, I will create the HTML files templates files based on the Wireframes. Next I will use IMDB from Rapid API to consume all the APIs needed when users are searching for movies and tv series.   

**Development**

The development was implemented by working from the backend towards the frontend, unless I required a view to visualise results, but in general it was developed in that manner. All API was tested as they were being developed by using **POSTMAN**. During implementation I tried to follow a MVC pattern as much as possible, so I have split my files in several folders, though all of it could and will be refactored I believe I did a good job in getting things more maintainable and readable than I would without splitting the logic from view and so on.

**Project Structure**

The project was structured in 5 folders, each folder contains files and or subfolder to structure the project in a easy and maintainable manner. Below you will find the project structure and what each one of them do:

- **Models**
	- **[db](https://github.com/tpsantos2120/unboxit/blob/main/unboxit/models/db.py)** -  This file will initialise **MongoEngine** so it can be used within the Models folder and it will give the functionality to use Documents and enforce schemas on MongoDB.
	- **[models](https://github.com/tpsantos2120/unboxit/blob/main/unboxit/models/models.py)** - Once DB is instantiated, it is then imported and by using classes we pass that instance where we are able to create documents or better said schemas.

- **Resources**
- 
	- **[app_api](https://github.com/tpsantos2120/unboxit/tree/main/unboxit/resources/app_api)** -  In this folder, it holds all the files that has **API Resources** that are related to the app itself not the backend. For example, routes to dashboard or home.
	
	- **[db_api](https://github.com/tpsantos2120/unboxit/tree/main/unboxit/resources/db_api)** - On the other hand this folder which also reference **API** is directly related to resources that are accessed from or to **MongoDB Atlas**. For example, logging and registering a user or adding movies or tv shows.

	- **[routes](https://github.com/tpsantos2120/unboxit/tree/main/unboxit/resources/routes)** - This folder is directly related to the **APIs** mentioned above, as this has a **routes file** where all routes are registered using Flask Restful.

	- **[utils](https://github.com/tpsantos2120/unboxit/tree/main/unboxit/resources/utils)** - The **utils** folder initialises and registers the **Cache**, **JWT** and **Errors**. The **Cache** is used to cache queries to the database queries to minimize queries to **IMDB** and **MongoDB**. The **JWT** is used to protect routes, generate tokens and it the important for the way authentication happens in the app. Finally, there the **Errors** file that is used to implement custom error handling by specifying which errors to customise with which error messages to return, these are then used with **TRY**, **EXCEPTION** and **RAISE** throughout the app. 

- **Services**

	- **[mail_service](https://github.com/tpsantos2120/unboxit/blob/main/unboxit/services/mail_service.py)** - The implementation for emailing was to offer users the feature to reset their passwords. In order to do this, I have used **Flask Mail** and **SendGrid**. The way this works is that **Flask Framework** uses **Flask Mail** extention to send emails through **SendGrid**. In addition, SendGrid is configured to use my personal email that I created for the purpose of this project, unboxit@tsantos.dev.

- **Static**
	- **[static](https://github.com/tpsantos2120/unboxit/tree/main/unboxit/static)** - This folder is where the assets are located. I have used quite a bit of JavaScript to handle dynamic content, so I have split them in several files, each file will be doing something specific.

- **Templates**
	- **[templates](https://github.com/tpsantos2120/unboxit/tree/main/unboxit/templates)** - All HTML files were split into 3 folders Views, Layout and Components. I have chosen to split them in folders to make it easier to understand as it currently contains 23 files this way it makes a bit easier to cope with bugs, if any.

# Testing

# Deployment