# Hom.ie
The Advanced Programming Project for Group D.


Introduction: 

	Dublin Housing Crisis isn’t a thing not heard of. Every year increasing number of students choose Dublin as their location for studies as well as work. This also however, makes the process of searching for an accommodation, extremely hectic and difficult. As a lot of students, working professionals try to find a home by scraping through different mediums such as Daft.ie and other websites like Airbnb or hostels, it’s a process that takes days and with no guarantee of ever being able to get an accommodation. Even when there are responses for an accommodation, there are more than ten parties looking to rent out the same place. This has been a personal experience for us when we landed in Dublin and even before reaching Dublin. It was also difficult to look for places near where we study like it would be for anyone in a new city.
 
	This is where Hom.ie comes in. Hom.ie is a Web Tool that extends help to people searching for their ideal accommodation. It does this by simply plotting all the available options on a map that can be then filtered by date as well as by specific areas around Dublin. Having the map helps in people identify exactly where the property is and they can glance over the plotted markers and click on the one that they find suitable to see more details about the particular posting. Here they can see how much the rent is, how many beds are available as well as the contact of the person if the location and details suite them.

	Another option available on the page is the ability to create your own listing. Plenty of the people who post their listings do it with the help of WhatsApp groups. These groups often have 500+ people with at least 5 to 10 postings being posted about property availability. This information is completely random and often there would be chances one misses out the available property on a text or ignores it as the number of messages is too much. The people posting also don’t necessarily follow a format and this makes retrieval of the information by someone seeking a place really difficult. This is where the ability of creating your own listing comes in. This form has been carefully designed studying the most asked questions and the most required criteria from the hundreds of ads posted. This form consists of some required fields as well as some optional fields that then enhance the result of it appearing on the map page readily available to anyone looking for a home.
	

Functionality: 

HomePage:

	The tool Hom.ie is created with a minimal design in mind wherein there aren’t a lot of options to stray away from the core functionality that is simply having the data of available properties being displayed visually on a map. When the user lands on the homepage, they are presented with the map of Dublin by default. This is achieved by setting the initial view with the set view and initial level of zoom by default that covers the entirety of Dublin City and some surrounding areas. 
	Once here, the user can now select a blank search which will query all the available properties in the Database and using JSON, return it to the frontend which will then plot every available property on the Map. Alternatively, there are two other options, the search bar, that accepts the first part of the EIR code, e.g. D15, which then queries the data of available properties in that available area as well as two date fields that can be set by the user to set a start date and an end date if they want to search for the properties in that manner. This will then query the properties only available in that timeframe. 
	Once the markers are plotted on the map, clicking on the markers also displays additional availability information that is collected during adding a listing to the database. 
This displays the EIR code, the number of beds available, the expected rent as well as the contact number of whom to contact if they are interested in the property. This is done by the queries written in Python Django that are then converted to SQL before querying the database that fetches the available listings for that area.

ListingPage:

	Another option alongside search on the HomePage is the Create a listing. This page comprises of a form that is used to create a listing on the map. The form includes details to be filled by the user while creating a listing. It accepts values with the help of validators that make sure data in a proper format is added to these fields. They also include the implementation of bootstrap in a way that the page is reactive to the size change of the screen. This makes sure that people on the phones can also have a proper layout while filling the form. The EIR code is a required field wherein once the user enters the EIR code, Google Map API is called to fetch the Lat and Lng values and stored in the Database along with other information which is then used to plot location on the OpenStreetMap.
	
	
Implementation:

File Structure:

TEMPLATE:

	The frontend consists of two HTML files, listingPage.html & homePage.html in TEMPLATE that have the bootstrap as well as some CSS that make up the two main pages.


	 
PYTHON:

	The backend is handled by the .py files with the views.py file consisting of all the functions that executes once the user lands on either of the pages and presses submit or search. 
	
	The validators.py is written with validators for different functionality such as fetching EIR code and even accepting correct values and maintaining proper type of data being entered in the proper table.

	Settings.py consists of all the settings required for the project to run and work as intended.

	Models.py consists of the class that creates a table in the backend database as well as setting default values for null as well as default values once an entry is made in the backend database table.

JavaScript:

	The static files that can include CSS and JS files in this project consists of a single file called MapLogic.js that holds the code to set a default view of the map over Dublin. This code also is responsible for implementing the map as well as holds a loop that accepts the injected value from the python code and then plots the markers on the map once it is returned with a result. This is the functioning of the MapLogic.js file.





Version Control:

	GitHub was used as the repository for the following project to enable working in a team. Three branches created, Main, PreProd and Development. The majority of the project was being developed and committed to the development branch while the PreProd branch was used as a testing area once modules were developed. Ultimately the code was then committed to the main branch.

Link: https://github.com/Napster1998/Hom.ie


PostgreSQL:
	
	PostgreSQL was used as a database due to the further possible expandability of the data. SQL Queries are also possible to be written as Python and hence SQL DB was used as it’s powerful and can handle huge amount of data which futureproofs the tool. The credentials for the DB were provided in the settings.py file. 








Future Scope:

	Future scope will include addition of the Login Module wherein every person who creates a listing will have to login. This will help in the ability for users to delete their listings as well once the property is no longer available.

Additional filters also can be made available since the data is already collected and stored about preferences during the registration process. This will fine tune the search result on the map for most users. 



