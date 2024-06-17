from src.database.db import get_connection

class NotificationCenter:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)
    def notify(self, message):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                for subscriber in self.subscribers:
                    cursor.execute('INSERT INTO messageXEstudianteUsuario VALUES(%s,%s,%s,%s)',(subscriber,message,0,1))
                    connection.commit()
            
            connection.close()
        except Exception as ex:
            raise Exception(ex)   
        

            