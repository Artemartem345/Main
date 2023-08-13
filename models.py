from sqlalchemy import create_engine, Column, String, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.dialects.postgresql import UUID 
import uuid
# коннект урл к бд
connection_url = "postgresql://polka:qwerty@127.0.0.1:5432/Food_menu"
# движок для подключения
engine = create_engine(connection_url)
# сессия с привязанным движко
sessionlocal = scoped_session(sessionmaker(bind=engine))
metadata = MetaData()
Base = declarative_base()


def get_db():
    session = sessionlocal()
    try:
        yield session
    finally:
        session.close()

class Menu(Base):
    __tablename__ = 'menus'

    # обрати внимание как прописана автогенерация UUID
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    title = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
    submenus = relationship('Submenu', back_populates='menu', cascade='all, delete')


class Submenu(Base):
    __tablename__ = 'submenus'

    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    title = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
    menu_id = Column(UUID, ForeignKey('menus.id'))
    menu = relationship('Menu', back_populates='submenus')
    dishes = relationship('Dish', back_populates='submenu', cascade='all, delete')


class Dish(Base):
    __tablename__ = 'dishes'

    # обрати внимание как прописана автогенерация UUID
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    title = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
    price = Column(String, nullable=False)
    submenu_id = Column(UUID, ForeignKey('submenus.id'))
    submenu = relationship('Submenu', back_populates='dishes')

Base.metadata.create_all(bind=engine)

### для миграции просто пропиши alembic upgrade head в консоли

