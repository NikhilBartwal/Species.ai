import os
import numpy as np
import tensorflow as tf
import streamlit as st
from model import *
from utils import *

def display_homepage():
    #Containizing the two parts of the page for stability
    welcome_container = st.beta_container()
    info_container = st.beta_container()
    uploaded_file = st.file_uploader('Please upload an image here-> ')

    #Check whether user has uploaded an image and move on to the next page
    if uploaded_file is not None:
        st.warning('Please close the image to go back to the homepage')

        #Since the file is uploaded as a Bytes object in Streamlit, we need to
        # process it to PIL image object to display
        image = process_image(uploaded_file)
        #Display the image and accept the desired category from the user
        category, predict_button = display_image(image)

        #The actual model loading and inference is used when the predict button is clicked
        if predict_button:
            model, input_details, output_details = load_model(category)
            species = run_inference(model, image, input_details, output_details)
            #Create a list of all species from labels txt files
            labels = get_labels(category)

            #Calculate and display the top 3 predictions along with the species info
            display_inference(species, labels, category, image)
    else:
        #This part is used to display the homepage when user has not uploaded any image
        with welcome_container:
            #Splitting the space into a 2:1 ratio for better experience
            welcome_text, app_logo = st.beta_columns([2,1])
            with welcome_text:
                st.title('Welcome to Species.AI!')
                st.subheader('Made with :heart: by - Nikhil Bartwal')
            with app_logo:
                st.image('logo.png')

        with info_container:
            animals_count, flowers_count, birds_count = st.beta_columns(3)

            #Streamlit's `subheader` and`write` support complete Markdown features!
            with animals_count:
                st.subheader(':dog: 30+ Animals')
            with flowers_count:
                st.subheader(':maple_leaf: 100+ Flowers')
            with birds_count:
                st.subheader(':bird: 200+ Birds')

            st.subheader('Our mother earth has blessed us with such a huge variety \
                    of flora and fauna. Yet, due to this vast variety, sometimes\
                    it becomes tedious to identify them.\nWe solve exactly that! \
                    Upload any image you want and let us take care of the rest!')
            #Creates a divider between he info section and the upload button
            st.write(" ----- ")

def deploy_speciesai():
    options = ['Homepage', 'Species Encyclopedia', 'About the project']
    option = display_sidebar(options)

    #Determining the page to display depending on the user choice from sidebar
    #Option[0] is selected by default
    if option == options[0]:
        display_homepage()
    elif option == options[1]:
        #To-DO: Add the encyclopedia page
        st.write('**Species Encyclopedia coming soon!**')
    elif option == options[2]:
        #Link to Github repo
        st.write('Hey there, if you want to know more about the project or have \
            a feature/query in mind, please open an issue at the github repo\
            [here](https://github.com/NikhilBartwal/Species.ai)')
        st.write('**Thank you for checking us out :heart:**')

if __name__ == '__main__':
    deploy_speciesai()
