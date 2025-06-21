
# 🏠 AI-Driven Real Estate Price Prediction & Recommendation System
An end-to-end machine learning solution to predict property prices and recommend real estate listings using data scraped from 99acres. Deployed as an interactive Streamlit web app on Microsoft Azure.

## 🚀 Overview
This project combines web scraping, machine learning, interactive dashboards, and cloud deployment to build a powerful real estate analytics and recommendation platform. Users can explore property price trends, receive property recommendations, and predict prices based on input features—all in real-time.

 ## 📦 Key Features
- 🔍 Data Extraction: Scraped property listings from 99acres.com using requests and BeautifulSoup.

- 🧹 Data Preprocessing & EDA: Cleaned and visualized data, engineered meaningful features, and handled outliers.

- 🧠 ML Model Training: Trained and compared multiple regression models:

- Support Vector Regression (SVR)

- Gradient Boosting Regressor (GBR)


- 🗺️ Recommendation Engine: Implemented a content-based recommendation system using cosine similarity.

- 📊 Interactive UI: Built a Streamlit dashboard with tabs for analytics, price prediction, and apartment recommendation.

- ☁️ Deployment: Dockerized and deployed on Microsoft Azure for scalable and global access.

| Layer           | Tools Used                                     |
| --------------- | ---------------------------------------------- |
| Web Scraping    | `requests`, `BeautifulSoup`                    |
| Data Processing | `pandas`, `numpy`, `matplotlib`, `seaborn`     |
| ML Models       | `scikit-learn` (SVR, GBR), `cosine_similarity` |
| Dashboard       | `Streamlit`, `Plotly`, `WordCloud`             |
| Deployment      | `Docker`, `Microsoft Azure`                    |

## ⚙️ How to Run
# Step 1: Clone the repo
```
git clone https://github.com/Bhanuraj23m0316iitb/AI-Driven-Real-Estate-Price-Prediction-Recommendation-System.git
cd AI-Driven-Real-Estate-Price-Prediction-Recommendation-System
```

# Step 2: Install dependencies
```
pip install -r requirements.txt
```

# Step 3: Run the app
```
streamlit run App_master/app.py
```
🌍 Live App
Check out the full project here: [AI-Driven Real Estate Recommender](https://realestateprice-csekbrbvegfge0f6.southeastasia-01.azurewebsites.net/)

---

### **🔗 Contributors**  
👤 **Bhanuraj**  
📧 **badalbhanuraj@gmail.com**  

📌 **GitHub Repo**: [GitHub](https://github.com/Bhanuraj23m0316iitb/AI-Driven-Real-Estate-Price-Prediction-Recommendation-System)  


---


