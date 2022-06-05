# pokemon team builder
This web app allows you to log in and create teams specific to any pokemon game and then assess their ability to beat that game's gym leaders. I have created this as the capstone project for CS50's Web Programming with Python and JavaScript. The project is ongoing and currently in development but is in a working state.

## Distinctiveness and Complexity
This web app uses a combination of a restful API and SQLite database to load data. You can create a username, therefor your teams will only be accessible to you however the app can be utilized by many people. Once you have logged in you will pick a game and then build your team for that game. Search for pokemon to check if they are available in that game and receive basic info on that pokemon. If they are available and you would like to, you can add them to your team. You also have the option to remove pokemon from teams. Teams are capped at 6 pokemon (just like the game). 

## Models
The models built for this app are supplementary to the Poke API. Since this api does not contain any gym or leader information the model structure exists to track this data. 
### Game
This information was taken from the poke api however, I found it to be more efficient to permanently store in the SQLite database rather than making lots of calls for information that is not changing. The only downside to this structure is any new game data will need to be manually added. However, that does not happen very often, so the change feels justified. Information stored in this model includes name, region, generation, color. There is also some information that would make future api calls simpler, including group_name and url. 
### Leader 
This model contains the name and a color for each leader. The color is utilized by JavaScript upon hover on the gyms.html page. 
### Location 
Since I anticipated multiple gyms using the same location, I built this as a separate model which currently contains a name field only.
### Reward 
This model also has the potential to be used by multiple gyms. There are currently two fields, Name and Type. At the moment, this model is not being utilized by the app and I believe could greatly benefit from some restructuring.
### Gym
This model pulls in the above four models, Game, Leader, Location and Reward (reward is a manytomany field so there can be more than one). It also contains additional fields order and team. Order is simply the order in the game which you would challenge the gym. Team is a CharField and it’s intended to contain a comma delaminated list of pokemon ids. Within my views.py file I will parse this list and pull data on each pokemon via the poke api.
### Team
This model is the only one not directly related to saving gym information. This provides structure for saving team information per user. Fields include, user, pk_ids, pk_count, and game. Teams are specific to user and to game. The pk_ids field stores a comma deliminated list of pokemon ids. 

## Static

### main.js 
This file controls dynamic color display throughout the application
### mystyles.css
This is the singular css styling for the entire application. There is also mobile responsive styling defined here. 
### PocketMonk
There are three files here that contain the information for the pokemon font that is used throughout the site
### images
I have two images, pikachu and pysduck used within the application

## Templates
This folder contains various hmtl files used for the application. For the most part, each file extends the layout.html file. The exception to this is login.html, register.html and test.html. 

## Views.py
This file contains most of the code that powers this application. There is logic for registering, logging in, logging out, verifying that a user is signed in before running code. Logic also exists to build and view teams, select a game to play, load gym leader data. The logic for determining if your team would win against a gym is rudimentary and more of a place holder for something more significant.  