import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QWidget
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from conexion import Comunication
from datetime import datetime

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('interfaz_Nueva.ui', self)

        self.producto_a_borrar = None
        self.regcargo = QtWidgets.QLineEdit(self)
        label_cliente_registrado = self.page_registrar.findChild(QtWidgets.QLabel, 'label_cliente_registrado')
        if label_cliente_registrado:
            self.page_registrar.setText('Cliente Registrado')
        else:
            print("No se encontró el widget correcto en page_registrar.")
        self.row_flag = None
        self.Id = None
        self.bt_refrescar.clicked.connect(self.mover_menu)
        self.Prueba = Comunication() #clase comunicacion con sqlite

        #ocultamos los botones
        self.bt_reservas.hide()
        #botones
        self.bt_refrescar.clicked.connect(self.mostrar_productosClientes)
        self.bt_agregar.clicked.connect(self.registrar_productos)
        self.bt_borrar.clicked.connect(self.eliminar_productos)
        self.bt_actualiza_tabla.clicked.connect(self.modificar_empleados)
        self.bt_ajustes.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_ajustes))
        self.bt_buscar_borrar.clicked.connect(self.buscar_por_nombre_eliminar)

        #control barra de titulos
        self.bt_habitaciones.clicked.connect(self.control_bt_minimizar)
        self.bt_reservas.clicked.connect(self.control_bt_normal)
        self.bt_servicios.clicked.connect(self.control_bt_maximizar)
        self.bt_facturacion.clicked.connect(lambda: self.close())

        #eliminar barra y de titulo
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        #mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana

        #conexion botones
        self.bt_datos.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_datos))
        self.bt_registrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_registrar))
        self.bt_actualizar_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_actulizar))
        self.bt_eliminar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_eliminar))
        self.bt_ajustes.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_ajustes))


        #ancho de columna adaptableaz
        self.tabla_borrar.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla_productos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    
    def control_bt_minimizar(self):
        self.showMinimized()
        
    def control_bt_normal(self):
        self.showNormal()
        self.bt_restaurar.hide()
        self.bt_restaurar.show()

    def control_bt_maximizar(self):
        self.showMaximized()
        self.bt_maximizar.hide()
        self.bt_restaurar.show()

    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    def mousePressEvent(self, event):
        self.click_position = event.globalPos()


    def mover_ventana(self, event):
        if self.isMaximized() == False:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.click_position)
                self.click_position = event.globalPos()  # Añade esta línea
                event.accept()
        if event.globalPos().y() <= 10:
            self.showMaximized()
            self.bt_maximizar.hide()
            self.bt_restaurar.show()
        else:
            self.showNormal()
            self.bt_resturar.hide()
            self.bt_maximizar.show()

    def mover_menu(self):
        if True:
            width = self.frame_control.width()
            normal = 0
            if width == 0:
                extender = 200
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.frame_control, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()

    def mostrar_productosClientes(self):
        datos = self.Prueba.mostrar_productosClientes()
        i = len(datos)
        self.tabla_productos.setRowCount(i)
        tablerow = 0
        for row in datos:
            fecha_nacimiento_str = row[4].strftime('%Y-%m-%d')  # Convierte a cadena en el formato deseado
            self.tabla_productos.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_productos.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.tabla_productos.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.tabla_productos.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(fecha_nacimiento_str))
            tablerow += 1
            self.signal_actualizar.setText("")
            self.signal_agregar.setText("")
            self.signal_eliminacion.setText("")

    def registrar_productos(self):
        codigo = self.reg_codigo.text().upper()
        nombre = self.reg_nombre.text().upper()
        apellido = self.reg_apellido.text().upper()
        cedula = self.reg_cedula.text()
        telefono = self.reg_telefono.text()
        self.Prueba.inserta_productoClientes(codigo, nombre, apellido, cedula, telefono)
        # Obtener la fecha de nacimiento del QDateEdit
        fecha_nacimiento_widget = self.findChild(QtWidgets.QDateEdit, 'reg_telefono')  # Asegúrate de usar el nombre correcto
        fecha_nacimiento = None
        if fecha_nacimiento_widget:
            try:
                fecha_nacimiento = fecha_nacimiento_widget.date().toPyDate()
            except Exception as e:
                print(f"Error al obtener la fecha de nacimiento: {e}")

        if codigo != '' and nombre != '' and apellido != '' and cedula != '' and telefono != '' and fecha_nacimiento is not None:
            try:
                self.Prueba.inserta_productoClientes(codigo, nombre, apellido, cedula, telefono, fecha_nacimiento)
                self.label_registro.setText('Cliente Registrado')
            except Exception as e:
                print(f"Error al registrar cliente: {e}")
        else:
            self.label_mensaje_registrar = self.page_registrar.findChild(QtWidgets.QLabel, 'label_mensaje_registrar')
            self.reg_codigo.clear()
            self.reg_nombre.clear()
            self.reg_apellido.clear()
            self.reg_cedula.clear()
            self.reg_telefono.clear()
            fecha_nacimiento_widget = self.findChild(QtWidgets.QDateEdit, 'reg_fecha_nacimiento')


    def buscar_por_nombrea(self):
        id_producto = self.act_buscar.text().upper()
        id_producto = str("'" + id_producto + "'")
        self.mostrar_producto = self.Prueba.busca_producto(id_producto)
        if len(self.mostrar_producto) !=0:
            self.Id = self.mostrar_producto[0][0]
            self.act_codigo.setText(str(self.mostrar_producto[0][1]))
            self.act_cargo.setText(str(self.mostrar_producto[0][2]))
            self.act_nombre.setText(str(self.mostrar_producto[0][3]))
            self.act_apellido.setText(str(self.mostrar_producto[0][4]))
            self.act_cedula.setText(str(self.mostrar_producto[0][5]))
            self.act_telefono.setText(str(self.mostrar_producto[0][6]))
            self.act_direccion.setText(str(self.mostrar_producto[0][7]))
            self.act_edad.setText(str(self.mostrar_producto[0][8]))


    def modificar_empleados(self):
        if self.mostrar_productos:
            codigo = self.act_codigo.text().upper()
            nombre = self.act_nombre.text().upper()
            apellido = self.act_apellido.text().upper()
            cedula = self.act_cedula.text().upper()
            telefono = self.act_telefono.text().upper()
            # Actualiza la llamada al método actualiza_productos según la definición real
            act = self.Prueba.actualiza_productos(self.Id, codigo, nombre, apellido, cedula, telefono)
            if act == 1:
                self.signal_actualizar.setText("Actualizado")
                self.act_codigo.clear()
                self.act_cargo.clear()
                self.act_nombre.clear()
                self.act_apellido.clear()
                self.act_cedula.clear()
                self.act_telefono.clear()
                self.act_direccion.clear()
                self.act_edad.clear()
            elif act == 0:
                self.signal_actualizar.setText("Error")
            else:
                self.signal_actualizar.setText("Incorrecto")
        else:
            print("Error: La variable mostrar_producto está vacía o no definida.")


    def buscar_por_nombre_eliminar(self):
        nombre_producto = self.eliminar_buscar.text().upper()
        nombre_producto = str("'" + nombre_producto + "'")
        producto = self.Prueba.busca_producto(nombre_producto)
        self.tabla_borrar.setRowCount(len(producto))
        
        if len(producto) == 0:
            self.signal_eliminacion.setText('No existe')
            self.producto_a_borrar = None
        else:
            self.signal_eliminacion.setText('Empleado Seleccionado')
            self.producto_a_borrar = producto[0][2]

        tablerow = 0
        for row in producto:
            self.producto_a_borrar = row[2]
            self.tabla_borrar.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_borrar.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2]))
            self.tabla_borrar.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3]))
            self.tabla_borrar.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4]))
            self.tabla_borrar.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
            self.tabla_borrar.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[6]))
            self.tabla_borrar.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[7]))
            self.tabla_borrar.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[8]))
            tablerow += 1

    def eliminar_productos(self):
        if self.producto_a_borrar is not None:
            row_flag = self.tabla_borrar.currentRow()
            if self.row_flag == 0:
                self.tabla_borrar.removeRow(0)
                self.Prueba.elimina_productos("'" + self.producto_a_borrar + "'")
                self.signal_eliminacion.seText('Producto Eliminado')
                self.eliminar_buscar.setText('')
            self.producto_a_borrar = None
        else:
            print("No hay producto a borrar.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = VentanaPrincipal()
    mi_app.show()
    sys.exit(app.exec_())