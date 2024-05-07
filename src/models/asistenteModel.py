from src.database.db import get_connection
from .entities.Asistente import Asistente

class asistenteModel():
    

    @classmethod
    def añadirAsistente(self, correo, contraseña, idSede):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""call addAsistente(%s, %s, %s);""", (correo, contraseña, idSede))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def deleteAsistente(self, correo):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""call deleteAsistente(%s);""", (correo))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_Asistente(self, correoAsis):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                print(correoAsis)
                cursor.execute("call obtenerAsistente(%s)", (correoAsis,))
                resultset = cursor.fetchone()
                print(resultset)
                if resultset == None:
                    
                    Asist = {'message': "El profe no esta registrado como guia o esta inactivo"}
                else:
                    Asist = Asistente(resultset[0], resultset[1], resultset[2])
                    Asist=Asist.to_JSON()
            connection.close()
            return Asist
        except Exception as ex:
            raise Exception(ex)


