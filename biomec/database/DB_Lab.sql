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
Contraseña varchar(150) not null,
ID_Rol_ integer not null, 	 
primary key (ID),
ID_persona integer not null, 
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



-----------------POBLANDO LA BASE DE DATOS

-- personal
insert into Persona values(1,'Sandra', 'Tomicha', 'Rodriguez',798438,'Tomicha54@virtual.com','1996-06-15');
insert into Persona values(2,'Lola', 'Pacheco', 'Aldana',613114,'Pacheco53@virtual.com','1990-07-05');
insert into Persona values(3,'Pedro', 'Quevedo', 'Ribera',753534,'Quevedo47@virtual.com','1984-11-19');

-- laboratorista
insert into Persona values(4,'Leanne Grace', 'Zurita', 'Frias',709920,'Zurita49@virtual.com','1980-05-10');
insert into Persona values(5,'Fatima', 'Ferrufino', 'Robles',634105,'Ferrufino46@hemovirtual.com','1977-02-07');
insert into Persona values(6,'Lourdes Gerorgina', 'Garzón', 'Menacho',608678,'Garzon52@hemovirtual.com','1991-05-11');

-- paciente
insert into Persona values(7,'Yesmin','Manjares',null,null,'Manjares51@hemovirtual.com','1995-05-14');
insert into Persona values(8,'Nathaly', 'Lazarte',null,null,'Lazarte50@hemovirtual.com','1991-12-25');
insert into Persona values(9,'Yoana', 'Vaca', 'Lopez',785955,'Vaca48@hemovirtual.com','1989-01-20');
insert into Persona values(10,'Veronica', 'Carrizales', 'Tasima',609056,'Carrizales45@hemovirtual.com','1994-11-04');
insert into Persona values(11,'Katherin', 'Arteaga', 'Melgar',null,'Arteaga44@hemovirtual.com','1990-10-07');

--ADMIN
insert into Persona values(12,'CRISTIAN','CUELLAR','SERRANO',78021105,'ccuellar260@gmail.com','1990-10-07');
insert into Persona values(13,'LUIS EDUARDO','CESPEDES','VARGAS',77679046,'llxxlaloxxll@gmail.com','1990-10-07');
insert into Persona values(14,'BEBI','VARGAS','RIOS',70033034,'bbithalindaa@gmail.com','1990-10-07');
insert into Persona values(15,'NELSON','PANIAGUA','PORRAS',79492778,'nelson95sc@gmail.com','1990-10-07');
insert into Persona values(16,'FRANZ','RIBERA','SAAVEDRA',78596734,'ribera.franz@ficct.uagrm.edu.bo','1990-10-07');




insert into Rol values(1,'Admin');
insert into Rol values(2,'Recepcionista');
insert into Rol values(3,'Doctor');
insert into Rol values(4,'Paciente');



insert into Privilegio values(1,'Agregar Usuario')
insert into Privilegio values(2,'Eliminar Usuario')
insert into Privilegio values(3,'Registrar Paciente')
insert into Privilegio values(4,'Registrar Doctor')
insert into Privilegio values(5,'Reporte')


insert into Privilegio_Rol values(1,1);
insert into Privilegio_Rol values(2,1);
insert into Privilegio_Rol values(3,1);
insert into Privilegio_Rol values(4,1);
insert into Privilegio_Rol values(5,1);
insert into Privilegio_Rol values(3,2);
insert into Privilegio_Rol values(5,2);
insert into Privilegio_Rol values(5,3);
insert into Privilegio_Rol values(5,4);

-- usuarios administradores
insert into Usuario values(1,'cristian','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',1,12);
insert into Usuario values(2,'luis','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',1,13);
insert into Usuario values(3,'bebi','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',1,14);
insert into Usuario values(4,'nelson','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',1,15);
insert into Usuario values(5,'franz','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',1,16);

-- usuarios de personal ( recepcionista)
insert into Usuario values(6,'sandra','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',2,1);


-- usuarios de Tecnico o el doctor ( Laboratorista)
insert into Usuario values(7,'fatima','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',3,5);

-- usuarios de Paciente 
insert into Usuario values(8,'Yesmin','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',4,7);
insert into Usuario values(9,'Nathaly','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',4,8);
insert into Usuario values(10,'Yoana','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',4,9);
insert into Usuario values(11,'Veronica','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',4,10);
insert into Usuario values(12,'Katherin','pbkdf2:sha256:260000$UJdTDI1U1yespnS4$5ec3974d5906c6e3e28a87da7e44e191eeecba9a794ff4bf368072eac040d11e',4,11);






select * from Paciente



insert into Cargo values(1,'Gerente');
insert into Cargo values(2,'Secrearia');
insert into Cargo values(3,'Recepcionista');




insert into Personal values(1,1);
insert into Personal values(2,2);
insert into Personal values(3,3);






insert into seguro values(1,'Niño Jesús');
insert into seguro values(13,'Seguro Social Universitario');
insert into seguro values(16,'Nacional Vida');
insert into seguro values(3,'Satelite Norte');
insert into seguro values(5,'Alianza');






insert into Paciente values(7,13);
insert into Paciente values(8,16);
insert into Paciente values(9,1);
insert into Paciente values(10,3);
insert into Paciente values(11,5);





insert into Especialida_Med values(1,'Urologia');
insert into Especialida_Med values(2,'Oncologia');
insert into Especialida_Med values(3,'Medico Forence');





insert into Laboratorista values(4,1);
insert into Laboratorista values(5,2);
insert into Laboratorista values(6,1);




/*hidroxido de sodio*/ insert into Inventario values(1,'NaOH',3,4);
insert into Inventario values(2,'Azul de lactofeno',2,4);
insert into Inventario values(3,'Sistesis organica',3,5);
insert into Inventario values(4,'soluciones volumetricas',4,6);







insert into TipoMuestra values(1,'Heces fecales');
insert into TipoMuestra values(2,'Orina');
insert into TipoMuestra values(3,'Sangre');








insert into Metodo values(1,'Elisa');
insert into Metodo values(2,'Western Blot');
insert into Metodo values(3,'in situ (FLISH)');







insert into Muestra values(001,'2022-03-15','09:00:00',4,7,1,1);
insert into Muestra values(002,'2022-02-28','08:30:00',5,8,2,2);
insert into Muestra values(003,'2022-01-15','07:00:00',6,9,3,3);







Insert into Resultado_analisis values (1,'  ','2022-03-17','Bernardo Ortiz',4,8);
insert into Resultado_analisis values (2,'   ','2022-03-4','Maria del Carmen',4,9);
insert into Resultado_analisis values (3,'   ','2022-01-17','Brando Quispe',5,10);



--mostrar el monto total de los pacientes del medico "Maria del Carmen" 
select Muestra.fecha, persona.nombre
from Muestra, Resultado_analisis, persona

select DISTINCT  paciente.id_paciente, persona.nombre, resultado_analisis.orden_medico, recibo_analisis.monto_total
from Resultado_analisis, persona, recibo_analisis, paciente
where resultado_analisis.orden_medico = 'Maria del Carmen' 
		and paciente.id_paciente = persona.ci 
		and recibo_analisis.ci_paciente = paciente.id_paciente
order by paciente.id_paciente

--mostrar el nombre de las muestras y sus precios que realizan los pacientes del medico "Bernardo Ortiz"

select DISTINCT  paciente.id_paciente, persona.nombre, resultado_analisis.orden_medico,
					recibo_analisis.monto_total, l_analisis.nombre
from Resultado_analisis, persona, recibo_analisis, paciente, detalle,l_analisis
where resultado_analisis.orden_medico = 'Bernardo Ortiz' 
		and paciente.id_paciente = persona.ci 
		and recibo_analisis.ci_paciente = paciente.id_paciente
		and detalle.id_recibo = recibo_analisis.id
		and l_analisis.id =  detalle.id_l_analisis
order by paciente.id_paciente

--mostrar el nombre laboratoristas que realizan analisis a los pacientes del medico "Brando Quispe"

select DISTINCT   paciente.id_paciente,persona.nombre, resultado_analisis.orden_medico,
					recibo_analisis.monto_total, l_analisis.nombre
from Resultado_analisis, persona, recibo_analisis, paciente, detalle,l_analisis, laboratorista
where resultado_analisis.orden_medico = 'Maria del Carmen' 
		and paciente.id_paciente = persona.ci 
		and recibo_analisis.ci_paciente = paciente.id_paciente
		and detalle.id_recibo = recibo_analisis.id
		and l_analisis.id =  detalle.id_l_analisis
		and laboratorista.id_laboratorista = persona.ci 
		and laboratorista.id_esp_med = resultado_analisis.id
order by  paciente.id_paciente


insert into Paquete_analisis values (1,'Parasitologia');
insert into Paquete_analisis values (2,'Orina');
insert into Paquete_analisis values (3,'Drogas');





insert into L_Analisis values (1,'Moco Fecal',90,1); 
insert into L_Analisis values (2,'Parasitologia Simple',70,1); 
insert into L_Analisis values (3,'Orina Completo',80,2); 
insert into L_Analisis values (4,'Magnesuria',67,2); 
insert into L_Analisis values (5,'Cocaina',150,3); 
insert into L_Analisis values (6,'Marihuana',100,3);


select * from L_Analisis


insert into Recibo_Analisis values (2020,'2022-03-15',90,1,8);
insert into Recibo_Analisis values (3030,'2022-02-28',70,2,9);
insert into Recibo_Analisis values (4040,'2022-01-15',80,3,10);







insert into Detalle values (2020,1);
insert into Detalle values (3030,2);
insert into Detalle values (4040,5);
