Create database if not exists MHNU;
use MHNU;
create table if not exists usuarios(
 	cod_usuar int auto_increment primary key,
  	nomb_usuar varchar(20),
  	clave varchar(20),
  	tipo_us varchar(20)
);

create table if not exists coleccion(
	cod_col int auto_increment primary key,
	nomb_comun varchar(20),
	nomb_cientifico varchar(20),
	carac_col varchar(100)
);

create table if not exists clase(
	cod_cla int auto_increment primary key,
	nomb_cla varchar(20),	
	cod_col int ,
	constraint fk_codcol foreign key (cod_col) references coleccion(cod_col)
);

create table if not exists orden(
  	cod_ord int auto_increment primary key,
  	nomb_ord varchar(20),
	carac_ord varchar (100),
  	cod_cla int,
	constraint fk_codcla foreign key (cod_cla) references clase(cod_cla)
);

create table if not exists familia(
  	cod_fam int auto_increment primary key,
  	nomb_fam varchar(20),
  	cod_ord int,
	constraint fk_codord foreign key (cod_ord) references orden(cod_ord)
);

create table if not exists genero(
  	cod_gen int auto_increment primary key,
  	nomb_gen varchar(20),
  	cod_fam int,
	constraint fk_codfam foreign key (cod_fam) references familia(cod_fam)
);

create table if not exists especies(
  	cod_esp int auto_increment primary key,
  	nomb_esp varchar(40),
	cod_gen int,
	constraint fk_codgen foreign key (cod_gen) references genero(cod_gen)
);

create table if not exists subespecie(
  	cod_sub int auto_increment primary key,
  	nomb_sub varchar(40),
	cod_esp int,
	constraint fk_codesp foreign key (cod_esp) references especies(cod_esp)
);

create table if not exists pais(
  	cod_pais int auto_increment primary key,
  	nomb_pais varchar(20)
);

create table if not exists departamento(
  	cod_dept int auto_increment primary key,
  	nomb_dept varchar(20),
	cod_pais int,
	constraint fk_codpais foreign key (cod_pais) references pais(cod_pais)
);

create table if not exists municipio(
  	cod_mun int auto_increment primary key,
  	nomb_mun varchar(90),
  	cod_dept int,
	constraint fk_coddep foreign key (cod_dept) references departamento(cod_dept)
);

create table if not exists localizacion(
	cod_loc int auto_increment primary key,
  	lat_grad int,
	lat_min int,	
	lat_seg float,
	lon_grad int,
	lon_min int,	
	lon_seg float,
	altitud float,
	vereda varchar (30),
	cod_mun int,
	constraint fk_codmun foreign key (cod_mun) references municipio(cod_mun)
);

create table if not exists colectores(
  	cod_col int auto_increment primary key,
  	nomb_col varchar(20),
  	correo varchar(50)
);

create table if not exists animal_colectado(
	cod_ani int auto_increment primary key,
  	cod_col int,
	cod_sub int,
	cod_loc int,
	Estado varchar(15),
	metodo varchar(20),
	fecha date,
	nomb_ani varchar(30),
	peso float,
	habitat varchar (100),
	anotaciones varchar (100),
	sexo varchar (2),
	constraint fk_codsubes foreign key (cod_sub) references subespecie(cod_sub),
	constraint fk_codcolec foreign key (cod_col) references colectores(cod_col),
	constraint fk_codlocal foreign key (cod_loc) references localizacion(cod_loc)	
);

create table if not exists tejidos( 
	cod_teji  int auto_increment primary key,
  	cod_ani int,
  	nombre varchar (20),
  	tipo varchar (30),
  	descripcion varchar (50),
  	constraint fk_codanimales foreign key (cod_ani) references animal_colectado(cod_ani)
  	);

create table if not exists ornitologia(
	cod_ani int,
	cod_orn int auto_increment primary key,
  	edad varchar (20) ,
  	envergadura float ,
  	inf_repro varchar(50),
  	grasa float ,
  	cont_est varchar(50),
  	muda varchar (200),
  	part_blan varchar (200),
  	gonadas varchar (200),
  	oscificacion int,
  	constraint fk_codanimal foreign key (cod_ani) references animal_colectado(cod_ani)
  	);
  	
 create table if not exists aportes(
 codigo int auto_increment primary key,
 apor varchar(300),
 otro varchar(10)
 );

insert into pais (nomb_pais) values ('Colombia');

insert into departamento (nomb_dept,cod_pais) values ('Amazonas',1);
insert into departamento (nomb_dept,cod_pais) values ('Antioquia',1);
insert into departamento (nomb_dept,cod_pais) values ('Arauca',1);
insert into departamento (nomb_dept,cod_pais) values ('Atlantico',1);
insert into departamento (nomb_dept,cod_pais) values ('Bolivar',1);
insert into departamento (nomb_dept,cod_pais) values ('Boyaca',1);
insert into departamento (nomb_dept,cod_pais) values ('Caldas',1);
insert into departamento (nomb_dept,cod_pais) values ('Caqueta',1);
insert into departamento (nomb_dept,cod_pais) values ('Casanare',1);
insert into departamento (nomb_dept,cod_pais) values ('Cauca',1);
insert into departamento (nomb_dept,cod_pais) values ('Cesar',1);
insert into departamento (nomb_dept,cod_pais) values ('Choco',1);
insert into departamento (nomb_dept,cod_pais) values ('Cordoba',1);
insert into departamento (nomb_dept,cod_pais) values ('Cundinamarca',1);
insert into departamento (nomb_dept,cod_pais) values ('Guania',1);
insert into departamento (nomb_dept,cod_pais) values ('Guaviare',1);
insert into departamento (nomb_dept,cod_pais) values ('Huila',1);
insert into departamento (nomb_dept,cod_pais) values ('La guajira',1);
insert into departamento (nomb_dept,cod_pais) values ('Magdalena',1);
insert into departamento (nomb_dept,cod_pais) values ('Meta',1);
insert into departamento (nomb_dept,cod_pais) values ('Nariño',1);
insert into departamento (nomb_dept,cod_pais) values ('Norte de Santander',1);
insert into departamento (nomb_dept,cod_pais) values ('Putumayo',1);
insert into departamento (nomb_dept,cod_pais) values ('Quindio',1);
insert into departamento (nomb_dept,cod_pais) values ('Risaralda',1);
insert into departamento (nomb_dept,cod_pais) values ('San andres',1);
insert into departamento (nomb_dept,cod_pais) values ('Santander',1);
insert into departamento (nomb_dept,cod_pais) values ('Sucre',1);
insert into departamento (nomb_dept,cod_pais) values ('Tolima',1);
insert into departamento (nomb_dept,cod_pais) values ('Valle del cauca',1);
insert into departamento (nomb_dept,cod_pais) values ('Vaupes',1);
insert into departamento (nomb_dept,cod_pais) values ('Vichada',1);

INSERT INTO municipio (cod_mun, cod_dept, nomb_mun) VALUES
(1,1,'Leticia'),
(2,1,'Puerto Nariño'),
(3,2,'Abejorral'),
(4,2,'Abriaquí'),
(5,2,'Alejandria'),
(6,2,'Amagá'),
(7,2,'Amalfi'),
(8,2,'Andes'),
(9,2,'Angelópolis'),
(10,2,'Angostura'),
(11,2,'Anorí'),
(12,2,'Anzá'),
(13,2,'Apartadó'),
(14,2,'Arboletes'),
(15,2,'Argelia'),
(16,2,'Armenia'),
(17,2,'Barbosa'),
(18,2,'Bello'),
(19,2,'Belmira'),
(20,2,'Betania'),
(21,2,'Betulia'),
(22,2,'Bolívar'),
(23,2,'Briceño'),
(24,2,'Burítica'),
(25,2,'Caicedo'),
(26,2,'Caldas'),
(27,2,'Campamento'),
(28,2,'Caracolí'),
(29,2,'Caramanta'),
(30,2,'Carepa'),
(31,2,'Carmen de Viboral'),
(32,2,'Carolina'),
(33,2,'Caucasia'),
(34,2,'Cañasgordas'),
(35,2,'Chigorodó'),
(36,2,'Cisneros'),
(37,2,'Cocorná'),
(38,2,'Concepción'),
(39,2,'Concordia'),
(40,2,'Copacabana'),
(41,2,'Cáceres'),
(42,2,'Dabeiba'),
(43,2,'Don Matías'),
(44,2,'Ebéjico'),
(45,2,'El Bagre'),
(46,2,'Entrerríos'),
(47,2,'Envigado'),
(48,2,'Fredonia'),
(49,2,'Frontino'),
(50,2,'Giraldo'),
(51,2,'Girardota'),
(52,2,'Granada'),
(53,2,'Guadalupe'),
(54,2,'Guarne'),
(55,2,'Guatapé'),
(56,2,'Gómez Plata'),
(57,2,'Heliconia'),
(58,2,'Hispania'),
(59,2,'Itagüí'),
(60,2,'Ituango'),
(61,2,'Jardín'),
(62,2,'Jericó'),
(63,2,'La Ceja'),
(64,2,'La Estrella'),
(65,2,'La Pintada'),
(66,2,'La Unión'),
(67,2,'Liborina'),
(68,2,'Maceo'),
(69,2,'Marinilla'),
(70,2,'Medellín'),
(71,2,'Montebello'),
(72,2,'Murindó'),
(73,2,'Mutatá'),
(74,2,'Nariño'),
(75,2,'Nechí'),
(76,2,'Necoclí'),
(77,2,'Olaya'),
(78,2,'Peque'),
(79,2,'Peñol'),
(80,2,'Pueblorrico'),
(81,2,'Puerto Berrío'),
(82,2,'Puerto Nare'),
(83,2,'Puerto Triunfo'),
(84,2,'Remedios'),
(85,2,'Retiro'),
(86,2,'Ríonegro'),
(87,2,'Sabanalarga'),
(88,2,'Sabaneta'),
(89,2,'Salgar'),
(90,2,'San Andrés de Cuerquía'),
(91,2,'San Carlos'),
(92,2,'San Francisco'),
(93,2,'San Jerónimo'),
(94,2,'San José de Montaña'),
(95,2,'San Juan de Urabá'),
(96,2,'San Luís'),
(97,2,'San Pedro'),
(98,2,'San Pedro de Urabá'),
(99,2,'San Rafael'),
(100,2,'San Roque'),
(101,2,'San Vicente'),
(102,2,'Santa Bárbara'),
(103,2,'Santa Fé de Antioquia'),
(104,2,'Santa Rosa de Osos'),
(105,2,'Santo Domingo'),
(106,2,'Santuario'),
(107,2,'Segovia'),
(108,2,'Sonsón'),
(109,2,'Sopetrán'),
(110,2,'Tarazá'),
(111,2,'Tarso'),
(112,2,'Titiribí'),
(113,2,'Toledo'),
(114,2,'Turbo'),
(115,2,'Támesis'),
(116,2,'Uramita'),
(117,2,'Urrao'),
(118,2,'Valdivia'),
(119,2,'Valparaiso'),
(120,2,'Vegachí'),
(121,2,'Venecia'),
(122,2,'Vigía del Fuerte'),
(123,2,'Yalí'),
(124,2,'Yarumal'),
(125,2,'Yolombó'),
(126,2,'Yondó (Casabe)'),
(127,2,'Zaragoza'),
(128,3,'Arauca'),
(129,3,'Arauquita'),
(130,3,'Cravo Norte'),
(131,3,'Fortúl'),
(132,3,'Puerto Rondón'),
(133,3,'Saravena'),
(134,3,'Tame'),
(135,4,'Baranoa'),
(136,4,'Barranquilla'),
(137,4,'Campo de la Cruz'),
(138,4,'Candelaria'),
(139,4,'Galapa'),
(140,4,'Juan de Acosta'),
(141,4,'Luruaco'),
(142,4,'Malambo'),
(143,4,'Manatí'),
(144,4,'Palmar de Varela'),
(145,4,'Piojo'),
(146,4,'Polonuevo'),
(147,4,'Ponedera'),
(148,4,'Puerto Colombia'),
(149,4,'Repelón'),
(150,4,'Sabanagrande'),
(151,4,'Sabanalarga'),
(152,4,'Santa Lucía'),
(153,4,'Santo Tomás'),
(154,4,'Soledad'),
(155,4,'Suan'),
(156,4,'Tubará'),
(157,4,'Usiacuri'),
(158,5,'Achí'),
(159,5,'Altos del Rosario'),
(160,5,'Arenal'),
(161,5,'Arjona'),
(162,5,'Arroyohondo'),
(163,5,'Barranco de Loba'),
(164,5,'Calamar'),
(165,5,'Cantagallo'),
(166,5,'Cartagena'),
(167,5,'Cicuco'),
(168,5,'Clemencia'),
(169,5,'Córdoba'),
(170,5,'El Carmen de Bolívar'),
(171,5,'El Guamo'),
(172,5,'El Peñon'),
(173,5,'Hatillo de Loba'),
(174,5,'Magangué'),
(175,5,'Mahates'),
(176,5,'Margarita'),
(177,5,'María la Baja'),
(178,5,'Mompós'),
(179,5,'Montecristo'),
(180,5,'Morales'),
(181,5,'Norosí'),
(182,5,'Pinillos'),
(183,5,'Regidor'),
(184,5,'Río Viejo'),
(185,5,'San Cristobal'),
(186,5,'San Estanislao'),
(187,5,'San Fernando'),
(188,5,'San Jacinto'),
(189,5,'San Jacinto del Cauca'),
(190,5,'San Juan de Nepomuceno'),
(191,5,'San Martín de Loba'),
(192,5,'San Pablo'),
(193,5,'Santa Catalina'),
(194,5,'Santa Rosa '),
(195,5,'Santa Rosa del Sur'),
(196,5,'Simití'),
(197,5,'Soplaviento'),
(198,5,'Talaigua Nuevo'),
(199,5,'Tiquisio (Puerto Rico)'),
(200,5,'Turbaco'),
(201,5,'Turbaná'),
(202,5,'Villanueva'),
(203,5,'Zambrano'),
(204,6,'Almeida'),
(205,6,'Aquitania'),
(206,6,'Arcabuco'),
(207,6,'Belén'),
(208,6,'Berbeo'),
(209,6,'Beteitiva'),
(210,6,'Boavita'),
(211,6,'Boyacá'),
(212,6,'Briceño'),
(213,6,'Buenavista'),
(214,6,'Busbanza'),
(215,6,'Caldas'),
(216,6,'Campohermoso'),
(217,6,'Cerinza'),
(218,6,'Chinavita'),
(219,6,'Chiquinquirá'),
(220,6,'Chiscas'),
(221,6,'Chita'),
(222,6,'Chitaraque'),
(223,6,'Chivatá'),
(224,6,'Chíquiza'),
(225,6,'Chívor'),
(226,6,'Ciénaga'),
(227,6,'Coper'),
(228,6,'Corrales'),
(229,6,'Covarachía'),
(230,6,'Cubará'),
(231,6,'Cucaita'),
(232,6,'Cuitiva'),
(233,6,'Cómbita'),
(234,6,'Duitama'),
(235,6,'El Cocuy'),
(236,6,'El Espino'),
(237,6,'Firavitoba'),
(238,6,'Floresta'),
(239,6,'Gachantivá'),
(240,6,'Garagoa'),
(241,6,'Guacamayas'),
(242,6,'Guateque'),
(243,6,'Guayatá'),
(244,6,'Guicán'),
(245,6,'Gámeza'),
(246,6,'Izá'),
(247,6,'Jenesano'),
(248,6,'Jericó'),
(249,6,'La Capilla'),
(250,6,'La Uvita'),
(251,6,'La Victoria'),
(252,6,'Labranzagrande'),
(253,6,'Macanal'),
(254,6,'Maripí'),
(255,6,'Miraflores'),
(256,6,'Mongua'),
(257,6,'Monguí'),
(258,6,'Moniquirá'),
(259,6,'Motavita'),
(260,6,'Muzo'),
(261,6,'Nobsa'),
(262,6,'Nuevo Colón'),
(263,6,'Oicatá'),
(264,6,'Otanche'),
(265,6,'Pachavita'),
(266,6,'Paipa'),
(267,6,'Pajarito'),
(268,6,'Panqueba'),
(269,6,'Pauna'),
(270,6,'Paya'),
(271,6,'Paz de Río'),
(272,6,'Pesca'),
(273,6,'Pisva'),
(274,6,'Puerto Boyacá'),
(275,6,'Páez'),
(276,6,'Quipama'),
(277,6,'Ramiriquí'),
(278,6,'Rondón'),
(279,6,'Ráquira'),
(280,6,'Saboyá'),
(281,6,'Samacá'),
(282,6,'San Eduardo'),
(283,6,'San José de Pare'),
(284,6,'San Luís de Gaceno'),
(285,6,'San Mateo'),
(286,6,'San Miguel de Sema'),
(287,6,'San Pablo de Borbur'),
(288,6,'Santa María'),
(289,6,'Santa Rosa de Viterbo'),
(290,6,'Santa Sofía'),
(291,6,'Santana'),
(292,6,'Sativanorte'),
(293,6,'Sativasur'),
(294,6,'Siachoque'),
(295,6,'Soatá'),
(296,6,'Socha'),
(297,6,'Socotá'),
(298,6,'Sogamoso'),
(299,6,'Somondoco'),
(300,6,'Sora'),
(301,6,'Soracá'),
(302,6,'Sotaquirá'),
(303,6,'Susacón'),
(304,6,'Sutamarchán'),
(305,6,'Sutatenza'),
(306,6,'Sáchica'),
(307,6,'Tasco'),
(308,6,'Tenza'),
(309,6,'Tibaná'),
(310,6,'Tibasosa'),
(311,6,'Tinjacá'),
(312,6,'Tipacoque'),
(313,6,'Toca'),
(314,6,'Toguí'),
(315,6,'Topagá'),
(316,6,'Tota'),
(317,6,'Tunja'),
(318,6,'Tunungua'),
(319,6,'Turmequé'),
(320,6,'Tuta'),
(321,6,'Tutasá'),
(322,6,'Ventaquemada'),
(323,6,'Villa de Leiva'),
(324,6,'Viracachá'),
(325,6,'Zetaquirá'),
(326,6,'Úmbita'),
(327,7,'Aguadas'),
(328,7,'Anserma'),
(329,7,'Aranzazu'),
(330,7,'Belalcázar'),
(331,7,'Chinchiná'),
(332,7,'Filadelfia'),
(333,7,'La Dorada'),
(334,7,'La Merced'),
(335,7,'La Victoria'),
(336,7,'Manizales'),
(337,7,'Manzanares'),
(338,7,'Marmato'),
(339,7,'Marquetalia'),
(340,7,'Marulanda'),
(341,7,'Neira'),
(342,7,'Norcasia'),
(343,7,'Palestina'),
(344,7,'Pensilvania'),
(345,7,'Pácora'),
(346,7,'Risaralda'),
(347,7,'Río Sucio'),
(348,7,'Salamina'),
(349,7,'Samaná'),
(350,7,'San José'),
(351,7,'Supía'),
(352,7,'Villamaría'),
(353,7,'Viterbo'),
(354,8,'Albania'),
(355,8,'Belén de los Andaquíes'),
(356,8,'Cartagena del Chairá'),
(357,8,'Curillo'),
(358,8,'El Doncello'),
(359,8,'El Paujil'),
(360,8,'Florencia'),
(361,8,'La Montañita'),
(362,8,'Milán'),
(363,8,'Morelia'),
(364,8,'Puerto Rico'),
(365,8,'San José del Fragua'),
(366,8,'San Vicente del Caguán'),
(367,8,'Solano'),
(368,8,'Solita'),
(369,8,'Valparaiso'),
(370,9,'Aguazul'),
(371,9,'Chámeza'),
(372,9,'Hato Corozal'),
(373,9,'La Salina'),
(374,9,'Maní'),
(375,9,'Monterrey'),
(376,9,'Nunchía'),
(377,9,'Orocué'),
(378,9,'Paz de Ariporo'),
(379,9,'Pore'),
(380,9,'Recetor'),
(381,9,'Sabanalarga'),
(382,9,'San Luís de Palenque'),
(383,9,'Sácama'),
(384,9,'Tauramena'),
(385,9,'Trinidad'),
(386,9,'Támara'),
(387,9,'Villanueva'),
(388,9,'Yopal'),
(389,10,'Almaguer'),
(390,10,'Argelia'),
(391,10,'Balboa'),
(392,10,'Bolívar'),
(393,10,'Buenos Aires'),
(394,10,'Cajibío'),
(395,10,'Caldono'),
(396,10,'Caloto'),
(397,10,'Corinto'),
(398,10,'El Tambo'),
(399,10,'Florencia'),
(400,10,'Guachené'),
(401,10,'Guapí'),
(402,10,'Inzá'),
(403,10,'Jambaló'),
(404,10,'La Sierra'),
(405,10,'La Vega'),
(406,10,'López (Micay)'),
(407,10,'Mercaderes'),
(408,10,'Miranda'),
(409,10,'Morales'),
(410,10,'Padilla'),
(411,10,'Patía (El Bordo)'),
(412,10,'Piamonte'),
(413,10,'Piendamó'),
(414,10,'Popayán'),
(415,10,'Puerto Tejada'),
(416,10,'Puracé (Coconuco)'),
(417,10,'Páez (Belalcazar)'),
(418,10,'Rosas'),
(419,10,'San Sebastián'),
(420,10,'Santa Rosa'),
(421,10,'Santander de Quilichao'),
(422,10,'Silvia'),
(423,10,'Sotara (Paispamba)'),
(424,10,'Sucre'),
(425,10,'Suárez'),
(426,10,'Timbiquí'),
(427,10,'Timbío'),
(428,10,'Toribío'),
(429,10,'Totoró'),
(430,10,'Villa Rica'),
(431,11,'Aguachica'),
(432,11,'Agustín Codazzi'),
(433,11,'Astrea'),
(434,11,'Becerríl'),
(435,11,'Bosconia'),
(436,11,'Chimichagua'),
(437,11,'Chiriguaná'),
(438,11,'Curumaní'),
(439,11,'El Copey'),
(440,11,'El Paso'),
(441,11,'Gamarra'),
(442,11,'Gonzalez'),
(443,11,'La Gloria'),
(444,11,'La Jagua de Ibirico'),
(445,11,'La Paz (Robles)'),
(446,11,'Manaure Balcón del Cesar'),
(447,11,'Pailitas'),
(448,11,'Pelaya'),
(449,11,'Pueblo Bello'),
(450,11,'Río de oro'),
(451,11,'San Alberto'),
(452,11,'San Diego'),
(453,11,'San Martín'),
(454,11,'Tamalameque'),
(455,11,'Valledupar'),
(456,12,'Acandí'),
(457,12,'Alto Baudó (Pie de Pato)'),
(458,12,'Atrato (Yuto)'),
(459,12,'Bagadó'),
(460,12,'Bahía Solano (Mútis)'),
(461,12,'Bajo Baudó (Pizarro)'),
(462,12,'Belén de Bajirá'),
(463,12,'Bojayá (Bellavista)'),
(464,12,'Cantón de San Pablo'),
(465,12,'Carmen del Darién (CURBARADÓ)'),
(466,12,'Condoto'),
(467,12,'Cértegui'),
(468,12,'El Carmen de Atrato'),
(469,12,'Istmina'),
(470,12,'Juradó'),
(471,12,'Lloró'),
(472,12,'Medio Atrato'),
(473,12,'Medio Baudó'),
(474,12,'Medio San Juan (ANDAGOYA)'),
(475,12,'Novita'),
(476,12,'Nuquí'),
(477,12,'Quibdó'),
(478,12,'Río Iró'),
(479,12,'Río Quito'),
(480,12,'Ríosucio'),
(481,12,'San José del Palmar'),
(482,12,'Santa Genoveva de Docorodó'),
(483,12,'Sipí'),
(484,12,'Tadó'),
(485,12,'Unguía'),
(486,12,'Unión Panamericana (ÁNIMAS)'),
(487,13,'Ayapel'),
(488,13,'Buenavista'),
(489,13,'Canalete'),
(490,13,'Cereté'),
(491,13,'Chimá'),
(492,13,'Chinú'),
(493,13,'Ciénaga de Oro'),
(494,13,'Cotorra'),
(495,13,'La Apartada y La Frontera'),
(496,13,'Lorica'),
(497,13,'Los Córdobas'),
(498,13,'Momil'),
(499,13,'Montelíbano'),
(500,13,'Monteria'),
(501,13,'Moñitos'),
(502,13,'Planeta Rica'),
(503,13,'Pueblo Nuevo'),
(504,13,'Puerto Escondido'),
(505,13,'Puerto Libertador'),
(506,13,'Purísima'),
(507,13,'Sahagún'),
(508,13,'San Andrés Sotavento'),
(509,13,'San Antero'),
(510,13,'San Bernardo del Viento'),
(511,13,'San Carlos'),
(512,13,'San José de Uré'),
(513,13,'San Pelayo'),
(514,13,'Tierralta'),
(515,13,'Tuchín'),
(516,13,'Valencia'),
(517,14,'Agua de Dios'),
(518,14,'Albán'),
(519,14,'Anapoima'),
(520,14,'Anolaima'),
(521,14,'Apulo'),
(522,14,'Arbeláez'),
(523,14,'Beltrán'),
(524,14,'Bituima'),
(525,14,'Bogotá D.C.'),
(526,14,'Bojacá'),
(527,14,'Cabrera'),
(528,14,'Cachipay'),
(529,14,'Cajicá'),
(530,14,'Caparrapí'),
(531,14,'Carmen de Carupa'),
(532,14,'Chaguaní'),
(533,14,'Chipaque'),
(534,14,'Choachí'),
(535,14,'Chocontá'),
(536,14,'Chía'),
(537,14,'Cogua'),
(538,14,'Cota'),
(539,14,'Cucunubá'),
(540,14,'Cáqueza'),
(541,14,'El Colegio'),
(542,14,'El Peñón'),
(543,14,'El Rosal'),
(544,14,'Facatativá'),
(545,14,'Fosca'),
(546,14,'Funza'),
(547,14,'Fusagasugá'),
(548,14,'Fómeque'),
(549,14,'Fúquene'),
(550,14,'Gachalá'),
(551,14,'Gachancipá'),
(552,14,'Gachetá'),
(553,14,'Gama'),
(554,14,'Girardot'),
(555,14,'Granada'),
(556,14,'Guachetá'),
(557,14,'Guaduas'),
(558,14,'Guasca'),
(559,14,'Guataquí'),
(560,14,'Guatavita'),
(561,14,'Guayabal de Siquima'),
(562,14,'Guayabetal'),
(563,14,'Gutiérrez'),
(564,14,'Jerusalén'),
(565,14,'Junín'),
(566,14,'La Calera'),
(567,14,'La Mesa'),
(568,14,'La Palma'),
(569,14,'La Peña'),
(570,14,'La Vega'),
(571,14,'Lenguazaque'),
(572,14,'Machetá'),
(573,14,'Madrid'),
(574,14,'Manta'),
(575,14,'Medina'),
(576,14,'Mosquera'),
(577,14,'Nariño'),
(578,14,'Nemocón'),
(579,14,'Nilo'),
(580,14,'Nimaima'),
(581,14,'Nocaima'),
(582,14,'Pacho'),
(583,14,'Paime'),
(584,14,'Pandi'),
(585,14,'Paratebueno'),
(586,14,'Pasca'),
(587,14,'Puerto Salgar'),
(588,14,'Pulí'),
(589,14,'Quebradanegra'),
(590,14,'Quetame'),
(591,14,'Quipile'),
(592,14,'Ricaurte'),
(593,14,'San Antonio de Tequendama'),
(594,14,'San Bernardo'),
(595,14,'San Cayetano'),
(596,14,'San Francisco'),
(597,14,'San Juan de Río Seco'),
(598,14,'Sasaima'),
(599,14,'Sesquilé'),
(600,14,'Sibaté'),
(601,14,'Silvania'),
(602,14,'Simijaca'),
(603,14,'Soacha'),
(604,14,'Sopó'),
(605,14,'Subachoque'),
(606,14,'Suesca'),
(607,14,'Supatá'),
(608,14,'Susa'),
(609,14,'Sutatausa'),
(610,14,'Tabio'),
(611,14,'Tausa'),
(612,14,'Tena'),
(613,14,'Tenjo'),
(614,14,'Tibacuy'),
(615,14,'Tibirita'),
(616,14,'Tocaima'),
(617,14,'Tocancipá'),
(618,14,'Topaipí'),
(619,14,'Ubalá'),
(620,14,'Ubaque'),
(621,14,'Ubaté'),
(622,14,'Une'),
(623,14,'Venecia (Ospina Pérez)'),
(624,14,'Vergara'),
(625,14,'Viani'),
(626,14,'Villagómez'),
(627,14,'Villapinzón'),
(628,14,'Villeta'),
(629,14,'Viotá'),
(630,14,'Yacopí'),
(631,14,'Zipacón'),
(632,14,'Zipaquirá'),
(633,14,'Útica'),
(634,15,'Inírida'),
(635,16,'Calamar'),
(636,16,'El Retorno'),
(637,16,'Miraflores'),
(638,16,'San José del Guaviare'),
(639,17,'Acevedo'),
(640,17,'Agrado'),
(641,17,'Aipe'),
(642,17,'Algeciras'),
(643,17,'Altamira'),
(644,17,'Baraya'),
(645,17,'Campoalegre'),
(646,17,'Colombia'),
(647,17,'Elías'),
(648,17,'Garzón'),
(649,17,'Gigante'),
(650,17,'Guadalupe'),
(651,17,'Hobo'),
(652,17,'Isnos'),
(653,17,'La Argentina'),
(654,17,'La Plata'),
(655,17,'Neiva'),
(656,17,'Nátaga'),
(657,17,'Oporapa'),
(658,17,'Paicol'),
(659,17,'Palermo'),
(660,17,'Palestina'),
(661,17,'Pital'),
(662,17,'Pitalito'),
(663,17,'Rivera'),
(664,17,'Saladoblanco'),
(665,17,'San Agustín'),
(666,17,'Santa María'),
(667,17,'Suaza'),
(668,17,'Tarqui'),
(669,17,'Tello'),
(670,17,'Teruel'),
(671,17,'Tesalia'),
(672,17,'Timaná'),
(673,17,'Villavieja'),
(674,17,'Yaguará'),
(675,17,'Íquira'),
(676,18,'Albania'),
(677,18,'Barrancas'),
(678,18,'Dibulla'),
(679,18,'Distracción'),
(680,18,'El Molino'),
(681,18,'Fonseca'),
(682,18,'Hatonuevo'),
(683,18,'La Jagua del Pilar'),
(684,18,'Maicao'),
(685,18,'Manaure'),
(686,18,'Riohacha'),
(687,18,'San Juan del Cesar'),
(688,18,'Uribia'),
(689,18,'Urumita'),
(690,18,'Villanueva'),
(691,19,'Algarrobo'),
(692,19,'Aracataca'),
(693,19,'Ariguaní (El Difícil)'),
(694,19,'Cerro San Antonio'),
(695,19,'Chivolo'),
(696,19,'Ciénaga'),
(697,19,'Concordia'),
(698,19,'El Banco'),
(699,19,'El Piñon'),
(700,19,'El Retén'),
(701,19,'Fundación'),
(702,19,'Guamal'),
(703,19,'Nueva Granada'),
(704,19,'Pedraza'),
(705,19,'Pijiño'),
(706,19,'Pivijay'),
(707,19,'Plato'),
(708,19,'Puebloviejo'),
(709,19,'Remolino'),
(710,19,'Sabanas de San Angel (SAN ANGEL)'),
(711,19,'Salamina'),
(712,19,'San Sebastián de Buenavista'),
(713,19,'San Zenón'),
(714,19,'Santa Ana'),
(715,19,'Santa Bárbara de Pinto'),
(716,19,'Santa Marta'),
(717,19,'Sitionuevo'),
(718,19,'Tenerife'),
(719,19,'Zapayán (PUNTA DE PIEDRAS)'),
(720,19,'Zona Bananera (PRADO - SEVILLA)'),
(721,20,'Acacías'),
(722,20,'Barranca de Upía'),
(723,20,'Cabuyaro'),
(724,20,'Castilla la Nueva'),
(725,20,'Cubarral'),
(726,20,'Cumaral'),
(727,20,'El Calvario'),
(728,20,'El Castillo'),
(729,20,'El Dorado'),
(730,20,'Fuente de Oro'),
(731,20,'Granada'),
(732,20,'Guamal'),
(733,20,'La Macarena'),
(734,20,'Lejanías'),
(735,20,'Mapiripan'),
(736,20,'Mesetas'),
(737,20,'Puerto Concordia'),
(738,20,'Puerto Gaitán'),
(739,20,'Puerto Lleras'),
(740,20,'Puerto López'),
(741,20,'Puerto Rico'),
(742,20,'Restrepo'),
(743,20,'San Carlos de Guaroa'),
(744,20,'San Juan de Arama'),
(745,20,'San Juanito'),
(746,20,'San Martín'),
(747,20,'Uribe'),
(748,20,'Villavicencio'),
(749,20,'Vista Hermosa'),
(750,21,'Albán (San José)'),
(751,21,'Aldana'),
(752,21,'Ancuya'),
(753,21,'Arboleda (Berruecos)'),
(754,21,'Barbacoas'),
(755,21,'Belén'),
(756,21,'Buesaco'),
(757,21,'Chachaguí'),
(758,21,'Colón (Génova)'),
(759,21,'Consaca'),
(760,21,'Contadero'),
(761,21,'Cuaspud (Carlosama)'),
(762,21,'Cumbal'),
(763,21,'Cumbitara'),
(764,21,'Córdoba'),
(765,21,'El Charco'),
(766,21,'El Peñol'),
(767,21,'El Rosario'),
(768,21,'El Tablón de Gómez'),
(769,21,'El Tambo'),
(770,21,'Francisco Pizarro'),
(771,21,'Funes'),
(772,21,'Guachavés'),
(773,21,'Guachucal'),
(774,21,'Guaitarilla'),
(775,21,'Gualmatán'),
(776,21,'Iles'),
(777,21,'Imúes'),
(778,21,'Ipiales'),
(779,21,'La Cruz'),
(780,21,'La Florida'),
(781,21,'La Llanada'),
(782,21,'La Tola'),
(783,21,'La Unión'),
(784,21,'Leiva'),
(785,21,'Linares'),
(786,21,'Magüi (Payán)'),
(787,21,'Mallama (Piedrancha)'),
(788,21,'Mosquera'),
(789,21,'Nariño'),
(790,21,'Olaya Herrera'),
(791,21,'Ospina'),
(792,21,'Policarpa'),
(793,21,'Potosí'),
(794,21,'Providencia'),
(795,21,'Puerres'),
(796,21,'Pupiales'),
(797,21,'Ricaurte'),
(798,21,'Roberto Payán (San José)'),
(799,21,'Samaniego'),
(800,21,'San Bernardo'),
(801,21,'San Juan de Pasto'),
(802,21,'San Lorenzo'),
(803,21,'San Pablo'),
(804,21,'San Pedro de Cartago'),
(805,21,'Sandoná'),
(806,21,'Santa Bárbara (Iscuandé)'),
(807,21,'Sapuyes'),
(808,21,'Sotomayor (Los Andes)'),
(809,21,'Taminango'),
(810,21,'Tangua'),
(811,21,'Tumaco'),
(812,21,'Túquerres'),
(813,21,'Yacuanquer'),
(814,22,'Arboledas'),
(815,22,'Bochalema'),
(816,22,'Bucarasica'),
(817,22,'Chinácota'),
(818,22,'Chitagá'),
(819,22,'Convención'),
(820,22,'Cucutilla'),
(821,22,'Cáchira'),
(822,22,'Cácota'),
(823,22,'Cúcuta'),
(824,22,'Durania'),
(825,22,'El Carmen'),
(826,22,'El Tarra'),
(827,22,'El Zulia'),
(828,22,'Gramalote'),
(829,22,'Hacarí'),
(830,22,'Herrán'),
(831,22,'La Esperanza'),
(832,22,'La Playa'),
(833,22,'Labateca'),
(834,22,'Los Patios'),
(835,22,'Lourdes'),
(836,22,'Mutiscua'),
(837,22,'Ocaña'),
(838,22,'Pamplona'),
(839,22,'Pamplonita'),
(840,22,'Puerto Santander'),
(841,22,'Ragonvalia'),
(842,22,'Salazar'),
(843,22,'San Calixto'),
(844,22,'San Cayetano'),
(845,22,'Santiago'),
(846,22,'Sardinata'),
(847,22,'Silos'),
(848,22,'Teorama'),
(849,22,'Tibú'),
(850,22,'Toledo'),
(851,22,'Villa Caro'),
(852,22,'Villa del Rosario'),
(853,22,'Ábrego'),
(854,23,'Colón'),
(855,23,'Mocoa'),
(856,23,'Orito'),
(857,23,'Puerto Asís'),
(858,23,'Puerto Caicedo'),
(859,23,'Puerto Guzmán'),
(860,23,'Puerto Leguízamo'),
(861,23,'San Francisco'),
(862,23,'San Miguel'),
(863,23,'Santiago'),
(864,23,'Sibundoy'),
(865,23,'Valle del Guamuez'),
(866,23,'Villagarzón'),
(867,24,'Armenia'),
(868,24,'Buenavista'),
(869,24,'Calarcá'),
(870,24,'Circasia'),
(871,24,'Cordobá'),
(872,24,'Filandia'),
(873,24,'Génova'),
(874,24,'La Tebaida'),
(875,24,'Montenegro'),
(876,24,'Pijao'),
(877,24,'Quimbaya'),
(878,24,'Salento'),
(879,25,'Apía'),
(880,25,'Balboa'),
(881,25,'Belén de Umbría'),
(882,25,'Dos Quebradas'),
(883,25,'Guática'),
(884,25,'La Celia'),
(885,25,'La Virginia'),
(886,25,'Marsella'),
(887,25,'Mistrató'),
(888,25,'Pereira'),
(889,25,'Pueblo Rico'),
(890,25,'Quinchía'),
(891,25,'Santa Rosa de Cabal'),
(892,25,'Santuario'),
(893,26,'Providencia'),
(894,27,'Aguada'),
(895,27,'Albania'),
(896,27,'Aratoca'),
(897,27,'Barbosa'),
(898,27,'Barichara'),
(899,27,'Barrancabermeja'),
(900,27,'Betulia'),
(901,27,'Bolívar'),
(902,27,'Bucaramanga'),
(903,27,'Cabrera'),
(904,27,'California'),
(905,27,'Capitanejo'),
(906,27,'Carcasí'),
(907,27,'Cepita'),
(908,27,'Cerrito'),
(909,27,'Charalá'),
(910,27,'Charta'),
(911,27,'Chima'),
(912,27,'Chipatá'),
(913,27,'Cimitarra'),
(914,27,'Concepción'),
(915,27,'Confines'),
(916,27,'Contratación'),
(917,27,'Coromoro'),
(918,27,'Curití'),
(919,27,'El Carmen'),
(920,27,'El Guacamayo'),
(921,27,'El Peñon'),
(922,27,'El Playón'),
(923,27,'Encino'),
(924,27,'Enciso'),
(925,27,'Floridablanca'),
(926,27,'Florián'),
(927,27,'Galán'),
(928,27,'Girón'),
(929,27,'Guaca'),
(930,27,'Guadalupe'),
(931,27,'Guapota'),
(932,27,'Guavatá'),
(933,27,'Guepsa'),
(934,27,'Gámbita'),
(935,27,'Hato'),
(936,27,'Jesús María'),
(937,27,'Jordán'),
(938,27,'La Belleza'),
(939,27,'La Paz'),
(940,27,'Landázuri'),
(941,27,'Lebrija'),
(942,27,'Los Santos'),
(943,27,'Macaravita'),
(944,27,'Matanza'),
(945,27,'Mogotes'),
(946,27,'Molagavita'),
(947,27,'Málaga'),
(948,27,'Ocamonte'),
(949,27,'Oiba'),
(950,27,'Onzaga'),
(951,27,'Palmar'),
(952,27,'Palmas del Socorro'),
(953,27,'Pie de Cuesta'),
(954,27,'Pinchote'),
(955,27,'Puente Nacional'),
(956,27,'Puerto Parra'),
(957,27,'Puerto Wilches'),
(958,27,'Páramo'),
(959,27,'Rio Negro'),
(960,27,'Sabana de Torres'),
(961,27,'San Andrés'),
(962,27,'San Benito'),
(963,27,'San Gíl'),
(964,27,'San Joaquín'),
(965,27,'San José de Miranda'),
(966,27,'San Miguel'),
(967,27,'San Vicente del Chucurí'),
(968,27,'Santa Bárbara'),
(969,27,'Santa Helena del Opón'),
(970,27,'Simacota'),
(971,27,'Socorro'),
(972,27,'Suaita'),
(973,27,'Sucre'),
(974,27,'Suratá'),
(975,27,'Tona'),
(976,27,'Valle de San José'),
(977,27,'Vetas'),
(978,27,'Villanueva'),
(979,27,'Vélez'),
(980,27,'Zapatoca'),
(981,28,'Buenavista'),
(982,28,'Caimito'),
(983,28,'Chalán'),
(984,28,'Colosó (Ricaurte)'),
(985,28,'Corozal'),
(986,28,'Coveñas'),
(987,28,'El Roble'),
(988,28,'Galeras (Nueva Granada)'),
(989,28,'Guaranda'),
(990,28,'La Unión'),
(991,28,'Los Palmitos'),
(992,28,'Majagual'),
(993,28,'Morroa'),
(994,28,'Ovejas'),
(995,28,'Palmito'),
(996,28,'Sampués'),
(997,28,'San Benito Abad'),
(998,28,'San Juan de Betulia'),
(999,28,'San Marcos'),
(1000,28,'San Onofre'),
(1001,28,'San Pedro'),
(1002,28,'Sincelejo'),
(1003,28,'Sincé'),
(1004,28,'Sucre'),
(1005,28,'Tolú'),
(1006,28,'Tolú Viejo'),
(1007,29,'Alpujarra'),
(1008,29,'Alvarado'),
(1009,29,'Ambalema'),
(1010,29,'Anzoátegui'),
(1011,29,'Armero (Guayabal)'),
(1012,29,'Ataco'),
(1013,29,'Cajamarca'),
(1014,29,'Carmen de Apicalá'),
(1015,29,'Casabianca'),
(1016,29,'Chaparral'),
(1017,29,'Coello'),
(1018,29,'Coyaima'),
(1019,29,'Cunday'),
(1020,29,'Dolores'),
(1021,29,'Espinal'),
(1022,29,'Falan'),
(1023,29,'Flandes'),
(1024,29,'Fresno'),
(1025,29,'Guamo'),
(1026,29,'Herveo'),
(1027,29,'Honda'),
(1028,29,'Ibagué'),
(1029,29,'Icononzo'),
(1030,29,'Lérida'),
(1031,29,'Líbano'),
(1032,29,'Mariquita'),
(1033,29,'Melgar'),
(1034,29,'Murillo'),
(1035,29,'Natagaima'),
(1036,29,'Ortega'),
(1037,29,'Palocabildo'),
(1038,29,'Piedras'),
(1039,29,'Planadas'),
(1040,29,'Prado'),
(1041,29,'Purificación'),
(1042,29,'Rioblanco'),
(1043,29,'Roncesvalles'),
(1044,29,'Rovira'),
(1045,29,'Saldaña'),
(1046,29,'San Antonio'),
(1047,29,'San Luis'),
(1048,29,'Santa Isabel'),
(1049,29,'Suárez'),
(1050,29,'Valle de San Juan'),
(1051,29,'Venadillo'),
(1052,29,'Villahermosa'),
(1053,29,'Villarrica'),
(1054,30,'Alcalá'),
(1055,30,'Andalucía'),
(1056,30,'Ansermanuevo'),
(1057,30,'Argelia'),
(1058,30,'Bolívar'),
(1059,30,'Buenaventura'),
(1060,30,'Buga'),
(1061,30,'Bugalagrande'),
(1062,30,'Caicedonia'),
(1063,30,'Calima (Darién)'),
(1064,30,'Calí'),
(1065,30,'Candelaria'),
(1066,30,'Cartago'),
(1067,30,'Dagua'),
(1068,30,'El Cairo'),
(1069,30,'El Cerrito'),
(1070,30,'El Dovio'),
(1071,30,'El Águila'),
(1072,30,'Florida'),
(1073,30,'Ginebra'),
(1074,30,'Guacarí'),
(1075,30,'Jamundí'),
(1076,30,'La Cumbre'),
(1077,30,'La Unión'),
(1078,30,'La Victoria'),
(1079,30,'Obando'),
(1080,30,'Palmira'),
(1081,30,'Pradera'),
(1082,30,'Restrepo'),
(1083,30,'Riofrío'),
(1084,30,'Roldanillo'),
(1085,30,'San Pedro'),
(1086,30,'Sevilla'),
(1087,30,'Toro'),
(1088,30,'Trujillo'),
(1089,30,'Tulúa'),
(1090,30,'Ulloa'),
(1091,30,'Versalles'),
(1092,30,'Vijes'),
(1093,30,'Yotoco'),
(1094,30,'Yumbo'),
(1095,30,'Zarzal'),
(1096,31,'Carurú'),
(1097,31,'Mitú'),
(1098,31,'Taraira'),
(1099,32,'Cumaribo'),
(1100,32,'La Primavera'),
(1101,32,'Puerto Carreño'),
(1102,32,'Santa Rosalía');


insert into localizacion (lat_grad,lat_min,lat_seg,lon_grad,lon_min,lon_seg,altitud,vereda,cod_mun) values (04,19,21.5,    -72,02,30.1,    215, 'alto manacacias',738);
insert into localizacion (lat_grad,lat_min,lat_seg,lon_grad,lon_min,lon_seg,altitud,vereda,cod_mun) values (04,04,20.5,    -73,34,53.32,  200, 'cocuy-unillanos',748);
insert into localizacion (lat_grad,lat_min,lat_seg,lon_grad,lon_min,lon_seg,altitud,vereda,cod_mun) values (04,08,15.8,    -73,40,31.63,  200,'vereda el carmen',748);
insert into localizacion (lat_grad,lat_min,lat_seg,lon_grad,lon_min,lon_seg,altitud,vereda,cod_mun) values (06,11,14.2,    -75,38,27.321,215,'vereda la verde',70);
insert into localizacion (lat_grad,lat_min,lat_seg,lon_grad,lon_min,lon_seg,altitud,vereda,cod_mun) values (10,14,12.07,    -74,16,36.32,215, 'corregimiento monterrubio',710);


insert into coleccion (nomb_comun,nomb_cientifico,carac_col) values ('Aves','Ornitologica',' La Colección Ornitológica del Museo de Historia Natural de la Universidad de los llanos.MHNU-O');
insert into coleccion (nomb_comun,nomb_cientifico,carac_col) values ('Peces','Ictiologica',' La Colección Ictiógica del Museo de Historia Natural de la Universidad de los llanos.MHNU-I');
insert into coleccion (nomb_comun,nomb_cientifico,carac_col) values ('Mamiferos','Mustozoologica',' La Colección mastozoológica del Museo de Historia Natural de la Universidad de los llanos.MHNU-M');
insert into coleccion (nomb_comun,nomb_cientifico,carac_col) values ('Reptiles y anfibios','Herpetologia',' La Colección Herpetológica del Museo de Historia Natural de la Universidad de los llanos.MHNU-H');
insert into coleccion (nomb_comun,nomb_cientifico,carac_col) values ('Tejidos','Tejidos',' La Colección de tejidos del Museo de Historia Natural de la Universidad de los llanos.MHNU-T');
insert into coleccion (nomb_comun,nomb_cientifico,carac_col) values ('__','Invertebrados',' La Colección de invertebrados del Museo de Historia Natural de la Universidad de los llanos.MHNU-IN');

insert into usuarios (nomb_usuar,clave,tipo_us) values ('EstebanRamos','nikol','ADMINISTRADOR');
insert into usuarios (nomb_usuar,clave,tipo_us) values ('DanielMuñoz','juliana','ADMINISTRADOR');
insert into usuarios (nomb_usuar,clave,tipo_us) values ('SebastianLoaiza','sara','INVITADO');
insert into usuarios (nomb_usuar,clave,tipo_us) values ('Santiagolozada','natalie','INVITADO');

insert into clase (nomb_cla,cod_col) values ('aves',1);

insert into orden  values (1,'APODIFORMES',' caracterizadas por el pequeño tamaño de las patas, lo que da nombre al orden',1);
insert into orden  values (2,'CAPRIMULGIFORMES','  aves nocturnas con gran facilidad para camuflarse durante el día',1);
insert into orden  values (3,'Struthioniformes','grupo parafilético de aves paleognatas, no voladoras, algunas de ellas ya desaparecidas',1);
insert into orden  values (4,'Piciformes','las piciformes son insectívoras, aunque los tucanes se alimentan principalmente de frutas,',1);
insert into orden  values (5,'Casuariiformes','grandes aves corredoras propias de Australia y Nueva Guinea.,',1);
insert into orden  values (6,'PODICIPEDIFORMES ',' Este orden es integrado por aves acuáticas, a las cuales, entre otros nombres, se les llaman somormujos y zampullines',1);
insert into orden  values (7,'Passeriformes ',' Orden representado con mayor número de especies en las aves, aquí se agrupan todos los pájaros. ',1);
insert into orden  values (8,'Pelecaniformes ',' Orden integrado por aves acuáticas, a las cuales, entre otros nombres, se les llaman totipalmados',1);
insert into orden  values (9,'Strigiformes ',' Orden donde se estudian las aves rapaces nocturnas. Formado por dos familias',1);


insert into familia  values (1,'Apodidae',1);	
insert into familia  values (2,'Hemiprocnidae',1);	
insert into familia  values (3,'Trochilidae',1);	
insert into familia  values (4,'Caprimulgidae',2);
insert into familia  values (5,'Steatornithidae',2);
insert into familia  values (6,'Struthionidae',3);
insert into familia  values (7,'Picidae',3);
insert into familia  values (8,'reidhae',3);
insert into familia  values (9,'Casuariidae',3);
insert into familia  values (10,'Picidae',4);
insert into familia  values (11,'Capitonidae',4);
insert into familia  values (12,'Casuariidae',5);
insert into familia  values (13,'Dromaiidae',5);
insert into familia  values (14,'Podicipedidae',6);
insert into familia  values (15,'Bombycillidae',7);
insert into familia  values (16,'Cardinalidae',7);
insert into familia  values (17,'Anhingidae',8);
insert into familia  values (18,'Tytonidae',9);




insert into genero  values (1,'Aerodramus',1);
insert into genero  values (2,'Aeronautes',1);
insert into genero  values (3,'Nyctiprogne',1);
insert into genero  values (4,'Amazilia',3);
insert into genero  values (5,'Lurocalis',4);
insert into genero  values (6,'Nyctiphrynus',4);
insert into genero  values (7,'Struthio',6);
insert into genero  values (8,'Veniliornis',7);
insert into genero  values (9,'Jynx',10);
insert into genero  values (10,'Picumnus',10);
insert into genero  values (11,'Trachyphonus',11);
insert into genero  values (12,'Gymnobucco',11);
insert into genero  values (13,'Stactolaema',11);







insert into especies values (1,'Aerodramus elaphrus',1);
insert into especies  values (2,'Fimbriata',4);
insert into especies  values (3,'lactea',4);
insert into especies  values (4,'Struthio camelus',7);
insert into especies  values (5,'passerinus',8);
insert into especies  values (6,'Trachyphonus purpuratus',11);
insert into especies  values (7,'Trachyphonus vaillantii',11);
insert into especies  values (8,'Trachyphonus margaritatus',11);
insert into especies  values (9,'Trachyphonus erythrocephalus',11);
insert into especies  values (10,'Trachyphonus darnaudii',11);
insert into especies  values (11,'Gymnobucco calvus',12);
insert into especies  values (12,'Gymnobucco peli',12);
insert into especies  values (13,'Gymnobucco sladeni',12);
insert into especies  values (14,'Stactolaema leucotis',13);
insert into especies  values (15,'Stactolaema anchietae',13);
insert into especies  values (16,'Stactolaema whytii',13);



insert into subespecie  values (1,'Struthio camelus camelus',4);
insert into subespecie  values (2,'Struthio camelus syriacus',4);
insert into subespecie  values (3,'Struthio camelus massaicus',4);
insert into subespecie  values (4,'Stactolaema whytii peli',5);
insert into subespecie  values (5,'Aerodramus francicus',1);
insert into subespecie  values (6,'Gymnobucco sladeni alto',6);
insert into subespecie  values (7,'Stactolaema anchiet',7);
insert into subespecie  values (8,'Stactolaema anchietae',8);
insert into subespecie  values (9,'Trachyphonus margaritatus',9);
insert into subespecie  values (10,'lactea',10);
insert into subespecie  values (11,'Stactolaema leucotis',11);
insert into subespecie  values (12,'Stactolaema',2);
insert into subespecie  values (13,'passerinus',3);
insert into subespecie  values (14,'Aerodramus',13);
insert into subespecie  values (15,'nulo',14);
insert into subespecie  values (16,'Trachyphonus margaritates',15);




insert into colectores  values (1,'A. Contreras','');
insert into colectores  values (2,'F. Aponte','');
insert into colectores  values (3,'J.E. Avendaño','');
insert into colectores  values (4,'J.J. Amaya','');
insert into colectores  values (5,'K.E. Mendez','');
insert into colectores  values (6,'R. Valencia','');
insert into colectores  values (7,'A. L. Diaz','');
insert into colectores  values (8,'C. Romero','');
insert into colectores  values (9,'D .Morales','');




insert into animal_colectado values (01, 5,  4, 1, 'Disponible',	'captura en red',	'20110117',		'Veniliornis passerinus',			22,		'borde rastrojo bajo'	, 'Sin ectoparásitos.'			, 'M');
INSERT INTO animal_colectado vALUES (02, 2,  2, 1, 'Disponible', 	'caza', 			'20140216', 	'Struthio camelus syriacus 2', 		21, 	'llanura'				, 'Con ectoparásitos.'			, 'H');
INSERT INTO animal_colectado VALUES (03, 3,  3, 2, 'no Disponible', 'Trampas Sherman', 	'20130315', 	'Águila calzada',					02, 	'montes seccos'			, 'Iba con pareja.'				, 'I');
INSERT INTO animal_colectado VALUES (04, 1,  2, 2, 'Disponible', 	'Trampas Sherman', 	'20130414', 	'Búho chico', 						20, 	'PRADERA'				, 'Sin ectoparásitos.'			, 'H');
INSERT INTO animal_colectado VALUES (05, 2,  1, 2, 'no Disponible', 'Redes de Niebla', 	'20120513', 	'Charrán de Forster', 				05, 	'montes seccos'			, 'con nematodos preservados'	, 'H');
INSERT INTO animal_colectado VALUES (06, 9,  7, 3, 'Disponible', 	'Trampas Tomahawk',	'20120612', 	'Escribano aureolado',		 		34, 	'borde rastrojo bajo'	, ''							, 'M');
INSERT INTO animal_colectado VALUES (07, 1,  7, 3, 'Disponible', 	'Redes de Niebla', 	'20140711', 	'Focha común', 						36, 	'montes seccos'			, 'Sin ectoparásitos.'			, 'M');
INSERT INTO animal_colectado VALUES (08, 9, 14, 3, 'no Disponible', 'captura en red', 	'20140810', 	'Gallineta común', 					37, 	'PRADERA'				, 'Con ectoparásitos.'			, 'H');
INSERT INTO animal_colectado VALUES (09, 8,  6, 4, 'Disponible', 	'Trampas Sherman', 	'20130909', 	'Halcón de Eleonora', 				39, 	'borde rastrojo bajo'	, ''							, 'I');
INSERT INTO animal_colectado VALUES (10, 3,  2, 4, 'Disponible', 	'captura en red', 	'20131008', 	'Ibis sagrado', 					50, 	'montes seccos'			, 'Iba con pareja.'				, 'H');
INSERT INTO animal_colectado VALUES (11, 9,  8, 4, 'no Disponible', 'Trampas Tomahawk',	'20111207', 	'Marabú africano', 					21, 	'borde rastrojo bajo'	, 'Sin ectoparásitos.'			, 'M');
INSERT INTO animal_colectado VALUES (12, 5,  5, 5, 'Disponible', 	'Redes de Niebla', 	'20121206', 	'Ostrero euroasiático', 			22, 	'BOSQUE'				, ''							, 'H');
INSERT INTO animal_colectado VALUES (13, 5,  3, 5, 'no Disponible', 'captura en red', 	'20120105', 	'Págalo parásito', 					25, 	'montes seccos'			, 'con nematodos preservados'	, 'M');
INSERT INTO animal_colectado VALUES (14, 4,  2, 5, 'Disponible', 	'Trampas Sherman', 	'20140204', 	'Pagaza piquirroja', 				10, 	'BOSQUE'				, ''							, 'H');
INSERT INTO animal_colectado VALUES (15, 7,  1, 1, 'no Disponible', 'captura en red', 	'20100303', 	'Rabijunco etéreo', 				15, 	'PRADERA'				, 'Sin ectoparásitos.'			, 'H');
INSERT INTO animal_colectado VALUES (16, 2,  9, 2, 'Disponible', 	'Redes de Niebla', 	'20100402', 	'Reinita de Luisiana', 				16, 	'DESIERTO'				, 'Con ectoparásitos.'			, 'M');
INSERT INTO animal_colectado VALUES (17, 1, 11, 3, 'no Disponible', 'Trampas Tomahawk',	'20130501', 	'Ruiseñor coliazul', 				13, 	'montes seccos'			, 'con nematodos preservados'	, 'H');
INSERT INTO animal_colectado VALUES (18, 2, 12, 4, 'Disponible', 	'Trampas Sherman', 	'20110629', 	'Ruiseñor pechiazul', 				12, 	'DESIERTO'				, 'Sin ectoparásitos.'			, 'I');
INSERT INTO animal_colectado VALUES (19, 8, 16, 5, 'no Disponible', 'captura en red', 	'20140730', 	'Urraca', 							11, 	'REGIÓN POLAR'			, 'Iba con pareja.'				, 'H');



INSERT INTO  ornitologia values ( 1 	, 1 	, 'nulo',276, 'oviparo','NULO' ,'vacio'				, 'Corporal general moderado' 	,'Iris marrón, maxila gris oscuro, mandíbula gris claro borde de pico gris oscuro, tarsos dedos y uñas gris oscuro, suelas color carne','T.I 3,3 mm X 1,5 mm',100);
INSERT INTO  ornitologia VALUES ( 3 	, 2 	, 'NULO', 70, 'oviparo', 10, 'Restos de insectos'	, 'Corporal general moderado' 	, 'los pies', 2, 12);
INSERT INTO  ornitologia VALUES ( 5 	, 3 	, 'NULO',510, 'oviparo', 22, 'Material vegetal'		, 'Muda en el pecho' 			, 'los pies', 2, 12);
INSERT INTO  ornitologia VALUES ( 6 	, 4 	, 'NULO', 25, 'oviparo', 14, 'huevos'				, 'Corporal general moderado' 	, 'los pies', 2, 12);
INSERT INTO  ornitologia VALUES ( 7 	, 5 	, 'NULO',145, 'oviparo', 67, 'Restos de insectos'	, 'Corporal general moderado' 	, 'los pies', 2, 12);
INSERT INTO  ornitologia VALUES ( 9 	, 6 	, 'NULO',200, 'oviparo', 12, 'huevos'				, 'Corporal general moderado' 	, 'los pies', 2, 12);
INSERT INTO  ornitologia VALUES ( 2 	, 7 	, 'nulo',134, 'oviparo', 02, 'USA057'				, 'Corporal general moderado' 	, 'los pies', 2, 12);
INSERT INTO  ornitologia VALUES ( 3 	, 8 	, 'NULO', 56, 'oviparo', 12, 'Restos de insectos'	, 'Corporal general moderado' 	, 'los pies', 2, 12);
INSERT INTO  ornitologia VALUES ( 1 	, 9 	, 'NULO', 70, 'oviparo', 15, 'Material vegetal'		, 'Muda en el pecho' 			, 'los pies', 2, 12);
INSERT INTO  ornitologia VALUES (13 	,10 	, 'NULO', 98, 'oviparo', 65, 'huevos'				, 'Corporal general moderado' 	, 'los pies', 2, 12);	
INSERT INTO  ornitologia VALUES (14 	,11 	, 'NULO',102, 'oviparo', 12, 'Restos de insectos'	, 'Corporal general moderado' 	, 'los pies', 2, 12);
INSERT INTO  ornitologia VALUES (15 	,12 	, 'NULO',142, 'oviparo', 62, 'USA057'				, 'Muda en el pecho' 			, 'los pies', 2, 12);
INSERT INTO  ornitologia VALUES (19 	,13 	, 'NULO',567, 'oviparo', 12, 'Material vegetal'		, 'Corporal general moderado' 	, 'los pies', 2, 12);
INSERT INTO  ornitologia VALUES (11 	,14 	, 'nulo',023, 'oviparo', 52, 'Restos de insectos'	, 'Muda en el pecho' 			, 'los pies', 2, 12);
INSERT INTO  ornitologia VALUES (18 	,15 	, 'NULO',123, 'oviparo', 12, 'huevos'				, 'Corporal general moderado' 	, 'los pies', 2, 12);





INSERT INTO tejidos VALUES ( 1, 3, 'Corazon'	, 'tejido'	, ''); 
INSERT INTO tejidos Values ( 2, 5, 'adn'		, 'adn'		, '');
INSERT INTO tejidos VALUES ( 3, 3, 'adn'		, 'adn'		, ''); 
INSERT INTO tejidos Values ( 4, 2, 'carcasa'	, 'carcasa'	, '');
INSERT INTO tejidos VALUES ( 5, 6, 'adn'		, 'adn'		, ''); 
INSERT INTO tejidos Values ( 6, 6, 'Corazon'	, 'tejido'	, '');
INSERT INTO tejidos VALUES ( 7, 1, 'higado'		, 'tejido'	, ''); 
INSERT INTO tejidos Values ( 8, 2, 'tejido'		, 'tejido'	, '');
INSERT INTO tejidos VALUES ( 9, 3, 'huevo'		, 'adn'		, ''); 
INSERT INTO tejidos Values (10, 4, 'Corazon'	, 'tejido'	, '');
INSERT INTO tejidos VALUES (11, 6, 'carcasa'	, 'carcasa'	, ''); 
INSERT INTO tejidos Values (12, 1, 'adn'		, 'adn'		, '');
















###################################
###################################
#####                        ######
#####      CONSULTAS         ######
#####                        ######
###################################
###################################
###################################

select concat (lat_grad,'-',lat_min,'-',lat_seg) as latitud,concat (lon_grad,'-',lon_min,'-',lon_seg) as longitud from localizacion;

select a.nomb_ani,concat (l.lat_grad,'-',l.lat_min,'-',l.lat_seg) as latitud,concat (l.lon_grad,'-',l.lon_min,'-',l.lon_seg) as longitud from localizacion Natural join animal_colectado;

select nomb_sub as subespecie, nomb_esp as especie,nomb_ani,concat (lat_grad,'-',lat_min,'-',lat_seg) as latitud,concat (lon_grad,'-',lon_min,'-',lon_seg) as longitud from localizacion Natural join animal_colectado natural join subespecie natural join especies;


select nomb_sub as subespecie, nomb_esp as especie,nom_gen as genero, nom_fam as familia, nomb_ ord as orden  from localizacion Natural join animal_colectado natural join subespecie natural join especies;
select nomb_sub as subespecie, nomb_esp as especie,nomb_gen as genero,nomb_fam as familia ,nomb_ord as orden,nomb_cla as clase from  animal_colectado natural join subespecie natural join especies natural join genero natural join familia natural join orden natural join clase;

select nomb_sub as subespecie, nomb_esp as especies,nomb_gen as genero, nomb_fam as familia ,nomb_ord as orden, nomb_cla as clase,nomb_cientifico as coleccion from subespecie natural join especies natural join genero natural join familia natural join orden natural join clase natural join coleccion;



#consulticas
select concat (s.nomb_sub ,"-",e.nomb_esp,"-", g.nomb_gen,"-", f.nomb_fam,"-", o.nomb_ord ,"-", c.nomb_cla ,"-", co.nomb_cientifico) as todo 
from animal_colectado as a inner join subespecie as s inner join especies as e inner join genero as g inner join familia as f inner join 
orden as o inner join clase as c inner join coleccion as co  where s.cod_sub = a.cod_sub and s.cod_esp = e.cod_esp and e.cod_gen = g.cod_gen
 and g.cod_fam=f.cod_fam and f.cod_ord = o.cod_ord and o.cod_cla = c.cod_cla and c.cod_col = co.cod_col;


select concat (a.cod_ani,"-",m.nomb_mun,"-",d.nomb_dept,"-",p.nomb_pais) as localizacion from animal_colectado as a inner join localizacion as l inner join municipio as m inner join departamento as d inner join pais as p  where a.cod_loc = l.cod_loc and l.cod_mun = m.cod_mun and m.cod_dept = d.cod_dept and d.cod_pais = p.cod_pais ;

select o.gonadas from ornitologia as o where o.cod_ani=(select cod_ani from animal_colectado where nomb_ani='Veniliornis passerinus');
select o.gonadas from ornitologia as o where o.cod_ani=(select cod_ani from animal_colectado where nomb_ani='Veniliornis passerinus');


select count(o.cod_ani) as cantidad from ornitologia as o where o.cod_ani=(select cod_ani from animal_colectado where nomb_ani='Veniliornis passerinus');

select * from ornitologia as o where o.cod_ani=(select cod_ani from animal_colectado where nomb_ani='Veniliornis passerinus');

select * from ornitologia as o where o.cod_ani=(select cod_ani from animal_colectado where nomb_ani='Struthio camelus syriacus 2');

select orn.cod_orn ,concat (s.nomb_sub ,"-",e.nomb_esp,"-", g.nomb_gen,"-", f.nomb_fam,"-", o.nomb_ord ,"-", c.nomb_cla ,"-", co.nomb_cientifico) as todo from ornitologia as orn natural join  animal_colectado as a inner join subespecie as s inner join especies as e inner join genero as g inner join familia as f inner join orden as o inner join clase as c inner join coleccion as co  where orn.cod_ani=(select cod_ani from animal_colectado where nomb_ani='Struthio camelus syriacus 2') and s.cod_sub = (select cod_ani from animal_colectado where nomb_ani='Struthio camelus syriacus 2') and s.cod_esp = e.cod_esp and e.cod_gen = g.cod_gen and g.cod_fam=f.cod_fam and f.cod_ord = o.cod_ord and o.cod_cla = c.cod_cla and c.cod_col = co.cod_col;


select orn.cod_orn,concat (m.nomb_mun,"-",d.nomb_dept,"-",p.nomb_pais) as localizacion,a.nomb_ani,concat (l.lat_grad,'-',l.lat_min,'-',l.lat_seg) as latitud,concat (l.lon_grad,'-',l.lon_min,'-',l.lon_seg) as longitud from  ornitologia as orn natural join animal_colectado as a inner join localizacion as l inner join municipio as m inner join departamento as d inner join pais as p  where orn.cod_ani=(select cod_ani from animal_colectado where nomb_ani='Struthio camelus syriacus 2') and a.cod_loc = l.cod_loc and l.cod_mun = m.cod_mun and m.cod_dept = d.cod_dept and d.cod_pais = p.cod_pais ;
 
 select nomb_ani from animal_colectado;

,col.nomb_col as colector

select a.nomb_ani as nombre ,orn.cod_orn codigo  ,concat (s.nomb_sub ,"-",e.nomb_esp,"-", g.nomb_gen,"-", f.nomb_fam,"-", o.nomb_ord ,"-", c.nomb_cla ,"-", co.nomb_cientifico)
		as taxonomia,concat (m.nomb_mun,"-",d.nomb_dept,"-",p.nomb_pais) as localizacion,concat (l.lat_grad,'-',l.lat_min,'-',l.lat_seg) as latitud,concat (l.lon_grad,'-',l.lon_min,'-',l.lon_seg) as longitud , l.altitud,col.nomb_col as colector 

from  ornitologia as orn natural join animal_colectado as a natural join localizacion as l natural join municipio as m natural join departamento as d natural join pais as p ,
	  colectores as col , subespecie as s natural join especies as e natural join genero as g natural join familia as f natural join orden as o natural join clase as c
	  natural join coleccion as co 

where   orn.cod_ani=(select cod_ani from animal_colectado where nomb_ani='Struthio camelus syriacus 2')  
 		and a.cod_loc = l.cod_loc and l.cod_mun = m.cod_mun and m.cod_dept = d.cod_dept and d.cod_pais = p.cod_pais 
        and a.cod_col = col.cod_col 
        and a.cod_sub = s.cod_sub and  s.cod_esp = e.cod_esp and e.cod_gen = g.cod_gen and g.cod_fam=f.cod_fam and f.cod_ord = o.cod_ord and o.cod_cla = c.cod_cla ;


 // DATOS BASICOS POR nombre : Departamento subespecie especie sexo edad colector 

 select concat('MHNU-O - ',orn.cod_orn) as codigo ,a.nomb_ani as nombre , d.nomb_dept  as departamento ,a.estado as estado ,s.nomb_sub as subespecie, e.nomb_esp as especie , a.sexo as sexo , orn.edad as edad, col.nomb_col as colector 
 from 	ornitologia as orn natural join animal_colectado as a natural join localizacion as l natural join municipio as m natural join departamento as d , colectores as col , 
 		subespecie as s natural join especies as e
 where 	orn.cod_ani=(select cod_ani from animal_colectado where nomb_ani='Struthio camelus syriacus 2')
 		and a.cod_col = col.cod_col
 		and a.cod_loc = l.cod_loc and l.cod_mun = m.cod_mun and m.cod_dept = d.cod_dept
 		and a.cod_sub = s.cod_sub and  s.cod_esp = e.cod_esp ;

select concat('MHNU-O - ',orn.cod_orn) as codigo ,a.nomb_ani as nombre , d.nomb_dept  as departamento ,a.estado,s.nomb_sub as subespecie, e.nomb_esp as especie , a.sexo as sexo , orn.edad as edad, col.nomb_col as colector 
 from 	ornitologia as orn natural join animal_colectado as a natural join localizacion as l natural join municipio as m natural join departamento as d , colectores as col , 
 		subespecie as s natural join especies as e
 where  a.cod_col = col.cod_col
 		and a.cod_loc = l.cod_loc and l.cod_mun = m.cod_mun and m.cod_dept = (select cod_dept from departamento where nomb_dept = 'Meta')
 		and a.cod_sub = s.cod_sub and  s.cod_esp = e.cod_esp ;

select concat('MHNU-O - ',orn.cod_orn) as codigo ,a.nomb_ani as nombre , d.nomb_dept  as departamento ,a.estado,s.nomb_sub as subespecie, e.nomb_esp as especie , a.sexo as sexo , orn.edad as edad, col.nomb_col as colector 
 from 	ornitologia as orn natural join animal_colectado as a natural join localizacion as l natural join municipio as m natural join departamento as d , colectores as col , 
 		subespecie as s natural join especies as e
 where  a.cod_col = col.cod_col
 		and a.cod_loc = l.cod_loc and l.cod_mun = m.cod_mun and a.cod_sub = (select cod_sub from subespecie where nomb_sub = 'Struthio camelus camelus')
 		and a.cod_sub = s.cod_sub and  s.cod_esp = e.cod_esp ;



select concat('MHNU-O - ',orn.cod_orn) as codigo ,a.nomb_ani as nombre , d.nomb_dept  as departamento ,a.estado,s.nomb_sub as subespecie, e.nomb_esp as especie , a.sexo as sexo , orn.edad as edad, col.nomb_col as colector 
 from 	ornitologia as orn natural join animal_colectado as a natural join localizacion as l natural join municipio as m natural join departamento as d , colectores as col , 
 		subespecie as s natural join especies as e
 where  a.cod_col = col.cod_col
 		and a.cod_loc = l.cod_loc and l.cod_mun = m.cod_mun and a.cod_col = (select cod_col from colectores where nomb_col = 'f. aponte')
 		and a.cod_sub = s.cod_sub and  s.cod_esp = e.cod_esp ;

select count(orn.cod_orn) as cantidad 
 from 	ornitologia as orn natural join animal_colectado as a natural join localizacion as l natural join municipio as m natural join departamento as d , colectores as col , 
 		subespecie as s natural join especies as e
 where  a.cod_col = col.cod_col
 		and a.cod_loc = l.cod_loc and l.cod_mun = m.cod_mun and m.cod_dept = (select cod_dept from departamento where nomb_dept = 'Meta')
 		and a.cod_sub = s.cod_sub and  s.cod_esp = e.cod_esp ;

select 
	concat('MHNU-O - ',orn.cod_orn) as codigo, a.nomb_ani, concat (s.nomb_sub ,"-",e.nomb_esp,"-", g.nomb_gen,"-", f.nomb_fam,"-", o.nomb_ord ,"-", c.nomb_cla ,"-", co.nomb_cientifico) as taxonomia, 
	concat (l.lat_grad,'-',l.lat_min,'-',l.lat_seg) as latitud,concat (l.lon_grad,'-',l.lon_min,'-',l.lon_seg) as longitud, concat (l.vereda,"-", m.nomb_mun,"-",d.nomb_dept,"-",p.nomb_pais) as localizacion,
	a.estado as estado, a.metodo as metodo, a.fecha as fecha_ingreso, a.sexo as sexo, a.peso as peso, a.habitat as habitat, a.anotaciones as anotaciones, orn.edad as edad, orn.envergadura as envergadura, 
	orn.inf_repro as informacion_reproductiva , orn.grasa as grasa, orn.cont_est as contenido_estomacal, orn.muda as muda, orn.part_blan as partes_blandas, orn.gonadas as gonadas , orn.oscificacion as osficicacion
from 
	ornitologia as orn natural join animal_colectado as a natural join localizacion as l natural join municipio as m natural join departamento as d natural join pais as p, colectores as col,
	subespecie as s natural join especies as e natural join genero as g natural join familia as f natural join orden as o natural join clase as c
	natural join coleccion as co 
where
	a.cod_col = col.cod_col
	and  orn.cod_orn="15"
	and a.cod_sub = s.cod_sub;
	
select 
	concat('MHNU-O - ',orn.cod_orn) as codigo, a.nomb_ani, s.nomb_sub as subespecie,e.nomb_esp as especie, g.nomb_gen as genero, f.nomb_fam as familia , o.nomb_ord  as orden , c.nomb_cla  as clase , co.nomb_cientifico as coleccion, 
	concat (l.lat_grad,'-',l.lat_min,'-',l.lat_seg) as latitud,concat (l.lon_grad,'-',l.lon_min,'-',l.lon_seg) as longitud, concat (l.vereda,'-', m.nomb_mun,'-',d.nomb_dept,'-',p.nomb_pais) as localizacion,
	a.estado as estado, a.metodo as metodo, a.fecha as fecha_ingreso, a.sexo as sexo, a.peso as peso, a.habitat as habitat, a.anotaciones as anotaciones, orn.edad as edad, orn.envergadura as envergadura, 
	orn.inf_repro as informacion_reproductiva , orn.grasa as grasa, orn.cont_est as contenido_estomacal, orn.muda as muda, orn.part_blan as partes_blandas, orn.gonadas as gonadas , orn.oscificacion as osficicacion
from 
	ornitologia as orn natural join animal_colectado as a natural join localizacion as l natural join municipio as m natural join departamento as d natural join pais as p, colectores as col,
	subespecie as s natural join especies as e natural join genero as g natural join familia as f natural join orden as o natural join clase as c
	natural join coleccion as co 
where
	a.cod_col = col.cod_col
	and  orn.cod_orn='15'	and a.cod_sub = s.cod_sub;


#Datos para busqueda en la tabla

Struthio camelus syriacus 2
Meta
Struthio camelus camelus
f. aponte


