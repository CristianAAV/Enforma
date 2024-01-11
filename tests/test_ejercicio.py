from datetime import date
import unittest
from faker import Faker
from src.logica.logicaEnForma import LogicaEnForma
from src.logica.declarative_base import Session, engine, Base
from src.logica.persona import Persona
from src.logica.ejercicio import Ejercicio
from src.logica.entrenamiento import Entrenamiento

#Generacion de datos con Faker
f = Faker() 

Faker.seed(1000)

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

                # print(self.logica.personas)
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
                self.logica.data_persona=session.query(Persona.id_persona,Persona.nombre,Persona.apellido,Persona.edad,Persona.peso,Persona.talla,Persona.brazo,Persona.pecho,Persona.cintura, Persona.pierna).all()
                """Se hace un for para agregar a self.personas los datos de la base de datos, recorriendo la informacion obtenida con la linea anterior"""
                for datosp in self.logica.data_persona:
                    self.logica.personas.append({'id_persona':datosp.id_persona,'nombre': datosp.nombre, 'apellido':datosp.apellido, 'edad': datosp.edad, 'talla': datosp.talla, 'peso': datosp.peso, 'brazo': datosp.brazo, 'pecho': datosp.pecho, 'cintura': datosp.cintura, 'pierna': datosp.pierna, 'fecha_retiro': '', 'razon_retiro': ''})
                
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


                # print(self.logica.ejercicios)

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
                    self.logica.entrenamientos.append({'persona': self.logica.personas[f.random_int(0,9)]['nombre'], 'ejercicio': self.logica.ejercicios[f.random_int(0,9)]['nombre'], 'fecha': f.date(), 'repeticiones': f.random_int(1,15), 'tiempo': f.random_int(1,300)})

                # print(self.logica.entrenamientos)
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
                    self.logica.entrenamientos.append({'id':datosEN.id,'persona': datosEN.persona, 'ejercicio':datosEN.ejercicio, 'fecha': datosEN.fecha, 'repeticiones': datosEN.repeticiones, 'tiempo': datosEN.tiempo})
                
                session.close()                
                self.logica.data_entrenamientos.clear()
            """se retorna la informacion recuperada."""   
        
  
        
        

# METODOS
class MetodosEnForma(LogicaEnForma):
    def __init__(self):
        self.logica = LogicaEnForma()
        
    def existenciaEjercicio(self):
        return self.logica.ejercicios[-1]
    
    def editar_ejercicio(self, nombre="Sentadilla", descripcion = "ejercicio de pierna", youtube = 'www.youtube.com', calorias = 385):
        self.logica.ejercicios[-1]['nombre'] == nombre
        self.logica.ejercicios[-1]['descripcion']  == descripcion 
        self.logica.ejercicios[-1]['youtube']  == youtube
        self.logica.ejercicios[-1]['calorias'] == calorias   
        
    def ejericio_guardado(self):
        return self.logica.ejercicios[-1]
    
    def borrar_ejercicio(self):
        del self.logica.ejercicios[-1]  
    
        
        
        
        
        
 #PRUEBAS       
        

class TestNewlogica(unittest.TestCase):
   
    def setUp(self):
        self.logica= LogicaEnForma()
        self.logic = MetodosEnForma()
        self.objeto_test = "Objeto para el test"
    
    def tearDown(self):
        self.logicaa = None

    def test_SeCrearLasPruebas(self):
        self.assertIsNotNone(self.objeto_test)

 
    # Historia de usuario 7 - Crear ejercicio       

        ### Prueba 1
    def test_crearEjercicio(self):
       self.logica.crear_ejercicio(f'ejercicio '+str(f.random_int(10,100)),f.sentence(),f'https://www.youtube.com/watch?v='+str(f.random_int(10000,99999)),f.random_int(1,300))        
       self.assertIsNotNone(self.logica.ejercicios[-1])
       
        ### Prueba 2
    def test_existeEjercicios(self):
        self.existeEjericcios = self.logica.ejercicios[-1]
        self.assertIsNotNone(self.existeEjericcios['nombre'])
       
        ### Prueba 3
    def test_ejercicioDescripcion(self):
        self. ejercicioDescripcion= self.logica.ejercicios[-1]
        self.assertIsNotNone(self.ejercicioDescripcion['descripcion'])

        ### Prueba 4
    def test_ejercicioDescripcion(self):
        self. ejercicioDescripcion= self.logica.ejercicios[-1]
        self.assertTrue(len(self.ejercicioDescripcion['descripcion'])<=200)    

    # Historia de usuario 8 - ver listar ejercicios

     ### Prueba 1
    def test_darEjercicio(self):
       self.ejerciciolistado = self.logica.dar_ejercicios()
       self.assertIsNotNone(self.ejerciciolistado[f.random_int(0,9)]['nombre'])
       
    ### Prueba 2
    def test_verificarNombreEjercicio(self):
        self.verificarNombreEjercicio = self.logica.dar_ejercicios()
        self.assertIsInstance(self.verificarNombreEjercicio[f.random_int(0,9)]['nombre'],str)
        self.assertIsInstance(self.verificarNombreEjercicio[f.random_int(0,9)]['descripcion'],str)

    ### Prueba 3
    def test_lendescripcionejercicio(self):
        self.ejercicioDescripcion = self.logica.dar_ejercicios()
        self.assertTrue(len(self.ejercicioDescripcion[f.random_int(0,9)]['descripcion'])<=200)    
    
    ### Prueba 4
    def test_verificarCalorias(self):
        self.verificarCalorias = self.logica.dar_ejercicios()
        self.assertIsInstance(self.verificarCalorias[f.random_int(0,9)]['calorias'],float)
        
    # Historia de usuario 9 - editar ejercicios
    
    def  test_verificarExistenciaEjercicio(self):
        self.existenciaEjericicio = self.logic.existenciaEjercicio()
        self.assertIsInstance(self.existenciaEjericicio,dict)
    
    def test_editar_ejercicio(self):
        self.editar_ejercicio = self.logic.editar_ejercicio()
        self.assertNotEqual(self.editar_ejercicio,self.logica.ejercicios[-1])
        
    def test_verificacion_ejericio_guardado(self):
        self.ejercicio_guardado = self.logic.ejericio_guardado()
        self.assertIsInstance(self.ejercicio_guardado,dict)
        
    def test_borrar_ejercicio(self):
        self.borrar_ejercicio = self.logic.borrar_ejercicio()
        self.assertIsNone(self.borrar_ejercicio)
    
    
    # Historia de usuario 10 - borrar ejercicios
    
    

if __name__ == "__main__":
    unittest.main()