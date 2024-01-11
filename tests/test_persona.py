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
        
  
        
        
# PRUEBAS

class TestNewlogica(unittest.TestCase):
   
    def setUp(self):
        self.logica= LogicaEnForma()
        self.objeto_test = "Objeto para el test"
    
    def tearDown(self):
        self.logicaa = None

    def test_SeCrearLasPruebas(self):
        self.assertIsNotNone(self.objeto_test)
    
    
    
    # Historia de usuario 2 - Crear nueva persona


    # Historia de usuario 3 - listar personas

        ### Prueba 1
    def test_personEsCreada(self):
       nombre=self.logica.dar_personas()
       self.assertIsNotNone(nombre[f.random_int(0,9)]['nombre'])
       self.assertIsNotNone(nombre[f.random_int(0,9)]['apellido'])
       
        ### Prueba 2
    def test_personTieneNombre(self):
       self.nombrePersona = self.logica.dar_personas()
       self.assertIsInstance(self.nombrePersona[f.random_int(0,9)]['nombre'],str)
       self.assertIsInstance(self.nombrePersona[f.random_int(0,9)]['apellido'],str)
       
        ### Prueba 3
    def test_personEsNumero(self):
       self.nombreEsNumero = self.logica.dar_personas()
       self.assertNotIsInstance(self.nombreEsNumero[f.random_int(0,9)]['nombre'],int)
       self.assertNotIsInstance(self.nombreEsNumero[f.random_int(0,9)]['apellido'],int)

        ### Prueba 4
    def test_personEsNumero(self):
       self.edadEsNumero = self.logica.dar_personas()
       self.assertIsInstance(self.edadEsNumero[f.random_int(0,9)]['edad'],int)
       
       
    # Historia de usuario 4 - Editar informacion persona
    
    
    # Historia de usuario 6 - Eliminar informacion persona
    
    
    # Historia de usuario 15 - Generar reporte persona  #### Pair programing
    
        ### Prueba 1
    def test_Reporteperson(self):
       self.reporte = self.logica.dar_reporte(4)
       self.assertIsNotNone(self.reporte)

        ### Prueba 2
    def test_prueba_fecha(self):
       self.reporte = self.logica.entrenamientos_fecha(self.logica.personas[4])
       self.assertIsNotNone(self.reporte)
       
       ### Prueba 3
       
    def test_cantidad_ejercicios_realizados(self):
        self.reporte=[]
        self.reporte = self.logica.entrenamientos_fecha(self.logica.personas[4])
        self.reporte,repeticiones,calorias = self.logica.entrenamientos_fecha(self.logica.personas[4])
        self.assertEqual(self.reporte[0]['repeticiones'],8)   
        self.assertIsNotNone(repeticiones)     

       ### Prueba 4
    def test_cantidad_calorias(self):    
        self.reporte,repeticiones,calorias = self.logica.entrenamientos_fecha(self.logica.personas[4])
        self.assertIsNotNone(calorias)

       ### Prueba 5
       
    def test_IMC(self):
        self.reporte = self.logica.calcular_imc(float(self.logica.personas[4]['peso']),float(self.logica.personas[4]['talla']))
        self.assertIsInstance(self.reporte,float) 
    
       ### Prueba 6 
    def test_categoria_IMC(self):
        self.imc = self.logica.calcular_imc(float(self.logica.personas[4]['peso']),float(self.logica.personas[4]['talla']))
        self.reporte = self.logica.clasificar_imc(self.imc)
        
        self.assertEqual(self.reporte,"Bajo peso")
    
    
       ### Prueba 7
    def test_reporte(self):
        self.reporte=self.logica.reportes[0]
        self.assertIsNotNone(self.reporte)
       
       ### Prueba 8
    def test_inforeporte(self):
        self.reporte=self.logica.reportes[0]
        self.assertIsInstance(self.reporte['persona'],str)
        self.assertIsInstance(self.reporte['imc'],float)
        self.assertIsInstance(self.reporte['clasificacion'],str)
        self.assertIsInstance(self.reporte['entrenamientos'],list)


if __name__ == "__main__":
    unittest.main()