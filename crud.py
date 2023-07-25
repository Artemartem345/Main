from sqlalchemy.orm import Session
from models import *
from schema import *
from fastapi import HTTPException
from starlette import status

# Menu
def create_menu(db: Session, menu: MenuCreate):
    """функция для создания меню"""
    _menu = Menu(**menu.dict())
    db.add(_menu)
    db.commit()
    db.refresh(_menu)
    return _menu

def get_all_menu(db:Session):
    return db.query(Menu).all()


def get_menu_by_id(db: Session, menu_id: int):
    menu = db.query(Menu).filter(Menu.id == menu_id).first()
    if not menu:
        raise HTTPException(
            detail='menu not found',
            status_code=status.HTTP_404_NOT_FOUND
            )
        
    return menu
    

def remove_menu(db:Session, menu_id:UUID):
    _menu = get_menu_by_id(db=db, menu_id=menu_id)
    db.delete(_menu)
    db.commit()
    
def update_menu(db:Session, menu_id:uuid.UUID, data:MenuUpdate):

    menu = db.query(Menu).filter(Menu.id == menu_id).first()
    menu.title = data.title
    menu.description = data.description
    db.add(menu)
    db.commit()
    db.refresh(menu)
  
    return menu
    

# SubMenu
def get_submenu_all(db:Session):
    return db.query(Submenu).all()

def get_submenu_with_menu(db:Session, menu, submenu):
    submenu = db.query(Submenu).filter_by(
        id=submenu,
        menu_id=menu
        ).first()
    return submenu

def create_submenu(db: Session, submenu:uuid.UUID):
    _menu = Submenu(**submenu)
    db.add(_menu)
    db.commit()
    db.refresh(_menu)
    return _menu

def remove_submenu(db:Session, submenu_id: UUID):
    _menu = get_submenu_with_menu(title=submenu_id.title, description=submenu_id.description)
    db.delete(_menu)
    db.commit()
    
def update_submenu(db:Session, submenu_id:UUID, menu_id, data=SubmenuUpdate):
    _submenu = get_submenu_with_menu(db=db, submenu_id=submenu_id, menu_id=menu_id)
    db.commit()
    db.refresh(_submenu)
    return _submenu


def get_dish(db:Session):
    return db.query(Dish).all()
# Получение блюда по айдишнику
def get_dish_by_id(db:Session, dish_id:UUID):
    return db.query(Dish(DishResponse)).filter(Dish.id == dish_id).first()
# Создание блюда
def create_dish(db:Session, dish: DishCreate):
    _dish = Dish(title=dish.title,description=dish.description)
    db.add(_dish)
    db.commit()
    db.refresh(_dish)
    return _dish
# Удаление блюда
def remove_dish(db:Session, dish_id: UUID):
    _dish = get_dish_by_id(db=db, dish_id=dish_id)
    db.delete(_dish)
    db.commit()
# Обновление блюда
def update_dish(db:Session, dish_id: UUID, title:str, description:str):
    _dish = get_dish_by_id(db=db, dish_id=dish_id)
    _dish.title = title
    _dish.description = description
    db.commit()
    db.refresh(_dish)
    return _dish
    
