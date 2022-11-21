from pydantic import EmailStr, BaseModel

class EmailSchema(BaseModel):
  email: EmailStr
  username: str
  new_clave: str