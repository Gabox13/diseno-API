from src.database.db import get_connection


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


