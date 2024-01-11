from datetime import datetime
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
class MetodosEnForma(LogicaEnForma):
    def __init__(self):
        self.logica = LogicaEnForma()

    def crearEntrenamiento(self):
        if(self.logica.dar_entrenamientos!=0):
            return True  
        
    def entrenamientoTieneNombre(self):
        return self.logica.entrenamientos[-1]['persona']
        
    def entrenamientoRepetido(self):
        return self.logica.entrenamientos[-1],self.logica.entrenamientos[-2]   
    
    def fechaEntrenamiento(self):
        print(datetime.now().date())
        print(self.logica.entrenamientos[-1]['fecha'])
        if (self.logica.entrenamientos[-1]['fecha']!= datetime.now().date()):
            return True
        else:    
            raise ValueError('Date cannot be before than today') 
        
    def cantidadDeRepeticiones(self):
        if(self.logica.entrenamientos[-1]["repeticiones"]>0):
            return True
        
    def tiempoDeEjercicio(self):
        return self.logica.entrenamientos[-1]['tiempo']
    
    def guardadoEjericicio(self):
        if (self.logica.entrenamientos[-1]["ejercicio"] == self.logica.ejercicios[-1]["nombre"]):
            return True
        
        

class TestNewlogica(unittest.TestCase):
   
    def setUp(self):
        self.logica= LogicaEnForma()
        self.logic = MetodosEnForma()
        self.objeto_test = "Objeto para el test"
    
    def tearDown(self):
        self.logicaa = None


    # registrar entrenamiento de personas HU0011

        ### Prueba 1
    def test_listarEntrenamiento(self):
        entrenamiento=self.logica.entrenamientos              
        self.assertIsNotNone(entrenamiento[f.random_int(0,9)]['persona'])
        self.assertIsNotNone(entrenamiento[f.random_int(0,9)]['ejercicio'])

        ### Prueba 2
    def test_listarEntrenamientostr(self):
        entrenamiento=self.logica.entrenamientos              
        self.assertIsInstance(entrenamiento[f.random_int(0,9)]['persona'],str)
        self.assertIsInstance(entrenamiento[f.random_int(0,9)]['ejercicio'],str)

        ### Prueba 3
    def test_listarEntrenamientoint(self):
        entrenamiento=self.logica.entrenamientos              
        self.assertIsInstance(entrenamiento[f.random_int(0,9)]['repeticiones'],int)
                
        ### Prueba 4
    def test_listarPersonaEntrenamiento(self):
        self.logica.dar_entrenamientos(2)
        for self.dataEN in self.logica.entrenamientos:
            if self.dataEN['persona'] == self.logica.personas[2]['nombre']:                
                self.assertEqual(self.dataEN['persona'],self.logica.personas[2]['nombre'])
                
        ### Prueba 5
    def test_listarEjercicioEntrenamiento(self):
        self.logica.dar_entrenamientos(2)
        for self.dataEN in self.logica.entrenamientos:
            if self.dataEN['ejercicio'] == self.logica.ejercicios[6]['nombre']:                
                self.assertEqual(self.dataEN['ejercicio'],self.logica.ejercicios[6]['nombre'])
        
    def test_crearEntrenamiento(self):
        self.crearEntrenamiento = self.logic.crearEntrenamiento()
        self.assertEqual(self.crearEntrenamiento,True)
       
    def test_entrenamientoTieneNombre(self):
        self.nombreEntrenamiento = self.logic.entrenamientoTieneNombre()
        self.assertNotEqual(self.nombreEntrenamiento,'')
    
    def test_entrenamientoRepetido(self):
        self. entrenamientoRepetido= self.logic.entrenamientoRepetido()
        self.assertNotEqual(self.entrenamientoRepetido[-1],self.entrenamientoRepetido[-2])
        
    def test_fechaCreacionDeEntrenamiento(self):
        self.fechaEntrenamiento = self.logic.fechaEntrenamiento()
        self.assertEqual(self.fechaEntrenamiento,True)
        
    def test_cantidadDeRepetirciones(self):
        self.cantidadDeRepeciones = self.logic.cantidadDeRepeticiones()
        self.assertEqual(self.cantidadDeRepeciones,True)
        
    def test_tiempoDeEjericicio(self):
        self.tiempoDeEjercicio = self.logic.tiempoDeEjercicio()
        self.assertIsInstance(self.tiempoDeEjercicio,float)
        
    def test_verificarGuardadoEjercicio(self):
        self.guardadoEjercicio = self.logic.guardadoEjericicio()
        self.assertNotEqual(self.guardadoEjercicio,False)



    # ver entrenamiento personas HU0012


    # def test_darEntrenamiento(self):
    #    self.darEntrenamiento = self.logica.darEntrenamiento()
    #    self.assertIsNotNone(self.darEntrenamiento)
       
    # def test_tipoDeDatoEntrenamiento(self):
    #     self.tipoDeDatoEntrenamiento = self.logica.tipoDeDatoEntrenamiento()
    #     self.assertIsInstance(self.tipoDeDatoEntrenamiento,dict)
        
    # def test_verificarFecha(self):
    #     self.darFecha = self.logica.verificarFecha()
    #     self.assertTrue(self.darFecha)


    # Editar ejercicios entrenados HU0013
    
        ### Prueba 1
    def test_editarejercicioEntrenado(self):
        self.ejercicioantes = self.logica.entrenamientos
        self.assertEqual(self.ejercicioantes[0]['ejercicio'],self.logica.ejercicio[7]['nombre'])

        ### Prueba 2
    def test_editarejercicioEntrenado(self):
        self.logica.editar_entrenamiento(0, self.logica.personas[4], self.logica.ejercicios[2]['nombre'], self.logica.entrenamientos[0]['fecha'], self.logica.entrenamientos[0]['repeticiones'], self.logica.entrenamientos[0]['repeticiones'])
        self.ejerciciodespues = self.logica.entrenamientos
        print(self.ejerciciodespues[0]['ejercicio'])
        self.assertEqual(self.ejerciciodespues[0]['ejercicio'],self.logica.ejercicios[7]['nombre'])
    
        ### Prueba 3
    def test_editarejercicioEntrenadoNone(self):
        self.ejerciciodespues = self.logica.entrenamientos
        self.assertIsNotNone(self.ejerciciodespues[0]['ejercicio'])
        self.assertIsNotNone(self.logica.entrenamientos[0])
       
        ### Prueba 4
    def test_ejercicioEntrenadoEqualejercicio(self):
        self.logica.dar_entrenamientos(0)
        for self.dataEN in self.logica.entrenamientos:
            if self.dataEN['ejercicio'] == self.logica.ejercicios[2]['nombre']:                
                self.assertEqual(self.dataEN['ejercicio'],self.logica.ejercicios[2]['nombre'])
        
        ### Prueba 5
    def test_ejercicioEntrenadoEqualejercicio(self):
        self.logica.dar_entrenamientos(0)
        for self.dataEN in self.logica.entrenamientos:
            if self.dataEN['ejercicio'] == self.logica.ejercicios[3]['nombre']:                
                self.assertEqual(self.dataEN['ejercicio'],self.logica.ejercicios[3]['nombre'])

        
        ### Prueba 5
#     def test_verInformacionReporte(self):
#         self.verInformacionReporte = self.logica.verInformacionReporte()
#         self.assertIsInstance(self.verInformacionReporte,dict)

# borrar ejercicios entrenados HU0014
        ### Prueba 1
    def test_eliminarentrenamiento(self):
        self.eliminarentrenamiento = self.logica.eliminar_entrenamiento(0, self.logica.personas[4])
        self.assertIsNone(self.eliminarentrenamiento)

        ### Prueba 2
    def test_leneliminarentrenamiento(self):
        self.eliminarentrenamiento = self.logica.eliminar_entrenamiento(0, self.logica.personas[4])
        lenentrenamient=len(self.logica.entrenamientos)
        self.assertTrue(lenentrenamient<10)

        ### Prueba 3
    def test_leneliminarentrenamiento(self):
        self.eliminarentrenamiento = self.logica.eliminar_entrenamiento(0, self.logica.personas[4])

        self.assertNotEqual(self.logica.entrenamientos[1],'Denise')


    
    
if __name__ == "__main__":
    unittest.main()