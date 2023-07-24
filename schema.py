import decimal
import uuid
from typing import Optional

from pydantic import BaseModel


# # Action with DISH
class DishCreate(BaseModel):
    title: str
    description: str
    price: decimal.Decimal


class DishUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    price: Optional[decimal.Decimal]


class DishResponse(BaseModel):
    id: uuid.UUID
    title: str
    description: str
    submenu_id: uuid.UUID
    price: decimal.Decimal

    class Config:
        from_attributes = True


# Action with Menu
class MenuCreate(BaseModel):
    title: str
    description: str


class MenuUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]


class MenuResponse(BaseModel):
    id: uuid.UUID
    title: str
    description: str
    submenus_count: int = 0
    dishes_count: int = 0

    class Config:
        from_attributes = True

#
# Action with SubMenu
class SubmenuCreate(BaseModel):
    title: str
    description: str


class SubmenuUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]


class SubmenuResponse(BaseModel):
    id: uuid.UUID
    title: str
    description: str
    menu_id: uuid.UUID
    dishes_count: int = 0

    class Config:
        from_attributes = True
