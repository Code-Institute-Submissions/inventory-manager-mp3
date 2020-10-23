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
* application should be responsive.

## User ideas:
* "Update function should be available"
* "Incorporate text to guide new users"
* "Products cannot be delete easily"
* "Fields should be prepopulated"

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

## Design:
The design for this application is based around multiple pages. Some of these pages are available via the navigation bar whilst others will appear depending on the function requested. 
The pages available via the navigation bar will be home, solvents, consumables, requests and admin page. The solvent and consumable pages will be similar in style but will have different fields, the icons will link to either a page for editting fields, mainly used for the quantity available, and there you can update the database. 
With the trash icon this will take to a page so that you can confirm the deletion of a record. 
This page will display the name and catalogue number of the product you were trying to delete. 
This is a safe guard as not to delete the product by accident of the stock page.
A small description will also be added to the pages. Page layout will be simple and the colours will match the imagery of the banner.

## Images:
Icons have be taken from the [font awesome website]( https://fontawesome.com/) and the main image is from [Freepik website](https://www.freepik.com/photos/background). Image is called Group of Liquids. The main image used is glass beakers filled with coloured liquids and I believe this represents well a laboratory environment.
<a href="https://www.freepik.com/photos/background">Background photo created by pressfoto - www.freepik.com</a>
## Fonts:
I have chosen the [Google Fonts](https://fonts.google.com).

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
![Screen shot after record added and counter increases](https://github.com/hob71/inventory-manager-mp3/blob/master/static/assets/img/after_add.PNG)
![Screen shot after deletion of record and counter decrease](https://github.com/hob71/inventory-manager-mp3/blob/master/static/assets/img/after_delete.PNG)
![Edit item record](https://github.com/hob71/inventory-manager-mp3/blob/master/static/assets/img/edited_comment.PNG)
![Screen shot before adding record](https://github.com/hob71/inventory-manager-mp3/blob/master/static/assets/img/before_add.PNG)
![Add request]()
![complete request]()

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

## Technologies used:
* HTML
* CSS
* Javascript
* Bootstrap
* Flask
* Python
* MongoDB
* Pymongo

## Deployment:


Below are links to my GitHub and published sites.

#### Published site: https://inventory-manager-mp3.herokuapp.com/
#### GitHub site: https://github.com/hob71/inventory-manager-mp3

The code in the deployed version is the same as my gitpod repository.

## Credits:
* Font Awesome for icons.
* Thanks go to the author of the background image. Background photo created by pressfoto - www.freepik.com

## Acknowledge:



## Final Notes and Future Additions:

