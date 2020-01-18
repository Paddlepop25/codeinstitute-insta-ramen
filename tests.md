# InstaRamen - Testing #

The deployed project 'InstaRamen' is on [Heroku](https://linda-instaramen.herokuapp.com/)

[**Main README.md file**](https://github.com/Paddlepop25/codeinstitute-insta-ramen/blob/master/README.md)

## Automated Testing

### Validating Code

Validation services were used to ensure that the respective codes were valid used to develop the website.

- [W3C Markup Validation Service](https://validator.w3.org/) was used to test HTML code to ensure it was valid code. Errors were shown where there were Jinja codes and this was expected as the latter are not html codes. Aside from these there were no other errors.

- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to test CSS code to ensure it was valid code. No errors were found.

## Manual Testing

A number of manual tests were done on each page to confirm that the website functioned well.

This website was tested on different web browsers and on different devices. I also requested friends and co-workers for feedback on what they liked and didn't like about this website. Adjustments were made accordingly until the final product upon project submission.

Devices and browesers:
* iPad 3
    * Safari
* MacBook Air
    * Google Chrome
    * Firefox
    * Safari
* MacBook Pro
    * Google Chrome
    * Firefox
    * Safari
* MacPro
    * Google Chrome
    * Firefox
* Windows 10 Enterprise
    * Google Chrome
    * Mircosoft Edge
* Samsung Galaxy 8
    * Google Chrome
    * Samsung web browser

Additionally, Google Chrome Devtools was used throughout the project to view this website on a number of stimulated mobile, tablet, laptop and desktop devices to ensure compatibility and responsiveness. Devices include Galaxy S5, Pixel 2, Pixel 2 XL, iPhone 5 / SE, iPhone 6/7/8, iPhone 6/7/8 plus, iPhone X, iPad, and iPad Pro.

#### 1. Home Page

I ensured that:
- The navbar is responsive across all screen sizes. This include clicking on the hamburger icon for smaller screens to check that the drop down selection is possible.
- All the links on the navbar was clicked on to check if the user is brought to the correct pages
- The large background picture of ramen is responsive for all devices.
- The search function is working at the click of the 'search' button and brings the user to display his/her ramen flavour search or a picture of a sad faced cat if the search is not found.
- The 3 most recently added ramen is displayed on the home page, and I added new ramens every day to see if they appear here. They are confimed by comparing the 'id' numbers from MongoDB.
- Each of the ramen card brings the user to the correct display ramen page when the user clicks on the 'more' button.
- The images of ramen / noodles are displayed within the card across all screen sizes.
- The vertical scroll is working when either the brand or flavour is longer than the allocated character spaces.
- The ramen icon and 'InstaRamen' link reloads the page and the user is brought back to the top of the home page.
- The links in the footer brings the user to the correct pages after clicking on the social media buttons.

#### 2. Search result page

I ensured that:
- On top of the page, the user's search from the home page is displayed.
- If there are matches, the correct ramen cards are displayed.
- Each card is responsive across all screens, the vertical scroll is available when there is overflow of text content and the image stays inside the card no matter the screen size.
- The 'more' button brings the user to the display ramen page when clicked on
- If there is no result from the search, a picture of a sad faced kitty cat is shown and that it is responsive across all devices

#### 3. Display ramen page

I ensured that:
- The correct ramen information is displayed, from the 'more' button the user clicked on, whether from the home page's ramen cards, the ramen collection's ramen cards or one of the continent's ramen cards
- The image stays on the left and is responsive across all devices
- All the attributes of the ramen is displayed
- The 'edit' button brings the user to the 'edit ramen' page when it is clicked on
- The ramen is deleted when the user clicks on the 'delete' button. As the user would be brought to the 'ramen collection' page, this can be checked easily with scrolling through the page to see if it is still there or not.

#### 4. Ramen collection page

I ensured that:
- The page is populated with all the ramen from the ramens collection in MongoDB.
- The ramen is displayed in cards that are responsive across all devices
- The images on the cards stay within the cards
- The vertical scroll is available when the characters overflow
- The 'more' button brings the user to the 'display ramen' page when it is clicked on

#### 5. 'Ramen Around The World' (Asia/Europe/The Americas/Rest of the World' pages

I ensured that:
- On either one of the continent's page, the correct ramen cards are displayed and this can be verified by looking at the 'country' on the card. The country should be from that continent.
- The ramen is displayed in cards that are responsive across all devices
- The images on the cards stay within the cards
- The vertical scroll is available when the characters overflow
- The 'more' button brings the user to the 'display ramen' page when it is clicked on

#### 6. Add ramen page

I ensured that:
- The `<h4>Title</h4>` title is displayed on top of the form in the center.
- The form displays well across all screen sizes with a light orange coloured background and a shadow around it's border
- The icons for each input field is displayed
- Each input field animates correctly when it is active
- Validation is implemented for all required fields with a reminder message popping up next to the fields if the user clicks on the submit button without filling them in prior.
- The 'brands' drop down selection shows all the brands from the 'brands' collection in mongoDB.
- When the 'add brand' button is clicked, the user would be brought to the 'add brand' page
- The 'country' drop down and 'continent' drop down selections displays the correct countries and continents which is confirmed when comparing with the 'countries' collection in MongoDB.
- When the 'Add Ramen' button is clicked, a new entry is sent to MongoDB, and that the user is brought to the 'Ramen Collection' page which his/her newly added ramen is displayed on the top left.
- When the 'Cancel' button is clicked, the user is brought to the 'Ramen Collection' page.

#### 7. Edit ramen page

I ensured that:
- The `<h4>Title</h4>` title is displayed on top of the form in the center.
- The form displays well across all screen sizes with a light orange coloured background and a shadow around it's border
- The icons for each input field is displayed
- Each input field has been populated with the original entries from the ramen database
- Each input field animates correctly when it is active
- The 'brands' drop down selection shows all the brands from the 'brands' collection in mongoDB.
- When the 'add brand' button is clicked, the user would be brought to the 'add brand' page
- The 'country' drop down and 'continent' drop down selections displays the correct countries and continents which is confirmed when comparing with the 'countries' collection in MongoDB.
- When the 'Save changes' button is clicked, this ramen is updated with the edited entries and the data is sent to MongoDB. The user would be brought to the 'Ramen Collection' page and the user could click on the 'more' button of the newly edited ramen to see if the details are updated.
- When the 'Cancel' button is clicked, the user is brought to the 'Ramen Collection' page.

#### 8. 404 Error page

I ensured that:
- If the URL doesn't match with the pre-determined functions from app.py, this page would load and display to the user.
- The `<h4>Title</h4>` title is displayed on top of the form in the center.
- A picture of a shocked cat's face is displayed
- A brief description is displayed at the bottom of the picture.
- The 'home' button would bring the user back to the home page when clicked on.

## Bugs 

1. Search ramen flavour:
This was my initial code for users to search for ramen flavours. It worked for a few weeks and one day, it stopped working. An error message saying '1 attribute is expected but 2 were given' was displayed.
```
@app.route('/search_ramen')
def search_ramen():
    orig_query = request.args['query']
    query = {'$regex': re.compile('.*{}.*'.format(orig_query)), '$options': 'i'}
    print(query)
    results=mongo.db.ramens.find({'flavour': query})
    
    ramen = []
    for result in results:
        ramen.append(result)
    
    return render_template('ramen_search.html', title="Search Results", query=orig_query, ramen_search=ramen)
```

  I narrowed the bug down to the line 
```
query = {'$regex': re.compile('.*{}.*'.format(orig_query)), '$options': 'i'}
```
and if i removed the `$options` key-pair values, the code would work but doesn't not allow search on both upper and lower cases of the same search text input.

  I changed the search codes to this and it worked again:
```
@app.route('/search_ramen/', methods=["GET", "POST"])
def search_ramen():
    post_request = request.args['query']
    return render_template("ramen_search.html",
                            title="Search Results",
                            query=post_request,
                            ramen_search=mongo.db.ramens.find({"flavour" : {"$regex": post_request, "$options": "i"}}),
                            ramen_count=mongo.db.ramens.find({"flavour" : {"$regex": post_request, "$options": "i"}}).count())
```

2. Ramen cards:
Initially, the images overflow and overspill out of the placeholder of the card. They appeared stretched at different screen sizes and were hard to manage. Also, I gave a very long text input for the 'flavour' field to see how the card would look and the card adjusted to the number of characters. This made the cards unbalanced and of different height sizes. To force the cards to look identical I set the image height to a fixed pixel, set the max-height of the card-content to a fixed pixel and gave a scroll function should the text content overflows from the height. Here are the code fix:
```
.card .card-image img {
  height: 214px;
}
.index-page-card .card .card-content {
  overflow-y: scroll;
  max-height: 144px;
}
``` 
    
## Further Testing
- In the future, I would like to implement unit testing while building a website of this kind
- A special acknowledgement and thanks to family and friends for their time to test this website on their device and their invaluable feedback.