from pydantic import BaseModel

class UserLogin(BaseModel):
    username: str
    password: str

class UserCreate(UserLogin):
    pass

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class ProductBase(BaseModel):
    name: str
    type: str
    sku: str
    image_url: str
    description: str
    quantity: int
    price: float

class ProductOut(ProductBase):
    id: int
    class Config:
        orm_mode = True

class QuantityUpdate(BaseModel):
    quantity: int
