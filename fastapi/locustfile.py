from locust import HttpUser, task, between
import random

class EmployeeAPIUser(HttpUser):
    # Simulates a delay between 1 to 2 seconds between tasks per user
    wait_time = between(1, 2)

    @task(3)
    def view_all_employees(self):
        """Hits your @app.get('/read') endpoint"""
        self.client.get("/read")

    @task(2)
    def view_specific_employee(self):
        """Hits your @app.get('/read/{employee_id}') endpoint"""
        # Testing a known ID format from your Pydantic examples
        self.client.get("/read/001")

    @task(2)
    def sort_employees(self):
        """Hits your @app.get('/sort') endpoint with query parameters"""
        order = random.choice(["asc", "desc"])
        self.client.get(f"/sort?sort_by=experience&order={order}")

    @task(1)
    def create_employee(self):
        """Hits your @app.post('/create') endpoint with complete Pydantic data"""
        # Generating a unique random ID so it doesn't constantly trigger your 
        # 'employee already exists' 400 HTTPException
        random_id = str(random.randint(100, 999))
        
        payload = {
            "id": random_id,
            "name": f"Load Test User {random_id}",
            "role": "Data Engineer",
            "experience": random.randint(2, 9),  # Must be gt 1 and lt 10
            "skills": ["Python", "FastAPI", "Locust"],
            "assigned_tasks": ["Optimize APIs", "Write Load Tests"]
        }
        
        self.client.post("/create", json=payload)