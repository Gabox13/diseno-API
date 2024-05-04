from src.database.db import get_connection
from .entities.profe import profe
from .entities.profeGuia import profeGuia


class profesModel():

    @classmethod
    def get_Profes(self, idSede):
        try:
            connection = get_connection()
            profes = []

            with connection.cursor() as cursor:

                cursor.execute('call obtenerProfesorxSede(%s)', (idSede,))
                resultset = cursor.fetchall()

                for row in resultset:
                    Profe = profe(row[0], row[1], row[2],
                                  row[3], row[4], row[5], row[6])
                    profes.append(Profe.to_JSON())
            connection.close()
            return profes
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_ProfeGuia(self, correo):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:

                cursor.execute("call obtenerProfesor(%s)", (correo,))
                resultset = cursor.fetchone()

                if resultset == None:
                    connection.close()
                    return {'message': "El profe no esta registrado como guia o esta inactivo"}
                else:
                    ProfeG = profeGuia(resultset[0], resultset[1], resultset[2], resultset[3], resultset[4],
                                       resultset[6], resultset[5], resultset[7],resultset[8],resultset[9])
            connection.close()
            return ProfeG.to_JSON()
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_detalleEquipo(self, idEquipo):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:

                cursor.execute("call obtenerEquipos", (correo,))
                resultset = cursor.fetchone()

                if resultset == None:
                    connection.close()
                    return {'message': "El profe no esta registrado como guia o esta inactivo"}
                else:
                    ProfeG = profeGuia(resultset[0], resultset[1], resultset[2], resultset[3], resultset[4],
                                       resultset[5], resultset[6], resultset[7])
            connection.close()
            return ProfeG.to_JSON()
        except Exception as ex:
            raise Exception(ex)

