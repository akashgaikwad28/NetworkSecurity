
## 🛡️ NetworkSecurity: Intelligent Threat Detection Pipeline

A modular, reproducible, and cloud-integrated machine learning pipeline for network security threat detection. Built with FastAPI, DVC, MLflow, and AWS S3, this project demonstrates end-to-end automation—from data ingestion to model deployment—with robust validation and monitoring.

---

## 🚀 Key Features

- ✅ **Modular ML Pipeline**: Ingestion → Validation → Transformation → Training → Deployment
- ✅ **Data Drift Detection**: KS test-based drift reports for production monitoring
- ✅ **Artifact Tracking**: Structured `@dataclass` artifacts for each pipeline stage
- ✅ **Reproducibility**: DVC for data/model versioning, GitHub Actions for CI/CD
- ✅ **Cloud Sync**: AWS S3 integration for artifact and model storage
- ✅ **Experiment Logging**: MLflow tracking via DagsHub
- ✅ **Secure API**: FastAPI backend with CORS and file upload support
- ✅ **Custom Estimator**: `NetworkModel` class for unified preprocessing and prediction

---

## 🧠 Technologies Used

| Category            | Tools & Libraries                                                                 |
|---------------------|-----------------------------------------------------------------------------------|
| **Language**         | Python 3.10+                                                                     |
| **ML Frameworks**    | Scikit-learn, XGBoost, TensorFlow (optional)                                     |
| **Data Validation**  | KS Test (`scipy.stats.ks_2samp`), YAML drift reports                            |
| **Pipeline Tracking**| DVC, MLflow, GitHub Actions                                                      |
| **Cloud Storage**    | AWS S3 via `boto3` and custom `S3Sync` class                                     |
| **API Framework**    | FastAPI, Uvicorn, Jinja2Templates                                                |
| **Security**         | SSL, DNS setup, HTTPS-ready deployment                                           |
| **Artifact Logging** | `@dataclass` for ingestion, validation, transformation, metrics, and model      |
| **Frontend Support** | CORS middleware for React/Next.js integration                                    |

---

## 🧱 Project Structure

```
NetworkSecurity/
├── networksecurity/
│   ├── components/           # Modular pipeline stages
│   ├── entity/               # Config and artifact dataclasses
│   ├── utils/                # ML utilities, metrics, estimators
│   ├── logging/              # Custom logger
│   ├── exception/            # Custom exception handler
│   ├── cloud/                # S3 sync logic
├── templates/                # Jinja2 HTML templates
├── valid_data/               # Cleaned datasets
├── final_model/              # Saved model for deployment
├── .dvc/                     # DVC metadata
├── .env                      # MLflow credentials (not committed)
├── setup.py                  # Package installer
├── requirements.txt          # Dependencies
```

---

## 🔁 Pipeline Flow

1. **Data Ingestion**  
   - Reads raw data, splits into train/test  
   - Stores in feature store and ingested directories

2. **Data Validation**  
   - Schema checks, missing value handling  
   - Drift detection via KS test  
   - Generates YAML drift report

3. **Data Transformation**  
   - Preprocessing (scaling, encoding)  
   - Saves `.npy` arrays and preprocessor object

4. **Model Training**  
   - Trains multiple classifiers with hyperparameter tuning  
   - Logs metrics and artifacts to MLflow  
   - Saves final model and wrapped estimator

5. **Cloud Sync**  
   - Uploads artifacts and final model to AWS S3  
   - Timestamped for reproducibility

---

## 📦 Installation

```bash
git clone https://github.com/akashgaikwad28/NetworkSecurity.git
cd NetworkSecurity
pip install -e .
```

---

## 🔐 Environment Setup

Create a `.env` file in the root directory:

```env
MLFLOW_TRACKING_URI=https://dagshub.com/akashgaikwad746/NetworkSecurity.mlflow
MLFLOW_TRACKING_USERNAME=your_username
MLFLOW_TRACKING_PASSWORD=your_token
```

---

## 🧪 Run the Pipeline

```python
from networksecurity.pipeline.training_pipeline import TrainingPipeline

pipeline = TrainingPipeline()
pipeline.run_pipeline()
```

---

## 📊 MLflow Dashboard

Track experiments, metrics, and models on [DagsHub MLflow UI](https://dagshub.com/akashgaikwad746/NetworkSecurity.mlflow).

---

## ☁️ S3 Integration

Artifacts and final models are synced to:

```
s3://<your-bucket>/artifact/<timestamp>/
s3://<your-bucket>/final_model/<timestamp>/
```

