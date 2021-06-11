# Species.AI 
Deep Learning based web application for identifying flowers, birds, animals and providing general trivia about them (Hosted on Streamlit).<br>
Take a look at it here: []()

## Table of Contents

* [About the App](#about-the-app)
* [Installation](#installation)
* [Technologies](#Technologies)

## About the App

It allows the user to simply take a photo of any plant, animal, bird right at the moment(if using on the phone) or load it from the gallery/disk and then, gives the top 3 predictions for the species along with providing some interesting information about them including their description, family and genus, nicknames, countries where they are found etc. completely offline<br><br>
Species.AI can classify around 350+ categories of various plants, flowers, animals and birds on the go. The deep learning model used for classification uses the State of the art EfficientNet B0 architecture as the backbone. The database used in the application was created using Wikipedia's MediaWiki API.

## Screenshots

![Langing page](screenshots/homepage.PNG?raw=true)
![Image_upload](screenshots/image_upload.PNG?raw=true)
![Trial](screenshots/trial.PNG?raw=true)
![Trial_info](screenshots/trial_info.PNG?raw=true)

## Contents of Repo

* **database:** Contains the species information database with tables animaldata, plantdata and birddata, for each category of species.
* **labels:** Contains the names of all species to map the model output probability to.
* **models:** TFLite models for each category of species, trained with EfficientNet B0 architecture.
* **screenshots:** Screenshots of the landing page etc, to be used in README.
* **specimens:** Contains images of all 350+ species, to be used while displaying Top 3 predictions.
* **requirements.txt** Contains the necessary packages for the Streamlit app.

### Scripts

* **SpeciesAI_webapp.py:** Defines the overall Streamlit app interface, widgets and workflow logic.
* **model.py:** Used to load the model and provide inference. Also displays the predicted image and its information.
* **database_utils.py** Used to load and get info about the about from the database and display on screen.
* **utils:** Helper utils to process and display uploaded image as well as rendering the sidebar.


## Installation

Use [this]() to checkout the web application and follow the on-screen instructions. 

#### To run the Streamlit app locally
* Fork the repository using `git clone https://github.com/NikhilBartwal/Species.ai`
* Install the Streamlit module locally using `pip install streamlit`
* Checkout the local repo and use `streamlit run SpeciesAI_webapp.py` to run the app locally.
* After making any changes in the source-code, use `Ctrl+C` to stop current streamlit session. Repeat previous step to re-launch the web-app

## Technologies

### For the deep learning model:

* **Python:** Python was used for training the models as well as scraping information about the various species and constructing the database using the MediaWiki API. Python was used due to it being easy to read, dynamically-typed and the vast number of libraries present, which help developers focus on what matters the most instead of boilerplate code.
* **Tensorflow:** Tensorflow framework was used for training and evaluating the deep learning models. After training, the models were converted using Tensorflow Lite to their portable versions. The final models had an accuracy of ~95%
* **Kaggle Kernel:** The entire modelling process was carried out on Kaggle Kernels, which are similar in nature to Jupyter Notebooks. Kaggle provides free GPU and TPU resources (30 hours per week each) which can train the model many times faster than on CPU.
* **Libraries like Numpy, Matplotlib, PIL etc.** were used to data and image processing as well as visualizing the input and output images.

### For the web application:

* **Streamlit:** Thanks to the amazing people at Streamlit, it is now possible to create a web app completely in python! It provides many widgets like buttons, check boxes, select boxs, file uploader, side bar etc. which can all be used in tandom with each other and create wonderful applications. 
* **SQLite3:** The SQLite3 library was used to load the database and extract the information about the necessary species.
