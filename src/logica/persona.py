import enum

from src.logica.declarative_base import Base
from sqlalchemy import Column, Integer, String, Float

class Persona(Base):
    
    __tablename__ = 'Personas'
    
    id_persona = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    edad = Column(Integer, nullable=False)
    peso = Column(Integer, nullable=False)
    talla = Column(Integer, nullable=False)
    brazo = Column(Integer, nullable=False)
    pecho = Column(Integer, nullable=False)
    cintura = Column(Integer, nullable=False)
    pierna = Column(Integer, nullable=False)
    fecha_retiro = Column(Integer, nullable=False)
    razon_retiro = Column(String(length=200), nullable=False)

    
    
    def __init__(self, nombre,apellido,edad,peso,talla,brazo,pecho,cintura,pierna,razon_retiro,fecha_retiro):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.peso = peso
        self.talla = talla
        self.brazo = brazo
        self.pecho = pecho
        self.cintura = cintura
        self.pierna = pierna
        self.fecha_retiro = fecha_retiro
        self.razon_retiro = razon_retiro
    
    def __repr__(self):
        return f'Persona({self.nombre}, {self.apellido}, {self.edad}, {self.peso}), {self.talla}', {self.brazo}, {self.pecho}, {self.cintura}, {self.pierna}
    