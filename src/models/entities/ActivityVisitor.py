from .Visitor import Visitor
from datetime import datetime, timedelta
from src.database.db import get_connection
class ActivityVisitor(Visitor):
    def __init__(self, system_date):
        self.system_date = system_date
        self.observer = None
    
    def visit(self, activity):
        if activity.estado == 'Planeada' and activity.fechaPublicacion == self.system_date:
            try:
                 
                connection = get_connection()
                with connection.cursor() as cursor:
                    cursor.execute('call cambiarEstadoActividad(%s,%s)',(activity.idActividad,"Notificada"))
                    connection.commit()
                    print(type(activity.nombre))
                    mensajeFormat = f"""Notificacion: La  actividad '{activity.nombre}' sera realizada el dia {activity.fechaRealizacion.strftime('%d/%m/%Y')}, 
                    le agradecemos su participacion a esta en la siguiente direccion {activity.direccion}, esta es de indole {activity.tipo} y sera {activity.modalidad}. No se la pierda"""
                    cursor.execute('call addMensage(%s,%s,%s,%s)',("Sistema",mensajeFormat,activity.nombre,self.system_date.strftime('%Y-%m-%d')))
                    connection.commit()
                    cursor.execute('SELECT LAST_INSERT_ID()')
                    ultimoID = cursor.fetchone()[0]
                    print(ultimoID)
                    self.observer.notify(ultimoID)  
                connection.close()
            except Exception as ex:
                raise Exception(ex)
        elif activity.estado == 'Notificada':
            reminder_dates = activity.fechaRecordatorio
            
            try:
                connection = get_connection()
                for recordatorio in reminder_dates:
                    print(recordatorio.fechaR,self.system_date)
                    if self.system_date == recordatorio.fechaR:
                            with connection.cursor() as cursor:
                                cursor.execute('SELECT * FROM notificacionXrecordatorios where idRec= %s',(recordatorio.idFecRec))
                                validar = cursor.fetchone()
                                if validar ==None:
                                    mensajeFormat = f"""Recordatorio: Se le recuerda que la actividad '{activity.nombre}' sera realizada el dia {activity.fechaRealizacion.strftime('%d/%m/%Y')}, 
                                    le agradecemos su participacion de ante mano, esta sera en la siguiente direccion {activity.direccion} para mas informacion comunicarse con la escuela"""
                                    cursor.execute('call addMensage(%s,%s,%s,%s)',("Sistema",mensajeFormat,f"Recordatorio de actividad: {activity.nombre}",self.system_date.strftime('%Y-%m-%d')))
                                    connection.commit()
                                    cursor.execute('SELECT LAST_INSERT_ID()')
                                    ultimoID = cursor.fetchone()[0]
                                    print(ultimoID)
                                    cursor.execute('call addnotificacionXrecordatorios(%s,%s)',(recordatorio.idFecRec,ultimoID))
                                    connection.commit()
                                    self.observer.notify(ultimoID)  
                connection.close()
            except Exception as ex:
                raise Exception(ex)
        elif activity.estado == 'Cancelada':
            try:
                    connection = get_connection()
                    with connection.cursor() as cursor:
                        cursor.execute('call cambiarEstadoActividad(%s,%s)',(activity.idActividad,"Cancelada(Notificada)"))
                        connection.commit()
                        mensajeFormat = f"""Notificacion de cancelacion: Se le avisa que la actividad '{activity.nombre}' ha sido cancelada, 
                        le pedimos disculpas del caso, para mas informacion comunicarse con la escuela"""
                        cursor.execute('call addMensage(%s,%s,%s,%s)',("Sistema",mensajeFormat,f"Cancelacion de actividad: {activity.nombre}",self.system_date.strftime('%Y-%m-%d')))
                        connection.commit()
                        cursor.execute('SELECT LAST_INSERT_ID()')
                        ultimoID = cursor.fetchone()[0]
                        print(ultimoID)
                        self.observer.notify(ultimoID)
                    connection.close()
            except Exception as ex:
                    raise Exception(ex)
    def attach(self, observer):
        self.observer = observer

    def detach(self):
        self.observer = None
