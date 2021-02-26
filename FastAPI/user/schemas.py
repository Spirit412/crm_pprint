from pydantic import BaseModel, condecimal
from datetime import datetime

class UserSchema(BaseModel):
    id: str
    email: str
    name: str
    created_on: datetime
    updated_on: datetime
    is_active: str
    is_admin: str
    role: str
