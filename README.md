
# Site Objective
Racing Cars Reviews-Page is where the user will find more about various information of motorsport categories currently competing in their own.

The live link can be found here: [Live Site](https://hkcarracing.herokuapp.com/)

![Mock Up](/djcarracing/docs/readme_imgs/mockup-responsive.jpg)


# UX Design

## The-Strategy-Plane

### Site-Goals

The site aim to give the user a brief review of the main motorsport categories of cars such as: Formula 1, IndyCar Series and Karting, for instance.

The user can access the contents, make their comments of the reviews, update and delete them, once their are authenticated. They can also submit any queries on the contact page, to the authors.

### Agile Methodologies

This project was developed using agile methodologies by categorise them into three instances: to-do, in-progress and done.

All issues were prioritized under the labels: 'Low Priority', 'Medium Priority' and 'High Priority'. They were assigned the user story pointed according to their needs. "High Priority" stories were completed first, following by "Medium Priority" and last but not least "Low Priority". It was done this way to ensure that all core requirements were completed first to give the project a complete user experience, with the nice to have features being added should there be capacity.

The Kanban board was created using github projects and can be located here and can be viewed to see more information on the project cards. All stories except the documentation tasks have a full set of acceptance criteria in order to define the functionality that marks that story as complete.

![Dashboard](/djcarracing/docs/readme_imgs/user%20stories%20dasboard.jpg)

### Project User Stories

The following user stories were completed developed as below:

* As a Site Admin I can read, create, update and delete reviews so that I can manage my review list

* As a User/Site Admin I can comment the reviews posted so that I can interact with the author of the review

* As a Site Admin I can approve or desaprove comments so that I can filter out objectionable comments

* As a User I can ** view a paginated list of reviews** so that I can easily select a review to view

* As a Site User / Admin I can ** view comments on an individual review** so that I can read the conversation and comments

* As a User I can ** update and edit reviews** so that I can amend errors or add extra information

* As a User I can ** create an account ** so that I can I can comment and rating the review

* As a Site Admin I can ** create drafts of my reviews** so that I can finish writing the content later

* As a User I can rate the content of the review so that I can interact with the author and give my feedback

* As a User I can ** easily see the purpose of the site from the landing page** so that I can see if the site and its content are relevant to me

* As a User I can ** see the exerpt of the review on the front page** so that I can choose if the content is interesting to me and by clicking on it, I can see the full review

* As a User I can ** delete a comment I made** so that I can be certain that my comment is exactly what I meant to make

* As a User I can submit a a message to the author so that I can interact with them


## The-Scope-Plane

* Responsive Design - Site should be fully functional on all devices

* Ability to perform CRUD functionality 

* Review Page with information about racing cars

## The-Structure-Plane

### Features

**Navigation Bar**

The Navigation Bar contain links for All Reviews, Sign Up, Login and Contact and are visible to all visitors.

![Navigation Bar](/djcarracing/docs/readme_imgs/nav-bar.jpg)

* All Reviews page (index.html)

It works as a front page showing a list of all reviews from the author
It has a convidative message "What is your passion?" for those that are affictionated about motorsport.
It also has a video of a racing car on a track, giving the idea of speed and robustness.

![Message](/djcarracing/docs/readme_imgs/passion-img.jpg)


It also lists all reviews that the author have made about racing cars and if there are more than 04 images per page, the auto paginated services will split the list in further pages.

![Review List](/djcarracing/docs/readme_imgs/review-list.jpg)


The front page also has a footer, available for all users, either authenticated or not.
It contains the a description of the Page (Racing Cars Page) and links to the following social media: Twitter (or now X), Instagram, Youtube and Facebook.

![Footer](/djcarracing/docs/readme_imgs/footer.jpg)


* Sign Up Page (signup.html)

This is were the user can create their account and therefore, being able to make comments, update them and delete them, once their are logged in.
It has a message and a form, which the user can create their account.



![Sign Up](/djcarracing/docs/readme_imgs/signup.jpg)

* Login Page (signin.html)

Here, the user once logged in and once again will be able to to make comments, update them and delete them.
Once they are logged in, the Navigation Bar will be listing only 'All Reviews', 'Logout' and 'Contact Us' options

![Sign In](/djcarracing/docs/readme_imgs/signin.jpg)



* Sign Out Page (logout.html)

This page is only accessible for authorised users and they must be logged in order to logout

![Sign Out](/djcarracing/docs/readme_imgs/signout.jpg)

* Contact Us Page (contact.html)

Here is where the user, authenticated or not, can access, so they can submit queries, suggestions and interactions with the authors

**Features left to implement**
Some of these features will be resumed in the future, for improving site:
* adjust like or rating feature
* improve minor Bootstrap/CSS styling, in order to 


## The-Skeleton-Plane
## Wireframes

All Reviews Template

![All Reviews](/djcarracing/docs/readme_imgs/index%20.jpg)

![All Reviews-mobile](/djcarracing/docs/readme_imgs/index%20mobile.jpg)

Sign Up Template

![Sign Up](/djcarracing/docs/readme_imgs/Sign%20Up.jpg)

![Sign Up-mobile](/djcarracing/docs/readme_imgs/Sign%20Up%20mobile.jpg)


Sign In Template

![Sign In](/djcarracing/docs/readme_imgs/Sign%20In.jpg)

![Sign In-mobile](/djcarracing/docs/readme_imgs/Sign%20In%20mobile.jpg)

Sign Out Template

![Sign out](/djcarracing/docs/readme_imgs/Sign%20Out.jpg)

![Sign out-mobile](/djcarracing/docs/readme_imgs/Sign%20Out%20mobile.jpg)


Contact template

![Contact](/djcarracing/docs/readme_imgs/Contact.jpg)

![Contact-mobile](/djcarracing/docs/readme_imgs/Contact%20mobile.jpg)


### Database-Design

The database was designed to allow CRUD functionality to be available to registered users, when signed in. The user model is at the heart of the application as it is connected the the main booking and menu tables, linked by primary/foreign key relationships.


Entity relationship diagram was created using [Dbeaver](https://www.dbeaver.com/) and shows the schemas for each of the models and how they are related.

![Entity Relationship Diagram](/djcarracing/docs/readme_imgs/db-.jpg)


### Colour-Scheme

The main color schemes for the website are dark-gray ( #4A4A4F ) ground. White font (#FFF) 

### Typography

The Racing Sans One font was used throughout the website. This font is from google fonts and was imported into the style sheet.

# Technologies Used

- GitHub
  - Code is hosted on GitHub
- Git
  - Used to commit and push code during the development of the Website
- HTML
  - The structure of the Website was developed using HTML as the main language.
- CSS
  - The Website was styled using custom CSS .
- JavaScript
  - JavaScript was used to make the custom messages.
- Python
  - Python was the main programming language used for the application using the Django Framework.
- Font Awesome
  - This was used for various icons throughout the site
- TinyPNG
  - This was used to compress the featured images of the cars
- Wireframe
  - wireframes were created using WireframePro from https://wireframepro.mockflow.com/


# Testing

**Authentication**

Navigate to (https://hkcarracing.herokuapp.com/)

Description:

Ensure a user can sign up to the website

Steps:

1. Click on Sign Up at the Navigation Bar
2. Enter username, email(optional) and password (repeat)
3. Click Sign up

Expected:

A message pops up stating the the account has been created successfully and the user is automatically logged in

Actual: 

A message pops up stating the the account has been created successfully and the user is automatically logged in

<hr>

Description:

Ensure a user can log in once signed up

Steps:
1. Click on Loggin at the Navigation Bar
2. Enter login details created 
3. Click login

Expected:

A message pops up stating the user is logged in successfully as their chosen username and it redirected to the All Reviews page

Actual:

A message pops up stating the user is logged in successfully as their chosen username and it redirected to the All Reviews page

<hr>

Description:

Ensure a user can sign out

Steps:

1. Login to the website
2. Click the logout button
3. Click confirm on the confirm logout page

Expected:

User is logged out

Actual:

User is logged out

<hr>

**Comment a Review**

Description:

Ensure the user can comment a review posted by the author

Steps:

1. Once logged in, click on a selected review in the All Reviews Page
2. The site will redirect to the review detail page of the review
3. Fill out the form "Leve a comment" with your comment
4. Click Submit

Expected:

A message states "Comment awaiting moderation" will pop up

Actual:

A message states "Comment awaiting moderation" will pop up

<hr> 

**Update or Delete a Comment**

Description:

Ensure the user can update (edit)  a comment.

Steps:

1. Once logged in and the moderator has been approved your comment
2. Go back to your comment
3. Click Update, just below your comment
4. Modify your comment as you wish
5. Click Update to confirm or cancel to cancel and go back the All Reviews Page


Expected:

Update successfully as a message pops up to confirm

Actual:

Update successfully as a message pops up to confirm

<hr>

Description:

Ensure the user can delete a comment.

Steps:
1. Once logged in and the moderator has been approved your comment
2. Go back to your comment
3. Click Delete, just below your comment
4. Click Yes

Expected:

Comment is successfully deleted

Actual:

Comment is successfully deleted

<hr>

**Footer**

Testing was performed on the footer links by clicking the icons and ensuring that all social media were redirected to their specific website.
Tests performed as expected.

## Validation

### HTML

All pages were tested through the [w3 HTML Validator](https://validator.w3.org/). 
There were some errors due to stray script tags, misuse of headings within spans and some unclosed elements. 
All of these issues were corrected and all pages passed validation.

![HTML Validator](/djcarracing/docs/readme_imgs/html-validator-after.jpg)


### CSS

All pages were tested through the (https://jigsaw.w3.org/) CSS Validator.
No errors were found.

![CSS Validator](/djcarracing/docs/readme_imgs/css-validator.jpg)



# Deployment

## HEROKU
The site was deployed to Heroku (https://www.heroku.com/). The steps to deploy are as follows:

- Navigate to heroku and create an account
- Click the new button in the top right corner
- Select create new app
- Enter app name
- Select region and click create app
- Click the resources tab and search for Heroku Postgres
- Select hobby dev and continue
- Go to the settings tab and then click reveal config vars
- Add the following config vars:
  - SECRET_KEY: (Your secret key)
  - DATABASE_URL: (This should already exist with add on of postgres)
  - EMAIL_HOST_USER: (email address)
  - EMAIL_HOST_PASS: (email app password)
  - CLOUNDINARY_URL: (cloudinary api url)
- Click the deploy tab
- Scroll down to Connect to GitHub and sign in / authorize when prompted
- In the search box, find the repositoy you want to deploy and click connect
- Scroll down to Manual deploy and choose the main branch
- Click deploy

The app should now be deployed.


# Credits

## Images

All images were selected using (https://pexel.com/) image storages.


## Acknowledgments

I would like to thank all the lecturers of CI for their unique classes, as well as their tutors and specially my mentor Daisy Mc Girr for her patience and priceless guidance.
