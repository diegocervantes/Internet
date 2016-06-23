-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-06-2016 a las 17:53:52
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
(1, 'juan', '321', 'Limpieza', 'Limpiar todas las salas', 'Jose Robles'),
(2, 'INT-2016-01', 'holaA-=', 'Anatomia', 'Esta area es chevere', 'Juanito '),
(4, 'ANT-1998-01', 'Axd09./', 'Oficinas', 'bla bla bla bla', 'Jose Bernardo'),
(5, 'INT-2016-02', '13123AS-[', 'Carbonería', 'nada', 'Rosa Beltr?n');

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
  `celular` varchar(13) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`id`, `codigo`, `user`, `nombre`, `password`, `fecha_nacimiento`, `dni`, `ingreso`, `email`, `telefono`, `celular`) VALUES
(1, '123', '', '', '', '0000-00-00', '0', 0000, '', '0', '0'),
(2, '123', '', '', '', '0000-00-00', '0', 0000, '', '0', '0'),
(3, '312', '312', '312', '312', '0000-00-00', '312', 0000, '312', '312', '312'),
(4, 'INT-45628-2016-01', 'INT-45628-2016-01', 'Pancho Rodriguez', 'aleluya123A-&gt;', '0000-00-00', '71440896', 2006, 'pancho@inigo.com', '54272222', '978767562'),
(5, 'PAS-45628-2016-01', 'PAS-45628-2016-01', 'Rodrigo abd', 'asdhQ-;', '0000-00-00', '23231231', 2006, 'c2089930@trbvn.com', '54272798', '976782309');

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
  ADD PRIMARY KEY (`id`);

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
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT de la tabla `asistencia`
--
ALTER TABLE `asistencia`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `empleados`
--
ALTER TABLE `empleados`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
