from src.logica.declarative_base import Base
from sqlalchemy import Column, Integer, String, Float

class Entrenamiento(Base):
    
    __tablename__ = 'Entrenamiento'
    id = Column(Integer, primary_key=True)
    persona = Column(String, nullable=False)
    ejercicio = Column(String)
    fecha = Column(String)
    repeticiones = Column(Integer)
    tiempo = Column(Float)
    
    
    
    def __init__(self, persona, ejercicio,fecha, repeticiones,tiempo):
        self.persona = persona
        self.ejercicio = ejercicio
        self.fecha = fecha
        self.repeticiones = repeticiones
        self.tiempo = tiempo
    
    def __repr__(self):
        return f'Entrenamiento({self.persona}, {self.ejercicio}, {self.fecha}, {self.repeticiones}, {self.tiempo})'
    