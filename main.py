import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from starlette.responses import Response
from starlette import status
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




if __name__ == '__main__':
    uvicorn.run(app)
