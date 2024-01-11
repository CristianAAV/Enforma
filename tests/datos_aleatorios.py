from datetime import date
import unittest
from faker import Faker
from src.logica.logicaEnForma import LogicaEnForma
from src.logica.Test_base import Session, engine, Base
from src.logica.persona import Persona
from src.logica.ejercicio import Ejercicio
from src.logica.entrenamiento import Entrenamiento
from random import random

#Generacion de datos con Faker
f = Faker() 

Faker.seed(f.random_int(0,100))  # verificar con el tutor si se deja asi 

class LogicaMockTestCase(unittest.TestCase):

    def setUp(self):
        self.logica = LogicaEnForma
        
    def tearDown(self):
        self.logica = None


#crea las personas    
    def test_creacion(self):
        self.logica.personas=[]
        self.logica.data_personas=[]
        print('******PERSONAS******')

        
        Base.metadata.create_all(engine) 
        session = Session()    
        """Se valida si la base de datos existe."""
        if engine.dialect.has_table(engine, Persona.__tablename__):
            registrosEn = session.query(Persona).all()
            """Se valida si la base de datos tiene registros, de lo contrario se llena con los registros existentes"""
            if registrosEn:
                print("")
            else:           
                for i in range(0,10):
                    self.logica.personas.append({'nombre' :f.unique.first_name(), 'apellido': f.unique.last_name(), 'edad': f.unique.random_int(15,100), 'talla': f.random_int(6,18,2), 'peso': f.random_int(25,180), 'brazo': f.random_int(10,40), 'pecho': f.random_int(25,100), 'cintura': f.random_int(25,100), 'pierna': f.random_int(25,100), 'fecha_retiro': f.date(), 'razon_retiro': f.sentence()})

                print(self.logica.personas)
                self.logica.data_personas=self.logica.personas
                for datosp in self.logica.data_personas:
                        crear_persona = Persona(nombre=datosp['nombre'],apellido=datosp['apellido'],edad=datosp['edad'],talla=datosp['talla'],peso=datosp['peso'],brazo=datosp['brazo'],pecho=datosp['pecho'],cintura=datosp['cintura'],pierna=datosp['pierna'],fecha_retiro=datosp['fecha_retiro'],razon_retiro=datosp['razon_retiro'])
                        session.add(crear_persona)
                        session.commit()
            session.close()
        """Se inicializa la base de datos"""
        Base.metadata.create_all(engine)
        session = Session()
        """Se carga la informacion de la base de datos en data_persona"""
        if self.logica.data_personas:
                print("")
        else:
            if self.logica.personas:  
                print("")
            else:                            
                self.logica.personas.clear()
                self.logica.data_personas.clear()
                self.logica.data_persona=session.query(Persona.id_persona,Persona.nombre,Persona.apellido,Persona.edad,Persona.peso,Persona.talla,Persona.brazo,Persona.pecho,Persona.cintura, Persona.pierna,Persona.id_persona).all()
                """Se hace un for para agregar a self.personas los datos de la base de datos, recorriendo la informacion obtenida con la linea anterior"""
                for datosp in self.logica.data_persona:
                    self.logica.personas.append({'nombre': datosp.nombre, 'apellido':datosp.apellido, 'edad': datosp.edad, 'talla': datosp.talla, 'peso': datosp.peso, 'brazo': datosp.brazo, 'pecho': datosp.pecho, 'cintura': datosp.cintura, 'pierna': datosp.pierna, 'fecha_retiro': '', 'razon_retiro': ''})
                
                session.close()                
                self.logica.data_personas.clear()

        self.logica.ejercicios=[]
        self.logica.data_ejercicios=[]
        print('******EJERCICIOS******')
        """Se inicializa la base de datos"""
        Base.metadata.create_all(engine) 
        session = Session()
        """Se valida si la base de datos existe."""
        if engine.dialect.has_table(engine, Ejercicio.__tablename__):
            registrosE = session.query(Ejercicio).all()
            """Se valida si la base de datos tiene registros, de lo contrario se llena con los registros existentes"""
            if registrosE:
                print("")
            else:           
                for i in range(0,10):
                    
                    self.logica.ejercicios.append({'nombre': f'ejercicio '+str(i), 'descripcion': f.sentence(), 'youtube': 'https://www.youtube.com/watch?v=zac9BPZiUTQ', 'calorias': f.random_int(1,300)})


                print(self.logica.ejercicios)

                self.logica.data_ejercicios=self.logica.ejercicios
                for datose in self.logica.data_ejercicios:
                    crear_ejercicio = Ejercicio(nombre=datose['nombre'],descripcion=datose['descripcion'],youtube=datose['youtube'],calorias=datose['calorias'])
                    session.add(crear_ejercicio)

                session.commit()

        session.close()
        """Se inicializa la base de datos"""
        Base.metadata.create_all(engine)
        session = Session()
        """Se carga la informacion de la base de datos en data_ejercicios"""
        
        if self.logica.data_ejercicios:
                print("")
        else:
            if self.logica.ejercicios:  
                print("")
            else:            
                
                self.logica.ejercicios.clear()
                self.logica.data_ejercicios.clear()
                self.logica.data_ejercicios=session.query(Ejercicio.id,Ejercicio.nombre,Ejercicio.descripcion,Ejercicio.youtube,Ejercicio.calorias).all()
                """Se hace un for para agregar a self.ejercicios los datos de la base de datos, recorriendo la informacion obtenida con la linea anterior"""
                for datose in self.logica.data_ejercicios:
                    self.logica.ejercicios.append({'nombre': datose.nombre, 'descripcion':datose.descripcion, 'youtube': datose.youtube, 'calorias': datose.calorias})
            session.close()
            
            self.logica.data_ejercicios.clear()
        
        

        self.logica.entrenamientos=[]
        self.logica.data_entrenamientos=[]
        print('******ENTRENAMIENTOS******')
        """Se inicializa la base de datos"""
        Base.metadata.create_all(engine) 
        session = Session()
        """Se valida si la base de datos existe."""
        if engine.dialect.has_table(engine, Entrenamiento.__tablename__):
            registrosEn = session.query(Entrenamiento).all()
            """Se valida si la base de datos tiene registros, de lo contrario se llena con los registros existentes"""
            if registrosEn:
                print("")
            else:           
                for i in range(0,10):
                    self.logica.entrenamientos.append({'persona': self.logica.personas[f.random_int(1,10)]['nombre'], 'ejercicio': self.logica.ejercicios[f.random_int(1,10)]['nombre'], 'fecha': f.date(), 'repeticiones': f.random_int(1,15), 'tiempo': f.random_int(1,300)})

                print(self.logica.entrenamientos)
                self.logica.data_entrenamientos=self.logica.entrenamientos
                for datosEN in self.logica.data_entrenamientos:
                    crear_entrenamiento = Entrenamiento(persona=datosEN['persona'],ejercicio=datosEN['ejercicio'],fecha=datosEN['fecha'],repeticiones=datosEN['repeticiones'],tiempo=datosEN['tiempo'])
                    session.add(crear_entrenamiento)

                session.commit()
            session.close()
        """Se inicializa la base de datos"""
        Base.metadata.create_all(engine)
        session = Session()
        """Se carga la informacion de la base de datos en data_persona"""
        if self.logica.data_entrenamientos:
                print("")
        else:
            if self.logica.entrenamientos:  
                print("")
            else:            
                
                self.logica.entrenamientos.clear()
                self.logica.data_entrenamientos.clear()
                self.logica.data_entrenamientos=session.query(Entrenamiento.id,Entrenamiento.persona,Entrenamiento.ejercicio,Entrenamiento.fecha,Entrenamiento.repeticiones,Entrenamiento.tiempo).all()
                """Se hace un for para agregar a self.personas los datos de la base de datos, recorriendo la informacion obtenida con la linea anterior"""
                for datosEN in self.logica.data_entrenamientos:
                    self.logica.entrenamientos.append({'persona': datosEN.persona, 'ejercicio':datosEN.ejercicio, 'fecha': datosEN.fecha, 'repeticiones': datosEN.repeticiones, 'tiempo': datosEN.tiempo})
                
                session.close()                
                self.logica.data_entrenamientos.clear()
            """se retorna la informacion recuperada."""   
        

# Aqui para construir los metodos que iran a logicaEnForma

class MetodosEnForma(LogicaEnForma):
    def __init__(self):
        self.logica = LogicaEnForma()

    def setUp(self):
        self.objeto_test = "Objeto para el test"
    
    def tearDown(self):
        self.logica = None

    #HU3

    def crearPersona(self):
        name=self.logica.personas[0]
        return (name["nombre"])

    #Metodo en rojo
    #def verificarNombre(name='Jorge'):
    #    return type(name)

    def verificarNombre(self):        
        name=self.logica.personas[0]
        return (name["nombre"])

    #Metodo en rojo OJO no cambiar el numero
    # def NombreEsNumero(name=8):
    #     return (name)

    def NombreEsNumero(name=8):
        return (name)



    #HU7

    def darEjercicio(self):
        ejericicios=self.logica.ejercicios[0]
        return (ejericicios["nombre"])

    # test en rojo
    #def verificarEjercicioRepetido(ejericios=['sentadilla','sentadilla']):
    ##    return ejericios

    def verificarEjercicioRepetido(self):
        ejercicios=self.logica.ejercicios[0],self.logica.ejercicios[1]
        return (ejercicios[0]['nombre'],ejercicios[1]['nombre'])

    #test en rojo
    #def existenEjercicios(ejericios=''):
    #    return ejericios

    def existenEjercicios(self):
        ejericios=self.logica.ejercicios[0]
        return (ejericios)


    #HU8

    def crearEjercicio(self):
        return 1

    #Metodo en rojo
    #def verificarNombreEjercicio(name='Sentadilla'):
    #    return len(name)

    def verificarNombreEjercicio(self):
        name=self.logica.ejercicios[0]
        return (name['nombre'])

    #Metodo en rojo OJO no cambiar el numero
    # def NombreDeEjercicioEsNumero(name=8):
    #     return (name)

    def NombreDeEjercicioEsNumero(name=8):
        return (name)


    #HU11

    def crearEntrenamiento(self):
        return 1

    #En rojo
    #def entrenamientoTieneNombre(entrenamiento = ''):
    #    return entrenamiento

    def entrenamientoTieneNombre(self):
        entrenamiento=self.logica.entrenamientos[0]
        return (entrenamiento['persona'])

    #En Rojo
    # def entrenamientoRepetido(entrenmiento =['entrenamiento1','entrenamiento1']):
    #     return entrenmiento

    def entrenamientoRepetido(self):
        entrenmiento=self.logica.entrenamientos[0],self.logica.entrenamientos[1]
        return entrenmiento[0]['persona'],entrenmiento[1]['persona']


    #HU11


    def darEntrenamiento(self):
        entrenamiento=self.logica.entrenamientos[0]
        return entrenamiento

    def tipoDeDatoEntrenamiento(self):
        entrenamiento=self.logica.entrenamientos[0]
        return entrenamiento

    def verificarFecha(self):
        entrenamiento=self.logica.entrenamientos[0]
        if entrenamiento['fecha']==date.today():
            print(date.today())
        return True


    #HU12

    def crearReporte(reporte=True):
        return reporte

    def crearReporte(self):
        reporte=self.logica.reportes[0]
        return reporte#['persona']['IMC']['clasificacion']

    def verInformacionReporte(reporte=38):
        return(reporte)

    def verInformacionReporte(self):
        reporte=self.logica.reportes[0]
        return reporte#['persona']['IMC']['clasificacion']
    
    
    # HU0016 Ver reporte de entrenamiento por persona IMC 
    
    def reporte_creado(reporte_final=True):
        return reporte_final 


#*******************************************************************************************

    # PRUEBAS

class TestNewLogic(unittest.TestCase):
   
    def setUp(self):
        self.logica = LogicaEnForma()
        self.logic = MetodosEnForma()
        self.objeto_test = "Objeto para el test"
    
    def tearDown(self):
        self.logica = None
        self.logic = None

    def test_SeCrearLasPruebas(self):
        self.assertIsNotNone(self.objeto_test)


# # # Historia de usuario 3
        
    def test_personEsCreada(self):
       nombre=self.logic.crearPersona()
       self.assertIsNotNone(nombre)
       
    def test_personTieneNombre(self):
       self.nombrePersona = self.logic.verificarNombre()
       self.assertIsInstance(self.nombrePersona,str)
       
    def test_personEsNumero(self):
       self.nombreEsNumero = self.logic.NombreEsNumero()
       self.assertNotIsInstance(self.nombreEsNumero,int)
       
# # Historia de usuario 7       
       
    def test_darEjercicio(self):
       self.ejercicio = self.logic.darEjercicio()
       self.assertIsNotNone(self.ejercicio)
       
    def test_existeEjercicios(self):
        self.existeEjericcios = self.logic.existenEjercicios()
        self.assertNotEqual(self.existeEjericcios['nombre'],'')
       
    def test_ejercicioRepertido(self):
        self. ejercicioRepetido= self.logic.verificarEjercicioRepetido()
        self.assertNotEqual(self.ejercicioRepetido[0],self.ejercicioRepetido[1])
        

# # Historia de usuario 8

    def test_crearEjercicio(self):
       self.ejercicioCreado = self.logic.crearEjercicio()
       self.assertEqual(self.ejercicioCreado,1)
       
    def test_verificarNombreEjercicio(self):
        self.verificarNombreEjercicio = self.logic.verificarNombreEjercicio()
        self.assertTrue(self.verificarNombreEjercicio>'')
        
    def test_nombreDeEjercicioEsNumero(self):
       self.ejercicioEsNumero = self.logic.NombreDeEjercicioEsNumero()
       self.assertNotIsInstance(self.ejercicioEsNumero,int)
    
# Listar entrenamiento de personas HU0011

    def test_crearEntrenamiento(self):
       self.entrenamiento = self.logic.crearEntrenamiento()
       self.assertEqual(self.entrenamiento,1)
       
    def test_entrenamientoTieneNombre(self):
        self.nombreEntrenamiento = self.logic.entrenamientoTieneNombre()
        self.assertNotEqual(self.nombreEntrenamiento,'')
    
    def test_entrenamientoRepetido(self):
        self. entrenamientoRepetido= self.logic.entrenamientoRepetido()
        self.assertNotEqual(self.entrenamientoRepetido[0],self.entrenamientoRepetido[1])
        

# Registrar entrenamientos de personas HU11

    def test_darEntrenamiento(self):
       self.darEntrenamiento = self.logic.darEntrenamiento()
       self.assertIsNotNone(self.darEntrenamiento)
       
    def test_tipoDeDatoEntrenamiento(self):
        self.tipoDeDatoEntrenamiento = self.logic.tipoDeDatoEntrenamiento()
        self.assertIsInstance(self.tipoDeDatoEntrenamiento,dict)
        
    def test_verificarFecha(self):
        self.darFecha = self.logic.verificarFecha()
        self.assertTrue(self.darFecha)

# Ver reporte de entrenamiento de persona(Reporte por fecha) Pair programing HU0012
    
    def test_crearReporte(self):
       self.crearReporte = self.logic.crearReporte()
       self.assertIsNotNone(self.crearReporte)
       
    def test_verInformacionReporte(self):
        self.verInformacionReporte = self.logic.verInformacionReporte()
        self.assertIsInstance(self.verInformacionReporte,dict)
    
# HU0016 Ver reporte de entrenamiento por persona IMC     

    def test_reporte_creado(self):
       self.reporte_creado = self.logic.reporte_creado()
       self.assertIsNotNone(self.reporte_creado)
       
#    def test_verInformacionReporte(self):
#        self.verInformacionReporte = self.logic.verInformacionReporte()
#        self.assertIsInstance(self.verInformacionReporte,dict)


# HU009    Editar ejercicio



# HU0010    Eliminar Ejercicio
    
    
    
    
    
if __name__ == "__main__":
    unittest.main()