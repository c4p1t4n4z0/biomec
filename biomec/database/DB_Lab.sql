create database BD_Lab;
use BD_Lab;
Create table Persona
(	CI integer not null,
	Nombre varchar(40)not null,
    ApellidoP varchar(15) not null,
	ApellidoM varchar(15) ,
	Telefono Decimal(10),
    Correo varchar(40),
	Fecha_Nacimiento date not null,
	primary key (CI)
);
create table Privilegio(
ID integer not null,
Descripcion varchar(60) not null,
primary key(ID)
);

create table Rol(
ID integer not null,
Nombre varchar(60) not null,
primary key(ID)
);

create table Privilegio_Rol(
ID_Privilegio integer not null,
ID_Rol integer not null,
primary key (ID_Privilegio,ID_Rol),
foreign key (ID_Privilegio) references Privilegio(ID)
on update cascade
on delete cascade,
foreign key (ID_Rol) references Rol(ID)
on update cascade
on delete cascade
);


create table Usuario
(
ID integer not null,
Nombre varchar(30) not null,
Contraseña varchar(15) not null,
ID_Rol_ integer not null, -- que acepte valores nulos
primary key (ID),
ID_persona integer,		 -- que acepte valores nulos
foreign key (ID_persona) references Persona(CI)
on update cascade
on delete cascade,
foreign key (ID_Rol_) references Rol(ID)
on update cascade
on delete cascade
);





create table Cargo
(
	ID_Cargo integer not null,
	Nombre varchar(25) not null,
	primary key(ID_Cargo)
);

create table Personal
(
	ID_Persona integer not null,
	ID_Crg integer not  null,
	primary key (ID_Persona),
    foreign key (ID_Persona) references Persona(CI),
	foreign key (ID_Crg) references Cargo(ID_Cargo)
	on update cascade
	on delete cascade
);

create table seguro
(
	Nro_Seguro integer not null,
	Nombre_Seguro varchar(30),
	primary key(Nro_Seguro)
);

create table Paciente
(
	ID_Paciente integer not null,
	Nro_Sg integer not null,
	primary key(ID_Paciente),
    foreign key (ID_Paciente) references Persona(CI),
	foreign key (Nro_Sg) references Seguro(Nro_Seguro)
	on update cascade
	on delete cascade
);

create table Especialida_Med
(
	ID integer not null,
	Nombre_Esp varchar(30),
	primary key(ID)
);

create table Laboratorista
(
	ID_Laboratorista integer not null,
	ID_Esp_med integer not null,
	primary key(ID_Laboratorista),
    foreign key (ID_Laboratorista) references Persona(CI),
	foreign key (ID_Esp_med) references Especialida_Med(ID)
	on update cascade
	on delete cascade
);

create table Inventario
(
	ID integer not null,
	Nombre varchar(50)not null,
	cantidad integer not null,
	ID_lb integer not null,
	primary key(ID),
	foreign key (ID_lb) references Laboratorista(ID_Laboratorista)
	on update cascade
	on delete cascade
);

create table TipoMuestra
(
	ID integer not null,
	Nombre varchar(30) not null,
	primary key(ID)
);

create table Metodo
(
	ID integer not null,
	Nombre varchar(15) not null,
	primary key(ID)
);

create table Muestra
(
	ID integer not null,
	Fecha date not null,
	Hora time not null,
	ID_lb integer not null,
	ID_pct integer not null,
	ID_TM integer not null,
	ID_Met integer not null,
	primary key(ID),
	foreign key (ID_lb) references Laboratorista(ID_Laboratorista)
	on update cascade
	on delete cascade,
	foreign key (ID_pct) references Paciente(ID_Paciente)
	on update cascade
	on delete cascade,
	foreign key(ID_TM) references TipoMuestra(ID)
	on update cascade
	on delete cascade,
	foreign key(ID_Met) references Metodo(ID)
	on update cascade
	on delete cascade
);

create table Resultado_analisis
(
	ID integer not null,
	Descripcion varchar(50),
	Fecha_Emision datetime not null,
	Orden_medico varchar(50) not null,
	ID_lb integer not null,
	ID_pct integer not null,
	primary key(ID),
	foreign key (ID_lb) references Laboratorista(ID_Laboratorista)
	on update cascade
	on delete cascade,
	foreign key (ID_pct) references Paciente(ID_Paciente)
	on update cascade
	on delete cascade
);

create table Paquete_analisis
(
	ID integer not null,
	Nombre varchar(20) not null,
	primary key(ID)
);
create table L_Analisis 
(
	ID integer not null,
	Nombre varchar(30) not null,
	Precio real not null,
	ID_PqA integer not null,
	primary key(ID),
	foreign key (ID_PqA) references Paquete_analisis(ID)
	on update cascade
	on delete cascade
);

create table Recibo_Analisis
(
	ID integer not null,
	Fecha datetime not null,
	Monto_total real not null,
    ID_Per integer not null,
    CI_Paciente integer not null,
	primary key(ID),
    foreign key (ID_Per) references Personal(ID_Persona),
    foreign key (CI_Paciente) references Paciente(ID_Paciente)
);

create table Detalle
(
	ID_Recibo integer not null,
	ID_L_Analisis integer not null,
    primary key (ID_Recibo, ID_L_Analisis),
    foreign key (ID_Recibo) references Recibo_Analisis(ID)
		on update cascade
        on delete cascade,
	foreign key (ID_L_Analisis) references L_Analisis(ID)
		on update cascade
        on delete cascade
);