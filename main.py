import uvicorn
from fastapi import FastAPI, Depends
from starlette.responses import Response
from starlette import status
from crud import *

app = FastAPI()





@app.post('/api/v1/menus/', response_model=MenuResponse, status_code=201)
def post_menu(data: MenuCreate,
              db: Session = Depends(get_db)):
    """Ручка для пост запроса создания меню"""
    create_new_menu = create_menu(db, data)
    return create_new_menu

@app.get('/api/v1/menus/{menu_id}', response_model=MenuResponse, status_code=200)
def get_menu(menu_id: uuid.UUID, db: Session = Depends(get_db)):
    """Ручка для получения детальной информации меню по айдишнику"""
    menu = get_menu_by_id(db, menu_id)
    return menu



@app.get('/api/v1/menus/{menu_id}', response_model=MenuResponse, status_code=200)
def get_menu_detail(menu_id: uuid.UUID, db: Session = Depends(get_db)):
    menu = get_menu_by_id(db, menu_id)
    return menu


@app.patch('/api/v1/menus/{menu_id}', response_model=MenuResponse, status_code=200)
def update(menu_id:uuid.UUID, data:MenuUpdate, db: Session = Depends(get_db)) -> str:
    menu = update_menu(db=db, menu_id=menu_id, data=data)
    return menu


# @app.get('{{LOCAL_URL}}/api/v1/menus', response_model=MenuResponse, status_code=200)
# def get_local_url_menu(data: MenuResponse, db: Session = Depends(get_db)):
#     menu_url = get_local_url_menu(data, db)
#     return menu_url



# @app.get('{{LOCAL_URL}}/api/v1/menus/{{target_menu_id}}')
# def get_local_by_menu_id(target_menu_id, title, description):
#     id_menu = get_menu_by_id(target_menu_id, title,description, target_menu_id)
#     return id_menu




# @app.get('{{LOCAL_URL}}/api/v1/menus/{{target_menu_id}}', status_code=200)
# def check_menu_by_id(menu):
#     menu = get_menu_by_id(menu)
#     return menu



# @app.middleware('http')
# def db_session_middleware(request: Request, call_next):
#     """это middleware для того чтобы к реквесту нашу бд сессию прикрепить"""
#     response = Response('Internal server error', status_code=500)
#     try:
#         request.state.db = sessionlocal
#         response = call_next(request)
#     finally:
#         request.state.db.close()
#     return response


if __name__ == '__main__':
    uvicorn.run(app)
