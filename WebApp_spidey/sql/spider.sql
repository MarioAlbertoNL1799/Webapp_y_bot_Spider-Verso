CREATE DATABASE spider_bot;

USE spider_bot;

CREATE TABLE spiders(
    id_spidey int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre varchar(70) NOT NULL,
    identidad varchar(80) NOT NULL,
    genero enum('Femenino', 'Masculino', 'Animal', 'Traje alternativo') NOT NULL,
    universo varchar(15)NOT NULL,
    aparicion varchar(100) NOT NULL,
    colores varchar(70) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO spiders (nombre, identidad, genero, universo, aparicion, colores) VALUES
('Spider-Man','Peter Parker',2,'616','Amazing Fantasy #15','Rojo con azul y detalles negros'),
('Spider-Man 2099','Miguel O´Hara',2,'2099','Spider-Man 2099 #1','Azul con detalles rojos'),
('Superior Spider-Man','Otto Octavius(en cuerpo de Peter Parker)',2,'616','The Superior Spider-Man #1','Rojo y negro'),
('Scarlet Spider','Ben Reilly',2,'616','Web of Spider-Man #117','Rojo con sudadera azul'),
('Aracnido Junior','',2,'TRN521','Spider-Verse #2','Azul con rojo'),
('Spider-Punk','Hobie Brown',2,'138','Amazing SPider-Man(Vol. 3) #10','Azul con rojo, chaqueta y detalles blancos'),
('Lady Spider','May Reilly',1,'803','Spider-Verse #1','Gris con azul y rojo, detalles cafes'),
('Silk','Cindy Moon',1,'616','Amazing Spider-Man(Vol. 3) #8','Blanco con negro'),
('Ghost Spider','Peter Parker',2,'11638','Annual Amazing Spider-Man(Vol.1) #38','Blanco y detalles negros, craneo flamenate azul'),
('Spider-Man Cosmico','Peter Parker',2,'13','Spectacular Spider-Man #158','Blanco con detalles cosmicos'),
('Spider-Knight','Peter Parker',2,'TRN458','Fairy tale of Spider-Man #4','Armadura gris con rojo'),
('Spider-Man 1602','Peter Parquash',2,'1602','Marvel 1602 #1','Azul con rojo y detalles blancos'),
('Ghost-Spider','Gwen Stacy',1,'65','Edge of Spider-verse #2','Blanco con negro y detalles rosados'),
('Scarlet-Spider','Kaine',2,'616','Scarlet-Spider #2','Rojo con negro'),
('Spider-Man India','Pavitr Prabhakar',2,'50101','Spider-Man India #1','Blanco con Rojo y azul'),
('Spider-Man Assassin','Peter Parker',2,'8351','What if? Spider-Man vs. Wolverine #1','Negro con rojo'),
('Spider-Man Ultimate','Miles Morales',2,'1610','Ultimate Comics: Spider-Man #5','Negro con detalles rojos'),
('Spider-Man Bullet Points','Bruce Banner',2,'70105','Bullet Points #4','Negro con verde grisaseo'),
('Spider-Girl','Anya Corazon',1,'616','Young Alliance(Vol. 2) #5','Negro con blanco'),
('Mangaverse Spider-Man','Peter Parker',2,'2301','Marvel mangaverse: Spider-Man #1','Rojo con azul, detalles negros y vendajes'),
('Spider-Man Future Fundation','Peter Parker',4,'616','Amazing Spider-Man #658','Blanco y negro'),
('Spider-Man Dinastia de M','Peter Parker',2,'58163','Spider-Man: House of M','Azul con rojo'),
('Spider-Man Noir','Peter Parker',2,'90214','Spider-Man Noir #1','Negro'),
('Spider-Man Last Stand','Peter Parker',2,'312500','Amazing Spider-Man #500','Rojo con negro y oantalon'),
('Spider-Girl','May Day Parker',1,'982','What if? #105','Azul Marino y rojo con detalles negros'),
('Spider-Man Earth X','Peter Parker',2,'9997','Earth X#1','Azul y rojo '),
('Spider-UK','Billy Braddock',2,'833','Edge of Spider-Verse #2','Azul claro con rojo y detalles blancos'),
('Spider-Girl','Ashley Barton',1,'807128','Old Man Logan #3','Rojo con azul'),
('Spider-Man Dr.Aikman','Aaron Aikman',2,'31411','Edge of Spider-Verse #3','Rojo con negro'),
('Spider-Man 2211','Max Borne',2,'9500','Spider-Man 2099 know Spider-Man #1','Azul con blancco y rojo'),
('Captain Spider','Flash Thompson',2,'78127','What if? #7','Rojo con Azul y detalles negros'),
('Iron-Spider','Peter Parker',4,'616','Amazing Spider-Man #529','Rojo con detalles dorados'),
('Spider-Man Ends of the earth','Peter Parker',4,'616','Amazing Spider-Man #682','Rojo con negro y detalles grises'),


SHOW TABLES;

SELECT * FROM spiders;

DESCRIBE spiders;

CREATE USER 'spidey'@'localhost' IDENTIFIED BY 'spidey.2019';
GRANT ALL PRIVILEGES ON spider_bot.* TO 'spidey'@'localhost';
FLUSH PRIVILEGES;
