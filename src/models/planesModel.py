from src.database.db import get_connection
from .entities.plan import plan
from .entities.ActividadFactory import ActividadFactory
from .entities.comentario import comentario
from .entities.respuesta import respuesta
from .entities.Recordatorio import Recordatorio


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

    @classmethod
    def get_ActividadesXPlan(self, id):
        try:
            connection = get_connection()
            actividades = []
            with connection.cursor() as cursor:

                cursor.execute('call obtenerActividadesxPlan(%s)', (id,))
                resultset = cursor.fetchall()
                
                for row in resultset:
                    
                    cursor.execute('call obtenerComentarios(%s)', (row[0],))
                    resultset1 = cursor.fetchall()
                    
                    
                    comentarios = []
                    for row1 in resultset1:
                        
                        cursor.execute('call obtenerRespuestas(%s)', (row1[0],))
                        resultset2 = cursor.fetchall()
                        respuestas = []
                        for row2 in resultset2:
                            
                            Respuesta = respuesta(
                                row2[0], row2[1], row2[2], str(row2[3]), row2[4], row2[5])
                            respuestas.append(Respuesta.to_JSON())

                        com = comentario(
                            row1[0], row1[1], row1[2], str(row1[3]), row1[4], row1[5], respuestas)
                        comentarios.append(com.to_JSON())

                    cursor.execute(
                        'call obtenerFechasRecordatorioActividad(%s)', (row[0],))
                    resultset3 = cursor.fetchall()
                    recordatorios = []
                    for row3 in resultset3:
                        recordatorio = Recordatorio(row3[0], row3[1], str(row3[2]))
                        recordatorios.append(recordatorio.to_JSON())

                    cursor.execute(
                        'call obtenerImagenesActividad(%s)', (row[0],))
                    resultset4 = cursor.fetchall()
                    imagenes = []
                    for row4 in resultset4:
                        imagenes.append({'foto': row4[2]})
                    imagenes.append({'fotoParticipantes':row[12]})
                    cursor.execute(
                        'call obtenerResponsablesxActividad(%s)', (row[0],))
                    resultset5 = cursor.fetchall()
                    responsables = []
                    
                    for row5 in resultset5:
                        
                        responsables.append({
                            'correo': row5[1],
                            'nombre': row5[2]
                        })
                    
                    
                    actividad = ActividadFactory.crear_actividad(row[0], row[1], row[2], row[3], row[4], row[5], str(row[6]), str(row[7]),
                                                 row[8], row[9], recordatorios, comentarios, responsables, imagenes, row[10], str(row[11]))
                    actividades.append(actividad)
            
            connection.close()
            return actividades
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_ActividadProxima(self):
        try:
            connection = get_connection()
            actividades = []
            with connection.cursor() as cursor:

                cursor.execute('call obtenerProximaActividad()')
                resultset = cursor.fetchall()
                
                for row in resultset:
                    
                    cursor.execute('call obtenerComentarios(%s)', (row[0],))
                    resultset1 = cursor.fetchall()
                    
                    
                    comentarios = []
                    for row1 in resultset1:
                        
                        cursor.execute('call obtenerRespuestas(%s)', (row1[0],))
                        resultset2 = cursor.fetchall()
                        respuestas = []
                        for row2 in resultset2:
                            
                            Respuesta = respuesta(
                                row2[0], row2[1], row2[2], str(row2[3]), row2[4], row2[5])
                            respuestas.append(Respuesta.to_JSON())

                        com = comentario(
                            row1[0], row1[1], row1[2], str(row1[3]), row1[4], row1[5], respuestas)
                        comentarios.append(com.to_JSON())

                    cursor.execute(
                        'call obtenerFechasRecordatorioActividad(%s)', (row[0],))
                    resultset3 = cursor.fetchall()
                    recordatorios = []
                    for row3 in resultset3:
                        recordatorio = Recordatorio(row3[0], row3[1], str(row3[2]))
                        recordatorios.append(recordatorio.to_JSON())

                    cursor.execute(
                        'call obtenerImagenesActividad(%s)', (row[0],))
                    resultset4 = cursor.fetchall()
                    imagenes = []
                    for row4 in resultset4:
                        imagenes.append({'foto': row4[2]})
                    imagenes.append({'fotoParticipantes':row[12]})
                    cursor.execute(
                        'call obtenerResponsablesxActividad(%s)', (row[0],))
                    resultset5 = cursor.fetchall()
                    responsables = []
                    
                    for row5 in resultset5:
                        
                        responsables.append({
                            'correo': row5[1],
                            'nombre': row5[2]
                        })
                    
                    
                    actividad = ActividadFactory.crear_actividad(row[0], row[1], row[2], row[3], row[4], row[5], str(row[6]), str(row[7]),
                                                 row[8], row[9], recordatorios, comentarios, responsables, imagenes, row[10], str(row[11]))
                    actividades.append(actividad)
            
            connection.close()
            return actividades
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def añadirActividad(self,act,idPlan):
        try:
            
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""call addActividad(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", (act['valoresGenerales']['nombre'], act['valoresGenerales']['semana'], act['valoresGenerales']['direccion'], act['valoresGenerales']['tipo'], act['valoresGenerales']['modalidad'], 
                                                                act['valoresGenerales']['fechaPublicacion'], act['valoresGenerales']['fechaRealizacion'], act['valoresGenerales']['afiche'], act['valoresGenerales']['estado'], idPlan))
                affected_rows = cursor.rowcount
                connection.commit()
                cursor.execute("""select last_insert_id();""")
                result = cursor.fetchall()
            connection.close()
            return affected_rows, result[0][0]
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def modificarActividad(self, act):
        try:
            connection = get_connection()
            affected_rows = 0
            with connection.cursor() as cursor:
                if act['valoresGenerales']['estado'] in ["Notificada", "Planeada", "Realizada"]:
                    cursor.execute("""call updateActividad(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", (act['valoresGenerales']['idActividad'], act['valoresGenerales']['nombre'], act['valoresGenerales']['semana'], act['valoresGenerales']['direccion'], act['valoresGenerales']['tipo'], act['valoresGenerales']['modalidad'], 
                                                                act['valoresGenerales']['fechaPublicacion'], act['valoresGenerales']['fechaRealizacion'], act['valoresGenerales']['afiche'], act['valoresGenerales']['estado'], 
                                                                None, None, None))
                    affected_rows = cursor.rowcount 
                    connection.commit()
                if act['valoresGenerales']['estado'] == "Cancelada":
                    cursor.execute("""call updateActividad(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", (act['valoresGenerales']['idActividad'], act['valoresGenerales']['nombre'], act['valoresGenerales']['semana'], act['valoresGenerales']['direccion'], act['valoresGenerales']['tipo'], act['valoresGenerales']['modalidad'], 
                                                                act['valoresGenerales']['fechaPublicacion'], act['valoresGenerales']['fechaRealizacion'], act['valoresGenerales']['afiche'], act['valoresGenerales']['estado'], 
                                                                act['descripcionCancelacion'], act['fechaCancelacion'], None))
                    affected_rows = cursor.rowcount 
                    connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def añadirFechaRecordatorio(self, idActividad, fechaRecordatorio):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""call addRecordatorio(%s, %s);""", (idActividad, fechaRecordatorio))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def borrarFechaRecordatorio(self, idFechaRecordatorio):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""call deleteRecordatorio(%s);""", (idFechaRecordatorio))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def añadirResponsable(self, correo, idActividad):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""call addResponsable(%s, %s);""", (correo, idActividad))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def quitarResponsable(self, correo, idActividad):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""call deleteResponsable(%s, %s);""", (correo, idActividad))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def comentar(self, correo,idActividad, comment):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""call addComentario(%s, %s, %s);""", (correo, idActividad, comment))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def responder(self, correo,idComentario,replay):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""call addRespuesta(%s, %s, %s);""", (idComentario, correo, replay))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def borrarRespuesta(self, correo, idComentario):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""call deleteRespuesta(%s, %s);""", (correo, idComentario))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def borrarComentario(self, idComentario, correo, idActividad):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""call deleteRespuestasxComentario(%s); call deleteComentario(%s, %s);""", (idComentario, correo, idActividad))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def añadirFotos(self, idActividad, foto):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""call addImagen(%s, %s);""", (idActividad, foto))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def quitarFotos(self, idActividad):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""call deleteImagen(%s);""", (idActividad))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    