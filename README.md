# COVID-19 Vaccine Dashboard

## Purpose

The purpose of our COVID-19 dashboard is to help make information about the vaccine more publically available and easy to understand. As well, the dashboard will serve as a way to upload and save an image of your COVID-19 vaccine card for easy retrieval and back-up storage.

## Usage

**Our application is deployed and now available:
[COVID-19 Vaccine Dashboard Site](http://ec2-52-14-14-132.us-east-2.compute.amazonaws.com/)**

To run the application locally, first clone the git repository:

```
git clone https://github.com/catherine-oliver/Bioinformatics-Group.git
```

Next, navigate into the bioi-group-project-front-end directory and run the following command:

```
npm run serve
```

Now the front-end application can be accessed from the url **localhost:8080**

The back-end api can be started by navigating to the back-end directory, and running:

```
source flaskenv/Scripts/activate
set FLASK_APP=api.py
python -m run.py
```

## Documentation

Our documentation can be found on our github pages [here](https://catherine-oliver.github.io/Bioinformatics-Group/)

## Functionality
### General Information

The general information page contains a summary of what the COVID-19 vaccine is and how it generates immunity within our bodies. We have included data from peer-reviewed sources, as well as a video from Simple Explained (https://www.youtube.com/channel/UCnxrdFPXJMeHru_b4Q_vTPQ) which can help make sense of the scientific jargon surrounding the COVID-19 vaccine. Additionally, we have a section discussing the safety of the vaccine supported by peer-reviewed literature. 

### Vaccine Data Visualization

The data visualization page allows users to retrieve data regarding vaccinated individuals in the US. The page contains an interactive map of the United States on the left side, which the users can click to select a state. Beneath this, there is a form where the users can also select an age range and a vaccine manufacturer. The state selection is required, and the age range and vaccine manufacturer are optional. Once the desired filtered have been selected, the user can press the submit button. The number of vaccinated individuals in each category will be displayed in the right side of the page.

### Vaccine Card Storage

The vaccine card storage functionality consists of 3 pages that work together to allow individuals to store and retrieve their vaccine card. The image itself is tied to an account. A user can create an account on the Create Account page which requires a username, an 8+ character long password, and an image file to be submitted. Next, a user can login using their username and password on the login page. Upon a successful login, the user will be directed to the vaccine card viewing page where their vaccine will be displayed.


## Release Notes
### 08/13/2021
- Created the database refresh functionality
- Modified API to support different environments (test/dev and production)
- Automated the deployment of our application to an AWS instance using Jenkins
- Developed automated documentation (https://catherine-oliver.github.io/Bioinformatics-Group/)
   - Front-End and Back-end Documentation completed
- Wrote additional unit tests:
   - Validating that null data returned in the getVaccineData() API hook is changed to "Unreported"
   - Validating that passing a state only to the getVaccineData() API hook returns the correct data
   - Validating that passing a state and age range to the getVaccineData() API hook returns valid values for both
   - Validating that passing a state, age range, and vaccine type to the getVaccineData API hook returns valid data for all fields.
   - Checks that providing valid login credentials to the login() API hook returns an HTTP 200 status
   - Checks that providing an invalid username to the login() API hook returns an HTTP 401 status
   - Checks that providing an invalid password and valid username to the login() API hook returns an HTTP 401 status
   - Checks that sending an empty authentication header to the getCard() API hook returns an HTTP 400 status
   - Checks that sending an authentication header containing an invalid access token to the getCard() API hook returns an HTTP 400 status
- Conducted Manual Application Testing
### 07/29/2021
- Updated README Documentation with description of application
- Created the account create page
- Created the login page
- Created the vaccine card viewing page
- Developed the client-side manipulation and HTTP request methods
- Created API handler functions for creating a user, logging in, and grabbing a vaccine card
- Developed a user authentication system using JSON Web Token
- Created the User table in the database
- Created unite tests for
   - Loading the Content of the login page
   - Loading the content of the account creation page
   - Validating the client-side variables reflect what the user entered in input fields including:
     - The username field on the login and account creation pages
     - The password field on the login and account creation pages
   - Validating that entering a password less than 8 characters triggers and error message on the login and account creation pages
   - Validating that a adding a form error for the account creation page updates the HTML
### 07/15/2021
- Updated README Documentation with description of application
- Created data visualization Page
- Create interactive SVG Map of the United States
- Developed client side manipulation of data and prepartion of HTTP request
- Created database insert scripts 
- Installed MySQL and created database on AWS server
- Developed API functionality to receive GET request, parse parameters, and query the database
- Created unit tests for
   - Loading of SVG Map on visualization page
   - Validating submission without state does not send a request
   - Validating request submission with valid parameters
   - Validating reflection of drop-down selection in GET parameters
### 06/24/2021
- Updated README Documentation with description of application
- Created Vue project structure for front-end
- Configured Vue router and application landing page
- Created the General Information Page and populated it with data
- Created a Flask Project for future back-end API
- Configured mySQL database for future storage of vaccine card and vaccine data
