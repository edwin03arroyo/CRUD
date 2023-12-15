DROP DATABASE hotel_ricon_del_valle;
create database hotel_ricon_del_valle;

use hotel_ricon_del_valle;

CREATE TABLE Clientes (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(10),
    Apellido VARCHAR(255),
    Cedula  VARCHAR(100),
    Fecha_de_nacimiento DATE
  
);
INSERT INTO Clientes (ID, Nombre, Apellido, Cedula, Fecha_de_nacimiento) VALUES
    (39, 'Juan', 'Perez', '0150489169', '09/11/2000'),
    (41, 'Alex', 'Delgado', '0124314455', '20/02/1984'),
    (42, 'Pedro', 'Lopez', '0332454524', '07/09/1977'),
    (43, 'Pablo', 'Godoy', '278378437', '19/12/1980'),
    (44, 'Fernando', 'Torres', '673618938', '18/07/1990'),
    (45, 'Aron', 'Manzano', '737136483', '23/02/2000'),
    (46, 'Justin', 'Reinoso', '3419638634', '08/08/1998'),
    (47, 'Camila', 'Merchan', '3438738744', '27/12/1985'),
    (48, 'Cristina', 'Garcia', '1376731671', '16/11/1999'),
    (49, 'Ana', 'Caldas', '4738478913', '17/05/1992');
    
    CREATE TABLE Reservas (
    numero_de_reserva VARCHAR(20) PRIMARY KEY,
    servicio VARCHAR(10),
    cliente_id INT,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id)
  
);
INSERT INTO Reservas (numero_de_reserva, servicio, cliente_id) VALUES
    (22, 'pscina', '39'),
    (23, 'spa', '41'),
    (24, 'sauna', '42'),
    (25, 'juegos', '43'),
    (26, 'cancha de futbol', '44'),
    (27, 'spa', '45'),
    (28, 'cancha de basket', '46'),
    (29, 'pscina', '47'),
    (30, 'sauna', '48'),
    (31, 'pscina', '49');
    
	CREATE TABLE Habitaciones (
    numero_de_habitacion INT AUTO_INCREMENT PRIMARY KEY,
    tipo_de_habitacion VARCHAR(10),
    estado_de_habitacion VARCHAR(255)
  
);
INSERT INTO Habitaciones (numero_de_habitacion, tipo_de_habitacion, estado_de_habitacion) VALUES
    (09, 'grande', 'libre'),
    (10, 'mediana', 'ocupada'),
    (11, 'especial', 'libre'),
    (12, 'pequeña', 'libre'),
    (13, 'VIP', 'ocupada'),
    (14, 'pequeña', 'ocupada'),
    (15, 'mediana', 'libre'),
    (16, 'especial', 'ocupada'),
    (17, 'grande', 'libre'),
    (18, 'grande', 'ocupada');
    
	CREATE TABLE Servicios (
    ID_servicio INT AUTO_INCREMENT PRIMARY KEY,
    nombre_de_servicio VARCHAR(10),
    coste_de_servicio int
  
);
INSERT INTO Servicios (ID_servicio, nombre_de_servicio, coste_de_servicio) VALUES
    (60, 'pscina', 'libre'),
    (61, 'sauna', 'libre'),
    (62, 'spa', 'libre'),
    (63, 'cancha de futbol', 'libre'),
    (64, 'cancha de basket', 'libre'),
    (65, 'juegos', 'libre');


	CREATE TABLE Facturacion (
    ID_factura INT AUTO_INCREMENT PRIMARY KEY,
    Numero_de_reserva VARCHAR(10),
    fecha_facturacion Date,
    metodo_de_pago  VARCHAR(100)
  
);
INSERT INTO Facturacion (ID_factura, Numero_de_reserva, fecha_facturacion, metodo_de_pago) VALUES
    (01, 22, 'Garcia', '16/11/2023', 'efectivo'),
    (02, 23, 'Garcia', '22/11/2023', 'tarjeta'),
    (03, 24, 'Garcia', '23/11/2023', 'tarjeta'),
    (04, 25, 'Garcia', '29/11/2023', 'efectivo'),
    (05, 26, 'Garcia', '20/11/2023', 'efectivo'),
    (06, 27, 'Garcia', '09/12/2023', 'efectivo'),
    (07, 28, 'Garcia', '20/11/2023', 'tarjeta'),
    (08, 29, 'Garcia', '15/11/2023', 'tarjeta'),
    (09, 30, 'Garcia', '10/11/2023', 'efectivo'),
    (10, 31, 'Garcia', '16/11/2023', 'tarjeta');