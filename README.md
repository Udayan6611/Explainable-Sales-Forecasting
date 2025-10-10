# Explainable Sales Forecasting: An End-to-End Deployed Application

This repository documents the creation of a complete sales forecasting system, designed to deliver not just predictions, but actionable, transparent insights. The project transforms a complex, real-world dataset into an interactive web application, containerized with Docker and deployed live on Google Cloud Platform.

---

### Live Demonstration

**Live Application URL:** [**https://sales-forecaster-app-466236414757.us-central1.run.app/**]

![Demo GIF of the Streamlit Application](https://placehold.co/800x450/2d3748/ffffff?text=Add+a+GIF+of+your+live+app+here)

---

### The Business Problem

Standard forecasting models often act as "black boxes," providing predictions without explaining the underlying reasons. This creates a trust deficit, making it difficult for business leaders to make confident, data-driven decisions. The challenge was to build a tool that could not only predict future sales with high accuracy but also provide clear, intuitive explanations for its forecasts, directly addressing the question, "Why is the forecast what it is?"

### Key Results & Achievements

* **Improved Accuracy by 66%:** Through advanced feature engineering (lags, rolling averages), the model's predictive error (RMSE) was reduced by nearly two-thirds compared to a baseline model, demonstrating a strong command of time-series analysis.
* **Full End-to-End Deployment:** Successfully managed the entire project lifecycle from raw data ingestion and cleaning to building a containerized web application and deploying it on Google Cloud Run, showcasing proficiency in both data science and MLOps principles.
* **Achieved Model Transparency:** Integrated SHAP to make the model fully explainable, turning complex predictions into understandable business insights (e.g., quantifying the impact of promotions or holidays on sales).

### Technical Architecture

This project was built with a modern, scalable tech stack, chosen to reflect real-world industry practices.

* **Data Science & Machine Learning:**
    * **Pandas & NumPy:** For high-performance data manipulation and cleaning.
    * **LightGBM:** A gradient-boosting framework chosen for its speed and accuracy on large tabular datasets.
    * **SHAP:** The core library for implementing model-agnostic explainability.
* **Application & Deployment:**
    * **Streamlit:** Used to rapidly develop an interactive and user-friendly web dashboard.
    * **Docker:** For containerizing the application, ensuring consistency and reproducibility across environments.
    * **Google Cloud Platform (GCP):**
        * **Cloud Run:** For deploying the application as a scalable, serverless web service.
        * **Artifact Registry:** To store and manage the container image.
        * **Cloud Build:** To automate the build and packaging process directly in the cloud.

### Local Development Setup

To run this application on your own machine, please follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Udayan6611/Explainable-Sales-Forecasting.git](https://github.com/Udayan6611/Explainable-Sales-Forecasting.git)
    cd Explainable-Sales-Forecasting
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

### Project Learnings & Reflections

This project was a deep dive into the practical realities of building production-ready machine learning systems. The most significant takeaway was the immense value of feature engineering; it was the single most impactful factor in improving model performance. Navigating the challenges of cloud deployment, from dependency management within Docker to network configurations in GCP, provided critical hands-on experience in MLOps. Ultimately, this project solidified my ability to not only build a model but to build a complete, robust, and useful data product.

### Potential Future Enhancements

* **Hyperparameter Tuning:** Implement a systematic tuning process (e.g., using Optuna or Hyperopt) to further optimize the LightGBM model.
* **CI/CD Pipeline:** Automate the testing and deployment process using GitHub Actions to trigger new builds on every push to the main branch.
* **Data Ingestion Pipeline:** Develop a more robust pipeline to automatically pull and process new sales data from a database or data warehouse.

---

### Contact

* **Name:** Udaya Dusane
* **LinkedIn:** www.linkedin.com/in/udayan-dusane-447612291
* **Email:** udayandusane6611@gmail.com
