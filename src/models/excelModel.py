from src.database.db import get_connection
from .entities.estudiante import estudiante
from .entities.AdditionalAttributes import AdditionalAttributes
from .entities.message import Message
class excelModel():
    "Futuro agragar parameto id equipo"
    @classmethod
    def add_Excel(self,excel):
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                
                documento=excel["nombre"]
                print(documento)
                cursor.execute('call obtenerExcel(%s)',(documento,))
                existe1=cursor.fetchone()
                print(existe1)
                if not existe1:
                    
                    print(type(documento))
                    cursor.execute('call addExcel(%s,%s)',(documento,"rutaBase",))
                
                for row in excel["excel"]:
                    print(type(row["Carnet"]))
                    cursor.execute('call obtenerEstudiante(%s)', (str(row["Carnet"]),))
                    
                    
                    existe = cursor.fetchone()
                    print(existe)
                    if not existe:
                        print("agregar estudiante")
                        
                        if row["Sede"] == "SJ":
                            idSede = 1
                        elif row["Sede"] == "LI":
                            idSede = 2
                        elif row["Sede"] == "SC":
                            idSede = 3
                        elif row["Sede"] == "AL":
                            idSede = 4
                        elif row["Sede"] == "CA":
                            idSede = 5
                        print(idSede)
                        print(str(row["Carnet"]) ,row["Nombre"],row["Segundo Nombre"],row["Apellido"],row["Segundo Apellido"],row["Correo"],str(row["Cel"]),idSede)
                        cursor.execute("""call addEstudiante(%s,%s,%s,%s,%s
                                        ,%s,%s,%s)""",(str(row["Carnet"]) ,
                                                        row["Nombre"],row["Segundo Nombre"],row["Apellido"],
                                                        row["Segundo Apellido"],row["Correo"],str(row["Cel"]),idSede))
                        cursor.execute("call addExcelxEstudiantes(%s,%s)",(str(row["Carnet"]),documento,))
                        
                    else:
                        
                        cursor.execute("call estudianteInExcel(%s,%s)",(str(row["Carnet"]),documento,))
                        existe2=cursor.fetchone()

                        if not existe2:
                           cursor.execute("call addExcelxEstudiantes(%s,%s)",(str(row["Carnet"]),documento,))
                    affected_rows=cursor.rowcount



            connection.commit()     
            connection.close()
            return {"message":affected_rows}
        except Exception as ex:
            raise Exception(ex)
        
     
    @classmethod
    def recuperar_Excel(self):
        try:
            connection = get_connection()
            estudiantes = []

            with connection.cursor() as cursor:

                cursor.execute('SELECT * FROM excelList ORDER BY id DESC LIMIT 1')
                nombreExcel=cursor.fetchone()
                print(nombreExcel)
                cursor.execute('call obtenerExcelxEstudiantes(%s)', (nombreExcel[0],))
                resultset = cursor.fetchall()
                print(resultset)
                for row in resultset:
                    estu = estudiante(row[0], row[1], row[3],
                                  row[4], row[5], row[6], row[8],row[2])
                    estudiantes.append(estu.to_JSON())

            connection.close()
            return {'nombre':nombreExcel[0],'excel':estudiantes}
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def recuperar_GrupoSede(self,idSede):
        try:
            connection = get_connection()
            estudiantes = []

            with connection.cursor() as cursor:

                cursor.execute('call obtenerEstudiantesxSede(%s)', (idSede,))
                resultset = cursor.fetchall()
                
                for row in resultset:
                    estu = estudiante(row[0], row[1], row[3],
                                  row[4], row[5], row[6], row[7],row[2])
                    estudiantes.append(estu.to_JSON())

            connection.close()
            return estudiantes
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def recuperar_todos(self,):
        try:
            connection = get_connection()
            estudiantes = []

            with connection.cursor() as cursor:

                cursor.execute('call obtenerEstudiantes()')
                resultset = cursor.fetchall()
                
                for row in resultset:
                    estu = estudiante(row[0], row[1], row[3],
                                  row[4], row[5], row[6], row[7],row[2])
                    estudiantes.append(estu.to_JSON())

            connection.close()
            return estudiantes
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def inicio_sesion_es(self,correo):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:

                cursor.execute('call obtenerEstudianteUsuario(%s)',(correo,))
                resultset = cursor.fetchone()
                print(correo)
                if resultset == None :
                    decorated_estudiante={"message":"Estudiante no encontrado en el sistema"}
                elif resultset[8] == None:
                    estudiante_instance = estudiante(resultset[0],resultset[1],resultset[3],resultset[4],resultset[5],resultset[6],resultset[7],resultset[2])
                    decorated_estudiante = AdditionalAttributes(estudiante_instance, resultset[5], resultset[0], 'nuevo perfil Estudiante','1')
                    decorated_estudiante = decorated_estudiante.to_JSON()
                    cursor.execute('call addEstudianteUsuario(%s,%s,%s)',(resultset[5],resultset[0],'perfil registrado Estudiante'))
                    connection.commit()
                else:
                    estudiante_instance = estudiante(resultset[0],resultset[1],resultset[3],resultset[4],resultset[5],resultset[6],resultset[7],resultset[2])
                    decorated_estudiante = AdditionalAttributes(estudiante_instance, resultset[8], resultset[9],resultset[10] ,resultset[11])
                    decorated_estudiante = decorated_estudiante.to_JSON()
            connection.close()
            return decorated_estudiante
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def recuperar_notificaciones(self,username):
        try:
            connection = get_connection()
            notis = []
            with connection.cursor() as cursor:

                cursor.execute("""select * from message
inner join messageXEstudianteUsuario ON message.id = messageXEstudianteUsuario.idMe
WHERE messageXEstudianteUsuario.valActive =1 AND messageXEstudianteUsuario.userEU=%s
ORDER BY message.fechaGeneracion desc;""",(username,))
                resultset = cursor.fetchall()
                for row in resultset:
                    mes = Message(row[7],row[1],row[2],row[9],row[5],row[4])
                    notis.append(mes.to_JSON())
            connection.close()
            return notis
        except Exception as ex:
            raise Exception(ex)