import mysql.connector
from datetime import datetime

class Comunication():
    def __init__(self):
        self.conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="edwin2003.ec",
        database="hotel_ricon_del_valle"
    )
        self.crear_tablaClientes()

    def crear_tablaClientes(self):
        cursor = self.conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Clientes (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                Nombre VARCHAR(10),
                Apellido VARCHAR(255),
                Cedula VARCHAR(100),
                Fecha_de_nacimiento DATE
            )
        ''')

    def crear_tablaReservas(self):
            cursor = self.conexion.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Reservas (
                    ID INT AUTO_INCREMENT PRIMARY KEY,
                    Nombre VARCHAR(10),
                    Apellido VARCHAR(255),
                    Cedula VARCHAR(100),
                    Fecha_de_nacimiento DATE
                )
            ''')

    def crear_tablaHabitaciones(self):
            cursor = self.conexion.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Habitaciones (
                    ID INT AUTO_INCREMENT PRIMARY KEY,
                    Nombre VARCHAR(10),
                    Apellido VARCHAR(255),
                    Cedula VARCHAR(100),
                    Fecha_de_nacimiento DATE
                )
            ''')
    def crear_tablaServicios(self):
                cursor = self.conexion.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Servicios (
                        ID INT AUTO_INCREMENT PRIMARY KEY,
                        Nombre VARCHAR(10),
                        Apellido VARCHAR(255),
                        Cedula VARCHAR(100),
                        Fecha_de_nacimiento DATE
                    )
                ''')

    def crear_tablaFacturacion(self):
                cursor = self.conexion.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Facturacion (
                        ID INT AUTO_INCREMENT PRIMARY KEY,
                        Nombre VARCHAR(10),
                        Apellido VARCHAR(255),
                        Cedula VARCHAR(100),
                        Fecha_de_nacimiento DATE
                    )
                ''')
    def inserta_productoClientes(self, ID, nombre, apellido, cedula, fecha_nacimiento):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO Clientes (ID, Nombre, Apellido, Cedula, Fecha_de_nacimiento)
        VALUES(%s, %s, %s, %s, %s)'''
        valores=(ID, nombre, apellido, cedula, fecha_nacimiento)
        cursor.execute(bd, valores)
        self.conexion.commit()
        cursor.close()


    def inserta_productoReservas(self, numero_de_reserva, servicio, cliente_id):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO Reservas (numero_de_reserva, servicio, cliente_id)
        VALUES(%s, %s, %s)'''
        cursor.execute(bd, (numero_de_reserva, servicio, cliente_id))
        self.conexion.commit()
        cursor.close()

    def inserta_productoHabitaciones(self, numero_de_habitacion, tipo_de_habitacion, estado_de_habitacion):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO Habitaciones (numero_de_habitacion, tipo_de_habitacion, estado_de_habitacion)
        VALUES(%s, %s, %s, %s)'''
        cursor.execute(bd, (numero_de_habitacion, tipo_de_habitacion, estado_de_habitacion))
        self.conexion.commit()
        cursor.close()

    def inserta_productoServicios(self, ID_servicio, nombre_de_servicio, coste_de_servicio):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO Servicios (ID_servicio, nombre_de_servicio, coste_de_servicio)
        VALUES(%s, %s, %s, %s)'''
        cursor.execute(bd, (ID_servicio, nombre_de_servicio, coste_de_servicio))
        self.conexion.commit()
        cursor.close()

    def inserta_productoFacturacion(self, ID_factura, Numero_de_reserva, fecha_facturacion, metodo_de_pago):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO Facturacion (ID_factura, Numero_de_reserva, fecha_facturacion, metodo_de_pago)
        VALUES(%s, %s, %s, %s)'''
        cursor.execute(bd, (ID_factura, Numero_de_reserva, fecha_facturacion, metodo_de_pago))
        self.conexion.commit()
        cursor.close()


    def mostrar_productosClientes(self):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM Clientes "
        cursor.execute(bd)
        registro = cursor.fetchall()
        cursor.close()
        # Asegúrate de devolver los datos
        return registro
    
    def mostrar_productosReservas(self):
            cursor = self.conexion.cursor()
            bd = "SELECT * FROM Reservas "
            cursor.execute(bd)
            registro = cursor.fetchall()
            return registro
    
    def mostrar_productosHabitaciones(self):
            cursor = self.conexion.cursor()
            bd = "SELECT * FROM Habitaciones "
            cursor.execute(bd)
            registro = cursor.fetchall()
            return registro
    
    def mostrar_productosServicios(self):
            cursor = self.conexion.cursor()
            bd = "SELECT * FROM Servicios "
            cursor.execute(bd)
            registro = cursor.fetchall()
            return registro
    
    def mostrar_productosFacturacion(self):
            cursor = self.conexion.cursor()
            bd = "SELECT * FROM Facturacion "
            cursor.execute(bd)
            registro = cursor.fetchall()
            return registro


    def busca_productoClientes(self, nombre_producto):
        cursor = self.conexion.cursor()
        bd = '''SELECT * FROM Clientes WHERE NOMBRE = {}'''.format(nombre_producto)
        cursor.execute(bd)
        nombreX = cursor.fetchall()
        cursor.close()
        return nombreX
    
    def busca_productoReservas(self, nombre_producto):
        cursor = self.conexion.cursor()
        bd = '''SELECT * FROM Reservas WHERE NOMBRE = {}'''.format(nombre_producto)
        cursor.execute(bd)
        nombreX = cursor.fetchall()
        cursor.close()
        return nombreX
    
    def busca_productoHabitaciones(self, nombre_producto):
        cursor = self.conexion.cursor()
        bd = '''SELECT * FROM Habitaciones WHERE NOMBRE = {}'''.format(nombre_producto)
        cursor.execute(bd)
        nombreX = cursor.fetchall()
        cursor.close()
        return nombreX
    
    def busca_productoServicios(self, nombre_producto):
        cursor = self.conexion.cursor()
        bd = '''SELECT * FROM Servicios WHERE NOMBRE = {}'''.format(nombre_producto)
        cursor.execute(bd)
        nombreX = cursor.fetchall()
        cursor.close()
        return nombreX
    
    def busca_productoFacturacion(self, nombre_producto):
        cursor = self.conexion.cursor()
        bd = '''SELECT * FROM Facturacion WHERE NOMBRE = {}'''.format(nombre_producto)
        cursor.execute(bd)
        nombreX = cursor.fetchall()
        cursor.close()
        return nombreX
    

    def elimina_productosClientes(self, nombre):
        cursor = self.conexion.cursor()
        bd = '''DELETE FROM Clientes WHERE NOMBRE = '{}' '''.format(self.producto_a_borrar)
        cursor.execute(bd)
        self.conexion.commint()
        cursor.close

    def elimina_productosReservas(self, nombre):
        cursor = self.conexion.cursor()
        bd = '''DELETE FROM Reservas WHERE NOMBRE = '{}' '''.format(self.producto_a_borrar)
        cursor.execute(bd)
        self.conexion.commint()
        cursor.close

    def elimina_productosHabitaciones(self, nombre):
        cursor = self.conexion.cursor()
        bd = '''DELETE FROM Habitaciones WHERE NOMBRE = '{}' '''.format(self.producto_a_borrar)
        cursor.execute(bd)
        self.conexion.commint()
        cursor.close

    def elimina_productosServicios(self, nombre):
        cursor = self.conexion.cursor()
        bd = '''DELETE FROM Servicios WHERE NOMBRE = '{}' '''.format(self.producto_a_borrar)
        cursor.execute(bd)
        self.conexion.commint()
        cursor.close

    def elimina_productosFacturacion(self, nombre):
        cursor = self.conexion.cursor()
        bd = '''DELETE FROM Facturacion WHERE NOMBRE = '{}' '''.format(self.producto_a_borrar)
        cursor.execute(bd)
        self.conexion.commint()
        cursor.close


    def actualiza_productosClientes(self, ID, nombre, apellido, cedula, fecha_nacimiento):
        cursor = self.conexion.cursor()
        bd = '''UPDATE Clientes SET ID = '{}', NOMBRE = '{}', APELLIDO = '{}', CEDULA = '{}', FECHA_NACIMIENTO = '{}'
        WHERE ID = '{}' '''.format(ID, nombre, apellido, cedula, fecha_nacimiento)
        cursor. execute(bd)
        a = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return a
    
    def actualiza_productosReservas(self, numero_de_reserva, servicio, cliente_id):
        cursor = self.conexion.cursor()
        bd = '''UPDATE Reservas SET NUMERO_DE_RESERVA = '{}', SERVICIO = '{}', CLIENTE_ID = '{}'
        WHERE ID = '{}' '''.format(numero_de_reserva, servicio, cliente_id)
        cursor. execute(bd)
        a = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return a
    
    def actualiza_productosHabitaciones(self, numero_de_habitacion, tipo_de_habitacion, estado_de_habitacion):
        cursor = self.conexion.cursor()
        bd = '''UPDATE Habitaciones SET NUMERO_DE_HABITACION = '{}', TIPO_DE_HABITACION = '{}', ESTADO_DE_HABITACION = '{}'
        WHERE ID = '{}' '''.format(numero_de_habitacion, tipo_de_habitacion, estado_de_habitacion)
        cursor. execute(bd)
        a = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return a
    
    def actualiza_productosServicios(self, ID_servicio, nombre_de_servicio, coste_de_servicio):
        cursor = self.conexion.cursor()
        bd = '''UPDATE Servicios SET ID_SERVICIO = '{}', NOMBRE_DE_SERVICIO = '{}', COSTE_DE_SERVICIO = '{}'
        WHERE ID = '{}' '''.format(ID_servicio, nombre_de_servicio, coste_de_servicio)
        cursor. execute(bd)
        a = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return a
    
    def actualiza_productosFacturacion(self, ID_factura, Numero_de_reserva, fecha_facturacion, metodo_de_pago):
        cursor = self.conexion.cursor()
        bd = '''UPDATE Facturacion SET ID_FACTURA = '{}', NUMERO_DE_RESERVA = '{}', FECHA_FACTURACION = '{}', METODO_DE_PAGO = '{}'
        WHERE ID = '{}' '''.format(ID_factura, Numero_de_reserva, fecha_facturacion, metodo_de_pago)
        cursor. execute(bd)
        a = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return a