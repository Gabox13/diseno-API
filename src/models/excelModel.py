from src.database.db import get_connection
from .entities.estudiante import estudiante

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
    def recuperar_Excel(self,nombreExcel):
        try:
            connection = get_connection()
            estudiantes = []

            with connection.cursor() as cursor:

                cursor.execute('call obtenerExcelxEstudiantes(%s)', (nombreExcel,))
                resultset = cursor.fetchall()
                print(resultset)
                for row in resultset:
                    estu = estudiante(row[0], row[1], row[3],
                                  row[4], row[5], row[6], row[8],row[2])
                    estudiantes.append(estu.to_JSON())

            connection.close()
            return estudiantes
        except Exception as ex:
            raise Exception(ex)
