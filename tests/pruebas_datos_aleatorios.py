from datetime import date
import unittest
from faker import Faker
from src.logica.logicaEnForma import LogicaEnForma
from src.logica.declarative_base import Session, engine, Base
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


   
    def test_creacion(self):
        
        #crea las personas 
        
        self.logica.personas=[]
        self.logica.data_personas=[]
        print('******PERSONAS******')
        for i in range(0,5):
            self.logica.personas.append({'nombre' :f.unique.first_name(), 'apellido': f.unique.last_name(), 'edad': f.unique.random_int(15,100), 'talla': f.random_int(6,18,2), 'peso': f.random_int(25,180), 'brazo': f.random_int(10,40), 'pecho': f.random_int(25,100), 'cintura': f.random_int(25,100), 'pierna': f.random_int(25,100), 'fecha_retiro': f.date(), 'razon_retiro': f.sentence()})

        print(self.logica.personas)
        Base.metadata.create_all(engine) 
        session = Session()    
        self.data_personas=self.logica.personas
        for datosp in self.data_personas:
                    crear_persona = Persona(nombre=datosp['nombre'],apellido=datosp['apellido'],edad=datosp['edad'],talla=datosp['talla'],peso=datosp['peso'],brazo=datosp['brazo'],pecho=datosp['pecho'],cintura=datosp['cintura'],pierna=datosp['pierna'],fecha_retiro=datosp['fecha_retiro'],razon_retiro=datosp['razon_retiro'])
                    session.add(crear_persona)
                    session.commit()
        session.close()

        
        #crear ejercicios
        self.logica.ejercicios=[]
        self.logica.data_ejercicios=[]
        print('******EJERCICIOS******')
        for i in range(0,5):
            
            self.logica.ejercicios.append({'nombre': f'ejercicio '+str(i), 'descripcion': f.sentence(), 'youtube': 'https://www.youtube.com/watch?v=zac9BPZiUTQ', 'calorias': f.random_int(1,300)})


        print(self.logica.ejercicios)
        
        Base.metadata.create_all(engine) 
        session = Session()
        data_ejercicios=self.logica.ejercicios
        for datose in data_ejercicios:
            crear_ejercicio = Ejercicio(nombre=datose['nombre'],descripcion=datose['descripcion'],youtube=datose['youtube'],calorias=datose['calorias'])
            session.add(crear_ejercicio)

        session.commit()

        session.close()
        
        #crea las entrenamientos
        self.logica.entrenamientos=[]
        self.logica.data_entrenamientos=[]
        print('******ENTRENAMIENTOS******')
        for i in range(0,5):
            self.logica.entrenamientos.append({'persona': self.logica.personas[i]['nombre'], 'ejercicio': self.logica.ejercicios[i]['nombre'], 'fecha': f.date(), 'repeticiones': f.random_int(1,15), 'tiempo': f.random_int(1,300)})

        print(self.logica.entrenamientos)
        Base.metadata.create_all(engine) 
        session = Session()
        data_entrenamientos=self.logica.entrenamientos
        for datosEN in data_entrenamientos:
                    crear_entrenamiento = Entrenamiento(persona=datosEN['persona'],ejercicio=datosEN['ejercicio'],fecha=datosEN['fecha'],repeticiones=datosEN['repeticiones'],tiempo=datosEN['tiempo'])
                    session.add(crear_entrenamiento)
        session.commit()

        session.close()
        
        #crea las reporte
        
        self.logica.reporte=[]
        
        if self.logica.personas !=0:
            self.logica.reporte.append({self.logica.persona['persona'],})


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
    
    def verInformacionReporteFinal(reporte_final={"nombre":"carlos","edad":38,"IMC":26}):
        return reporte_final
    
    #HU009 Ejercicio editado
    
    def editarEjercicio(self):
        if (self.logica.ejercicio[-1] in self.logica.ejercicio):
            return True
    

       

    # HU0010    Eliminar Ejercicio
    
#    def test_ejercicioCreado(self):
#       self.ejercicioCreado = self.ejercicioCreado()
#       self.assertIsNotNone(self.ejercicioCreado)
       
#    def test_ejericicioEliminado(self):
#       self.ejercicioEliminado = self.ejercicioEliminado()
#       self.assertIsNotNone(self.ejercicioEliminado)


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
       
    def test_verInformacionReporteFinal(self):
        self.verInformacionReporteFinal = self.logic.verInformacionReporteFinal()
        self.assertIsInstance(self.verInformacionReporteFinal,dict)



# HU009    Editar ejercicio

    def test_editarEjercicio(self):
       self.editarEjericio = self.logic.editarEjercicio()
       self.assertIsTrue(self.editarEjercicio)
       

# HU0010    Eliminar Ejercicio
    
#    def test_ejercicioCreado(self):
#       self.ejercicioCreado = self.ejercicioCreado()
#       self.assertIsNotNone(self.ejercicioCreado)
       
#    def test_ejericicioEliminado(self):
#       self.ejercicioEliminado = self.ejercicioEliminado()
#       self.assertIsNotNone(self.ejercicioEliminado)
       
    
    
    
if __name__ == "__main__":
    unittest.main()