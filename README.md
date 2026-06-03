# Task1_inframind
A simple Worker Management System built using FastAPI that provides CRUD APIs to manage worker profiles, including skills, roles, experience, and assigned tasks. The service is containerized using Docker and deployed on a Kubernetes cluster with Horizontal Pod Autoscaler (HPA) to demonstrate scalable and self-adjusting backend infrastructure.

DockerHub Repo:
https://hub.docker.com/r/pjdocker1106/employee-management

Working and load test results :

1) FastAPI Interface :
   <img width="2940" height="1846" alt="image" src="https://github.com/user-attachments/assets/395567e8-fde7-4ec2-93e4-0c48286b0293" />

2) Libraries and Paramenters Used :
   <img width="1216" height="262" alt="image" src="https://github.com/user-attachments/assets/86636479-8b21-4fbd-8562-61049d94a445" />

3) Pods status while load was increased and decreased , hpa autoscaled pods to 5 nd then back to minimum 2 :
   <img width="1268" height="900" alt="image" src="https://github.com/user-attachments/assets/b2e22430-4143-4456-bd81-1720e1655dfa" />

4) This shows current cpu utilization during load , u see how percentage spiked first , then hpa did the math nd changed the no of replica :
   <img width="1280" height="876" alt="image" src="https://github.com/user-attachments/assets/0bc25625-1101-49a1-a4bf-cce6de8ba00c" />

5) Locust Dashboard:
   <img width="2940" height="1846" alt="image" src="https://github.com/user-attachments/assets/f731643c-5453-428e-a1c4-d6451ad0b873" />

Employee Management System & Performance Evaluation API

A resilient, containerized FastAPI-based CRUD application designed to manage employee records, simulate heavy production traffic using Locust, and dynamically scale using a Kubernetes Horizontal Pod Autoscaler (HPA) within a Minikube cluster.
🚀 Features
•	FastAPI Backend: Fully typed API endpoints for creating, reading, updating, deleting, and sorting employee details.
•	Data Persistence: Local database simulation using localized structured JSON file reading and updates.
•	Pydantic Validation: Strict metadata validations for schema compliance (e.g., specific ID requirements, experience range constraints).
•	Locust Performance Testing: Dedicated script to simulate realistic multi-user patterns pushing concurrent endpoints.
•	Cloud-Native Autoscaling: Instrumented with a Kubernetes deployment configuration ready to scale infrastructure dynamically up and down based on resource spikes.


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

