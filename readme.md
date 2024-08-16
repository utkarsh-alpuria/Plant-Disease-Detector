#  Plant Disease Detector 🌱

## 📋 About the Project
This repository contains a web application designed to detect diseases in potato and tomato plants using Convolutional Neural Networks (CNNs) based on images of plant leaves.

![Home Page Cover Image](https://github.com/utkarsh-alpuria/Plant-Disease-Detector/blob/main/static/assets/home_page_cover_img.png)

## 🤖 CNN Models Used in the Web App

1. **Potato Plant Disease Classification Model**
   - 🧩 183,747 trainable parameters
   - 📷 Trained on a dataset of 1,728 images of potato plant leaves (256x256 pixels each)
   - 🎯 Accuracy score: ~80% (79.29%) on a test dataset of 320 images

2. **Tomato Plant Disease Classification Model**
   - 🧩 184,202 trainable parameters
   - 📷 Trained on a dataset of 9,344 images of tomato plant leaves (256x256 pixels each)
   - 🎯 Accuracy score: ~88.24% on a test dataset of 1,216 images

## 🛠️ Technologies Used
- **Python**: TensorFlow, NumPy, Pandas, Matplotlib, Flask
- **Frontend**: HTML, CSS, JavaScript

## 📂 Project Directory Structure

- **training**: Contains Jupyter notebooks for model training
  - `Training.ipynb`: For training the potato plant disease classification model
  - `Training_tomato.ipynb`: For training the tomato plant disease classification model

  **To Retrain or Fine-Tune the Model**
  - Download the dataset from [Kaggle PlantVillage Dataset](https://www.kaggle.com/datasets/arjuntejaswi/plant-village).
  - Unzip the dataset and move the `PlantVillage` folder into the `training` directory.
  - Delete all folders related to Bell Pepper in the `PlantVillage` folder as they are not used in this project.
  - Create a new folder named `PlantVillage_tomato` within `training` and move all tomato plant folders into this folder.

- **app.py**: Contains the backend Flask server, which handles user input, applies the trained models, and returns results to the frontend.

- **Models**: Saved models after training
  - `1.keras`: First version of the potato plant disease classification model
  - `2.keras`: Second version of the potato plant disease classification model
  - `tomato_model_1.keras`: Tomato plant disease classification model

- **templates**: HTML files for the frontend of the Flask app
  - `home.html`: Home page structure
  - `potato_classify.html`: Potato disease classification page
  - `tomato_classify.html`: Tomato disease classification page

- **static**: Contains assets, CSS, and JavaScript files for the frontend
  - **assets**: Images used in the frontend
  - `home.css`: Stylesheet for `home.html`
  - `classify.css`: Stylesheet for both `potato_classify.html` and `tomato_classify.html`
  - `classify.js`: JavaScript file for both `potato_classify.html` and `tomato_classify.html`

- **requirements.txt**: Lists all dependencies required to create the Python virtual environment for the project.

## 🚀 Get Started with the Project

1. Ensure Python is installed on your machine.
2. Clone the project repository or download the zip file.
3. Open the project folder in VS Code or any other IDE.
4. Create a virtual environment using:
   ```bash
   python -m venv <name_of_virtual_environment>
   ```
5. Activate the virtual environment:
   - On Windows:
     ```bash
     .\<name_of_virtual_environment>\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source <name_of_virtual_environment>/bin/activate
     ```
6. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```
7. Run `app.py`:
   ```bash
   python app.py
   ```
   - You may see TensorFlow warnings and a localhost link (e.g., `http://127.0.0.1:5000`) in the terminal.
   - When you see `* Debugger is active!`, copy the localhost link and paste it into your browser.

8. You will be redirected to the web app's home page.

## 🖥️ How to Use the Web App

1. On the home page, select the model for the plant you want to check.
2. Upload an image of the plant leaf.
3. Click the "Predict" button.
4. The condition of the plant along with the confidence score will appear on the screen.

