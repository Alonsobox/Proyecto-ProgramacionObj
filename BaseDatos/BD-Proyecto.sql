use master
drop database VentaVehiculos
create database VentaVehiculos
use VentaVehiculos



create table modelo (
    cod_modelo int primary key not null,
    diseño_modelo varchar(255),
    tecnologia_modelo varchar(255),
    seguridad_modelo varchar(255),
    interior_modelo varchar(255)
);

INSERT INTO modelo (cod_modelo, diseño_modelo, tecnologia_modelo, seguridad_modelo, interior_modelo)
VALUES 
(95451, 'Sedán', 'Híbrido', 'Alta', 'Lujo'),
(94122, 'SUV', 'Eléctrico', 'Media', 'Deportivo'),
(98743, 'Coupé', 'Gasolina', 'Baja', 'Clásico');

update modelo
set precio = 50000
where cod_modelo=95451

update modelo
set precio = 45000
where cod_modelo=94122

update modelo
set precio = 30000
where cod_modelo=98743




create table marca (
    cod_marca int primary key not null,
    nombre_marca varchar(255),
    stock_marca int
);

INSERT INTO marca (cod_marca, nombre_marca, stock_marca)
VALUES 
(87411, 'Toyota', 100),
(84122, 'Ford', 150),
(84713, 'Chevrolet', 200);



create table vehiculo (
    cod_vehiculo int primary key not null,
    color_vehiculo varchar(255),
    año_vehiculo date,
    fichatec_vehiculo varchar(255),
    cod_marca int,
    cod_modelo int,
    foreign key (cod_marca) references marca(cod_marca),
    foreign key (cod_modelo) references modelo(cod_modelo)
);
select * from vehiculo

EXEC sp_rename 'vehiculo.fichatec_vehiculo', 'combus_vehiculo', 'COLUMN';
GO

update vehiculo
set combus_vehiculo  = 'Gasolida'
where cod_vehiculo=78411

update vehiculo
set combus_vehiculo  = 'Electrico'
where cod_vehiculo=74582

update vehiculo
set combus_vehiculo  = 'GLP'
where cod_vehiculo=74123






INSERT INTO vehiculo (cod_vehiculo, color_vehiculo, año_vehiculo, fichatec_vehiculo, cod_marca, cod_modelo)
VALUES 
(78411, 'Rojo', '2021-06-15', 'Ficha técnica 1', 87411, 95451),
(74582, 'Azul', '2022-03-21', 'Ficha técnica 2', 84122, 94122),
(74123, 'Negro', '2020-11-09', 'Ficha técnica 3', 84713, 98743);


create table cliente (
    cod_cliente int primary key not null,
    nombre_cliente varchar(255),
    apellido_cliente varchar(255),
    trabajo_cliente varchar(255),
    telefono_cliente int,
    direccion_cliente varchar(255)
);

INSERT INTO cliente (cod_cliente, nombre_cliente, apellido_cliente, trabajo_cliente, telefono_cliente, direccion_cliente)
VALUES 
(64841, 'Juan', 'Pérez', 'Ingeniero', 123456789, 'Calle Principal 123'),
(65232, 'Ana', 'Gómez', 'Abogada', 987654321, 'Avenida Secundaria 456'),
(69873, 'Carlos', 'López', 'Doctor', 555666777, 'Boulevard Terciario 789');



create table vendedor (
    cod_vendedor int primary key not null,
    nombre_vendedor varchar(255),
    apellido_vendedor varchar(255),
    sueldo_vendedor money,
    ventas_vendedor int
);


INSERT INTO vendedor (cod_vendedor, nombre_vendedor, apellido_vendedor, sueldo_vendedor, ventas_vendedor)
VALUES 
(58741, 'Pedro', 'Martínez', 3000, 10),
(51482, 'Lucía', 'Fernández', 2500, 8),
(59613, 'Miguel', 'Rodríguez', 4000, 12);



create table proveedor (
    cod_proveedor int primary key not null,
    nombre_proveedor varchar(255),
    telefono_proveedor int,
    stock_proveedor int,
    direccion_proveedor varchar(255)
);

INSERT INTO proveedor (cod_proveedor, nombre_proveedor, telefono_proveedor, stock_proveedor, direccion_proveedor)
VALUES 
(45141, 'ProveeAuto', 444555666, 500, 'Av. Proveedores 123'),
(48752, 'AutoSuministros', 222333444, 750, 'Calle Abastecimiento 456'),
(49363, 'Distribuidores SA', 111222333, 300, 'Carrera Distribuidores 789');




create table concesionaria (
    cod_concesionaria int primary key not null,
    nombre_concesionaria varchar(255),
    cantidad_trabaja_concesionaria int,
    direccion_concesionaria varchar(255),
    cod_proveedor int,
    foreign key (cod_proveedor) references proveedor(cod_proveedor)
);


INSERT INTO concesionaria (cod_concesionaria, nombre_concesionaria, cantidad_trabaja_concesionaria, direccion_concesionaria, cod_proveedor)
VALUES 
(31541, 'Concesionaria Uno', 25, 'Calle Concesionarios 1', 45141),
(32162, 'Concesionaria Dos', 30, 'Avenida Vehículos 2', 48752),
(39743, 'Concesionaria Tres', 20, 'Boulevard Autos 3', 49363);




create table factura (
    cod_factura int primary key not null,
    fecha_factura date,
    importe_venta money,
    cod_cliente int,
    cod_vendedor int,
    cod_vehiculo int,
    cod_concesionaria int,
    foreign key (cod_cliente) references cliente(cod_cliente),
    foreign key (cod_vendedor) references vendedor(cod_vendedor),
    foreign key (cod_vehiculo) references vehiculo(cod_vehiculo),
    foreign key (cod_concesionaria) references concesionaria(cod_concesionaria)
);
go


INSERT INTO factura (cod_factura, fecha_factura, importe_venta, cod_cliente, cod_vendedor, cod_vehiculo, cod_concesionaria)
VALUES 
(24581, '2024-01-10', 20000, 64841, 58741, 78411, 31541),
(26982, '2024-02-15', 25000, 65232, 51482, 74582, 32162),
(29873, '2024-03-20', 30000, 69873, 59613, 74123, 39743);




select * from cliente
select * from concesionaria
select * from factura
select * from marca
select * from modelo
select * from proveedor
select * from vehiculo
select * from vendedor
