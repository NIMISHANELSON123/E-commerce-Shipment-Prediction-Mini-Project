# 📦 🚀 E-Commerce Shipment Prediction - Capstone Mini Project

<p align="center">
  <img src="screenshots/Screenshot 2026-10-08 213223.png" width="700" alt="Project Banner">
</p>

> A complete Machine Learning and Web Deployment capstone project to predict whether an e-commerce shipment will reach on time or be delayed.

---

## 🌟 Project Overview
In the fast-paced e-commerce industry, timely delivery is crucial for customer satisfaction. This project utilizes machine learning algorithms to analyze historical shipment data, identify patterns, and predict delivery outcomes. A user-friendly **Flask web application** is built and containerized using **Docker** for seamless deployment.

---

## 📊 Dataset Information
* **Source:** Kaggle (E-Commerce Shipping Data)
* **Total Rows (Instances):** 10,999+ records
* **Total Columns (Features):** 12 attributes including customer demographics, product details, and shipment metrics.
* **Target Column:** `Reached.on.Time_Y.N` 
  * `1` ➔ Shipment reached on time
  * `0` ➔ Shipment reached late / delayed

### Key Features in Dataset:
* `Warehouse_Block`: The block of the warehouse (A, B, C, D, E)
* `Mode_of_Shipment`: Shipping method (Ship, Flight, Road)
* `Customer_care_calls`: Number of calls made for inquiry
* `Customer_rating`: Rating given by customers (1 to 5)
* `Cost_of_the_Product`: Price of the product in USD
* `Prior_Purchases`: Number of prior purchases
* `Product_importance`: Category of importance (low, medium, high)
* `Gender`: Male or Female
* `Discount_offered`: Discount offered on that specific product
* `Weight_in_gms`: Weight of the product in grams

---

## 🛠️ Tech Stack & Libraries
* **Language:** Python 🐍
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Web Framework:** Flask 🌐
* **Containerization:** Docker 🐳
* **Development Environment:** Jupyter Notebook

---

## 📂 Project Directory Structure
```text
E-commerce-Shipment-Prediction-Mini-Project/
│
├── App/
│   ├── app.py                 # Flask backend application
│   └── Dockerfile             # Docker configuration file
│
├── templates/
│   └── index.html             # Frontend HTML user interface
│
├── screenshots/               # Application & project screenshots
│   ├── Screenshot 2026-10-08 213223.png
│   ├── Screenshot 2026-10-08 213351.png
│   ├── Screenshot 2026-10-08 213438.png
│   └── Screenshot 2026-10-08 213847.png
│
├── Mini_Project_E_Commerce_Prediction.ipynb  # EDA & Model Training Notebook
├── requirements.txt           # Python dependencies
└── README.md                  # Project Documentation


README.md                  # Project Documentation

⚙️ How to Run Locally
 * Clone the Repository:
   git clone [https://github.com/NIMISHANELSON123/E-commerce-Shipment-Prediction-Mini-Project.git](https://github.com/NIMISHANELSON123/E-commerce-Shipment-Prediction-Mini-Project.git)
cd E-commerce-Shipment-Prediction-Mini-Project

 * Install Dependencies:
   pip install -r requirements.txt

 * Run the Flask Application:
   cd App
python app.py

 * Open in Browser:
   Go to http://127.0.0.1:5000/ to use the prediction interface.
📸 Screenshots
<p float="left">
<img src="screenshots/Screenshot 2026-10-08 213351.png" width="45%" />
<img src="screenshots/Screenshot 2026-10-08 213438.png" width="45%" />
</p>
👩‍💻 Developed By
 * Nimisha Nelson
