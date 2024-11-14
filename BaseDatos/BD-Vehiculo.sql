CREATE TABLE [cliente] (
  [cod_cliente] int NOT NULL,
  [nombre_cliente] varchar(255) NULL,
  [apellido_cliente] varchar(255) NULL,
  [trabajo_cliente] varchar(255) NULL,
  [telefono_cliente] int NULL,
  [direccion_cliente] varchar(255) NULL,
  PRIMARY KEY CLUSTERED ([cod_cliente])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
)
GO

CREATE TABLE [concesionaria] (
  [cod_concesionaria] int NOT NULL,
  [nombre_concesionaria] varchar(255) NULL,
  [cantidad_trabaja_concesionaria] int NULL,
  [cod_proveedor] int,
  [direccion_concesionaria] varchar(255) NULL,
  PRIMARY KEY CLUSTERED ([cod_concesionaria])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
)
GO

CREATE TABLE [estado] (
  [cod_estado] int NOT NULL,
  [descripcion_estado] varchar(255) NULL,
  PRIMARY KEY CLUSTERED ([cod_estado])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
)
GO

CREATE TABLE [factura] (
  [cod_factura] int NOT NULL,
  [fecha_factura] date NULL,
  [importe_venta] money NULL,
  [cod_cliente] int,
  [cod_vendedor] int,
  [cod_vehiculo] int,
  [cod_concesionaria] int,
  PRIMARY KEY CLUSTERED ([cod_factura])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
)
GO

CREATE TABLE [marca] (
  [cod_marca] int NOT NULL,
  [nombre_marca] varchar(255) NULL,
  [stock_marca] int NULL,
  PRIMARY KEY CLUSTERED ([cod_marca])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
)
GO

CREATE TABLE [modelo] (
  [cod_modelo] int NOT NULL,
  [diseño_modelo] varchar(255) NULL,
  [tecnologia_modelo] varchar(255) NULL,
  [seguridad_modelo] varchar(255) NULL,
  [interior_modelo] varchar(255) NULL,
  PRIMARY KEY CLUSTERED ([cod_modelo])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
)
GO

CREATE TABLE [proveedor] (
  [cod_proveedor] int NOT NULL,
  [nombre_proveedor] varchar(255) NULL,
  [telefono_proveedor] int NULL,
  [stock_proveedor] int NULL,
  [direccion_proveedor] varchar(255) NULL,
  PRIMARY KEY CLUSTERED ([cod_proveedor])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
)
GO

CREATE TABLE [trasmicionVehiculo] (
  [cod_trasmision] int NOT NULL,
  [tipo_trasmision] varchar(255) NULL,
  PRIMARY KEY CLUSTERED ([cod_trasmision])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
)
GO

CREATE TABLE [vehiculo] (
  [cod_vehiculo] int NOT NULL,
  [color_vehiculo] varchar(255) NULL,
  [año_vehiculo] date NULL,
  [cod_marca] int,
  [cod_modelo] int,
  [fichaTec_vehiculo] varchar(255) NULL,
  [cod_trasmision] int,
  PRIMARY KEY CLUSTERED ([cod_vehiculo])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
)
GO

CREATE TABLE [vendedor] (
  [cod_vendedor] int NOT NULL,
  [nombre_vendedor] varchar(255) NULL,
  [apellido_vendedor] varchar(255) NULL,
  [sueldo_vendedor] money NULL,
  [ventas_vendedor] int NULL,
  PRIMARY KEY CLUSTERED ([cod_vendedor])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)
)
GO

ALTER TABLE [concesionaria] ADD CONSTRAINT [fk_concesionaria_proveedor_1] FOREIGN KEY ([cod_proveedor]) REFERENCES [proveedor] ([cod_proveedor])
GO
ALTER TABLE [estado] ADD CONSTRAINT [fk_estado_factura_1] FOREIGN KEY ([cod_estado]) REFERENCES [factura] ([cod_concesionaria])
GO
ALTER TABLE [factura] ADD CONSTRAINT [fk_venta_cliente_1] FOREIGN KEY ([cod_cliente]) REFERENCES [cliente] ([cod_cliente])
GO
ALTER TABLE [factura] ADD CONSTRAINT [fk_venta_vendedor_2] FOREIGN KEY ([cod_vendedor]) REFERENCES [vendedor] ([cod_vendedor])
GO
ALTER TABLE [factura] ADD CONSTRAINT [fk_venta_vehiculo_3] FOREIGN KEY ([cod_vehiculo]) REFERENCES [vehiculo] ([cod_vehiculo])
GO
ALTER TABLE [factura] ADD CONSTRAINT [fk_venta_concesionaria_4] FOREIGN KEY ([cod_concesionaria]) REFERENCES [concesionaria] ([cod_concesionaria])
GO
ALTER TABLE [vehiculo] ADD CONSTRAINT [fk_vehiculo_marca_1] FOREIGN KEY ([cod_marca]) REFERENCES [marca] ([cod_marca])
GO
ALTER TABLE [vehiculo] ADD CONSTRAINT [fk_vehiculo_modelo_2] FOREIGN KEY ([cod_modelo]) REFERENCES [modelo] ([cod_modelo])
GO
ALTER TABLE [vehiculo] ADD CONSTRAINT [fk_vehiculo_trasmicionVehiculo_3] FOREIGN KEY ([cod_trasmision]) REFERENCES [trasmicionVehiculo] ([cod_trasmision])
GO
ALTER TABLE [vendedor] ADD CONSTRAINT [fk_vendedor_concesionaria_1] FOREIGN KEY ([cod_vendedor]) REFERENCES [concesionaria] ([cod_proveedor])
GO

