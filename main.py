import uvicorn
from fastapi import FastAPI, Depends
from crud import *

app = FastAPI()







# get all menu
@app.get('/api/v1/menus')
def get_menu(db: Session = Depends(get_db)):
    menu = get_all_menu(db=db)
    return menu
# get menu by id

@app.get('/api/v1/menus/{menu_id}')
def get_menu_id(menu_id:uuid.UUID, db:Session = Depends(get_db)):
    return get_menu_by_id(db=db, menu_id=menu_id)
    # menu = db.query(Menu).filter(Menu.id == menu_id).first()
    # if menu is None:
    #     raise HTTPException(staus_code=404, detail='menu not found')
    # return menu

# create menu
@app.post('/api/v1/menus')
def post_menu(data: MenuCreate,
              db: Session = Depends(get_db)):
    create_new_menu = create_menu(db, data)
    return create_new_menu
# update menu

@app.patch('/api/v1/menus/{menu_id}')
def update(menu_id:uuid.UUID, data:MenuUpdate, db: Session = Depends(get_db)):
    menu = update_menu(db=db, menu_id=menu_id, data=data)
    return menu

# delete menu
@app.delete('/api/v1/menus/{menu_id}')
def delete_menu(menu_id:uuid.UUID, db: Session = Depends(get_db)):
    remove_menu(menu_id=menu_id, db=db)
    return {}


# Submenu
@app.get('/api/v1/menus/{api_test_menu_id}/submenus')
def get_submenu_(db: Session = Depends(get_db)):
    submenu = get_submenu_all(db)
    return submenu

@app.get('/api/v1/menus/{menu_id}/submenus/{submenu_id}')
def submenu_menu(menu_id:uuid.UUID, submenu_id:uuid.UUID, db: Session = Depends(get_db)):
    return get_submenu_with_menu(db=db, menu_id=menu_id, submenu_id=submenu_id)


@app.post('/api/v1/menus/{menu_id}/submenus')
def create_submenus(
        menu_id: uuid.UUID,
        data: SubmenuCreate,
        db: Session = Depends(get_db)
):
    return create_submenu(menu_id=menu_id, submenu=data, db=db)

@app.patch('/api/v1/menus/{menu_id}/submenus/{submenu_id}')
def update_submenu_(
        menu_id: uuid.UUID,
        submenu_id: uuid.UUID,
        data: SubmenuUpdate,
        db: Session = Depends(get_db)
):
    return update_submenu(
        db=db,
        menu_id=menu_id,
        submenu_id=submenu_id,
        data=data
    )
    
@app.delete('/api/v1/menus/{menu_id}/submenus/{submenu_id}')
def delete_submenu_(
        menu_id: uuid.UUID,
        submenu_id: uuid.UUID,
        db: Session = Depends(get_db)
):
    remove_submenu(
        db=db,
        menu_id=menu_id,
        submenu_id=submenu_id,
    )
    return {}

@app.get('/api/v1/menus/{api_test_menu_id}/submenus/{api_test_submenu_id}/dishes')
def get_dish_(db: Session = Depends(get_db)):
    dish = get_dish(db=db)
    return dish
    

@app.get('/api/v1/menus/{api_test_menu_id}/submenus/{api_test_submenu_id}/dishes/{api_test_dish_id}')
def get_dish_id_(dish_id:uuid.UUID, db: Session = Depends(get_db)):
    id_dish = get_dish_by_id(dish_id, db)
    return id_dish

@app.post('/api/v1/menus/{api_test_menu_id}/submenus/{api_test_submenu_id}/dishes')
def create_dish_(dish, db:Session = Depends(get_db)):
    new_dish = create_dish(dish, db)
    return new_dish

@app.patch('/api/v1/menus/{api_test_menu_id}/submenus/{api_test_submenu_id}/dishes/{api_test_dish_id}')
def update_dish_(dish_id, title, description, db:Session = Depends(get_db)):
    return update_dish(
        dish_id=dish_id,
        title=title,
        description=description,
        db=db
        )
    
@app.delete('/api/v1/menus/{api_test_menu_id}/submenus/{api_test_submenu_id}/dishes/{api_test_dish_id}')
def delete_dish(dish_id:uuid.UUID, db = Session(get_db)):
    return remove_dish(dish_id=dish_id, db=db)


if __name__ == '__main__':
    uvicorn.run(app)
