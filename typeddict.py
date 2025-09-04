from typing import TypedDict, Optional

class person(TypedDict):
    name: str
    age: int
    email: Optional[str]


new_person: person = {
    "name": "Alice",
    "age": 30,
}
print(new_person)