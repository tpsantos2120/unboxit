
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
	- As a user, I will be able to review movies and tv series I have watched off of my watchlist.
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

### **Planning**

The implementation will start by the backend working through the frontend. I will be setting up Python and Flask folders and environment. Next, I will setup MongoDB using the database structure planned in the Structure & Skeleton section. Once I am happy with these setups I will configure my environment variables and connect to the database. Afterwards, all API routes would then be written whilst performing some tests along the way to check if it works. When I have all API routes, I will create the HTML files templates files based on the Wireframes. Next I will use IMDB from Rapid API to consume all the APIs needed when users are searching for movies and tv series.   

### **Development**

The development was implemented by working from the backend towards the frontend, unless I required a view to visualise results, but in general it was developed in that manner. All API was tested as they were being developed by using **POSTMAN**. During implementation I tried to follow a MVC pattern as much as possible, so I have split my files in several folders, though all of it could and will be refactored I believe I did a good job in getting things more maintainable and readable than I would without splitting the logic from view and so on.

### **Project Structure**

The project was structured in 5 folders, each folder contains files and or subfolder to structure the project in a easy and maintainable manner. Below you will find the project structure and what each one of them do:

- **Models**
	- **[db](https://github.com/tpsantos2120/unboxit/blob/main/unboxit/models/db.py)** -  This file will initialise **MongoEngine** so it can be used within the Models folder and it will give the functionality to use Documents and enforce schemas on **MongoDB**.
	- **[models](https://github.com/tpsantos2120/unboxit/blob/main/unboxit/models/models.py)** - Once **DB** is instantiated, it is then imported and by using classes we pass that instance where we are able to create documents or better said schemas.

- **Resources**
- 
	- **[app_api](https://github.com/tpsantos2120/unboxit/tree/main/unboxit/resources/app_api)** -  In this folder, it holds all the files that has **API Resources** that are related to the app itself not the backend. For example, routes to dashboard or home.
	
	- **[db_api](https://github.com/tpsantos2120/unboxit/tree/main/unboxit/resources/db_api)** - On the other hand this folder which also reference **API** is directly related to resources that are accessed from or to **MongoDB Atlas**. For example, logging and registering a user or adding movies or tv shows.

	- **[routes](https://github.com/tpsantos2120/unboxit/tree/main/unboxit/resources/routes)** - This folder is directly related to the **APIs** mentioned above, as this has a **routes file** where all routes are registered using **Flask Restful**.

	- **[utils](https://github.com/tpsantos2120/unboxit/tree/main/unboxit/resources/utils)** - The **utils** folder initialises and registers the **Cache**, **JWT** and **Errors**. The **Cache** is used to cache queries to the database queries to minimize queries to **IMDB** and **MongoDB**. The **JWT** is used to protect routes, generate tokens and it the important for the way authentication happens in the app. Finally, there the **Errors** file that is used to implement custom error handling by specifying which errors to customise with which error messages to return, these are then used with **TRY**, **EXCEPTION** and **RAISE** throughout the app. 

- **Services**

	- **[mail_service](https://github.com/tpsantos2120/unboxit/blob/main/unboxit/services/mail_service.py)** - The implementation for emailing was to offer users the feature to reset their passwords. In order to do this, I have used **Flask Mail** and **SendGrid**. The way this works is that **Flask Framework** uses **Flask Mail** extension to send emails through **SendGrid**. In addition, **SendGrid** is configured to use my personal email that I created for the purpose of this project, unboxit@tsantos.dev.

- **Static**
	- **[static](https://github.com/tpsantos2120/unboxit/tree/main/unboxit/static)** - This folder is where the assets are located. I have used quite a bit of JavaScript to handle dynamic content, so I have split them in several files, each file will be doing something specific.

- **Templates**
	- **[templates](https://github.com/tpsantos2120/unboxit/tree/main/unboxit/templates)** - All HTML files were split into 3 folders Views, Layout and Components. I have chosen to split them in folders to make it easier to understand as it currently contains 23 files this way it makes a bit easier to cope with bugs, if any.

### **Implementation Issues and Bugs**


# Testing

### User Stories Tests

**User Story** *- As a user, I will have to sign up if they wish to be able to save movies or tv series to my watchlist.*

**Dashboard Implementation** - The registration form has several form details, the reason for it to be implemented this way is so that in the future there will be more customisation and features such as logging in with google authentication and allowing user to change their details.

**User Registration Test** - The test carried out allows the user to perform a registration, considering that there is no existing email. Following the registration user is redirected to the dashboard which initially will be empty. I have chosen to capture more details such as email because I tend to make it official app at one point, which also the reset password feature requires an email. This user story has been achieved as you can see below a mock operation of a user registering.
 
![User Registration](https://ik.imagekit.io/xsenqx8yi/user_stories_test/test_register_user_DZoZ8UFcu.gif)
<hr>

**User Story** *- As a user, I will be able to access a dashboard where I can view my watchlist and recommendations.*

**Dashboard Implementation** - I have decided to implement the dashboard using cards from the UIKIT framework. The reason behind is that they are able to hold quite a lot of images inside the slider before it starts to get slow. Though, I have not introduced pagination this is something that will be added later on as a feature.

**Dashboard Test** - The test carried out is to let the user access their dashboard as it can be seen below once user is logs in or register he or she will be directed to the dashboard where they will have access to their watchlist, recommendations and trending. The user story has been achieved by providing the user with easy process to access their dashboard. 

![Login](https://ik.imagekit.io/xsenqx8yi/user_stories_test/test_trending_and_recommendations_6Dr7Sd-SjI_.gif)
<hr>

**User Story** *- As a user, I will not have to sign up if they wish to search for a movie.*

**Search Implementation** - The implementation of the search feature was done in such a way that a user who is interested in just searching for movies or shows will not have to login, the main reason is that people may have different needs which does not involve getting registered, however by registering we offer trending movies and recommendations which are based on what they have on their watchlist. In order to achieve such dynamic recommendation feature the app collects all IDs for all watchlist movies or shows and based on that the app uses IMDB huge database to fetch all recommended shows or movies for the user. 

**Search Test** - The test below was carried to demonstrate that users can search for movies and shows but they wont be able to have a watchlist, get recommendations and what is trending. This has achieved the requirement of the user story above.

![Search](https://ik.imagekit.io/xsenqx8yi/user_stories_test/search_not_logged_in_cfnJXpxjh.gif)

<hr>

**User Story** *- As a user, I will be able to add a movie or a tv series to my watchlist.*

**Add Movies and Shows Implementation** - The way this has been implemented is by re-utilising the search feature in the home page, but by passing a variable to the rendered page I can then verify if user is logged in then we would display a button that allows for adding movies or shows. 

**Add Movies and Shows Test** - The User Story above has been implemented by allowing them users to add shows and movies to their watchlist as it can be seen in the image below. A user would select if they wish to search for a movie or show and then they would hit the search button, the results appears just below each image can then be clicked show details for that specific movie can be displayed.

<img src="https://ik.imagekit.io/xsenqx8yi/user_stories_test/test_add_show_gmA8mpnFEUj.gif"/>
<hr>

**User Story** *- As a user, I will be able to remove a movie or a tv series from my watchlist.*

**Delete Movies and Shows Implementation** - The user can remove whatever is in their watchlist by clicking over one of them to display information about the movie or tv show and at the end there will be a delete and review button. The reason a review can only be edited and not deleted is because there is a intention to accumulate as much reviews as possible so one day this app can become the app that users come to review what they watch or read reviews by other users.

**Delete Movies and Shows Test** - The User Story above has been achieved by allowing user to delete a movie or show from their watchlist, as well as adding and editing a review. The reviews are directly linked to the delete button because that is the only possible way to remove them, as the reasons explained above. The User Story has been achieved as you can see below.

**Deleting**
![Deleting](https://ik.imagekit.io/xsenqx8yi/user_stories_test/test_delete_5uQEDXLea0o.gif)

<hr>

**User Story** *- As a user, I will be able to review movies and tv series I have watched off of my watchlist.*

**Review Movies and Shows Implementation** - The review was implemented to allow users to add and edit within the same form, for it to be an easy to use feature. Each movie or show in the watchlist will have a review button once clicked a modal form pops up for user to add and edit a review.

**Review Movies and Shows Test** - The user Story has been achieved by giving the user a simple form to add and edit their movies and shows reviews. As it can be seen below, if a review has already been added and the user navigates to review again the form will hold what they have reviewed.

**Adding Review**
![enter image description here](https://ik.imagekit.io/xsenqx8yi/user_stories_test/test_add_review_V-jJ6OPvu.gif)

**Editing Review**
![enter image description here](https://ik.imagekit.io/xsenqx8yi/user_stories_test/test_edit_review_9uIkRgBl4.gif)

<hr>

**User Story** *- As a user, I will be able to change my password.*

**Reset Password Implementation** - There are two ways for the user to change their password. First way is within the dashboard in the settings navbar option where a form pops up and user can change their password. Second way to reset or change a password is when the user is logged out as this is handy if user has forgotten password. These two were implemented to give users the way to get into their dashboard or maybe if there is a security concern they can change their password themselves. 

**Reset Password Test** - The user Story has been achieved by giving the user a simple form to add and edit their movies and shows reviews. As it can be seen below, if a review has already been added and the user navigates to review again the form will hold what they have reviewed. The tests carried below shows how both ways are done, therefore this User Story has been achieved.

**Reset Password When Logged In**
![enter image description here](https://ik.imagekit.io/xsenqx8yi/user_stories_test/test_change_password_j2v8ql7E6.gif)

<hr>

**User Story** *- As a user, I will be able to see trending movies and tv series.*

**Trending Movies Implementation** - The implementation of trending was done by using IMDB database, where it provides with the API resource. The tricky issues during implementation was that they split their API in such way that you inly get IDs for movies and shows that are trending then after you have to query another query for details and another query for images. All this becomes very expensive for the user who would have to wait for long for all the queries to finish, hence why, I have only added images for trending and for recommendations.

**Trending Movies Test** - The app has the feature to fetch latest trending entertainment movies or shows whenever user login or register. Trending cannot be changed by the user and its purely based on IMDB API. This User Story has been achieved by displaying movies that are trending and user can always search for them in the search menu.  

**Trending**

<img src="https://ik.imagekit.io/xsenqx8yi/user_stories_test/test_trending_and_recommendations_6Dr7Sd-SjI_.gif"/>
<hr>

**User Story** *- As a user, I will be able to get recommended movies or tv series based on my watchlist.*

**Recommendations Implementation** - The recommendations are achieved by getting IDs a user's watchlist then using IMDB API to query movies or shows that could be similar every time a user adds a movie or show this are collected into a list which one ID is chosen at random and queried to get recommendations. In order to avoid querying IMDB API on every refresh the recommendations are cached one per time that a user registers or logins. This means that you wont always get the same recommendations. If there is no entries in the watchlist the app will display a message for the user to add movies or shows to get recommendations.

**Recommendations Test** - The User Story has been achieved as mentioned above, users can get recommendations based on their watchlist once every time they login. This can be seen on the test below.

**Recommendations**
![enter image description here](https://ik.imagekit.io/xsenqx8yi/user_stories_test/add_movie__xqgom_HAT.gif)

### Form Validations

The form validations are implemented in all forms, I have used jQuery Form Validator plugin as it gives me the functionality I needed to achieve the validations as well as other features in the app.

**Registration Form** - To implement validation in this form I have chosen to give as much freedom as possible to the user so the main constrains are passwords and usernames that must be minimum of 8 characters long, first name and last name maximum 30 characters long. Finally, the email has to have the correct format.

![enter image description here](https://ik.imagekit.io/xsenqx8yi/form_validation/signup_validation_c-e4EadTF.gif)

**Login Form** - The login form has validation for email and a minimum charter length of 8. The password field has to have a minimum of 8 characters long.

![enter image description here](https://ik.imagekit.io/xsenqx8yi/form_validation/login_validation_UQtKw2BjF.gif)

**Change Password Form** - The change password form is located in the settings from the navbar menu where form pops up so user can change password. It follows same validation as the other ones.

![enter image description here](https://ik.imagekit.io/xsenqx8yi/form_validation/settings_form_JXp7stM2r4F.gif)

**Reset Password Form** - The reset form validation is based on the user to enter two passwords that match, if it does not it will throw validation error. It will validate for email requirement as the other forms.

![enter image description here](https://ik.imagekit.io/xsenqx8yi/form_validation/reset_form_validation_6qU1UigbBYE.gif)

# Deployment