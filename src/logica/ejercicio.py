from src.logica.declarative_base import Base
from sqlalchemy import Column, Integer, String, Float

class Ejercicio(Base):
    
    __tablename__ = 'Ejercicio'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String(length=200), nullable=False)
    youtube =  Column(String, nullable = False)
    calorias = Column(Float, nullable = False)
    