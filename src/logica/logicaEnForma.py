from src.logica.FachadaEnForma import FachadaEnForma

from faker import Faker
from src.logica.declarative_base import Session, engine, Base
from src.logica.persona import Persona
from src.logica.ejercicio import Ejercicio
from src.logica.entrenamiento import Entrenamiento


#Generacion de datos con Faker
f = Faker() 

Faker.seed(1000)

class LogicaEnForma(FachadaEnForma):


    def __init__(self):
        """Se inicializa el metodo contructor para personas"""
        self.personas=[]
        self.data_personas=[]
        """Se inicializa el metodo contructor para ejercicios"""
        self.ejercicios=[]
        self.data_ejercicios=[]
        """Se inicializa el metodo contructor para Entrenamientos"""
        self.entrenamientos=[]
        self.data_entrenamientos=[]
        """Se inicializa la base de datos"""
        Base.metadata.create_all(engine) 
        session = Session()
        """Se valida si la base de datos existe."""
        if engine.dialect.has_table(engine, Persona.__tablename__):
            registrosP = session.query(Persona).all()
            
            """Se valida si la base de datos tiene registros, de lo contrario se llena con los registros existentes"""
            if registrosP:
                print("")
                                
            else:              
                # self.personas = [{'nombre': 'Federico', 'apellido': 'Contreras', 'edad': 15, 'talla': 1.53, 'peso': 50, 'brazo': 15, 'pecho': 80, 'cintura': 70, 'pierna': 35, 'fecha_retiro': '', 'razon_retiro': ''},
                #                 {'nombre': 'Angelica', 'apellido': 'Mora', 'edad': 42, 'talla': 1.90, 'peso': 75, 'brazo': 18, 'pecho': 95, 'cintura': 76, 'pierna': 40, 'fecha_retiro': '2023-03-30', 'razon_retiro': 'Incapacidad'},
                #                 {'nombre': 'Julian', 'apellido': 'Salazar', 'edad': 30, 'talla': 1.69, 'peso': 59, 'brazo': 17, 'pecho': 69, 'cintura': 60, 'pierna': 28, 'fecha_retiro': '2023-01-18', 'razon_retiro': 'Cambio de instructor'},
                #                 {'nombre': 'Bruno', 'apellido': 'Galan', 'edad': 26, 'talla': 1.53, 'peso': 60, 'brazo': 16, 'pecho': 72, 'cintura': 54, 'pierna': 20, 'fecha_retiro': '', 'razon_retiro': ''},
                #                 ]
                self.data_personas=self.personas
                """Se hace un for para que cargue con el metodo Persona los datos de las personas existentes"""
                for datosp in self.data_personas:
                    crear_persona = Persona(nombre=datosp['nombre'],apellido=datosp['apellido'],edad=datosp['edad'],talla=datosp['talla'],peso=datosp['peso'],brazo=datosp['brazo'],pecho=datosp['pecho'],cintura=datosp['cintura'],pierna=datosp['pierna'],fecha_retiro=datosp['fecha_retiro'],razon_retiro=datosp['razon_retiro'])
                    session.add(crear_persona)
                session.commit()
        session.close()
        """Se inicializa la base de datos"""
        Base.metadata.create_all(engine)
        session = Session()
        """Se carga la informacion de la base de datos en data_persona"""
        if self.data_personas:
                print("")
        else:
            if self.personas:  
                print("")
            else:                            
                self.personas.clear()
                self.data_personas.clear()
                self.data_persona=session.query(Persona.id_persona,Persona.nombre,Persona.apellido,Persona.edad,Persona.peso,Persona.talla,Persona.brazo,Persona.pecho,Persona.cintura, Persona.pierna).all()
                """Se hace un for para agregar a self.personas los datos de la base de datos, recorriendo la informacion obtenida con la linea anterior"""
                for datosp in self.data_persona:
                    self.personas.append({'id_persona':datosp.id_persona,'nombre': datosp.nombre, 'apellido':datosp.apellido, 'edad': datosp.edad, 'talla': datosp.talla, 'peso': datosp.peso, 'brazo': datosp.brazo, 'pecho': datosp.pecho, 'cintura': datosp.cintura, 'pierna': datosp.pierna, 'fecha_retiro': '', 'razon_retiro': ''})
                
                session.close()                
                self.data_personas.clear()
            """se retorna la informacion recuperada."""
            """Antes solo se manejaba sobre variables los datos, con el metodo anterior se guardan en una DB."""
            # self.personas = [{'nombre': 'Federico', 'apellido': 'Contreras', 'edad': 15, 'talla': 1.53, 'peso': 50, 'brazo': 15, 'pecho': 80, 'cintura': 70, 'pierna': 35, 'fecha_retiro': '', 'razon_retiro': ''},
            #                  {'nombre': 'Angelica', 'apellido': 'Mora', 'edad': 42, 'talla': 1.90, 'peso': 75, 'brazo': 18, 'pecho': 95, 'cintura': 76, 'pierna': 40, 'fecha_retiro': '2023-03-30', 'razon_retiro': 'Incapacidad'},
            #                  {'nombre': 'Julian', 'apellido': 'Salazar', 'edad': 30, 'talla': 1.69, 'peso': 59, 'brazo': 17, 'pecho': 69, 'cintura': 60, 'pierna': 28, 'fecha_retiro': '2023-01-18', 'razon_retiro': 'Cambio de instructor'},
            #                  {'nombre': 'Bruno', 'apellido': 'Galan', 'edad': 26, 'talla': 1.53, 'peso': 60, 'brazo': 16, 'pecho': 72, 'cintura': 54, 'pierna': 20, 'fecha_retiro': '', 'razon_retiro': ''},
            #                 ]

        
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
                # self.ejercicios = [
                #                     {'nombre': 'Press de pierna', 'descripcion': 'Ejercicio de entrenamiento con pesas en el que el individuo empuja un peso o una resistencia con las piernas', 'youtube': 'https://www.youtube.com/watch?v=zac9BPZiUTQ', 'calorias': 120}, \
                #                     {'nombre': 'Sentadilla', 'descripcion': 'Ejercicio de fuerza en el que se baja la cadera desde una posición de pie y luego vuelve a levantarse.', 'youtube': 'https://www.youtube.com/watch?v=l7aszLSPCVg', 'calorias': 80}, \
                #                     {'nombre': 'Abducción de cadera', 'descripcion': 'Mover la pierna derecha hacia la derecha o alejarla del cuerpo y viceversa', 'youtube': 'https://www.youtube.com/watch?v=dILxTvY88uI', 'calorias': 90}
                #                   ]       
                data_ejercicios=self.ejercicios
                for datose in data_ejercicios:
                    crear_ejercicio = Ejercicio(nombre=datose['nombre'],descripcion=datose['descripcion'],youtube=datose['youtube'],calorias=datose['calorias'])
                    session.add(crear_ejercicio)

                session.commit()


        session.close()
        """Antes solo se manejaba sobre variables los datos, con el metodo anterior se guardan en una DB."""
        # self.ejercicios = [
        #     {'nombre': 'Press de pierna', 'descripcion': 'Ejercicio de entrenamiento con pesas en el que el individuo empuja un peso o una resistencia con las piernas', 'youtube': 'https://www.youtube.com/watch?v=zac9BPZiUTQ', 'calorias': 120}, \
        #     {'nombre': 'Sentadilla', 'descripcion': 'Ejercicio de fuerza en el que se baja la cadera desde una posición de pie y luego vuelve a levantarse.', 'youtube': 'https://www.youtube.com/watch?v=l7aszLSPCVg', 'calorias': 80}, \
        #     {'nombre': 'Abducción de cadera', 'descripcion': 'Mover la pierna derecha hacia la derecha o alejarla del cuerpo y viceversa', 'youtube': 'https://www.youtube.com/watch?v=dILxTvY88uI', 'calorias': 90}
        # ]
        """Se inicializa la base de datos"""
        Base.metadata.create_all(engine)
        session = Session()
        """Se carga la informacion de la base de datos en data_ejercicios"""
        
        if self.data_ejercicios:
                print("")
        else:
            if self.ejercicios:  
                print("")
            else:            
                
                self.ejercicios.clear()
                self.data_ejercicios.clear()
                self.data_ejercicios=session.query(Ejercicio.id,Ejercicio.nombre,Ejercicio.descripcion,Ejercicio.youtube,Ejercicio.calorias).all()
                """Se hace un for para agregar a self.ejercicios los datos de la base de datos, recorriendo la informacion obtenida con la linea anterior"""
                for datose in self.data_ejercicios:
                    self.ejercicios.append({'id':datose.id,'nombre': datose.nombre, 'descripcion':datose.descripcion, 'youtube': datose.youtube, 'calorias': datose.calorias})
            session.close()
            self.data_ejercicios.clear()
        """se retorna la informacion recuperada."""


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

                # self.entrenamientos = [{'persona': 'Federico', 'ejercicio': 'Press de pierna', 'fecha': '2023-01-18', 'repeticiones': 15, 'tiempo': 20},
                #                     {'persona': 'Federico', 'ejercicio': 'Sentadilla', 'fecha': '2023-01-18', 'repeticiones': 12, 'tiempo': 5},
                #                     {'persona': 'Federico', 'ejercicio': 'Press de pierna', 'fecha': '2023-03-11', 'repeticiones': 15, 'tiempo': 20},
                #                     {'persona': 'Bruno', 'ejercicio': 'Press de pierna', 'fecha': '2023-01-18', 'repeticiones': 15, 'tiempo': 30},
                #                     {'persona': 'Bruno', 'ejercicio': 'Sentadilla', 'fecha': '2023-07-02', 'repeticiones': 10, 'tiempo': 5}
                #                     ]
                data_entrenamientos=self.entrenamientos
                for datosEN in data_entrenamientos:
                    crear_entrenamiento = Entrenamiento( persona=datosEN['persona'],ejercicio=datosEN['ejercicio'],fecha=datosEN['fecha'],repeticiones=datosEN['repeticiones'],tiempo=datosEN['tiempo'])
                    session.add(crear_entrenamiento)

                session.commit()
                
        session.close()

        """Antes solo se manejaba sobre variables los datos, con el metodo anterior se guardan en una DB."""
        # self.entrenamientos = [{'persona': 'Federico', 'ejercicio': 'Press de pierna', 'fecha': '2023-01-18', 'repeticiones': 15, 'tiempo': 20},
        #                             {'persona': 'Federico', 'ejercicio': 'Sentadilla', 'fecha': '2023-01-18', 'repeticiones': 12, 'tiempo': 5},
        #                             {'persona': 'Federico', 'ejercicio': 'Press de pierna', 'fecha': '2023-03-11', 'repeticiones': 15, 'tiempo': 20},
        #                             {'persona': 'Bruno', 'ejercicio': 'Press de pierna', 'fecha': '2023-01-18', 'repeticiones': 15, 'tiempo': 30},
        #                             {'persona': 'Bruno', 'ejercicio': 'Sentadilla', 'fecha': '2023-07-02', 'repeticiones': 10, 'tiempo': 5}
        #                             ]
        
        """Se inicializa la base de datos"""
        Base.metadata.create_all(engine)
        session = Session()
        """Se carga la informacion de la base de datos en data_persona"""
        if self.data_entrenamientos:
                print("")
        else:
            if self.entrenamientos:  
                print("")
            else:            
                self.entrenamientos.clear()
                self.data_entrenamientos.clear()
                self.data_entrenamientos=session.query(Entrenamiento.id,Entrenamiento.persona,Entrenamiento.ejercicio,Entrenamiento.fecha,Entrenamiento.repeticiones,Entrenamiento.tiempo).all()
                """Se hace un for para agregar a self.personas los datos de la base de datos, recorriendo la informacion obtenida con la linea anterior"""
                for datosEN in self.data_entrenamientos:
                    self.entrenamientos.append({'id':datosEN.id,'persona': datosEN.persona, 'ejercicio':datosEN.ejercicio, 'fecha': datosEN.fecha, 'repeticiones': datosEN.repeticiones, 'tiempo': datosEN.tiempo})#, 'fecha_retiro': '', 'razon_retiro': ''})
                
                session.close()                
                self.data_entrenamientos.clear()
            """se retorna la informacion recuperada."""           



        self.reportes=[]
        for dataRP in self.personas:
            for dataREN in self.entrenamientos:
                if dataRP['nombre'] == dataREN['persona']:
                    self.entrenamientosfecha,self.totalrepeticiones,self.totalcalorias=self.entrenamientos_fecha(dataRP)
                    imc=self.calcular_imc(dataRP['peso'],dataRP['talla'])
                    self.reportes.append({'persona': dataREN['persona'],'imc':imc,'clasificacion':self.clasificar_imc(imc),'entrenamientos':self.entrenamientosfecha,'total_repeticiones':self.totalrepeticiones,'total_calorias':self.totalcalorias})
        



    def dar_personas(self):
        return self.personas.copy()

    def dar_persona(self, id_persona):
        return self.personas[id_persona].copy()  
        
    def validar_crear_editar_persona(self, id_persona, nombre, apellido, edad, talla, peso, brazo, pecho, cintura, pierna):
        return ""
    
    def eliminar_persona(self, id_persona):
        del self.personas[id_persona]

    def crear_persona(self, nombre, apellido, edad, talla, peso, brazo, pecho, cintura, pierna):
        self.personas.append({'nombre': nombre, 'apellido': apellido, 'edad': edad, 'talla': talla, \
                           'peso': peso, 'brazo': brazo, 'pecho': pecho, 'cintura': cintura, 'pierna': pierna, \
                           'fecha_retiro': '', 'razon_retiro': '' })
    
    
    def editar_persona(self, id_persona, nombre, apellido, edad, talla, peso, brazo, pecho, cintura, pierna):
        self.personas[id_persona]['nombre'] = nombre
        self.personas[id_persona]['apellido'] = apellido
        self.personas[id_persona]['edad'] = edad
        self.personas[id_persona]['talla'] = talla
        self.personas[id_persona]['peso'] = peso
        self.personas[id_persona]['brazo'] = brazo
        self.personas[id_persona]['pecho'] = pecho
        self.personas[id_persona]['cintura'] = cintura
        self.personas[id_persona]['pierna'] = pierna


    def dar_ejercicios(self):
        
        return self.ejercicios.copy()
    
    def dar_ejercicio(self, id_ejercicio):
        return self.ejercicios[id_ejercicio].copy()
    
    def validar_crear_editar_ejercicio(self, nombre, descripcion, enlace, calorias):
        return ""

    def crear_ejercicio(self, nombre, descripcion, enlace, calorias):
        self.ejercicios.append({'nombre': nombre, 'descripcion': descripcion, 'youtube': enlace, 'calorias': calorias})


    def editar_ejercicio(self,id_ejercicio, nombre, descripcion, enlace, calorias):
        self.ejercicios[id_ejercicio]['nombre']= nombre
        self.ejercicios[id_ejercicio]['descripcion'] = descripcion
        self.ejercicios[id_ejercicio]['enlace'] = enlace
        self.ejercicios[id_ejercicio]['calorias'] = calorias

    def eliminar_ejercicio(self, id_ejercicio):
        del self.ejercicios[id_ejercicio]


    def dar_entrenamientos(self, id_persona):
        persona = self.dar_persona(id_persona)
        return list(filter(lambda x: x['persona'] == persona['nombre'], self.entrenamientos))
        # return self.entrenamientos.copy()

    def dejar_de_entrenar_persona(self, id_persona, fecha, razon):
        self.personas[id_persona]['fecha_retiro'] = fecha
        self.personas[id_persona]['razon_retiro'] = razon


    def validar_crear_editar_entrenamiento(self, persona, ejercicio, fecha, repeticiones, tiempo):
        return ""

    def crear_entrenamiento(self, persona, ejercicio, fecha, repeticiones, tiempo):
        self.entrenamientos.append({'persona': persona['nombre'], 'ejercicio': ejercicio, 'fecha': fecha, 'repeticiones': repeticiones, 'tiempo': tiempo})


    def editar_entrenamiento(self, id_entrenamiento, persona, ejercicio, fecha, repeticiones, tiempo):
        entrenamientos_persona = list(filter(lambda x: x['persona'] == persona['nombre'], self.entrenamientos))
        entrenamientos_persona[id_entrenamiento]['ejercicio'] = ejercicio
        entrenamientos_persona[id_entrenamiento]['fecha'] = fecha
        entrenamientos_persona[id_entrenamiento]['repeticiones'] = repeticiones
        entrenamientos_persona[id_entrenamiento]['tiempo'] = tiempo

        Base.metadata.create_all(engine)
        session = Session()
        """Se carga la informacion de la base de datos en data_persona"""
        
        if self.entrenamientos:  
            print("")
        else:            
            
            self.logica.entrenamientos.clear()
            self.logica.data_entrenamientos.clear()
            self.editar_entrenamiento=self.entrenamientos({'id':id_entrenamiento,'persona': persona['nombre'], 'ejercicio':entrenamientos_persona.ejercicio, 'fecha': entrenamientos_persona.fecha, 'repeticiones': entrenamientos_persona.repeticiones, 'tiempo': entrenamientos_persona.tiempo})
            session.add(self.editar_entrenamiento)

            session.commit()
            session.close()                
            self.logica.data_entrenamientos.clear()
        """se retorna la informacion recuperada."""   

    def eliminar_entrenamiento(self, id_entrenamiento, persona):
        entrenamientos_persona = list(filter(lambda x: x['persona'] == persona['nombre'], self.entrenamientos))
        entrenamientos_diferentes = list(filter(lambda x: x['persona'] != persona['nombre'], self.entrenamientos))
        entrenamientos_persona.pop(id_entrenamiento)
        self.entrenamientos = entrenamientos_diferentes + entrenamientos_persona

    def dar_reporte(self, id_persona):
        persona = self.dar_persona(0)
        estadisticas = list(filter(lambda x: x['persona'] == persona['nombre'], self.reportes))[0]
        self.reportes.copy()
        return {'persona': persona, 'estadisticas': estadisticas}
    
    def validar_dejar_de_entrenar_persona(self, id_persona, fecha, razon):
        return ""


    def entrenamientos_fecha(self, persona):
        self.entrenamientosfecha=[]
        self.totalrepeticiones=0
        self.totalcalorias=0
        # list(filter(lambda x: x['persona'] == persona['nombre'], self.entrenamientos))
        for datosF in self.entrenamientos:
            if persona['nombre'] == datosF['persona']:
                self.entrenamientosfecha.append({'fecha':datosF['fecha'],'repeticiones':datosF['repeticiones'],'calorias':f.random_int(50,1000)})
        
        self.totalrepeticiones=[]
        self.totalcalorias=[]
        for datosT in self.entrenamientosfecha:
            self.totalrepeticiones=+datosT['repeticiones']
            self.totalcalorias=+datosT['calorias']    
        return self.entrenamientosfecha.copy(),self.totalrepeticiones,self.totalcalorias
        # return list(filter(lambda x: x['persona'] == persona['nombre'], self.entrenamientos))

        # return self.entrenamientos.copy()

    def calcular_imc(self, peso, talla):
        return peso/(talla**2)
        
    def clasificar_imc(self, imc):
        if imc < 18.5:
            return 'Bajo peso'
        elif imc < 25:
            return 'Peso saludable'
        elif imc < 30:
            return 'Sobrepeso'
        else:
            return 'Obesidad'
