# InstaRamen

An Interactive Front-end Web Development Project - Code Institute
<br>
By Linda Hsu

![Responsive displays of InstaRamen](https://raw.githubusercontent.com/paddlepop25/codeinstitute-insta-ramen/master/static/images/webpages/index.png)

<br>

[InstaRamen](https://linda-instaramen.herokuapp.com) is a website created for ramen lovers to view a collection of instant noodles from all around the world. One could search for by a ramen flavour, add a new ramen to the collection if it is not available, edit all ramens in the collection and even delete them. A feature of this website is that users could rate and leave their reviews on the ramen for the benefit of future visitors.

The deployed website can be found in
[**Heroku**](https://linda-instaramen.herokuapp.com)

### Project Purpose

The objective of InstaRamen is to enable users to search for information of ramens of their choice. If it couldn't be found, users could provide new entries to the collection and view them after they've filled in the 'add ramen' form. Users could also edit a ramen of their choice and even delete any one they choose.

### User Stories

- #### As a user, I'd like to see:
    - A professional, modern and clean looking website to attract me to continue clicking on the other features 
    - Easy to understand and clear selections which would point me to the correct pages
    - Buttons which are straightforward in their purpose that allow me to view more information or do an action.
    - Options to have full control on adding, viewing, editing and deleting any ramen in the collection 

## UX / UI

### User Experience

- Users are welcomed with a refreshing orange color and a large noodles picture when they first visit the site. This sets the tone that this website is all about ramen. 

- There is an eyecatching icon of a bowl of ramen on the navbar and also as the favicon to further enhance the website's purpose. 

- On larger screens, there are options on top of the navigation page for easy navigation on this website. On smaller screens, a hamburger on the left hand side of the navigation bar provides a menu of options when it is clicked on. 

- A search function is provided on the main page that enable users to search for ramen flavours

- If the user gives an input that is not found, a sad faced kitty cat's face will be shown on the search result page. The user could input a new search to search for other flavours. 

- An introductory message is given on the main page to explain the functions and purpose of the website. 

- The 3 latest ramen additions are shown below the introductory message in the form of cards and a 'more' button suggests a call-for-action from the users if they'd like to view more information. 

- The user could view the entire ramen collections or view them by continents. The display ramen cards in the ramen collection page is sorted by the latest added ramen for users to see the newest entry. The display ramen cards in each of the continents options are sorted by countries for easy reference. 

- A form is provided when the user would like to add a new entry to the ramen collection. The asterisks (*) imply that the fields are required to be filled before form submission. 

- A drop down selection of ramen brands is provided and if the user don't find the one he/she is looking for, a new brand could be added by clicking on the "add brand" button. The user would be brought to a new page to add a new brand. 

- After a new brand is added, the user is brought back to the the "add ramen" page where the newly added brand could be found in the drop down list. 

- After the user fills in all fields and selects a picture to upload, upon clicking on the "submit" button,  he/she is brought to the "ramen collection" page where the latest ramen would be shown on the top left. This way they could verify that their form submission is successful. 

- To see the full information of the recently added ramen, the user could click on the "more" button. 

- Should the user want to edit the form, they could be brought to the form by clicking on "edit" at the display ramen page. 

- The edit form is pre-filled with the original entries of the user for easy reference. After the user make changes, the form can be saved by clicking on the "save changes" button. 

- Once the user choose to delete a ramen entry, they would be brought back to the ramen collection page. 

- If there are any errors along the way, the user would be brought to an error 404 page where a shocked cat picture would hopefully shock the users into inputing or clicking on the right things. 

### Design Ideas

The website was designed with an orange theme color as it is refreshing and close to the colours of food and noodles, with a clean white background to ensure all the texts, cards, images and other elements to 'pop up' to the user.

- #### Fonts

    - The font **'Poppin'** was chosen as the primary font as it's rounded edges creates a warm and comforting feeling to the user.
    - The font **'Montserrat'** was chosen as the font for all titles  ```<h4>Titles</h4>``` to give a distint but subtle feel that it's different to make the texts look more interesting to the user.

- #### Colours

    - **Main Heading and Footer -** An orange theme colour was chosen for the navigation bar and footer for all pages to set a refreshing and subtle warm  connection to ramen because most noodles are yellowish, orangish in colour by nature. Black for the fonts on the bars are chosen to contrast against the bright orange for ease of reading.
    
    - **Cards -** A white background was chosen for each card and any lines in the original design of the card was taken out to give a smooth flow feeling from the image to the information underneath. Black was chosen for the fonts to contrast against the background for easy reading.
    
    - **Add, Edit, Search & More Buttons -** 'Add' buttons (for ramen and brand), 'edit,' 'search' and the 'more' buttons are in the theme orange color indication a call-to-action for the users for these important features.

    - **Cancel & Delete Buttons -** The 'cancel' button is in green to give a contrast against the orange theme button indicating a different function from the rest. The 'delete' button is in bright red because it indicates danger of not being able to retrieve the ramen once it is deleted. 
    
    - **Forms -** A ligtened yellow background was chosen for the 'add ramen' and 'edit ramen' forms to give it a pop-up look on the page. All the labels are in the orange colour to keep the theme consistent across all pages.
    
    - **Active Input fields -** When an input field is active, the materialized icons & bottom border transforms to orange, keeping the primary orange color theme consistent.
    
- #### Styling

    To achieve a warm, comforting feel for the user experience as well as keeping the website looking clean and modern, I used a CSS framework
    [Materialize!](https://materializecss.com/) to achieve this objective.
    
    **Special styles include:**
    
    - **Input fields -** When the user clicks on the field to input text, a simple but efficient animation provided by Materialize moves the placeholder to the top of the field while changing the bottom of the border to the theme orange colour. 

    - **Buttons -** Materialize also provides a neat animation in a class called 'waves' for buttons which gives an interesting effect when they are clicked on. Also, when all the buttons are hovered over, a shadow appears on the buttons to make them look 3D and pop-up, which indicates a call-to-action is possible.