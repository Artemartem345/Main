from sqlalchemy.orm import Session
from models import *
from schema import *

# Menu
def create_menu(db: Session, menu: MenuCreate):
    """функция для создания меню"""
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAA ", menu)
    _menu = Menu(**menu.dict())
    db.add(_menu)
    db.commit()
    db.refresh(_menu)
    return _menu

def get_menu_by_id(db: Session, menu_id: UUID):
    return db.query(Menu).filter(Menu.id == menu_id).first()

def remove_menu(db:Session, menu_id:UUID):
    _menu = get_menu_by_id(title=menu_id.title, description=menu_id.description)
    db.delete(_menu)
    db.commit()
    
def update_menu(db:Session, menu_id:str, data:MenuUpdate):
    menu = db.query(Menu).filter(Menu.id == menu_id).first()
    print('TESTSTSTSTSTSTTSTST', menu)
    menu.title = data.title
    menu.description = data.description
    db.commit()
    db.refresh(menu)
    print(menu)
    return menu
    

# SubMenu
def get_submenu(db:Session):
    return db.query(SubmenuResponse).all()

def get_submenu_by_id(db:Session, menu_id: UUID):
    return db.query(Submenu).filter(Submenu.id == menu_id).first()

def create_submenu(db: Session, menu):
    _menu = Submenu(**menu)
    db.add(_menu)
    db.commit()
    db.refresh(_menu)
    return _menu

def remove_submenu(db:Session, submenu_id: UUID):
    _menu = get_submenu_by_id(title=submenu_id.title, description=submenu_id.description)
    db.delete(_menu)
    db.commit()
    
def update_submenu(db:Session, submenu_id:UUID, data=SubmenuUpdate):
    _submenu = get_submenu_by_id(db=db, submenu_id=submenu_id, _data=data)
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
    
