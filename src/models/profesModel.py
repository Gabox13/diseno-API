from src.database.db import get_connection
from .entities.profe import profe
from .entities.profeGuia import profeGuia
from .entities.profeIntegrante import profeIntegrante


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
    def get_detalleEquipo(self):
        try:
            connection = get_connection()
            grupos=[]
            with connection.cursor() as cursor:

                cursor.execute("call obtenerEquipos()")
                resultset = cursor.fetchall()

                if resultset == None:
                    connection.close()
                    return {'message': "El profe no esta registrado como guia o esta inactivo"}
                else:
                    listaProfe=[]
                    idE=1
                    total_rows = len(resultset)

                    # Itera sobre el resultset
                    for idx, row in enumerate(resultset):
                        Profe = profeIntegrante(row[0], row[1], row[2], row[3], row[4],
                                                row[6], row[5], row[7], row[8], row[9], row[10])
                        print(row[10])

                        # Verifica si es la última fila
                        if idx == total_rows - 1:
                            # Última fila
                            listaProfe.append(Profe.to_JSON())
                            grupos.append(listaProfe)
                            listaProfe = []
                        elif row[10] != 1:
                            # No es la última fila y la columna 10 no es 1
                            grupos.append(listaProfe)
                            listaProfe = []
                        else:
                            listaProfe.append(Profe.to_JSON())
            connection.close()
            return grupos
        except Exception as ex:
            raise Exception(ex)

