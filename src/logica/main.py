import declarative_base
from persona import Persona
from entrenamiento import Entrenamiento
from ejercicio import Ejercicio
from reportes import Reportes


def run():
    pass

if __name__ == '__main__':
    declarative_base.Base.metadata.create_all(declarative_base.engine)
    run()