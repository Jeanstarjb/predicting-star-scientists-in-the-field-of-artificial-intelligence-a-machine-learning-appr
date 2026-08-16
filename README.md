# 🌟 Predicting Star Scientists in the Field of Artificial Intelligence: A Machine Learning Approach

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/<your-repo>/tree/main.svg?style=shield)](https://dl.circleci.com/status-badge/redirect/gh/<your-repo>/tree/main)
[![Python](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95.2-green.svg)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13-blue.svg)](https://www.postgresql.org/)
[![License](https://img.shields.io/github/license/<your-repo>)](./LICENSE)

## 🚀 Project Overview..

This project leverages **machine learning** and **data science** to identify and predict "star scientists" in the field of **Artificial Intelligence (AI)**. By analyzing academic and professional data such as citation counts, h-index, publication records, and collaboration patterns, this platform provides insights into the factors that contribute to impactful careers in AI research.

The application combines **FastAPI** for a robust backend API, **PostgreSQL** for data persistence, and **scikit-learn** for machine learning. With a clean and modular architecture, this platform offers an end-to-end pipeline for training, evaluating, and deploying models while providing an intuitive interface for users to interact with the system

---

## 💡 The Societal Problem It Solves

The rapid growth of AI research has made it challenging to identify emerging talent in the field. Academic institutions, funding agencies, and organizations often struggle to identify promising researchers who are poised to make groundbreaking contributions. This platform addresses this challenge by:

- **Empowering Research Institutions**: Helps organizations identify and support talented researchers early in their careers.
- **Promoting Diversity**: Provides tools to measure and improve diversity in AI research communities.
- **Enhancing Scientific Impact**: Helps researchers and organizations focus resources on high-potential individuals and projects.
- **Objective Decision-Making**: Reduces bias in talent identification by leveraging data-driven machine learning models.

---

## 🏗️ System Architecture

The application is structured as a **modular microservice-based architecture**, fostering scalability, maintainability, and flexibility.

### **Backend**
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) for high-performance and asynchronous API development.
- **Database**: [PostgreSQL](https://www.postgresql.org/) for storing user data, researcher profiles, publications, and predictions.
- **Machine Learning**: Models built with [scikit-learn](https://scikit-learn.org/) for predicting high-potential researchers.
- **Dockerized Deployment**: Backend is containerized using Docker for portability and consistency.

### **Frontend**
- **Frontend Framework**: React.js (future implementation).
- **API Integration**: Seamless connection with the FastAPI backend for interactive user interfaces.

### **Continuous Integration/Delivery**
- **CircleCI**: Automated testing and deployment pipeline for robust CI/CD.

### **Key Components**
1. **Authentication Service**:
   - User registration, login, and token-based authentication.
   - Role-based access control for admins and researchers.
2. **Prediction Service**:
   - Accepts input features and provides a prediction of the likelihood of a researcher becoming a "star scientist."
3. **Insights Service**:
   - Diversity metrics based on collaboration, institutional affiliations, and publication venues.
4. **Database**:
   - Stores user details, researcher profiles, and prediction logs.
5. **Machine Learning Model**:
   - Pre-trained model using scikit-learn with a custom preprocessing pipeline for feature transformation.

---

## 🛠️ Getting Started

### Prerequisites

Ensure you have the following installed:

- **Docker**: [Installation Guide](https://docs.docker.com/get-docker/)
- **Python 3.9+**: [Download Python](https://www.python.org/downloads/)
- **PostgreSQL 13+**: [Download PostgreSQL](https://www.postgresql.org/download/)

---

### Clone the Repository

```bash
git clone https://github.com/<your-repo>.git
cd <your-repo>
```

---

### Backend Setup

1. **Create a `.env` file** in the `backend` directory with the following content:

    ```env
    DATABASE_URI=postgresql://user:password@localhost:5432/dbname
    SECRET_KEY=your_secret_key
    ```

2. **Build and Run Docker Containers**:

    ```bash
    docker-compose up --build
    ```

3. **Run Backend Tests**:

    ```bash
    docker exec -it <backend_container_id> pytest backend/tests/
    ```

---

### Frontend Setup (Planned for Future)

Frontend development is in progress. Stay tuned for updates!

---

## ✨ Key Features

### 🎯 Predict Star Scientists
- Input researcher data (e.g., citation count, h-index, years since first publication) and predict their likelihood of becoming a star scientist.

### 📊 Diversity Metrics
- Analyze diversity metrics across collaboration networks, institutions, and publication venues.

### 🔒 Authentication
- Secure user authentication with role-based access control for researchers, admins, and funding agencies.

### 🌍 Insights Dashboard (Upcoming)
- Visualize trends in AI research, track emerging talent, and explore collaboration opportunities.

### ⚙️ RESTful API
- Fully documented API for seamless integration with external systems. [API Reference](docs/API_REFERENCE.md)

---

## 🔧 Development and Contribution

We welcome contributions! To contribute:

1. Fork this repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit: `git commit -m "Description of changes"`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

---

## 🧪 Testing

We use **pytest** for unit, integration, and end-to-end testing.

### Run Tests:

```bash
docker exec -it <backend_container_id> pytest backend/tests/
```

**Note**: Tests include database mocks, authentication flows, and prediction accuracy.

---

## 📂 File Structure

```plaintext
.
├── backend
│   ├── database.py         # Database connection setup
│   ├── main.py             # FastAPI app entry point
│   ├── models.py           # Database models (SQLAlchemy)
│   ├── routers             # Modular API routes
│   │   ├── auth.py
│   │   ├── predictions.py
│   │   ├── researchers.py
│   │   ├── insights.py
│   ├── schemas.py          # Pydantic models for API validation
│   ├── preprocessing.py    # Machine learning preprocessing pipelines
│   ├── tests               # Unit and integration tests
│       ├── test_auth.py
│       ├── test_predictions.py
│       ├── test_e2e.py
├── ml_model
│   ├── model.joblib        # Pre-trained machine learning model
├── .circleci
│   ├── config.yml          # CI/CD pipeline configuration
├── docker-compose.yml      # Docker Compose configuration
├── README.md               # Project documentation
```

---

## 🌟 Future Enhancements

- **Frontend Application**: Build a React-based UI for user interaction.
- **Advanced Analytics**: Add more insights, including geographic distribution and funding trends.
- **Real-Time Updates**: Enable real-time predictions and analytics.

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
