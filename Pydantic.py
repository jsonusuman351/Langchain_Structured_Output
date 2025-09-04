from pydantic import BaseModel,EmailStr, Field
from typing import Optional


class Person(BaseModel):
    name: str = "John"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(...,gt=0,lt=10,description="cgpa must be between 0 to 10")


new_person ={"age":32,"email":"abc@gmail.com","cgpa":9}
person=Person(**new_person)
person_dict=dict(person)
print(person_dict['name'])  

person_json=person.model_dump_json()
print(person_json)