from fastapi import FastAPI , Path , HTTPException , Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel , Field 
from typing import List , Annotated , Optional
import json

app = FastAPI()

class Employee(BaseModel): #annotated adds additional metadata
    id : Annotated[str, Field(...,description = 'ID of employee' , example= '001')]
    name : Annotated[str , Field(...,description = 'Name of employee ')]
    role : Annotated[str , Field(...,description = 'Role of employee' , example= 'Data Engineer')]
    experience : Annotated[int, Field(..., gt = 1 , lt = 10 , description = 'experience in years ', example= 4)]
    skills : List[str]
    assigned_tasks : List[str]
    '''
    from pydantic import computed_field
    @computed_field
    @property
    def position(self) -> str :
        if self.experience < 4:
            return 'Junior Employee'
        elif self.experience >=4:
            return 'Senior Employee'
    '''
class EmployeeUpdate(BaseModel):
    name : Annotated[Optional[str], Field(default = None)]
    role : Annotated[Optional[str],Field(default = None)]
    experience : Annotated[Optional[int],Field(default = None)]
    skills: Annotated[Optional[List[str]], Field(default=None)]
    assigned_tasks: Annotated[Optional[List[str]], Field(default=None)]



def load_data():
    with open('employee.json','r') as f:
        data = json.load(f)

        return data

def save_data(data):
    with open('employee.json','w') as f :
        json.dump(data,f)


@app.get("/")
def hello():
    return {"message": "Employee Management System API "}

@app.get("/read")
def read():
    data = load_data()

    return data

@app.get("/read/{employee_id}")
def view_employee(employee_id : str = Path(...,description = 'employee-id',example = '001')):
    #firstly we will load all the data corresponding to all employees
    data = load_data()

    if employee_id in data :
        return data[employee_id]
    else : raise HTTPException(status_code=404, detail= 'employee not found')

@app.get('/sort')
def sort_employee(sort_by:str = Query(...,description= 'sort on basis of experience'),order:str = Query('asc',description='sort in asc or desc order')):
    valid_fields = ['experience']

    if sort_by not in valid_fields:
        raise HTTPException(status_code = 400, detail='invalid field selected')
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='Invalid order select between asc or desc')
    
    data = load_data()

    reverse = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key=lambda x:x.get(sort_by,0), reverse = reverse)
    return sorted_data

@app.post('/create')
def create_employee(employee : Employee): #pydantic is called here , for all validations
    #firstly we will check if data already exists
    data = load_data()

    if employee.id in data:
        raise HTTPException(status_code =400 , detail='employee already exists')
    #currently data is python dictionary and employee is pydantic object so to concert
    data[employee.id] = employee.model_dump(exclude=['id'])
    #now save this new data to json file
    save_data(data)

    return JSONResponse(status_code=201 , content={'message': 'employee created successfully'})

@app.put('/update/{employee_id}')
def update_employee(employee_id : str , employee_update : EmployeeUpdate):

    data = load_data()

    if employee_id not in data :
        raise HTTPException(status_code = 404,detail='employee not found')
    
    existing_info = data[employee_id]
    updated_info = employee_update.model_dump(exclude_unset=True) #Only the field actually provided is included.

    for key,value in updated_info.items():  #loop chala rhe h on updated while changing values in existing data
        existing_info[key] = value
        
    data[employee_id] = existing_info
    save_data(data)
    return JSONResponse(status_code=200,content={'message':'employee updated successfully'})


@app.delete('/delete/{employee_id}')
def delete_employee(employee_id:str):
    
    data = load_data()

    if employee_id not in data :
        raise HTTPException(status_code = 404,detail='employee not found')

    del data[employee_id]
    save_data(data)

    return JSONResponse(status_code=200,content={'message':'employee deleted successfully'})






    









    

