# Task1_inframind
A simple Worker Management System built using FastAPI that provides CRUD APIs to manage worker profiles, including skills, roles, experience, and assigned tasks. The service is containerized using Docker and deployed on a Kubernetes cluster with Horizontal Pod Autoscaler (HPA) to demonstrate scalable and self-adjusting backend infrastructure.


Employee Management System & Performance Evaluation API

A resilient, containerized FastAPI-based CRUD application designed to manage employee records, simulate heavy production traffic using Locust, and dynamically scale using a Kubernetes Horizontal Pod Autoscaler (HPA) within a Minikube cluster.
🚀 Features
•	FastAPI Backend: Fully typed API endpoints for creating, reading, updating, deleting, and sorting employee details.
•	Data Persistence: Local database simulation using localized structured JSON file reading and updates.
•	Pydantic Validation: Strict metadata validations for schema compliance (e.g., specific ID requirements, experience range constraints).
•	Locust Performance Testing: Dedicated script to simulate realistic multi-user patterns pushing concurrent endpoints.
•	Cloud-Native Autoscaling: Instrumented with a Kubernetes deployment configuration ready to scale infrastructure dynamically up and down based on resource spikes.


## 🛠️ Project Architecture

```text
     [ Locust Test Runners ]
                │
                ▼ (HTTP Concurrent Traffic)
     [ Minikube Tunnel / Port-Forward ]
                │
                ▼
       [ Kubernetes Service ]
                │
       ┌────────┴────────┐ (Load Balancing)
       ▼                 ▼
   [ Pod 1 ]         [ Pod 2 ]  <─── Managed dynamically by HPA


📋 Prerequisites
Ensure you have the following installed locally:
•	Python 3.10+
•	Minikube & kubectl
•	Git


🔧 Installation & Local Setup
	1.	Clone the repository and navigate into the project directory:
git clone https://github.com/priyanshijain25/Task1_inframind.git
cd Task1_inframind
	2.	Set up a Python Virtual Environment:
python3 -m venv venv
source venv/bin/activate
(Windows users run: venv\Scripts\activate)
	1.	Install Dependencies:
pip install fastapi uvicorn pydantic locust
	2.	Run the Server Manually (Optional Dev Check):
uvicorn fastapi.main:app --reload
Once running, open http://localhost:8000/docs in your browser to interact with the Swagger UI documentation.

## 📡 API Endpoints Summary

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/` | API Home / Check Health Status |
| **GET** | `/read` | Fetch all registered employees |
| **GET** | `/read/{employee_id}` | Fetch profile of a specific employee |
| **GET** | `/sort?sort_by=experience` | Sort employee pool by years of experience (`asc`/`desc`) |
| **POST** | `/create` | Register a new compliant employee profile |
| **PUT** | `/update/{employee_id}` | Partially modify tracked employee data patches |
| **DELETE** | `/delete/{employee_id}` | Evict employee record from tracking system |