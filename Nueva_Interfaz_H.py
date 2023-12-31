# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interfaz_Nueva_H.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(822, 631)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color:rgb(149, 149, 149)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_superior = QtWidgets.QFrame(self.frame)
        self.frame_superior.setMinimumSize(QtCore.QSize(0, 42))
        self.frame_superior.setStyleSheet("Qframe{\n"
"backgrorund-color:rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton{\n"
"backgrorund-color:#000000ff;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"backgrorund-color:rgb(61,61,61);\n"
"border-radius:20px;\n"
"}")
        self.frame_superior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_superior.setObjectName("frame_superior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_clientes = QtWidgets.QPushButton(self.frame_superior)
        self.bt_clientes.setMaximumSize(QtCore.QSize(200, 16777215))
        self.bt_clientes.setIconSize(QtCore.QSize(38, 38))
        self.bt_clientes.setObjectName("bt_clientes")
        self.horizontalLayout.addWidget(self.bt_clientes)
        self.bt_reservas = QtWidgets.QPushButton(self.frame_superior)
        self.bt_reservas.setMinimumSize(QtCore.QSize(40, 40))
        self.bt_reservas.setObjectName("bt_reservas")
        self.horizontalLayout.addWidget(self.bt_reservas)
        self.bt_habitaciones = QtWidgets.QPushButton(self.frame_superior)
        self.bt_habitaciones.setMinimumSize(QtCore.QSize(40, 40))
        self.bt_habitaciones.setObjectName("bt_habitaciones")
        self.horizontalLayout.addWidget(self.bt_habitaciones)
        self.bt_servicios = QtWidgets.QPushButton(self.frame_superior)
        self.bt_servicios.setMinimumSize(QtCore.QSize(40, 40))
        self.bt_servicios.setObjectName("bt_servicios")
        self.horizontalLayout.addWidget(self.bt_servicios)
        self.bt_facturacion = QtWidgets.QPushButton(self.frame_superior)
        self.bt_facturacion.setMinimumSize(QtCore.QSize(40, 40))
        self.bt_facturacion.setObjectName("bt_facturacion")
        self.horizontalLayout.addWidget(self.bt_facturacion)
        self.verticalLayout_2.addWidget(self.frame_superior)
        self.frame_contenido = QtWidgets.QFrame(self.frame)
        self.frame_contenido.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_contenido.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_contenido.setObjectName("frame_contenido")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_contenido)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_control = QtWidgets.QFrame(self.frame_contenido)
        self.frame_control.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_control.setStyleSheet("QFrame{\n"
"background-color:rgb(0, 0, 255)\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:rgb(61,61,61);\n"
"border-top-left-radius: 20px;\n"
"border-buttom-left-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font: 77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border-buttom-left-radius:20px;\n"
"color: rgb(0,0,0);\n"
"font: 77 10pt \"Arial Black\";\n"
"}")
        self.frame_control.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_control.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_control.setObjectName("frame_control")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_control)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.bt_datos = QtWidgets.QPushButton(self.frame_control)
        self.bt_datos.setMinimumSize(QtCore.QSize(0, 40))
        self.bt_datos.setObjectName("bt_datos")
        self.verticalLayout_3.addWidget(self.bt_datos)
        self.bt_registrar = QtWidgets.QPushButton(self.frame_control)
        self.bt_registrar.setMinimumSize(QtCore.QSize(0, 40))
        self.bt_registrar.setObjectName("bt_registrar")
        self.verticalLayout_3.addWidget(self.bt_registrar)
        self.bt_actualizar_2 = QtWidgets.QPushButton(self.frame_control)
        self.bt_actualizar_2.setMinimumSize(QtCore.QSize(0, 40))
        self.bt_actualizar_2.setObjectName("bt_actualizar_2")
        self.verticalLayout_3.addWidget(self.bt_actualizar_2)
        self.bt_eliminar = QtWidgets.QPushButton(self.frame_control)
        self.bt_eliminar.setMinimumSize(QtCore.QSize(0, 40))
        self.bt_eliminar.setObjectName("bt_eliminar")
        self.verticalLayout_3.addWidget(self.bt_eliminar)
        self.bt_ajustes = QtWidgets.QPushButton(self.frame_control)
        self.bt_ajustes.setMinimumSize(QtCore.QSize(0, 40))
        self.bt_ajustes.setObjectName("bt_ajustes")
        self.verticalLayout_3.addWidget(self.bt_ajustes)
        self.horizontalLayout_2.addWidget(self.frame_control)
        self.frame_paginas = QtWidgets.QFrame(self.frame_contenido)
        self.frame_paginas.setStyleSheet("QFrame{\n"
"background-color:rgb(0, 0, 255);\n"
"}\n"
"\n"
"QLabel{\n"
"font: 87 12pt \"Arial Black\";\n"
"background-color:#000000ff;\n"
"color: rgb(49, 49, 49);\n"
"border:0px solid #14C8DC;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 0px;\n"
"color: rgb(255,255,255);\n"
"border.bottom:2px solid rgb(61,61,61);\n"
"font: 75 12pt \"Times New Roman\"\n"
"}\n"
"\n"
"QPussButton{\n"
"background-color: rgb(61, 61, 61);\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"font: 77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0,206,151);\n"
"border-radius: 15px;\n"
"color: rgb(0, 0, 0);\n"
"font: 77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"gridline-color: rgb(0, 206, 151);\n"
"font-size: 12pt;\n"
"color: #000000;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"background-color: rgb(0, 206, 151);\n"
"border: 1px solid rgb(0, 0, 0);\n"
"font-size: 12pt;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section{\n"
"background-color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(0, 206, 151);\n"
"}\n"
"")
        self.frame_paginas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_paginas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_paginas.setObjectName("frame_paginas")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_paginas)
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_paginas)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_datos = QtWidgets.QWidget()
        self.page_datos.setObjectName("page_datos")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_datos)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.page_datos)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.tabla_productos = QtWidgets.QTableWidget(self.page_datos)
        self.tabla_productos.setObjectName("tabla_productos")
        self.tabla_productos.setColumnCount(3)
        self.tabla_productos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(2, item)
        self.verticalLayout_5.addWidget(self.tabla_productos)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.bt_refrescar = QtWidgets.QPushButton(self.page_datos)
        self.bt_refrescar.setMinimumSize(QtCore.QSize(120, 30))
        self.bt_refrescar.setObjectName("bt_refrescar")
        self.horizontalLayout_3.addWidget(self.bt_refrescar)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.stackedWidget.addWidget(self.page_datos)
        self.page_registrar = QtWidgets.QWidget()
        self.page_registrar.setObjectName("page_registrar")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.page_registrar)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_19 = QtWidgets.QLabel(self.page_registrar)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_12.addWidget(self.label_19)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(30)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.page_registrar)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.page_registrar)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.label_4 = QtWidgets.QLabel(self.page_registrar)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSpacing(30)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.reg_codigo = QtWidgets.QLineEdit(self.page_registrar)
        self.reg_codigo.setObjectName("reg_codigo")
        self.verticalLayout_11.addWidget(self.reg_codigo)
        self.regcargo = QtWidgets.QLineEdit(self.page_registrar)
        self.regcargo.setObjectName("regcargo")
        self.verticalLayout_11.addWidget(self.regcargo)
        self.reg_nombre = QtWidgets.QLineEdit(self.page_registrar)
        self.reg_nombre.setObjectName("reg_nombre")
        self.verticalLayout_11.addWidget(self.reg_nombre)
        self.horizontalLayout_6.addLayout(self.verticalLayout_11)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_12.addLayout(self.horizontalLayout_6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.signal_agregar = QtWidgets.QLabel(self.page_registrar)
        self.signal_agregar.setMinimumSize(QtCore.QSize(200, 30))
        self.signal_agregar.setText("")
        self.signal_agregar.setAlignment(QtCore.Qt.AlignCenter)
        self.signal_agregar.setObjectName("signal_agregar")
        self.horizontalLayout_7.addWidget(self.signal_agregar)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.bt_agregar = QtWidgets.QPushButton(self.page_registrar)
        self.bt_agregar.setObjectName("bt_agregar")
        self.horizontalLayout_7.addWidget(self.bt_agregar)
        self.verticalLayout_12.addLayout(self.horizontalLayout_7)
        self.stackedWidget.addWidget(self.page_registrar)
        self.page_actulizar = QtWidgets.QWidget()
        self.page_actulizar.setObjectName("page_actulizar")
        self.layoutWidget_3 = QtWidgets.QWidget(self.page_actulizar)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 60, 572, 438))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setSpacing(30)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_24 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_13.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_13.addWidget(self.label_25)
        self.label_26 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_13.addWidget(self.label_26)
        self.horizontalLayout_8.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setSpacing(30)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.act_codigo = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.act_codigo.setObjectName("act_codigo")
        self.verticalLayout_14.addWidget(self.act_codigo)
        self.act_tipo = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.act_tipo.setObjectName("act_tipo")
        self.verticalLayout_14.addWidget(self.act_tipo)
        self.act_nombre = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.act_nombre.setObjectName("act_nombre")
        self.verticalLayout_14.addWidget(self.act_nombre)
        self.horizontalLayout_8.addLayout(self.verticalLayout_14)
        self.label_32 = QtWidgets.QLabel(self.page_actulizar)
        self.label_32.setGeometry(QtCore.QRect(140, 0, 311, 21))
        self.label_32.setObjectName("label_32")
        self.layoutWidget_5 = QtWidgets.QWidget(self.page_actulizar)
        self.layoutWidget_5.setGeometry(QtCore.QRect(10, 460, 572, 32))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.signal_actualizar = QtWidgets.QLabel(self.layoutWidget_5)
        self.signal_actualizar.setMinimumSize(QtCore.QSize(120, 30))
        self.signal_actualizar.setText("")
        self.signal_actualizar.setAlignment(QtCore.Qt.AlignCenter)
        self.signal_actualizar.setObjectName("signal_actualizar")
        self.horizontalLayout_14.addWidget(self.signal_actualizar)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem5)
        self.bt_actualiza_tabla = QtWidgets.QPushButton(self.layoutWidget_5)
        self.bt_actualiza_tabla.setMinimumSize(QtCore.QSize(120, 30))
        self.bt_actualiza_tabla.setObjectName("bt_actualiza_tabla")
        self.horizontalLayout_14.addWidget(self.bt_actualiza_tabla)
        self.layoutWidget = QtWidgets.QWidget(self.page_actulizar)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 571, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_33 = QtWidgets.QLabel(self.layoutWidget)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_13.addWidget(self.label_33)
        self.act_buscar = QtWidgets.QLineEdit(self.layoutWidget)
        self.act_buscar.setObjectName("act_buscar")
        self.horizontalLayout_13.addWidget(self.act_buscar)
        self.bt_actualiza_buscar = QtWidgets.QPushButton(self.layoutWidget)
        self.bt_actualiza_buscar.setMinimumSize(QtCore.QSize(120, 30))
        self.bt_actualiza_buscar.setObjectName("bt_actualiza_buscar")
        self.horizontalLayout_13.addWidget(self.bt_actualiza_buscar)
        self.stackedWidget.addWidget(self.page_actulizar)
        self.page_eliminar = QtWidgets.QWidget()
        self.page_eliminar.setObjectName("page_eliminar")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_eliminar)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_56 = QtWidgets.QLabel(self.page_eliminar)
        self.label_56.setAlignment(QtCore.Qt.AlignCenter)
        self.label_56.setObjectName("label_56")
        self.verticalLayout.addWidget(self.label_56)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_57 = QtWidgets.QLabel(self.page_eliminar)
        self.label_57.setObjectName("label_57")
        self.horizontalLayout_16.addWidget(self.label_57)
        self.eliminar_buscar = QtWidgets.QLineEdit(self.page_eliminar)
        self.eliminar_buscar.setObjectName("eliminar_buscar")
        self.horizontalLayout_16.addWidget(self.eliminar_buscar)
        self.bt_buscar_borrar = QtWidgets.QPushButton(self.page_eliminar)
        self.bt_buscar_borrar.setMinimumSize(QtCore.QSize(120, 30))
        self.bt_buscar_borrar.setObjectName("bt_buscar_borrar")
        self.horizontalLayout_16.addWidget(self.bt_buscar_borrar)
        self.verticalLayout.addLayout(self.horizontalLayout_16)
        self.tabla_borrar = QtWidgets.QTableWidget(self.page_eliminar)
        self.tabla_borrar.setMinimumSize(QtCore.QSize(200, 30))
        self.tabla_borrar.setObjectName("tabla_borrar")
        self.tabla_borrar.setColumnCount(3)
        self.tabla_borrar.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_borrar.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tabla_borrar)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.signal_eliminacion = QtWidgets.QLabel(self.page_eliminar)
        self.signal_eliminacion.setText("")
        self.signal_eliminacion.setObjectName("signal_eliminacion")
        self.horizontalLayout_17.addWidget(self.signal_eliminacion)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem6)
        self.bt_borrar = QtWidgets.QPushButton(self.page_eliminar)
        self.bt_borrar.setMinimumSize(QtCore.QSize(120, 30))
        self.bt_borrar.setObjectName("bt_borrar")
        self.horizontalLayout_17.addWidget(self.bt_borrar)
        self.verticalLayout.addLayout(self.horizontalLayout_17)
        self.stackedWidget.addWidget(self.page_eliminar)
        self.page_ajustes = QtWidgets.QWidget()
        self.page_ajustes.setObjectName("page_ajustes")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_ajustes)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.page_ajustes)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.codigoB = QtWidgets.QLineEdit(self.page_ajustes)
        self.codigoB.setObjectName("codigoB")
        self.horizontalLayout_4.addWidget(self.codigoB)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.tabla_buscar = QtWidgets.QTableWidget(self.page_ajustes)
        self.tabla_buscar.setObjectName("tabla_buscar")
        self.tabla_buscar.setColumnCount(3)
        self.tabla_buscar.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_buscar.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_buscar.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_buscar.setHorizontalHeaderItem(2, item)
        self.verticalLayout_7.addWidget(self.tabla_buscar)
        self.pushButton = QtWidgets.QPushButton(self.page_ajustes)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_7.addWidget(self.pushButton)
        self.stackedWidget.addWidget(self.page_ajustes)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_paginas)
        self.verticalLayout_2.addWidget(self.frame_contenido)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)
        self.horizontalLayout_15.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_clientes.setText(_translate("MainWindow", "Clientes"))
        self.bt_reservas.setText(_translate("MainWindow", "Reservas"))
        self.bt_habitaciones.setText(_translate("MainWindow", "Habitaciones"))
        self.bt_servicios.setText(_translate("MainWindow", "Servicios"))
        self.bt_facturacion.setText(_translate("MainWindow", "Facturacion"))
        self.bt_datos.setText(_translate("MainWindow", "Registrados"))
        self.bt_registrar.setText(_translate("MainWindow", "Agregar"))
        self.bt_actualizar_2.setText(_translate("MainWindow", "Actualizar"))
        self.bt_eliminar.setText(_translate("MainWindow", "Eliminar"))
        self.bt_ajustes.setText(_translate("MainWindow", "Buscar"))
        self.label.setText(_translate("MainWindow", "Empleados Registrados"))
        item = self.tabla_productos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "N° Habitacion"))
        item = self.tabla_productos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tipo"))
        item = self.tabla_productos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Estado"))
        self.bt_refrescar.setText(_translate("MainWindow", "Actulizar"))
        self.label_19.setText(_translate("MainWindow", "Agregar Habitacion"))
        self.label_5.setText(_translate("MainWindow", "Num_Habitacion"))
        self.label_6.setText(_translate("MainWindow", "Tipo"))
        self.label_4.setText(_translate("MainWindow", "Estado"))
        self.bt_agregar.setText(_translate("MainWindow", "Agregar"))
        self.label_24.setText(_translate("MainWindow", "Num_Habitacion"))
        self.label_25.setText(_translate("MainWindow", "Tipo"))
        self.label_26.setText(_translate("MainWindow", "Estado"))
        self.label_32.setText(_translate("MainWindow", "Actualizacion de Habitacion"))
        self.bt_actualiza_tabla.setText(_translate("MainWindow", "Actualizar"))
        self.label_33.setText(_translate("MainWindow", "Nombre:"))
        self.bt_actualiza_buscar.setText(_translate("MainWindow", "Buscar"))
        self.label_56.setText(_translate("MainWindow", "Eliminar Habitacion"))
        self.label_57.setText(_translate("MainWindow", "Ingrese el Nombre:"))
        self.bt_buscar_borrar.setText(_translate("MainWindow", "Buscar"))
        item = self.tabla_borrar.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "N° Habitacion"))
        item = self.tabla_borrar.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tipo"))
        item = self.tabla_borrar.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Estado"))
        self.bt_borrar.setText(_translate("MainWindow", "Eliminar"))
        self.label_7.setText(_translate("MainWindow", "Ingrese el codigo:"))
        item = self.tabla_buscar.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "N° Habitacion"))
        item = self.tabla_buscar.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tipo"))
        item = self.tabla_buscar.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Estado"))
        self.pushButton.setText(_translate("MainWindow", "Buscar Habitacion"))
