# Inventory Manager MP3
## Introduction:
The project ‘**Inventory Manager**’ is based on stock control within a research and development company. 
There are two different types of stock which are generally held, these are solvents (ethanol, methanol, dimethylsulfoxide etc) and consumables (pipettes, plates, tips, labels etc). 
All these items must be tracked to make sure the storeroom / warehouse does not run out and can reorder in time. 
The application will hold information around products which are held on stock, minimum quantities required before ordering and the ability to add, update and delete products when are no longer required.

## UX:
### User Goals
* Build an app that allows the user to search for products held within a stock room.
* User should be able to update the fields, mainly quantity available for day to day use.
* User can request for new products to be added through a request form.
* The application can display stocks, update, delete and add new products.
* Requests for new products can be sent to the admin page.
* Administrator level is password protected, nice to have.
* Interface is easy to use and navigate through.
* Application should be responsive.

## User ideas:
* "Update function should be available"
* "Incorporate text to guide new users"
* "Products cannot be delete easily"
* "Fields should be prepopulated"
* "Search function would help when database is populated with many items"
* "See how many product are available and with a search function see how many records are pulled back from the search"

## Requirements:
The requirements for the application are as follows:
* User can see what is available in both categories.
* Quantities can be updated when products are removed.
* All properties can be editable incase of changes to produces, for example catalogue number changes.
* Navigation bar will have drop down for administrative items.
* Products can be edited.
* New products can be added.
* Products which are no longer required can be removed from the database.
* New products can be requested.
* Requests are captured in a collection.
* Requests are displayed and can be deleted.
* Navigation between pages.
* Counter for number of products available.
* Search functionality with record of results found.

## Design:
The design for this application is based around multiple pages. Some of these pages are available via the navigation bar whilst others will appear depending on the function requested. 
The pages available via the navigation bar will be home, solvents, consumables, requests and admin page. The solvent and consumable pages will be similar in style but will have different fields, the icons will link to either a page for editting fields, mainly used for the quantity available, and there you can update the database. 
With the trash icon this will take to a page so that you can confirm the deletion of a record. 
This page will display the name and catalogue number of the product you were trying to delete. 
This is a safe guard as not to delete the product by accident of the stock page.
A small description will also be added to the pages. Page layout will be simple and the colours will match the imagery of the banner.

### Layout:
* Base layer - this consists of the navbar, banner and footer and will be the same across all pages. On smaller devices only the title is displayed on the banner.
* Index/Home - this contains four icons with a description below. Large screen the icons are side by side but will change into a column on smaller devices. The request, consumables and request icon can also link to the relevant pages.
* Solvent / Consumables - here you will see what is available in stock. A record of number of item will be displayed and there is the functionality to search, edit and delete items. 
The search function is not case sensitive and will display the results after button press or return key pressed. The display will change to show results, show how many results are displayed and addition button to show all records again.
Edit will take you to edit page and delete will take you to a confirmation edit page.
* Edit page - allows you to edit any field and submit. On submit you are returned to the solvent or consumable page.
* Requests - displays a form, details can be entered and submitted the request page.
* Add solvents / consumables - is a form page which allows new products t be entered and submitted to the database.
* New Requests - a page which displays all new requests as cards with details of what is needed to be ordered. Once ordered requested can be cleared by pressing the ordered button.

## Images:
Icons have be taken from the [font awesome website]( https://fontawesome.com/) and the main image is from [Freepik website](https://www.freepik.com/photos/background). Image is called Group of Liquids. The main image used is glass beakers filled with coloured liquids and I believe this represents well a laboratory environment.
<a href="https://www.freepik.com/photos/background">Background photo created by pressfoto - www.freepik.com</a>

## Fonts:
I have chosen the David Libre font from [Google Fonts](https://fonts.google.com).

## Colours:
The colours which I have used are in keeping with the main image of the coloured beakers.
They are:
* #070707. Navbar and footer - This is a dark grey/blue to compliment the background of the image.
* #ff6c00. Navbar and footer text - A vibrate orange matching one of the liquids in a beaker.
* #ff6c00. Edit and delete icons - Again in line with the main image.
* #30eef5. Buttons - This is to match the aqua colour beaker. The text is in the same colour spectrum but a darker version, #071213.

## Wireframe:
The wireframes are an initial representation of how I designed the layout. There have been a few changes during th process but essentially the wireframe matches the production app.
The wireframe document can be found at [wireframes](https://github.com/hob71/inventory-manager-mp3/tree/master/wireframes).

## Testing:
Testing was carried out on the functions required for the user. These included  adding records, editting records, deleting record and finding number of records in collection.
* Screen shot of database records.
![Screen shot before adding record](https://github.com/hob71/inventory-manager-mp3/blob/master/static/assets/img/before_add.PNG)

* Added additional recorded, new record displayed and number of item has increased.
![Screen shot after record added and counter increases](https://github.com/hob71/inventory-manager-mp3/blob/master/static/assets/img/after_add.PNG)

* Pressed delete icon, confirmation page displays.and then deleted entry., Now one less record and number of items changed.
![Screen shot of delete confirmation](https://github.com/hob71/inventory-manager-mp3/blob/master/static/assets/img/delete_screen.PNG)

* Entry deleted. Now one less record and number of items changed.
![Screen shot after deletion of record and counter decrease](https://github.com/hob71/inventory-manager-mp3/blob/master/static/assets/img/after_delete.PNG)

* Pressed edit icon and updated the record with a comment.
![Screen shot of editted record. Comment added.](https://github.com/hob71/inventory-manager-mp3/blob/master/static/assets/img/edited_comment.PNG)

* Screen shot of new page with search.
![Screen shot before search.](https://github.com/hob71/inventory-manager-mp3/blob/master/static/assets/img/before_search.PNG)

* After search records are returned. Additional button appears to show all records again and number of records found displayed.
![Screen shot after search.](https://github.com/hob71/inventory-manager-mp3/blob/master/static/assets/img/after_search.PNG)

* Active requests page with one entry.
![Screen shot of requests page before addition](https://github.com/hob71/inventory-manager-mp3/blob/master/static/assets/img/request_before_add.PNG)

* Requests page after ne request placed.
![Requests page after new entry](https://github.com/hob71/inventory-manager-mp3/blob/master/static/assets/img/request_after_add.PNG)

## Bugs:
**Problem-**
Headers for document appear for each product
**Fix-**
Potential fix, move table header out of 'for' loop. To investigate.

**Problem-**
When delete button pressed confirmation delete page appears, cannot move data for object across.
**Fix-**
App was looking for a html page which did not extist and was be called.

**Problem-**
Was unable to see database in Heroku app.
**Fix-**
Needed to add the MONGO_URI to the keys.

**Problem-**
Product count collects correct value but does not refresh on deletion or creation of record.
**Fix-**
Variables moved into app route and then changes picked up.

**Problem-**
An 'action' field is appearing in the mongo db.
**Fix-**
Found name="action" code in the button. Once removed database entries were correct.

**Problem-**
File static/assets/mail/jqBootstrapValidation.js exists in gitpod as a 'hangover' from bootstrap themes (all bootstrap themes removed after realising not allowed for project) when I removed all the code. Unable to remove. Message 'warning: could not open directory 'static/assets/mail/': No such file or directory'
**Fix-**
Removed via Github and deployed to Heroku.

## Technologies used:
* HTML
* CSS
* Javascript
* Bootstrap
* Flask
* Python
* MongoDB
* Pymongo
* MongoDB Compass

## Deployment:
The project was developed in Gitpod and pushed to GitHub and Heroku.

To deploy my Inventory Manager project in Heroku the process was as follows:-

Opened Heroku in the browser.
* Logged in with my username and password.
* Selected 'new' and 'create new app'.
* Created the name for the app, inventory-manager-mp3. Name has to be unique.
* Chose the region, Europe.
* Opened terminal window in gitpod and logged into heroku using 'heroku login -i'
* Entered my email address and password used to log into heroku app.
* In terminal window typed 'git remote heroku' and the URL provide by Heroku for my app.
* Create a 'requirements.txt' file and 'Procfile'.
* Start up a web process by typing heroku ps:scale web=1 in the terminal.
* In heroku opened up 'settings' and entered in config variables. The IP and PORT.
* In addition in variables connected the MONGO_URI.

Below are links to my GitHub and Heroku published sites.

#### Published site: https://inventory-manager-mp3.herokuapp.com/
#### GitHub site: https://github.com/hob71/inventory-manager-mp3

The code in the deployed version is the same as my gitpod repository.

## Credits:
* Font Awesome for icons.
* Thanks go to the author of the background image. Background photo created by pressfoto - www.freepik.com
* Information on how to index the collections taken from MongoDB manuals. The code which was used is `db.solvents.createIndex({ "$**": "text" },{ name: "TextIndex" })` and `db.consumables.createIndex({ "$**": "text" },{ name: "TextIndex" })`.
* Information for creating search was found on [stackoverflow.com](https://stackoverflow.com/). The code was `{ $text : { $search: <your string> } }` and original answer was provided by Dave Adelson.
* Pop up box taken from [bootstrap.com](https://getbootstrap.com/)

## Acknowledge:
I would like to say thank you to my mentor, Mark Railton, and the tutors and student care at the Code Institute for the help and support they gave me.


## Final Notes and Future Additions:
* Looking back at the project, even though the mongo database has worked I believe a structured (sql) database would be more suitable for a large scale system as the tables and fields would not change.
* Future additions:
    * Additoin administrator account which would restrict access to the add, delete functions.
    * Changing the request process to also email when new requests are placed.
    * Reorder button which would automatically send a request.
    * An alert appears when quantity_available is lower than min_quantity.
    * Add a check via an 'if' statement to see if a catalogue number already exists (run out of time to change code).
    * Add link from support email address.
