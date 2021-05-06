![enter image description here](https://ik.imagekit.io/xsenqx8yi/images/responsive_image_QEYtHwm-be-.PNG)

- [User Experience Design - UX](#user-experience-design---ux)
	- [Project Goal](#project-goal)
	- [Strategy](#strategy)
	- [Scope](#scope)
	- [Structure & Skeleton](#structure--skeleton)
	- [Surface](#surface)
		- [**Design Choices**](#design-choices)
- [Technologies Used](#technologies-used)
- [Resources](#resources)
- [Implementation](#implementation)
	- [**Planning**](#planning)
	- [**Development**](#development)
	- [**Project Structure**](#project-structure)
	- [**API Routes**](#api-routes)
	- [**Database Structure**](#database-structure)
	- [**Flask App Configuration**](#flask-app-configuration)
	- [**Emailing**](#emailing)
	- [**Implementation Issues, Bugs and Learnings**](#implementation-issues-bugs-and-learnings)
- [Testing](#testing)
	- [Unit Tests](#unit-tests)
	- [User Stories Tests](#user-stories-tests)
	- [Form Validations](#form-validations)
	- [Responsiveness  Test](#responsiveness--test)
	- [Authentication Test](#authentication-test)
	- [Password Reset Test](#password-reset-test)
- [Deployment](#deployment)
	- [MongoDB](#mongodb)
		- [STEP 1 - Create cluster project](#step-1---create-cluster-project)
		- [STEP 2 - Create Database User and Setup Network Access.](#step-2---create-database-user-and-setup-network-access)
		- [STEP 3 - Get database credentials.](#step-3---get-database-credentials)
	- [SendGrid](#sendgrid)
	- [IMDB API](#imdb-api)
	- [Local Deployment](#local-deployment)
		- [Download Project & Github CLI](#download-project--github-cli)
		- [Environment Variables](#environment-variables)
		- [Installing Dependencies and Running The App](#installing-dependencies-and-running-the-app)
	- [Heroku Deployment](#heroku-deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

# User Experience Design - UX

## Project Goal

This is **UNBOXIT** a website where it allows you to search for Movies and TV Series to add to a watchlist where you can use as a tracker, and once you have watched you can tick off your list. It also comes with Recommendations and Trending in the cinematography world, you will be able to watch trailers and also know more trivial information about your favourite Movies and TV Series. In addition, I will use IMDB endpoint from Rapid API to consume their huge database of Movies and TV Series. 

<hr>

[Back To Top](#user-experience-design---ux)

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

	- As a user, I will have to sign up if I wish to be able to save movies or tv series to my watchlist.
	- As a user, I will be able to access a dashboard where I can view my watchlist and recommendations.
	- As a user, I will not have to sign up if I wish to search for a movie.
	- As a user, I will be able to add a movie or a tv series to my watchlist.
	- As a user, I will be able to remove a movie or a tv series from my watchlist.
	- As a user, I will be able to review movies and tv series I have watched off of my watchlist.
	- As a user, I will be able to change my password.
	- As a user, I will be able to see trending movies and tv series.
	- As a user, I will be able to get recommended movies or tv series based on my watchlist.

<hr>

[Back To Top](#user-experience-design---ux)

## Scope

**Functional Specifications & Content Requirements**

The functional specification will be based on the [assessment criteria](https://drive.google.com/file/d/1GBoEwg5ODXp1Gg3oJJdXYpELdO7_s3MP/view?usp=sharing) and user stories. The content required to bring value to a product so I would say is crucial to have them set out. The written content has to be concise and to the point, relevant to the section of the game. It has to follow the same typography to maintain consistency throughout the website. The imagery has to be consistent throughout the website in terms of colours and sizes. The colours has to be consistent with the logo colours to bring a theme based to the visitors. The typography will have consistency between written content and logo. It is important that the game will have one typography for the logo and one for the content. The logo has to bring set the tone for the look and feel of the game so that the other parts can follow it nicely. All information to have the right amount of contrast between foreground and background to avoid distractions.

<hr>

[Back To Top](#user-experience-design---ux)

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

>     - GET	/api/watchlist
>     - GET	/api/watchlist/id
>     - POST  /api/watchlist/id
>     - GET   /api/users/id
>     - POST  /api/users

<hr>

[Back To Top](#user-experience-design---ux)

## Surface

### **Design Choices**

**Colours** - you can view my colour palette. The palette was created based on the Netflix website. I believe it brings the right colours for movie and tv series enthusiasts.
<p align="center">
  <img src="https://ik.imagekit.io/2a1in3cldn/Pallette_t2p3Xbrnuu2wL.png" width="500">
</p>

**Typography** - I will use Space Grotesk for headings and sub-headings and for the paragraphs it will be Jura. All these from [Google Fonts](https://fonts.google.com/).
**Images** - I will use images that are provided with the API Endpoints. Each movie or tv series will have their own poster image. 
**Logo** - I used [Canva](https://www.canva.com) to design logo and favicon. You can view this under **Resources** in this document.  The fonts used for the logo are Mont Thin and Alta which both are also from canva.
	**Icons** - I will be using icons from Font Awesome. more in the **Resources** section in this document.

<hr>

[Back To Top](#user-experience-design---ux)

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
- **[Uikit](https://getuikit.com/docs/introduction)**

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

<hr>

[Back To Top](#user-experience-design---ux)

# Resources

- **[Font Awesome](https://fontawesome.com/)**
- **[Canva](https://www.canva.com/)** 
- **[StackEdit](https://www.canva.com/)**
- **[Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/)**
- **[Flask](https://flask.palletsprojects.com/en/1.1.x/api/)**
- **[DevDocs](https://devdocs.io/)**
- **[ImageKit](https://imagekit.io/)** 
- **[Flask Restful](https://flask-restful.readthedocs.io/en/latest/api.html)** 
- **[MongoEngine](https://imagekit.io/)** 
- **[Flask MongoEngine](https://flask.palletsprojects.com/en/1.1.x/patterns/mongoengine/)** 
- **[Gunicorn](https://flask.palletsprojects.com/en/1.1.x/deploying/wsgi-standalone/)** 
- **[Flask-Caching](https://imagekit.io/)** 
- **[Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/)** 
- **[Python-dotenv](https://pypi.org/project/python-dotenv/)** 
- **[Requests](https://realpython.com/python-requests/)** 
- **[Ratelimit](https://pypi.org/project/ratelimit/)** 
- **[Jinja2](https://flask.palletsprojects.com/en/1.1.x/templating/)** 
- **[Testing](https://realpython.com/python-testing/)** 
- **[Flask-Mail](https://pythonhosted.org/Flask-Mail/)** 
- **[Flask Configuration Files](https://pythonise.com/series/learning-flask/flask-configuration-files)** 
- **[SendGrid](https://sendgrid.com/blog/sending-emails-from-python-flask-applications-with-twilio-sendgrid/)** 

<hr>

[Back To Top](#user-experience-design---ux)

# Implementation

## **Planning**

The implementation will start by the backend working through the frontend. I will be setting up Python and Flask folders and environment. Next, I will setup MongoDB using the database structure planned in the Structure & Skeleton section. Once I am happy with these setups I will configure my environment variables and connect to the database. Afterwards, all API routes would then be written whilst performing some tests along the way to check if it works. When I have all API routes, I will create the HTML files templates files based on the Wireframes. Next I will use IMDB from Rapid API to consume all the APIs needed when users are searching for movies and tv series.

<hr>

[Back To Top](#user-experience-design---ux)

## **Development**

The development was implemented by working from the backend towards the frontend, unless I required a view to visualise results, but in general it was developed in that manner. All API was tested as they were being developed by using **POSTMAN**. During implementation I tried to follow a MVC pattern as much as possible, so I have split my files in several folders, though all of it could and will be refactored I believe I did a good job in getting things more maintainable and readable than I would without splitting the logic from view and so on.

<hr>

[Back To Top](#user-experience-design---ux)

## **Project Structure**

The project was structured in 5 folders, each folder contains files and or subfolder to structure the project in a easy and maintainable manner. Below you will find the project structure and what each one of them do:

- **Models**
	- **[db](https://github.com/tpsantos2120/unboxit/blob/main/unboxit/models/db.py)** -  This file will initialise **MongoEngine** so it can be used within the Models folder and it will give the functionality to use Documents and enforce schemas on **MongoDB**.
	- **[models](https://github.com/tpsantos2120/unboxit/blob/main/unboxit/models/models.py)** - Once **DB** is instantiated, it is then imported and by using classes we pass that instance where we are able to create documents or better said schemas.

- **Resources**
- 
	- **[app_routes](https://github.com/tpsantos2120/unboxit/tree/main/unboxit/resources/app_api)** -  In this folder, it holds all the files that has **API Resources** that are related to the app itself not the backend. For example, routes to dashboard or home.
	
	- **[api_routes](https://github.com/tpsantos2120/unboxit/tree/main/unboxit/resources/db_api)** - On the other hand this folder which also reference **API** is directly related to resources that are accessed from or to **MongoDB Atlas**. For example, logging and registering a user or adding movies or tv shows.

	- **[routes](https://github.com/tpsantos2120/unboxit/tree/main/unboxit/resources/routes)** - This folder is directly related to the **APIs** mentioned above, as this has a **routes file** where all routes are registered using **Flask Restful**.

	- **[utils](https://github.com/tpsantos2120/unboxit/tree/main/unboxit/resources/utils)** - The **utils** folder initialises and registers the **Cache**, **JWT** and **Errors**. The **Cache** is used to cache queries to the database queries to minimize queries to **IMDB** and **MongoDB**. The **JWT** is used to protect routes, generate tokens and it the important for the way authentication happens in the app. Finally, there the **Errors** file that is used to implement custom error handling by specifying which errors to customise with which error messages to return, these are then used with **TRY**, **EXCEPTION** and **RAISE** throughout the app. 

- **Services**

	- **[mail_service](https://github.com/tpsantos2120/unboxit/blob/main/unboxit/services/mail_service.py)** - The implementation for emailing was to offer users the feature to reset their passwords. In order to do this, I have used **Flask Mail** and **SendGrid**. The way this works is that **Flask Framework** uses **Flask Mail** extension to send emails through **SendGrid**. In addition, **SendGrid** is configured to use my personal email that I created for the purpose of this project, unboxit@tsantos.dev.

- **Static**
	- **[static](https://github.com/tpsantos2120/unboxit/tree/main/unboxit/static)** - This folder is where the assets are located. I have used quite a bit of JavaScript to handle dynamic content, so I have split them in several files, each file will be doing something specific.

- **Templates**
	- **[templates](https://github.com/tpsantos2120/unboxit/tree/main/unboxit/templates)** - All HTML files were split into 3 folders Views, Layout and Components. I have chosen to split them in folders to make it easier to understand as it currently contains 23 files this way it makes a bit easier to cope with bugs, if any.

<hr>

[Back To Top](#user-experience-design---ux)

## **API Routes**

The API routes initially proposed were changed in the development stage, this is because it did not work well with what the app wanted to achieve through IMDB API. I will be adding the new APIs below, so there is a reference to how they are actually implemented. I have taken the decision to change some of the routes because I found issues as I was handling IMDB API that at times when I had to query 3 to 4 APIs to get the resources I required so I tried to simplify as much as possible. Also, I was using hyphen in some of the url segments pointed by my mentor therefore I decided to make them more standardized.

>     - GET		/api/watchlists
>     - POST		/api/watchlists
>     - PUT		/api/watchlist/<id>
>     - DELETE	/api/watchlist/<id>
>     - GET		/api/watchlist/<id>
>     - POST		/api/auth/login
>     - POST		/api/auth/register
>     - POST		/api/auth/reset
>     - POST		/api/auth/reset/password
>     - POST		/api/auth/forgot

<hr>

[Back To Top](#user-experience-design---ux)

## **Database Structure**

The database structure was changed the reason was that it was becoming resource intensive with querying different APIs from IMDB. So to economise resources I decided to have one watchlist holding both movies and shows, most fields are the same for both, so I discarded the fields that were different and kept the fields that were the same, so now it is all in one place, plus I have added two extra fields, one to hold images so I don't have to query IMDB for it and   the other is to distinguish if it is a movie or show, that field is called media_type.

 **User**
| Key |  Value |
|:--:|:--:|
| _id |  ObjectId|
| first_name | String|
| last_name | String|
| username | String|
| email | String|
| password | String|
| watchlists | Array|


 **Watchlist**
| Key |  Value |
|:--:|:--:|
| _id |  ObjectId|
| poster | String|
| media_type | String|
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
| stars | Array|
| directors | Array|
| creators | Array|
| added_by | Array|


## **Flask App Configuration**

The environment structure and app configuration has had several refactors as I saw through documentation that a better way could be implemented until I reached the refactoring that I was happy with it.

I have setup the app by having three files **run.py**, **config.py** and **__init__.py**. The way I implemented these was by using the .env file which you have to install the dotenv extension. Then you are able to use .env files where you would store key value pairs with the = sign and once the loadenv is executed it finds the file and executes it as environment variables.

In the config file I have three environments setup production, development and testing each has more or less the same configuration apart from the Mongo URI, each has its own database in this way we don't mix databases.

<hr>

[Back To Top](#user-experience-design---ux)

## **Emailing**

The emailing feature for users to reset password is fully functional, the email templates are basic but it all works fine. I took the decision to implement it to give users the option to reset the password since the information gathered during registration includes email it only makes sense to implement it.

In order to implement email service I had to configure Flask Mail which is the extension that allows emails to be sent from or to a flask app. Once that was setup I have configured my dev email server with SendGrid so my email could be used through SendGrid to send emails to users to reset their passwords. The way I have implemented it is depicted in the gif below.

<p align="center">
  <img src="https://ik.imagekit.io/xsenqx8yi/images/xoxo_X5pKjT-LqS-.gif">
</p>

<hr>

[Back To Top](#user-experience-design---ux)

## **Implementation Issues, Bugs and Learnings**

**Restful APIs**

The main issues with the APIs I have had was because they did not align properly with the ones IMDB provided. Also, all API keys provided by IMDB would not be possible to store in the backend. By using the same flask app to serve Web Pages as well as API resources meant that at times I created two APIs to not fetch them from client side, one to query IMDB and return results to another API where it would respond with whatever IMDB response was received. 

This was the wrong approach I should have had implemented and structured the APIs in a manner that it would keep things separate. This happened towards the middle of the project where I have refactored the URLs and APIs, The good thing is that I learned great deal of things not to do whilst doing this project.

**Dynamic Content**

This was a great issue because the nature of my app was to be very dynamic with very little whole page reloads. I learned Flask is horrible for this sort of apps and a mixture with a frontend framework would have done better even though outside of the scope of this project and course. 

The main issue was getting content to and from JavaScript, this cannot be done unless you have JS injected with Jinja templates which is wrong approach and it was something my mentor raised with me. However, looking through Flask documentation they actually have a part where they give examples where you inject Block Script with Block Content making things confusing to maintain later on. 

So here I go thinking how can I avoid writing tons of JS to handle so much dynamic content? Well, I cant so as I got into troubles I hard reset to a previous point where for some reason all the wrong JS I had written disappeared, so the good side was that I re-wrote completely everything JS related without having to inject them which is great but it ended up being at the cost of writing a lot of it.

I have looked into using Web Sockets, but at the end I didn't want to venture in that way because I wouldn't have the time to complete it. All in all for my personal projects I would never use templates anymore, instead Flask provides a great deal of other great things such as Flask Restful which is great.


**PyMongo vs MongoEngine**

I wanted from day one to implement schemas in my MongoDB documents, so instead of using PyMongo, I have used MongoEngine Document Object Mapper, instead of the low level drive PyMongo.

The issues I have had with MongoEngine was when handling errors until I saw in the Flask Restful documentation that I could use abstract classes and customise errors and use TRY and Raise to handle errors that could happen with Mongo.

The great thing about MongoEngine is that its classed based and as I have prior understanding of it from JS for me it was straight forward, It is something I would definitely use in the future. 

**Mixed Content Image Warning**

There is a error that is displayed to console that says images are being loaded as HTTP over HTTPS. Unfortunately, this is something out my control as all images are from IMDB and that is how they have their images. Also there are some images that cannot be loaded once they reach client side as there is no way for me to check if image exists once they are loaded in the browser there will be a console log error saying image could not be downloaded. To enhance experience in this situation I attempt to not display them.

<hr>

[Back To Top](#user-experience-design---ux)

# Testing

## Unit Tests

The tests were done with Unittests which comes with python. The setting up is easy as we don't have to install it as its already included. All tests are isolated meaning that once they are executed in the database they collections are teared down as well as most tests has a user registering and then performing an operation or logging out so there are different combinations.

I have written 20 tests in total for all the DB APIs for the app, except the APIs for the app itself, such as homepage. I have integrated tests for invalid id, no id, unauthorized, with payload and without it. I have considered as much scenarios as I could think of, though there is always more tests that can be done. All 20 tests has passed and no fails, based on the given use cases.

![enter image description here](https://ik.imagekit.io/xsenqx8yi/images/Capture_Jr9_KK7AB.PNG)

In order to run the tests the ENV in the environment file must be set to testing so the correct database is used for it. More details in the deployment section.

If you wish to run the tests locally make sure **ENV** in the **.env** file is set to **testing**, then use the following command to run them:

- `python -m unittest --buffer -v`

<hr>

[Back To Top](#user-experience-design---ux)

## User Stories Tests

**User Story** *- As a user, I will have to sign up if I wish to be able to save movies or tv series to my watchlist.*

**Dashboard Implementation** - The registration form has several form details, the reason for it to be implemented this way is so that in the future there will be more customisation and features such as logging in with google authentication and allowing user to change their details.

**User Registration Test** - The test carried out allows the user to perform a registration, considering that there is no existing email. Following the registration user is redirected to the dashboard which initially will be empty. I have chosen to capture more details such as email because I tend to make it official app at one point, which also the reset password feature requires an email. This user story has been achieved as you can see below a mock operation of a user registering.

**Test** - [Test User Registration](https://ik.imagekit.io/xsenqx8yi/user_stories_test/test_register_user_DZoZ8UFcu.gif)

<hr>

**User Story** *- As a user, I will be able to access a dashboard where I can view my watchlist and recommendations.*

**Dashboard Implementation** - I have decided to implement the dashboard using cards from the UIKIT framework. The reason behind is that they are able to hold quite a lot of images inside the slider before it starts to get slow. Though, I have not introduced pagination this is something that will be added later on as a feature.

**Dashboard Test** - The test carried out is to let the user access their dashboard as it can be seen below once user is logs in or register he or she will be directed to the dashboard where she will have access to their watchlist, recommendations and trending. The user story has been achieved by providing the user with easy process to access their dashboard. 

**Test** -  [Trending and Recommendations](https://ik.imagekit.io/xsenqx8yi/user_stories_test/test_trending_and_recommendations_6Dr7Sd-SjI_.gif)
<hr>

**User Story** *- As a user, I will not have to sign up if I wish to search for a movie.*

**Search Implementation** - The implementation of the search feature was done in such a way that a user who is interested in just searching for movies or shows will not have to login, the main reason is that people may have different needs which does not involve getting registered, however by registering we offer trending movies and recommendations which are based on what they have on their watchlist. In order to achieve such dynamic recommendation feature the app collects all IDs for all watchlist movies or shows and based on that the app uses IMDB huge database to fetch all recommended shows or movies for the user. 

**Search Test** - The test below was carried to demonstrate that users can search for movies and shows but they wont be able to have a watchlist, get recommendations and what is trending. This has achieved the requirement of the user story above.

**Test** - [Search If Not Logged In](https://ik.imagekit.io/xsenqx8yi/user_stories_test/search_not_logged_in_cfnJXpxjh.gif)

<hr>

**User Story** *- As a user, I will be able to add a movie or a tv series to my watchlist.*

**Add Movies and Shows Implementation** - The way this has been implemented is by re-utilising the search feature in the home page, but by passing a variable to the rendered page I can then verify if user is logged in then we would display a button that allows for adding movies or shows. 

**Add Movies and Shows Test** - The User Story above has been implemented by allowing them users to add shows and movies to their watchlist as it can be seen in the image below. A user would select if they wish to search for a movie or show and then they would hit the search button, the results appears just below each image can then be clicked show details for that specific movie can be displayed.

**Test** - [Add Show To Watchlist](https://ik.imagekit.io/xsenqx8yi/user_stories_test/test_add_show_gmA8mpnFEUj.gif)
<hr>

**User Story** *- As a user, I will be able to remove a movie or a tv series from my watchlist.*

**Delete Movies and Shows Implementation** - The user can remove whatever is in their watchlist by clicking over one of them to display information about the movie or tv show and at the end there will be a delete and review button. The reason a review can only be edited and not deleted is because there is a intention to accumulate as much reviews as possible so one day this app can become the app that users come to review what they watch or read reviews by other users.

**Delete Movies and Shows Test** - The User Story above has been achieved by allowing user to delete a movie or show from their watchlist, as well as adding and editing a review. The reviews are directly linked to the delete button because that is the only possible way to remove them, as the reasons explained above. The User Story has been achieved as you can see below.

**Test** - [Deleting Show](https://ik.imagekit.io/xsenqx8yi/user_stories_test/test_delete_5uQEDXLea0o.gif)

<hr>

**User Story** *- As a user, I will be able to review movies and tv series I have watched off of my watchlist.*

**Review Movies and Shows Implementation** - The review was implemented to allow users to add and edit within the same form, for it to be an easy to use feature. Each movie or show in the watchlist will have a review button once clicked a modal form pops up for user to add and edit a review.

**Review Movies and Shows Test** - The user Story has been achieved by giving the user a simple form to add and edit their movies and shows reviews. As it can be seen below, if a review has already been added and the user navigates to review again the form will hold what they have reviewed.

**Test** - [Adding Review](https://ik.imagekit.io/xsenqx8yi/user_stories_test/test_add_review_V-jJ6OPvu.gif)

**Test** - [Editing Review](https://ik.imagekit.io/xsenqx8yi/user_stories_test/test_edit_review_9uIkRgBl4.gif)

<hr>

**User Story** *- As a user, I will be able to change my password.*

**Reset Password Implementation** - There are two ways for the user to change their password. First way is within the dashboard in the settings navbar option where a form pops up and user can change their password. Second way to reset or change a password is when the user is logged out as this is handy if user has forgotten password. These two were implemented to give users the way to get into their dashboard or maybe if there is a security concern they can change their password themselves. 

**Reset Password Test** - The user Story has been achieved by giving the user a simple form to add and edit their movies and shows reviews. As it can be seen below, if a review has already been added and the user navigates to review again the form will hold what they have reviewed. The tests carried below shows how both ways are done, therefore this User Story has been achieved.

**Test** - [Reset Password When Logged In](https://ik.imagekit.io/xsenqx8yi/user_stories_test/test_change_password_j2v8ql7E6.gif)

<hr>

**User Story** *- As a user, I will be able to see trending movies and tv series.*

**Trending Movies Implementation** - The implementation of trending was done by using IMDB database, where it provides with the API resource. The tricky issues during implementation was that they split their API in such way that you inly get IDs for movies and shows that are trending then after you have to query another query for details and another query for images. All this becomes very expensive for the user who would have to wait for long for all the queries to finish, hence why, I have only added images for trending and for recommendations.

**Trending Movies Test** - The app has the feature to fetch latest trending entertainment movies or shows whenever user login or register. Trending cannot be changed by the user and its purely based on IMDB API. This User Story has been achieved by displaying movies that are trending and user can always search for them in the search menu.  

**Test** - [Trending](https://ik.imagekit.io/xsenqx8yi/user_stories_test/test_trending_and_recommendations_6Dr7Sd-SjI_.gif)
<hr>

**User Story** *- As a user, I will be able to get recommended movies or tv series based on my watchlist.*

**Recommendations Implementation** - The recommendations are achieved by getting IDs a user's watchlist then using IMDB API to query movies or shows that could be similar every time a user adds a movie or show this are collected into a list which one ID is chosen at random and queried to get recommendations. In order to avoid querying IMDB API on every refresh the recommendations are cached one per time that a user registers or logins. This means that you wont always get the same recommendations. If there is no entries in the watchlist the app will display a message for the user to add movies or shows to get recommendations.

**Recommendations Test** - The User Story has been achieved as mentioned above, users can get recommendations based on their watchlist once every time they login. This can be seen on the test below.

**Test** - [Recommendations](https://ik.imagekit.io/xsenqx8yi/user_stories_test/add_movie__xqgom_HAT.gif)

<hr>

[Back To Top](#user-experience-design---ux)

## Form Validations

The form validations are implemented in all forms, I have used jQuery Form Validator plugin as it gives me the functionality I needed to achieve the validations as well as other features in the app.

**Registration Form** - To implement validation in this form I have chosen to give as much freedom as possible to the user so the main constrains are passwords and usernames that must be minimum of 8 characters long, first name and last name maximum 30 characters long. Finally, the email has to have the correct format.

**Test** - [Registration Form](https://ik.imagekit.io/xsenqx8yi/form_validation/signup_validation_c-e4EadTF.gif)

<hr>

**Login Form** - The login form has validation for email and a minimum charter length of 8. The password field has to have a minimum of 8 characters long.

**Test** - [Login Form Validation](https://ik.imagekit.io/xsenqx8yi/form_validation/login_validation_UQtKw2BjF.gif)

<hr>

**Change Password Form** - The change password form is located in the settings from the navbar menu where form pops up so user can change password. It follows same validation as the other ones.

**Test** - [Change Password Form Validation](https://ik.imagekit.io/xsenqx8yi/form_validation/settings_form_JXp7stM2r4F.gif)

<hr>

**Reset Password Form** - The reset form validation is based on the user to enter two passwords that match, if it does not it will throw validation error. It will validate for email requirement as the other forms.

**Test** - [Reset Password Form Validation](https://ik.imagekit.io/xsenqx8yi/form_validation/reset_form_validation_6qU1UigbBYE.gif)

<hr>

**Search Form** - The search form only validation is to make sure user has entered something before a search is performed to avoid querying the database unnecessarily.

**Test** - [Search Form Validation](https://ik.imagekit.io/xsenqx8yi/form_validation/search_form_validation_iNs8ltQ5R.gif)

<hr>

[Back To Top](#user-experience-design---ux)

## Responsiveness  Test

The responsiveness of all UI components are good since it resizes in all screen sizes. To achieve this I have used the UIkit Framework where similar to Bootstrap I have used components to reduce CSS usage and repetitiveness. I have verified this on Chrome, Safari, Firefox and Edge they all behaved appropriate to screen sizes. On addition to this I have used Google Dev tools in the inspection mode to valuate how the app would look like when displayed in smaller sizes. Below I have tested the dashboard, forms and homepage.


- [Responsiveness Dashboard](https://ik.imagekit.io/xsenqx8yi/Responsiveness_Tests/dashboard_responsiviness_test_k3u4zzt6c.gif)
- [Responsiveness Forms](https://ik.imagekit.io/xsenqx8yi/Responsiveness_Tests/forms_responsiviness_test_Asn498lgIGZ.gif)
- [Responsiveness Home Page](https://ik.imagekit.io/xsenqx8yi/Responsiveness_Tests/home_responsiviness_test_s2GP0S_TT.gif)

<hr>

[Back To Top](#user-experience-design---ux)

## Authentication Test

The authentication was implemented using JWT which are created for the user when they login in or register. All tokens generated during these operations lasts for 7 days, after that user has to login again. Tokens are stores in cookies and accessed via the app to check if user is logged in or not.

- [Login Details Not Valid](https://ik.imagekit.io/xsenqx8yi/authentication/login_details_not_valid_Jmg8LyHcZ.gif)
- [Redirected Not Authenticated](https://ik.imagekit.io/xsenqx8yi/authentication/redirected_not_authenticated_hkyogkuUOhs.gif)
- [Email Already Exists](https://ik.imagekit.io/xsenqx8yi/authentication/register_details_email_already_exist_EcSTl433w.gif)
- [Cannot Access Home Logged In](https://ik.imagekit.io/xsenqx8yi/authentication/cannot_access_home_when_logged_in_CkPk1DzA1ZLK.gif)

<hr>

[Back To Top](#user-experience-design---ux)

## Password Reset Test

The password reset feature was tested multiple times with Gmail, Outlook and Yahoo to check if users receive the reset email and if it works, below you will find a gif showing that it works and that a user can reset their password this test was done with Gmail.

- [Email Reset Password](https://ik.imagekit.io/xsenqx8yi/form_validation/forgot_form_validation_QWwwx61dShV.gif)

<hr>

[Back To Top](#user-experience-design---ux)

# Deployment

## MongoDB

 This project requires MongoDB URI, so it is important to have it setup before pulling the project. I have split into 3 steps below showing how MongoDB can be setup. 
	
### STEP 1 - Create cluster project
![enter image description here](https://ik.imagekit.io/2a1in3cldn/MS2/mongo_strapi/mongoDB_setup_part_1_fbk2OzG_xPCb.gif)


### STEP 2 - Create Database User and Setup Network Access.
![enter image description here](https://ik.imagekit.io/2a1in3cldn/MS2/mongo_strapi/mongoDB_setup_part_1_fbk2OzG_xPCb.gif)


###  STEP 3 - Get database credentials.
![enter image description here](https://ik.imagekit.io/2a1in3cldn/MS2/mongo_strapi/mongoDB_setup_part_3_AjIeUVHn-.gif)

<hr>

[Back To Top](#user-experience-design---ux)

## SendGrid

To setup Flask Mail with SendGrid you must create an account with them and then you will be able to attain an API key and also verify the email sender domain as this will help your emails to not get blocked. I have prepared a visualisation below of how the SendGrid configuration would look so it makes it easier for you to configure things.

![enter image description here](https://ik.imagekit.io/xsenqx8yi/send_grid/settings_form_DE8RdoGc7K2.gif)

<hr>

[Back To Top](#user-experience-design---ux)

## IMDB API

This App currently make use of IMDB API database to fetch for movie content, and it is required that a KEY provided by them is set the environment variables so the app can function properly. Please follow these steps to obtain the IMDB API Key:
- Step 1 - Register with RAPID API [here](https://rapidapi.com/auth/sign-up). 
- Step 2 -  Subscribe for IMDB API [here](https://rapidapi.com/amrelrafie/api/movies-tvshows-data-imdb). 
Once these steps have been carried out after you have subscribed you will be provided with a KEY which will be placed in your .env file. 

<hr>

[Back To Top](#user-experience-design---ux)

## Local Deployment

###  Download Project & Github CLI
 
-  You can select to clone my repository via CLI.
	
	1. Open terminal in your preferred IDE.
	2. Navigate to the folder where you wish to close the repository.
	3. Enter `git clone https://github.com/tpsantos2120/unboxit.git`
	4. The project will be pulled to your current directory.

- To download this project do the following:
	1. Navigate to the menu in the very top of this page
	2. Click on the **Code** button.
	3. Then click on **Download.zip**
		- **Note** you can also click [here](https://github.com/tpsantos2120/unboxit/archive/refs/heads/main.zip) to download the zip file. 
	4. Choose the directory you wish to download it.
	5. Unzip file.
	6. Once unzipped project will be ready.

### Environment Variables 

**IMPORTANT**

Please make sure the your .env file is added to your gitignore file so your **API Keys** are not exposed if you commit to **Github**, though regardless environment files must always be included in the gitignore and .env file must be added to the top root folder.

The **JWT_SECRET_KEY** and ***SECRET_KEY*** can be generated using this  [password generator](https://passwordsgenerator.net/), or any other generator of your choice.


    ENV="development"
    IP="0.0.0.0"
    PORT="5000"
    IMDB_API_HOST="movies-tvshows-data-imdb.p.rapidapi.com"
    IMDB_BASE_URL="https://movies-tvshows-data-imdb.p.rapidapi.com/"
    IMDB_SECRET_KEY="YOUR KEY PROVIDED BY IMDB"
    SECRET_KEY="GENERATED KEY"
    JWT_SECRET_KEY="GENERATED KEY"
    MONGODB_PRODUCTION="SAME URI JUST CHANGE DATABASE NAME IN URI"
    MONGODB_TESTING ="SAME URI JUST CHANGE DATABASE NAME IN URI"
    MONGODB_DEVELOPMENT ="SAME URI JUST CHANGE DATABASE NAME IN URI"
    MAIL_SERVER='smtp.sendgrid.net'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME='apikey'
    MAIL_PASSWORD="YOUR API KEY PROVIDED BY SENDGRID"
    MAIL_DEFAULT_SENDER="YOUR DEFAULT SENDER EMAIL"

### Installing Dependencies and Running The App

Once you have cloned using your favourite IDE and obtained all necessary Keys, URI and setup the .env file, you will be ready to install all dependencies and run the app, execute the following in your IDE integrated terminal:

1.  `$ pip install -r requirements.txt`
2. `python run.py`

If all went correctly the app should be served at `http://127.0.0.1:5000/`.

<hr>

[Back To Top](#user-experience-design---ux)

## Heroku Deployment

To deploy the app publicly you will have to create an account with Heroku and create a new app before deploying it.

1.  Ensure the Procfile and requirements.txt files exist are present and up-to-date in your local repository.  
    Requirements:
    
    ```
    pip3 freeze --local > requirements.txt
    ```
    
2.  The Procfile should contain the following line:
    ```
    web: gunicorn --timeout=90 --workers=2 run:app
    ```
3. Once your app is created in Heroku navigate to the settings.
4. Click on the button **Reveal Config Vars**.
5. Add all your environment variables that was created during **Local Deployment**.
6. Make sure that you have pushed the app to github.
7. Connect your Github account to Heroku by going to Deploy tab and select Github as a **Deployment Method**.
8. Under the deploy tab, click on **Deploy Branch**.

<hr>

[Back To Top](#user-experience-design---ux)

# Credits

- [Background SVG Image](https://www.svgbackgrounds.com/)
- [SendGrid Email Setup](https://sendgrid.com/blog/sending-emails-from-python-flask-applications-with-twilio-sendgrid/) 
-   [Stackoverflow](https://stackoverflow.com/)  community for making their useful content available online.
-   I would like to thank my mentor [Simen](https://github.com/Eventyret)  for his tips about how to develop better software that is maintainable and readable.
- All documentation of all Flask extensions that I have used throughout the project. I have attached them in the **Resources Section** of this readme.

<hr>

[Back To Top](#user-experience-design---ux)

# Acknowledgements

-  I would like to mention my mentor here. Thank you [Simen](https://www.linkedin.com/in/simendaehlin/) for the support and guidance throughout the project. I believe you were crucial in helping and guiding me through all the ins and outs and I would like to recognise your Grandmaster title from yet another student. 

- Last but not least, I would like to thank the [Code Institute](https://codeinstitute.net/) for the course content and amazing support they have always provided me!

<hr>

[Back To Top](#user-experience-design---ux)