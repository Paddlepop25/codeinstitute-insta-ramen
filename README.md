# InstaRamen

A Data Centric Frontend Web Development Project - Code Institute
<br>
By Linda Hsu
<br>
<br>
![Responsive displays of InstaRamen](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-insta-ramen/master/static/images/webpages/InstaRamen%20responsive.png)

<br>

[InstaRamen](https://linda-instaramen.herokuapp.com) is a website created for ramen lovers to view a collection of instant noodles from all around the world. One could search by a ramen flavour, add a new ramen to the collection if it is not available, edit all ramens in the collection and even delete them. A feature of this website is that users could give ratings (0-5 stars) and leave their reviews on the ramen for the benefit of future visitors.

The deployed website can be found in
[**Heroku**](https://linda-instaramen.herokuapp.com)

### User Stories

- #### As a user, I'd like to see:
    - A professional, modern and clean looking website to attract me to continue clicking on the other features 
    - Easy to understand and clear selections which would point me to the correct pages
    - Buttons which are straightforward in their purpose that allow me to view more information or do an action.
    - Options to have full control on adding, viewing, editing and deleting any ramen in the collection 

## UX / UI

### User Experience

- Users are welcomed with a refreshing orange color and a large noodles picture when they first visit the site. This sets the tone that this website is all about ramen

- There is an eyecatching icon of a bowl of ramen on the navbar and also as the favicon to further enhance the website's purpose 

- On larger screens, there are options on top of the navigation page for easy navigation on this website. On smaller screens, a hamburger on the left hand side of the navigation bar provides a menu of options when it is clicked on 

- A search function is provided on the main page that enable users to search for ramen flavours

- If the user gives an input that is not found, a sad faced kitty cat's face will be shown on the search result page. The user could input a new search to search for other flavours on the same page 

- An introductory message is given on the main page to explain the functions and purpose of the website 

- The 3 latest ramen additions are shgown below the introductory message in the form of cards and a 'more' button suggests a call-for-action from the users if they'd like to view more information 

- The user could view the entire ramen collections or view them by continents. The display ramen cards in the ramen collection page is sorted by the latest added ramen for users to see the newest entry. The display ramen cards in each of the continents options are sorted by countries for easy reference 

- A form is provided when the user would like to add a new entry to the ramen collection. The asterisks (*) imply that the fields are required to be filled before form submission 

- A drop down selection of ramen brands is provided and if the user don't find the one he/she is looking for, a new brand could be added by clicking on the "add brand" button. The user would be brought to a new page to add a new brand 

- After a new brand is added, the user is brought back to the the "add ramen" page where the newly added brand could be found in the drop down list 

- After the user fills in all fields and selects a picture to upload, upon clicking on the "submit" button,  he/she is brought to the "ramen collection" page where the latest ramen would be shown on the top left. This way they could verify that their form submission is successful 

- To see the full information of the recently added ramen, the user could click on the "more" button 

- Should the user want to edit the form, they could be brought to the form by clicking on "edit" at the display ramen page 

- The edit form is pre-filled with the original entries of the user for easy reference. After the user make changes, the form can be saved by clicking on the "save changes" button 

- Once the user choose to delete a ramen entry, they would be brought back to the ramen collection page 

- If there are any errors along the way, the user would be brought to an error 404 page where a shocked cat picture would hopefully shock the users into inputing or clicking on the right things 

### Design Ideas

The website was designed with an orange theme color as it is refreshing and close to the colours of food and noodles, with a clean white background to ensure all the texts, cards, images and other elements to 'pop up' to the user.

- #### Fonts

    - The font **'Poppin'** was chosen as the primary font as it's rounded edges creates a warm and comforting feeling to the user
    - The font **'Montserrat'** was chosen as the font for all titles  ```<h4>Titles</h4>``` to give a distint but subtle feel that it's different to make the texts look more interesting to the user

- #### Colours

    - **Main Heading and Footer -** An orange theme colour was chosen for the navigation bar and footer for all pages to set a refreshing and subtle warm connection to ramen because most noodles are yellowish, orangish in colour by nature. Black for the fonts on the bars are chosen to contrast against the bright orange for ease of reading
    
    - **Cards -** A white background was chosen for each card and any lines in the original design of the card was taken out to give a smooth flow feeling from the image to the information underneath. Black was chosen for the fonts to contrast against the background for easy reading
    
    - **Add, Edit, Search & More Buttons -** 'Add' buttons (for ramen and brand), 'edit,' 'search' and the 'more' buttons are in the theme orange color indicating a call-to-action for the users for these important features

    - **Cancel & Delete Buttons -** The 'cancel' button is in green to give a contrast against the orange theme button indicating a different function from the rest. The 'delete' button is in bright red because it indicates danger of not being able to retrieve the ramen once it is deleted 
    
    - **Forms -** A ligtened yellow background was chosen for the 'add ramen', 'add brand' and 'edit ramen' forms to give it a pop-up look on the page. All the labels fonts are in the orange colour to keep the theme consistent across all pages
    
    - **Active Input fields -** When an input field is active, the materialized icons & bottom border transforms to orange, keeping the primary orange color theme consistent
    
- #### Styling

    To achieve a warm, comforting feel for the user experience as well as keeping the website looking clean and modern, I used a CSS framework [Materialize!](https://materializecss.com/) to achieve this objective.
    
    **Special styles include:**
    
    - **Input fields -** When the user clicks on the field to input text, a simple but efficient animation provided by Materialize moves the placeholder to the top of the field while changing the bottom of the border to the theme orange colour. 

    - **Buttons -** Materialize also provides a neat animation in a class called 'waves' for buttons which gives an interesting effect when they are clicked on. Also, when all the buttons are hovered over, a shadow appears on the buttons to make them look 3D and pop-up, which indicates a call-to-action is possible.
    
### Wireframes

Wireframes were created initially to help me vsualise the website in different sized screens. They can be viewed via this [link](https://github.com/Paddlepop25/codeinstitute-insta-ramen/tree/master/static/images/wireframes).

Initial planning was done on how to setup the database and the website. I used Microsoft Word to sketch out this ER diagram.
![InstaRamen's ER diagram](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-insta-ramen/master/static/images/ERdiagram.png)
 
## Features

### Existing Features

1. #### Home Page

![Responsive displays of InstaRamen Main Page](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-insta-ramen/master/static/images/webpages/index.png)
    
- When the user first arrives at the page, he/she is welcomed with a large background picture of ramen, or noodles, with a search function for ramen flavours. On top of the page is an orange navigational bar with an icon of a bowl of ramen and chopsticks and links to the other pages. For the mobile devices, the links are presented when the user clicks on the 'hamburger' icon of 3 horizontal lines

-  If the user scrolls down the main page, there is a few paragraphs of text describing the purpose and functions of the website. Further down, there are 3 recently added ramens shown in the form of cards with pictures and a short but important description of the ramen brand and flavour, with a 'more' button should the user would like to view more information

- At the bottom of the page, there is a footer in the orange color with the ramen icon which points the user to the top of the page and a short summary of the website. In the 'keep in touch' section, there are links to my personal social media sites, Github repository and LinkedIn sites for anyone who wishes to contact me. There is also a disclaimer that this website is meant for educational purposes only
    
2. #### Search Ramen Page

![Responsive displays of InstaRamen Search Results Page](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-insta-ramen/master/static/images/webpages/ramen-search.png)
    
- When the user has inputted a ramen flavour in the search box on the main page, he/she is brought to this search results page where on top of the page is a line that says 'Search Results for "whatever the user has input into the box."' If there is at least one possible result, the ramen is displayed in a card with an image along with the brand and flavour. There is a vertical scroll button for the user to scroll down in case the lines are too long for the card display section. A 'more' button is available for the user to click on it to view more information on the ramen on the display page

<br>

![Responsive displays of InstaRamen Search (No) Results Page](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-insta-ramen/master/static/images/webpages/no-results.png)

- If there isn't any results from the user's search, a big picture of a sad kitty cat is shown saying no results have been found. With the search function available on top of the page, the user can perform another search without having to go back to the main page to do this  

3. #### Ramen Display Page

![Responsive displays of InstaRamen Ramen Display Page](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-insta-ramen/master/static/images/webpages/display-ramen.png)
    
- This page displays all the information of the ramen which includes a picture, brand, flavour, number of stars, country of origin and even reviews

- There are 2 buttons underneath the information which allows the user to edit the information or to delete this ramen

- If the user clicks on the edit button, he/she is brought to the edit page

- If the user clicks on the delete button, he/she is brought back to the ramen collection page which displays all the ramen in the collection

4. #### Ramen Collection Page 

![Responsive displays of InstaRamen Ramen Collection Page](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-insta-ramen/master/static/images/webpages/ramen-collection.png)

- This page displays all the ramen in the collection and they are sorted by the newest entry or addition to the collection. This is to give users the confirmation that their ramen entry from the 'add ramen' page is successful

- The ramens are displayed in cards giving the 'brand' and 'flavour' information. An orange 'more' button is available for users to click on it for detailed information on that particular ramen, which would be shown on the 'display ramen' page

5. #### Ramen Continents Page 

![Responsive displays of InstaRamen Asia/Europe/The Americas/Rest of the World Page](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-insta-ramen/master/static/images/webpages/ramen-continents.png)

- Users can view ramens from different continents by clicking on a selection of 4 choices; namely Asia, Europe, The Americas and Rest of the World. This is for quick and easy reference for the users' experience

6. #### Add Ramen Page 

![Responsive displays of InstaRamen Add Ramen Page](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-insta-ramen/master/static/images/webpages/add-ramen.png)
    
- On this page, the user is presented with a light amber coloured form with the top line saying that all fields are required. Here the user could fill in the different fields and even upload a ramen picture. On clicking the 'add ramen' button, the user is brought to the ramen collection page where the newest added ramen is shown on the top left hand side. This newly added ramen is also shown on the main page along with 2 other newly added ramens

- If the user clicks on the 'cancel' button, he/she will also be brought to the ramen collection page 

7. #### Ramen Edit Page

![Responsive displays of InstaRamen Ramen Edit Page](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-insta-ramen/master/static/images/webpages/edit-ramen.png)
    
- At this edit page, the form is pre-filled with entries from the original information. All the fields are available for the user to change if he/she wishes to 

- On the click of the 'save changes' button, the user is brought back to the ramen collection page to view all the ramens in the collection

- If the user changes his/her mind and clicks on the 'cancel' button, the user is diverted to the ramen collection page
    
8. #### Error 404 Page

![Responsive displays of InstaRamen Error 404 Page](https://raw.githubusercontent.com/Paddlepop25/codeinstitute-insta-ramen/master/static/images/webpages/error404.png)
    
- If the user has inputted an invalid entry on the URL, he/she would be brought to this page which shows that there is an error with a picture of a shocked kitty cat

- When the user scrolls down, there is a 'home' button which allows them to be brought back to the main page with a click of the button

### Future Features to Implement

1. #### User log in

    - A user log in feature is essential to allow edit and delete functions only to the user who created the ramen. This is to ensure no one deletes the whole collection on purpose or tamper with other users' ramen entries

2. #### Pagination

    - Pagination on the ramen pages would be helpful with organizing the collection as it grows. It also looks neater and helps with loading time

3. #### Video

    - I'd like to include a video on the history of instant noodles for better users' experience in gaining more knowledge from this website

4. #### Email newsletter

    - An option for users to be alerted when there are new ramen entries to the collection, or if their added ramen has any edits, new reviews or deletion

5. #### Delete confirmation model

    - A confirmation box asking if the user is sure about deleting the ramen would be shown after the user clicks on the 'delete' button
    
## Database

### MongoDB

- A noSQL database [MongoDB](https://www.mongodb.com/) was chosen for this project for the developer to gain experience in learning to work with a document based database in this cloud era

### Data types

- These are the types of data that are used in this project:
    - ObjectId
    - String
    - Int32(Integer)
    
### Ramens Database

- A database called 'ramen_database' which contains a main collection called 'ramens' which is where the attributes of each ramen is stored. The data structure is as follows:

| Name of field | field key | field value | type |
--- | --- | --- | --- 
Ramen ID | _id | `<Creates ID automatically>` | ObjectId 
Ramen Brand | brand | `<Name of ramen brand>` | string
Ramen Flavour | flavour | `<Name of ramen flavour>` | string
Ramen Style | style | `<Packaging style of ramen>` | string
Ramen Country of Export | country | `<Country where Ramen is exported from>` | string
Continent of Country | continent | `<Continent of Country>` | string
Ramen Stars | stars | `<Rating of Ramen>` | int32
Ramen Reviews | reviews | `<Reviews of Ramen>` | string
Ramen Image | imageURL | `<Name of image file uploaded>` | string

- In addition to the above 'ramens' collection, there is the 'countries' collection where all the countries of the world is specificed to a particular continent. The data structure is as follows:

| Name of field | field key | field value | type |
--- | --- | --- | --- 
Ramen ID | _id | `<Creates ID automatically>` | ObjectId 
Country | country | `<Name of country>` | string
Continent of Country | continent | `<Name of continent>` | string

- There is also the 'brands' collection where all the brands of existing ramens are stored and future additions by users from the 'add brand' form submission will also be store. The data structure is as follows:

| Name of field | field key | field value | type |
--- | --- | --- | --- 
Ramen ID | _id | `<Creates ID automatically>` | ObjectId 
Ramen brand | brand | `<Brand of ramen>` | string

## Technologies Used
Here are a list of programming languages, frameworks, technologies and tools used for this website:
* HTML5
* CSS3
- #### [JQuery](https://jquery.com)
    - **JQuery** has been used to simplify DOM manipulation.
- #### [Google Colaboratory notebook](https://colab.research.google.com/)
    - **Colab notebook** is used for writing the markdown for this README.md file
- #### [Python](https://www.python.org/)
    - **Python** as the main programming language used to build this project
- #### [Flask](https://palletsprojects.com/p/flask/)
    - **Flask** along with [Werkzeug](https://palletsprojects.com/p/werkzeug/) and [Jinja](https://palletsprojects.com/p/jinja/) is a Python web application framework to display the html pages with entries from MongoDB database
- #### [Cloud9](https://c9.io)
    - **Cloud9** is an IDE used to develop the website.
- #### [MongoDB](https://www.mongodb.com/)
    - **MongoDB** short for (Humongous database) is a noSQL, cloud-based database platform used to store all of the data for each ramen that is used on the website
- #### [Materialize](https://materializecss.com/)
    - **Materialize** is s modern responsive front-end framework based on Material Design used to create professional looking cards, search boxes, forms & overall style of the website
- #### [Am I Responsive?](http://ami.responsivedesign.is/?url=#)
    - **Am I Responsive** is used to see across multiple devices with different screen sizes the responsiveness of the website
- #### [Git](https://git-scm.com/)
    - **Git** is used for version control to regularly commit codes to Github    
- #### [GitHub](https://github.com/)
    - **GitHub** is used as a remote backup of code used in this project
- #### [Heroku](https://www.heroku.com)
    - **Heroku** is used as a platform for this project to be deployed to
    - To view the deployed version, please click on [InstaRamen](https://linda-instaramen.herokuapp.com/)

## Testing

A full testing process can be found in a separate [tests.md](https://github.com/Paddlepop25/codeinstitute-insta-ramen/blob/master/tests.md) file.

## Deployment

### To run on your local IDE

The project was built using [Cloud9](https://c9.io).

- Please have the following installed on your machine before working on it in your IDE:
    - [PIP](https://pip.pypa.io/en/stable/installing/)
    - [Python 3](https://www.python.org/downloads/)
    - [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
    - Open an account in [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) or have it running locally on your machine. Instructions of setting it up can be found [here](https://docs.atlas.mongodb.com/)

#### Instructions
1. Go to the [InstaRamen repository](https://github.com/Paddlepop25/codeinstitute-insta-ramen) and click the green 'Clone or download' button and then click 'Download ZIP'
& extract the contents to a location of your choice. Otherwise, you can clone the project into
your IDE with running the following command in the terminal
```
git clone https://github.com/*username*/*repository*
```
2. Ensure you have open a terminal, cd to the correct location to where you have your ZIP file

3. If running in Cloud9, there is a built in virtual environment but if it doesn't, please run the following command to build a virtual environment:
```
python -m .venv venv
```  

4. Use the following command to run a DNS toolkit for Python
```
sudo pip3 install dnspython
```

5. Use the following command to allow your project to run along side mongodb in python
```
sudo pip3 install pymongo
```

6. If your IDE requires a virtual environment, run the following command to activate it:
```
.venv\Scripts\activate 
```

7. Install a requirements.txt file with of the correct packages that you need for the project with: 
```
pip -r requirements.txt
```

8.  If you need the latest version of pip, you can get it by running the following command.
```
pip install --upgrade pip
```

9. Go into the .flaskenv file & create a MONGO_URI which is a link to your database in MongoDB it should look something like this

```
mongodb+srv://<username>:<password in mongo db>@<cluster_name>-qtxun.mongodb.net/<database name>?retryWrites=true&w=majority
```

10. Run the app.py file using the following command

```
python3 app.py
```

11. Then click on `http://127.0.0.1:5000` which will display in the termimal to view the project

### Deploying to Heroku

- The following steps are to deploy to Heroku in the terminal:

1. Run the command `echo web: python app.py > Procfile` which will create a Procfile

2. Add a requirements.txt file by using the command `sudo pip3 freeze —local > requirements.txt` which will display all of the packages that is needed for this project

3. Use `git add .` to stage all of your files `git commit -m "<message here>"` to commit the changes ready to push to GitHub

4. Create a repository in GitHub & follow the instructions in order to push your work up to GitHub

5. Using `git push` & inputting your email & password when instructed, this will push all of the files.
that have been committed up to GitHub

6. Go to heroku [here](https://dashboard.heroku.com/) and log into your account

7. Go to your Heroku dashboard and click "New" & click "Create New App"

8. Enter the name of your choice and set the region to the one closet to you

9. Ensure you link the Heroku application to the correct GitHub repository

10. Click inside of your app that you've just created and go to "Settings" then to "Reveal Config Vars".
Click on add to enter the following:

| Key | Value |
--- | ---
MONGO_ URI | <string at number 9 in instructions>

11. On top of the page, click on "Deploy" and scroll down to the list of instructions given to deploy your project to Heroku. The steps should be done in the terminal

12. After these steps are done correctly, scroll to the very top of the page in Heroku & click "Open App". You will now be able to view the project in Heroku

## Credits

### Contents

- All wordings were written by the developer

### Media
- #### Inspiration
    - Inspiration for this project was from this dataset from [Kaggle](https://www.kaggle.com/residentmario/ramen-ratings)
- #### List of Countries and Continents
    - I followed the listing of countries and continents [here](https://www.countries-ofthe-world.com/all-countries.html)
- #### Images
    - The main background image for the website was found in [pexel](https://images.pexels.com/photos/2347311/pexels-photo-2347311.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940)
    - Ramen logo was taken from [flaticon](https://image.flaticon.com/icons/png/512/451/451936.png)
    - The Favicon was created [here](https://favicon.io/favicon-converter/)
    - Pictures of ramen/ instant noodles were downloaded from [Amazon](https://www.amazon.com/noodles/s?k=noodles) and edited on my phone
    - Image of [sorry cat](https://i.imgflip.com/y5u9k.jpg) and [shocked cat](http://dailypicksandflicks.com/wp-content/uploads/2011/01/shocked-cat-face.jpg)

### Codes

- Ideas on how to design an error page was from this
[blog](https://neilpatel.com/blog/how-to-create-a-spectacular-404-error-page-with-12-examples/)

### Acknowledgements

A huge thank you to:

- Mr S and Mr P, our teachers at [Trent Global College](trentglobal.edu.sg/diplomainsoftwaredevelopment/)
- Our helpful teaching assistants John and Arif
- My friends and family whom were the user testers of this website. They gave valuable feedback on how to improve the project

## Disclaimer

All content on this website, including reviews on ramens,  images and icons are used for educational purposes only.