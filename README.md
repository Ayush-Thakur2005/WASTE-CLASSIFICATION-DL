# AI-Based Waste Classification System

An end-to-end **deep learning project** that classifies waste images into categories like **Organic** and **Recyclable**. This project uses a **Convolutional Neural Network (CNN)** built with **TensorFlow/Keras** for image classification and a **Flask web application** for deploying the model so users can upload images and get predictions instantly.  

---

## **Table of Contents**
- [Overview](#overview)  
- [Features](#features)  
- [Dataset](#dataset)  
- [Architecture & Model](#architecture--model)  
- [Project Structure](#project-structure)  
- [Installation & Setup](#installation--setup)  
- [Usage](#usage)  
- [Demo](#demo)  
- [Future Improvements](#future-improvements)  
- [License](#license)  

---

## **Overview**
This project demonstrates the **full workflow of a deep learning image classification project**, including:

1. Dataset preprocessing  
2. CNN model creation and training  
3. Model evaluation  
4. Web deployment with Flask  
5. Handling unknown/unseen images gracefully  

It is an excellent showcase for **AI & web development skills**, making it perfect for portfolios or practical applications in waste management and environmental technology.

---

## **Features**
- CNN model trained on a custom waste dataset  
- Web interface built using Flask  
- Handles **image uploads** from users  
- **Confidence-based prediction:** displays “Unknown” if the model is not confident  
- Robust handling of **filenames with spaces or special characters**  
- Displays **predicted class with probability**  
- Fully **portfolio-ready** with attractive HTML/CSS  

---

## **Dataset**
- The model was trained on a **custom waste dataset** containing images for categories like `Organic` and `Recyclable`.  
- Dataset split: `TRAIN` and `TEST` folders.  
- Images resized to `128x128` and normalized before feeding into the CNN.  

> You can replace or extend the dataset to improve accuracy or add new waste categories.  

---

## **Architecture & Model**
- **Model type:** Convolutional Neural Network (CNN)  
- **Input:** 128x128 RGB images  
- **Output:** Softmax probabilities for each class  
- **Training:**  
  - Loss: Categorical crossentropy  
  - Optimizer: Adam  
  - Epochs: 10 (can be increased for better accuracy)  
- **Post-processing:** Confidence threshold to handle unknown/unseen images  

---

## **Project Structure**
waste_management/
│
├── model/ # Trained CNN model
│ └── waste_model.keras
├── templates/ # HTML templates
│ └── index.html
├── static/ # CSS, JS, uploaded images
├── app.py # Flask backend
├── README.md # Project description
├── requirements.txt # Required Python packages
└── .gitignore # Ignore venv, cache, system files


---

## Usage

Start the Flask server:

python app.py


Open your browser and go to:

http://127.0.0.1:5000/


Upload an image to see the predicted class and confidence probability.

Confidence threshold: Images with low prediction confidence are labeled as Unknown.



## **Installation & Setup**
1. **Clone the repository**
```bash
git clone https://github.com/Ayush-Thakur2005/WASTE-CLASSIFICATION-DL.git
cd WASTE-CLASSIFICATION-DL

Create and activate virtual environment

python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt


