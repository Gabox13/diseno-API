from src.database.db import get_connection
from .entities.plan import plan



class planesModel():
    "Futuro agragar parameto id equipo"
    @classmethod
    def get_PlanesXEquipo(self):
        try:
            connection = get_connection()
            planes = []
            with connection.cursor() as cursor:

                cursor.execute('call obtenerPlanesXEquipo(1)')
                resultset = cursor.fetchall()

                for row in resultset:
                    Plan = plan(row[0], row[1], row[2],
                                  row[3])
                    planes.append(Plan.to_JSON())
            connection.close()
            return planes
        except Exception as ex:
            raise Exception(ex)

