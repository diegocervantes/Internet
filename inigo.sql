-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-06-2016 a las 01:48:10
-- Versión del servidor: 10.1.13-MariaDB
-- Versión de PHP: 5.6.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `inigo`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `admin`
--

CREATE TABLE `admin` (
  `id` int(10) NOT NULL,
  `user` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `admin`
--

INSERT INTO `admin` (`id`, `user`, `password`) VALUES
(1, 'juanperez', 'hola');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `areas`
--

CREATE TABLE `areas` (
  `id` int(10) NOT NULL,
  `user` varchar(11) NOT NULL,
  `password` varchar(20) NOT NULL,
  `nombre_area` varchar(20) NOT NULL,
  `descripcion` text NOT NULL,
  `jefe_area` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `areas`
--

INSERT INTO `areas` (`id`, `user`, `password`, `nombre_area`, `descripcion`, `jefe_area`) VALUES
(1, 'juan', '321', 'Ninguna', 'prueba de areas', 'Jose Robles'),
(2, 'MER-2016-01', 'holaA-=', 'Mercadotecnia', 'Encargado de satisfacen sus necesidades al crear e intercambiar bienes y servicios', 'Luis Anibal'),
(3, 'PRO-1998-01', 'Axd09./', 'Produccion', 'Se encarga de manejar os productos de la empresa', 'Jose Bernardo'),
(4, 'FIN-2016-02', '13123AS-[', 'Finanzas', 'Encargado de manejar el estado económico, gastos e ingresos de la empresa', 'Rosa Beltran'),
(5, 'REH-2014-01', '1', 'Recursos Humanos', 'Esta area se encarga de organizar a los empleados en general', 'Rodrigo Begazo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asistencia`
--

CREATE TABLE `asistencia` (
  `id` int(10) NOT NULL,
  `user_id` int(10) NOT NULL,
  `area_id` int(10) NOT NULL,
  `fecha` date NOT NULL,
  `asistencia` tinyint(1) NOT NULL,
  `registro_asistencia` varchar(14) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `id` int(10) NOT NULL,
  `codigo` varchar(17) NOT NULL,
  `user` varchar(17) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  `password` varchar(20) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `dni` varchar(8) NOT NULL,
  `ingreso` year(4) NOT NULL,
  `email` varchar(30) NOT NULL,
  `telefono` varchar(13) NOT NULL,
  `celular` varchar(13) NOT NULL,
  `area_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`id`, `codigo`, `user`, `nombre`, `password`, `fecha_nacimiento`, `dni`, `ingreso`, `email`, `telefono`, `celular`, `area_id`) VALUES
(1, '123', '', '', '', '1988-06-29', '0', 0000, '', '0', '0', 0),
(2, '123', '', '', '', '1990-10-12', '0', 0000, '', '0', '0', 0),
(3, '312', '312', '312', '312', '1995-07-30', '312', 0000, '312', '312', '312', 0),
(4, 'MER-45628-2016-01', 'MER-45628-2016-01', 'Pancho Rodriguez', 'ale123A-&gt;', '1989-01-13', '71440896', 2006, 'pancho@inigo.com', '54272222', '978767562', 5),
(5, 'PRO-98264-2016-01', 'PRO-98264-2016-01', 'Rodrigo Alendro', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 2),
(6, 'FIN-82736-2016-01', 'FIN-82736-2016-01', 'Raul Loyola', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 3),
(7, 'REH-28356-2016-01', 'REH-28356-2016-01', 'Alejandro Valdivia', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 4),
(8, 'MER-28374-2016-01', 'MER-28374-2016-01', 'Natalia Guitierrez', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 5),
(9, 'MER-19260-2016-01', 'MER-19260-2016-01', 'Lucia Maraniego', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 5),
(10, 'MER-01723-2016-01', 'MER-01723-2016-01', 'Bruno Sandres', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 5),
(11, 'PRO-28374-2016-01', 'PRO-28374-2016-01', 'Ignacio Bustinza', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 2),
(12, 'PRO-27364-2016-01', 'PRO-27364-2016-01', 'Patricio Valderrama', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 2),
(13, 'PRO-36472-2016-01', 'PRO-36472-2016-01', 'Ana Lucia Rondon', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 2),
(14, 'FIN-19273-2016-01', 'FIN-19273-2016-01', 'Jimena Albarado', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 3),
(15, 'FIN-10254-2016-01', 'FIN-10254-2016-01', 'Sandra Zegarra', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 3),
(16, 'FIN-15351-2016-01', 'FIN-15351-2016-01', 'Samuel Carpio', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 3),
(17, 'FIN-11428-2016-01', 'FIN-11428-2016-01', 'David Jimenez', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 3),
(18, 'REH-10259-2016-01', 'REH-10259-2016-01', 'Daniela Bustos', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 4),
(19, 'REH-12321-2016-01', 'REH-12321-2016-01', 'Gabriela Hernandez', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 4),
(20, 'REH-10323-2016-01', 'REH-10323-2016-01', 'Juan Fernandez', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 4),
(21, 'MER-11972-2016-01', 'MER-11972-2016-01', 'Michell Gomez', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 5),
(22, 'MER-02642-2016-01', 'MER-02642-2016-01', 'Luisa Bedoya', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 5),
(23, 'MER-11923-2016-01', 'MER-11923-2016-01', 'Anabel Lazo', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 5),
(24, 'REH-12321-2016-01', 'REH-12321-2016-01', 'Ramiro Guitierrez', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 4),
(25, 'REH-12325-2016-01', 'REH-12325-2016-01', 'Hernan Salvador', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 4),
(26, 'PRO-10982-2016-01', 'PRO-10982-2016-01', 'Susana Alatrista', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 2),
(27, 'PRO-10442-2016-01', 'PRO-10442-2016-01', 'Milagros Moscozo', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 2),
(28, 'MER-98524-2016-01', 'MER-98524-2016-01', 'Robert Alaya', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 5),
(29, 'MER-97523-2016-01', 'MER-97523-2016-01', 'Carlos Lindo', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 5),
(30, 'MER-76232-2016-01', 'MER-76232-2016-01', 'Luis Sanchez', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 5),
(31, 'MER-89654-2016-01', 'MER-89654-2016-01', 'Manuel Bejarano', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 5),
(32, 'FIN-27364-2016-01', 'FIN-27364-2016-01', 'Isabel Quiroz', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 3),
(33, 'FIN-86374-2016-01', 'FIN-86374-2016-01', 'Rodrigo Juarez', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 3),
(34, 'FIN-28462-2016-01', 'FIN-28462-2016-01', 'Juan Beltran', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 3),
(35, 'REH-28646-2016-01', 'REH-28646-2016-01', 'Angel Cano', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 4),
(36, 'REH-28309-2016-01', 'REH-28309-2016-01', 'Jose Talavera', 'asdhQ-;', '1993-10-13', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309', 4);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `areas`
--
ALTER TABLE `areas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id` (`id`),
  ADD KEY `id_2` (`id`);

--
-- Indices de la tabla `asistencia`
--
ALTER TABLE `asistencia`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT de la tabla `areas`
--
ALTER TABLE `areas`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT de la tabla `asistencia`
--
ALTER TABLE `asistencia`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `empleados`
--
ALTER TABLE `empleados`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
