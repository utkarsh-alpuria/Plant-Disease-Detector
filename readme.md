# Plant Disease Detector

## About Project
This repository contains a web application for detecting diseases in potato and tomato plants with plant leaf images using Convolutional Neural Networks (CNNs).


## Technologies used
Python - Tensorflow, Numpy, Pandas, Matplotlib, Flask
HTML, CSS, JavaScript

## Project Directory Structure 

- requirements.txt - this file has all the dependencies required to create the python virtual enviornment to run this project.

- training - this folder has two ipynb files 
    - Training.ipynb - this is the file where potato plant disease classification model is trained
    - Training_tomato.ipynb - this is the file where tomato plant disease classification model is trained

    **To Go through model the training again**
    - If you want to train the model again or fine tune it you can use these two files, but first you have to download the dataset
    - The dataset used is from https://www.kaggle.com/datasets/arjuntejaswi/plant-village. 
    - download the dataset, unzip the dataset file, you will find a PlantVillage folder in it. Transfer the folder in the training folder.
    - Inside the PlantVillage folder you will have many folders representing different plant(Bell Pepper, Potato, Tomato) with diseases, delete all the Bell Peper folders, it is not used in the project.
    - now in the training folder create another folder named PlatVillage_tomato and move all the tomato plant folders in this folder from the PlantVillage folder.

**Backend**
- app.py - this python file have the backend flask server which takes the user input image from frontend web app, loads and apply the trained models and sends the result back to frontend.

- Models - this folder has the saved models after the training
    - 1.keras - this is first version of potato plant disease classification model.
    - 2.keras - this is second version of potato plant disease classification model.
    - tomato_model_1.keras - this is the model for tomato plant disease classification model.

**Frontend**
- templates - this folder has html files for frontend of flask app
    - home.html - html structure of home page of the web app
    - potato_classify.html - html structure for patato disease classification page
    - tomato_classify.html - html structure for tomato disease classification page

- static - this folder has an assets folder,  css and javascript files for the fontend
    - assets - this folder has images used in frontend of website
    - home.css - stylesheet linked to home.html file
    - classify.css - stylesheet linked to both potato_classify.html and tomato_classify.html
    - classify.js - javascript file linked to both potato_classify.html and tomato_classify.html


## Get started with project
- make sure python is installed in your machine.
- clone the project repository or download the zip file.
- open the project folder in vs code or any other IDE
- Create a virtual environment within the project folder using the command `python -m venv <name_of_virtual_environment>`.
- Activate the virtual environment with the command `.\<name_of_virtual_environment>\Scripts\activate`.
- In your code editor's terminal, install project dependencies with pip install `-r requirements.txt`.
- Run app.py file
- It will show few tensorflow warnings in terminal and then a http localhost link with port(`http://127.0.0.1:5000`) will appear in the terminal. 
- when you see  (`* Debugger is active!`) in terminal kopy the localhost link and pased it in your browswe and hit enter.
- you will see the web app home page.

## How to Interact or use the Web App
- in home page you will se two models for different plants, select abny one of you choice.
- new page will appear where you can give the image of leaf of the plant to.
- after uploading the image click on predict button
- the condition with score will appear on the screen
