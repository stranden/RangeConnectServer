-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: mariadb:3306
-- Generation Time: Dec 04, 2019 at 06:51 PM
-- Server version: 10.1.35-MariaDB
-- PHP Version: 7.0.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sius`
--

-- --------------------------------------------------------

--
-- Table structure for table `competitions`
--

CREATE TABLE `competitions` (
  `id` int(11) NOT NULL,
  `eventid` int(11) NOT NULL,
  `disciplineid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `competitions`
--

INSERT INTO `competitions` (`id`, `eventid`, `disciplineid`) VALUES
(1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `disciplines`
--

CREATE TABLE `disciplines` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `time` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `disciplines`
--

INSERT INTO `disciplines` (`id`, `name`, `time`) VALUES
(1, 'ISSF 10m AR Final', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `events`
--

CREATE TABLE `events` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `date` date NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `events`
--

INSERT INTO `events` (`id`, `name`, `date`, `status`) VALUES
(1, 'DM 2018 10m', '2018-09-23', 1);

-- --------------------------------------------------------

--
-- Table structure for table `names`
--

CREATE TABLE `names` (
  `id` int(11) NOT NULL,
  `shooter` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `names`
--

INSERT INTO `names` (`id`, `shooter`, `name`) VALUES
(1, 9, 'Henrik Strand'),
(2, 1, 'Lars Ørum'),
(3, 3, 'Morten Flecks'),
(4, 6, 'Alex Møberg'),
(5, 2, 'Erik Skovmand'),
(6, 10, 'Peter Strand'),
(7, 18, 'Morten Bjørn'),
(8, 14, 'Niels H. Overgaard'),
(9, 16, 'Rasmus Fisker'),
(10, 4, 'Knud Erik Holm');

-- --------------------------------------------------------

--
-- Table structure for table `nations`
--

CREATE TABLE `nations` (
  `id` int(11) NOT NULL,
  `shooter` int(11) NOT NULL,
  `nat` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `nations`
--

INSERT INTO `nations` (`id`, `shooter`, `nat`) VALUES
(1, 9, 'Men'),
(2, 1, 'Men'),
(3, 3, 'Men'),
(4, 6, 'Men'),
(5, 10, 'Men'),
(6, 2, 'Men'),
(7, 18, 'Men'),
(8, 14, 'Men'),
(9, 16, 'Men'),
(10, 4, 'Men');

-- --------------------------------------------------------

--
-- Table structure for table `series`
--

CREATE TABLE `series` (
  `id` int(11) NOT NULL,
  `disciplineid` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `shots` int(11) DEFAULT NULL,
  `singleshots` tinyint(1) DEFAULT NULL,
  `matchfire` tinyint(1) NOT NULL,
  `time` int(11) DEFAULT NULL,
  `elimination` tinyint(1) DEFAULT NULL,
  `eliminationshooters` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `series`
--

INSERT INTO `series` (`id`, `disciplineid`, `name`, `shots`, `singleshots`, `matchfire`, `time`, `elimination`, `eliminationshooters`) VALUES
(1, 1, 'Sighters', NULL, NULL, 0, 300, NULL, NULL),
(2, 1, '1-5', 5, 0, 1, 250, 0, NULL),
(3, 1, '6-10', 5, 0, 1, 250, 0, NULL),
(4, 1, '11-12', 2, 1, 1, 50, 1, 1),
(5, 1, '13-14', 2, 1, 1, 50, 1, 1),
(6, 1, '15-16', 2, 1, 1, 50, 1, 1),
(7, 1, '17-18', 2, 1, 1, 50, 1, 1),
(8, 1, '19-20', 2, 1, 1, 50, 1, 1),
(9, 1, '21-22', 2, 1, 1, 50, 1, 1),
(10, 1, '23-24', 2, 1, 1, 50, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `shooters`
--

CREATE TABLE `shooters` (
  `id` int(11) NOT NULL,
  `event` int(11) NOT NULL,
  `shooter` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `shooters`
--

INSERT INTO `shooters` (`id`, `event`, `shooter`) VALUES
(1, 1, 1002),
(2, 1, 1005),
(3, 1, 1003),
(4, 1, 1010),
(5, 1, 1002),
(6, 1, 1004),
(7, 1, 1005),
(8, 1, 1003),
(9, 1, 1001),
(10, 1, 1006),
(11, 1, 1004),
(12, 1, 1001),
(13, 1, 1006),
(14, 1, 1008),
(15, 1, 1008),
(16, 1, 1009),
(17, 1, 1009),
(18, 1, 1007);

-- --------------------------------------------------------

--
-- Table structure for table `shots`
--

CREATE TABLE `shots` (
  `id` int(11) NOT NULL,
  `shooter` int(11) NOT NULL,
  `lane` int(11) NOT NULL,
  `time` varchar(255) NOT NULL,
  `value` int(11) NOT NULL,
  `valueten` int(11) NOT NULL,
  `xaxis` varchar(255) NOT NULL,
  `yaxis` varchar(255) NOT NULL,
  `currentshot` int(11) NOT NULL,
  `maxshots` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `shots`
--

INSERT INTO `shots` (`id`, `shooter`, `lane`, `time`, `value`, `valueten`, `xaxis`, `yaxis`, `currentshot`, `maxshots`) VALUES
(1, 9, 1, '11:53:51.67', 10, 105, '0.00000000', '-0.00112500', 1, 60),
(2, 1, 2, '11:53:51.68', 10, 105, '0.00079550', '-0.00079550', 1, 60),
(3, 6, 4, '11:53:51.69', 10, 107, '0.00044194', '0.00044194', 1, 60),
(4, 2, 5, '11:53:51.70', 10, 101, '0.00150260', '0.00150260', 1, 60),
(5, 10, 6, '11:53:51.70', 9, 98, '0.00203293', '-0.00203293', 1, 60),
(6, 3, 3, '11:53:51.69', 10, 107, '-0.00044194', '0.00044194', 1, 60),
(7, 16, 9, '11:53:51.72', 9, 98, '0.00000000', '0.00287500', 1, 60),
(8, 4, 10, '11:53:51.72', 9, 95, '-0.00256326', '-0.00256326', 1, 60),
(9, 18, 7, '11:53:51.71', 10, 100, '-0.00167938', '0.00167938', 1, 60),
(10, 14, 8, '11:53:51.71', 9, 96, '-0.00238649', '-0.00238649', 1, 60),
(11, 9, 1, '11:53:52.12', 10, 104, '-0.00137500', '0.00000000', 2, 60),
(12, 1, 2, '11:53:52.13', 10, 104, '0.00000000', '0.00137500', 2, 60),
(13, 3, 3, '11:53:52.13', 9, 97, '-0.00312500', '0.00000000', 2, 60),
(14, 6, 4, '11:53:52.14', 9, 99, '-0.00185616', '0.00185616', 2, 60),
(15, 2, 5, '11:53:52.15', 10, 105, '0.00112500', '0.00000000', 2, 60),
(16, 10, 6, '11:53:52.16', 10, 107, '0.00044194', '-0.00044194', 2, 60),
(17, 18, 7, '11:53:52.17', 9, 97, '0.00000000', '-0.00312500', 2, 60),
(18, 14, 8, '11:53:52.18', 9, 97, '0.00000000', '-0.00312500', 2, 60),
(19, 16, 9, '11:53:52.18', 9, 96, '-0.00337500', '0.00000000', 2, 60),
(20, 4, 10, '11:53:52.19', 10, 104, '0.00000000', '0.00137500', 2, 60),
(21, 9, 1, '11:53:52.47', 10, 106, '0.00000000', '0.00087500', 3, 60),
(22, 1, 2, '11:53:52.48', 9, 99, '0.00262500', '0.00000000', 3, 60),
(23, 3, 3, '11:53:52.49', 9, 97, '0.00312500', '0.00000000', 3, 60),
(24, 6, 4, '11:53:52.51', 10, 101, '0.00150260', '0.00150260', 3, 60),
(25, 2, 5, '11:53:52.52', 10, 109, '0.00012500', '0.00000000', 3, 60),
(26, 10, 6, '11:53:52.53', 10, 102, '0.00132583', '-0.00132583', 3, 60),
(27, 18, 7, '11:53:52.54', 10, 103, '0.00000000', '0.00162500', 3, 60),
(28, 14, 8, '11:53:52.56', 10, 105, '0.00112500', '0.00000000', 3, 60),
(29, 16, 9, '11:53:52.57', 9, 96, '0.00000000', '0.00337500', 3, 60),
(30, 4, 10, '11:53:52.58', 10, 101, '-0.00150260', '-0.00150260', 3, 60),
(31, 9, 1, '11:53:52.70', 9, 97, '0.00000000', '0.00312500', 4, 60),
(32, 1, 2, '11:53:52.71', 9, 97, '0.00312500', '0.00000000', 4, 60),
(33, 3, 3, '11:53:52.72', 9, 96, '0.00238649', '-0.00238649', 4, 60),
(34, 6, 4, '11:53:52.74', 10, 107, '0.00044194', '-0.00044194', 4, 60),
(35, 2, 5, '11:53:52.75', 10, 107, '-0.00044194', '-0.00044194', 4, 60),
(36, 10, 6, '11:53:52.76', 9, 99, '-0.00262500', '0.00000000', 4, 60),
(37, 18, 7, '11:53:52.77', 10, 101, '0.00000000', '0.00212500', 4, 60),
(38, 14, 8, '11:53:52.79', 9, 99, '0.00185616', '0.00185616', 4, 60),
(39, 16, 9, '11:53:52.80', 9, 99, '-0.00262500', '0.00000000', 4, 60),
(40, 4, 10, '11:53:52.81', 10, 108, '-0.00037500', '0.00000000', 4, 60),
(41, 9, 1, '11:53:52.91', 10, 108, '0.00000000', '0.00037500', 5, 60),
(42, 1, 2, '11:53:52.93', 10, 100, '0.00000000', '-0.00237500', 5, 60),
(43, 3, 3, '11:53:52.94', 9, 97, '-0.00312500', '0.00000000', 5, 60),
(44, 6, 4, '11:53:52.96', 9, 98, '-0.00287500', '0.00000000', 5, 60),
(45, 2, 5, '11:53:52.98', 9, 95, '0.00000000', '0.00362500', 5, 60),
(46, 10, 6, '11:53:52.99', 9, 97, '-0.00220971', '0.00220971', 5, 60),
(47, 18, 7, '11:53:53.01', 9, 98, '-0.00203293', '-0.00203293', 5, 60),
(48, 14, 8, '11:53:53.02', 10, 108, '-0.00037500', '0.00000000', 5, 60),
(49, 16, 9, '11:53:53.04', 10, 108, '0.00026517', '0.00026517', 5, 60),
(50, 4, 10, '11:53:53.05', 10, 103, '-0.00114905', '0.00114905', 5, 60),
(51, 9, 1, '11:53:53.11', 9, 96, '0.00000000', '-0.00337500', 6, 60),
(52, 1, 2, '11:53:53.12', 9, 97, '0.00312500', '0.00000000', 6, 60),
(53, 3, 3, '11:53:53.14', 9, 96, '0.00238649', '0.00238649', 6, 60),
(54, 6, 4, '11:53:53.16', 9, 95, '0.00000000', '0.00362500', 6, 60),
(55, 2, 5, '11:53:53.18', 10, 108, '-0.00026517', '-0.00026517', 6, 60),
(56, 10, 6, '11:53:53.19', 10, 106, '0.00061872', '-0.00061872', 6, 60),
(57, 18, 7, '11:53:53.21', 10, 106, '0.00061872', '0.00061872', 6, 60),
(58, 14, 8, '11:53:53.23', 10, 106, '-0.00061872', '-0.00061872', 6, 60),
(59, 16, 9, '11:53:53.25', 10, 108, '0.00000000', '0.00037500', 6, 60),
(60, 4, 10, '11:53:53.27', 10, 100, '0.00000000', '-0.00237500', 6, 60),
(61, 9, 1, '11:53:53.32', 10, 105, '-0.00079550', '-0.00079550', 7, 60),
(62, 1, 2, '11:53:53.34', 9, 97, '0.00000000', '-0.00312500', 7, 60),
(63, 3, 3, '11:53:53.36', 9, 96, '-0.00238649', '0.00238649', 7, 60),
(64, 6, 4, '11:53:53.38', 10, 104, '-0.00137500', '0.00000000', 7, 60),
(65, 2, 5, '11:53:53.40', 10, 103, '-0.00162500', '0.00000000', 7, 60),
(66, 10, 6, '11:53:53.42', 9, 96, '0.00000000', '0.00337500', 7, 60),
(67, 18, 7, '11:53:53.44', 10, 107, '0.00044194', '-0.00044194', 7, 60),
(68, 14, 8, '11:53:53.47', 9, 97, '0.00000000', '-0.00312500', 7, 60),
(69, 16, 9, '11:53:53.49', 10, 100, '0.00167938', '-0.00167938', 7, 60),
(70, 4, 10, '11:53:53.50', 10, 101, '-0.00150260', '-0.00150260', 7, 60),
(71, 9, 1, '11:53:56.83', 10, 102, '-0.00132583', '-0.00132583', 1, 60),
(72, 1, 2, '11:53:56.87', 10, 104, '0.00000000', '0.00137500', 1, 60),
(73, 3, 3, '11:53:56.90', 10, 108, '0.00000000', '-0.00037500', 1, 60),
(74, 6, 4, '11:53:56.93', 9, 97, '0.00000000', '0.00312500', 1, 60),
(75, 2, 5, '11:53:56.97', 10, 105, '-0.00112500', '0.00000000', 1, 60),
(76, 10, 6, '11:53:57.00', 10, 105, '0.00000000', '-0.00112500', 1, 60),
(77, 18, 7, '11:53:57.03', 10, 103, '-0.00162500', '0.00000000', 1, 60),
(78, 14, 8, '11:53:57.07', 10, 100, '-0.00167938', '-0.00167938', 1, 60),
(79, 16, 9, '11:53:57.10', 9, 97, '-0.00220971', '0.00220971', 1, 60),
(80, 4, 10, '11:53:57.13', 9, 99, '0.00262500', '0.00000000', 1, 60),
(81, 9, 1, '11:53:58.05', 10, 108, '0.00037500', '0.00000000', 2, 60),
(82, 1, 2, '11:53:58.07', 9, 96, '-0.00337500', '0.00000000', 2, 60),
(83, 3, 3, '11:53:58.10', 10, 103, '0.00162500', '0.00000000', 2, 60),
(84, 6, 4, '11:53:58.12', 10, 105, '-0.00079550', '-0.00079550', 2, 60),
(85, 2, 5, '11:53:58.15', 10, 103, '-0.00162500', '0.00000000', 2, 60),
(86, 10, 6, '11:53:58.18', 10, 101, '0.00212500', '0.00000000', 2, 60),
(87, 18, 7, '11:53:58.20', 10, 103, '-0.00162500', '0.00000000', 2, 60),
(88, 14, 8, '11:53:58.23', 10, 103, '-0.00114905', '-0.00114905', 2, 60),
(89, 16, 9, '11:53:58.25', 10, 103, '0.00162500', '0.00000000', 2, 60),
(90, 4, 10, '11:53:58.28', 10, 104, '0.00000000', '-0.00137500', 2, 60),
(91, 9, 1, '11:53:59.04', 10, 103, '0.00000000', '0.00162500', 3, 60),
(92, 1, 2, '11:53:59.07', 10, 104, '-0.00097227', '0.00097227', 3, 60),
(93, 3, 3, '11:53:59.10', 10, 108, '0.00000000', '-0.00037500', 3, 60),
(94, 6, 4, '11:53:59.13', 10, 105, '0.00000000', '0.00112500', 3, 60),
(95, 2, 5, '11:53:59.16', 10, 100, '-0.00167938', '-0.00167938', 3, 60),
(96, 10, 6, '11:53:59.18', 9, 98, '0.00203293', '-0.00203293', 3, 60),
(97, 18, 7, '11:53:59.21', 10, 102, '-0.00132583', '-0.00132583', 3, 60),
(98, 14, 8, '11:53:59.24', 10, 100, '0.00237500', '0.00000000', 3, 60),
(99, 16, 9, '11:53:59.27', 9, 96, '0.00000000', '0.00337500', 3, 60),
(100, 4, 10, '11:53:59.30', 10, 106, '0.00000000', '-0.00087500', 3, 60),
(101, 9, 1, '11:53:59.95', 10, 109, '0.00008839', '0.00008839', 4, 60),
(102, 1, 2, '11:53:59.98', 10, 107, '-0.00044194', '0.00044194', 4, 60),
(103, 3, 3, '11:54:00.02', 9, 95, '0.00362500', '0.00000000', 4, 60),
(104, 6, 4, '11:54:00.05', 10, 101, '0.00150260', '-0.00150260', 4, 60),
(105, 2, 5, '11:54:00.08', 10, 104, '0.00097227', '-0.00097227', 4, 60),
(106, 10, 6, '11:54:00.11', 10, 104, '0.00097227', '0.00097227', 4, 60),
(107, 18, 7, '11:54:00.14', 10, 107, '-0.00044194', '-0.00044194', 4, 60),
(108, 14, 8, '11:54:00.17', 10, 105, '0.00000000', '-0.00112500', 4, 60),
(109, 16, 9, '11:54:00.20', 10, 106, '-0.00061872', '0.00061872', 4, 60),
(110, 4, 10, '11:54:00.23', 9, 98, '-0.00203293', '0.00203293', 4, 60),
(111, 9, 1, '11:54:00.94', 10, 103, '0.00000000', '0.00162500', 5, 60),
(112, 1, 2, '11:54:00.97', 10, 102, '0.00000000', '0.00187500', 5, 60),
(113, 3, 3, '11:54:01.00', 10, 105, '-0.00112500', '0.00000000', 5, 60),
(114, 6, 4, '11:54:01.04', 10, 106, '0.00061872', '-0.00061872', 5, 60),
(115, 2, 5, '11:54:01.07', 9, 99, '-0.00185616', '0.00185616', 5, 60),
(116, 10, 6, '11:54:01.10', 10, 107, '0.00044194', '0.00044194', 5, 60),
(117, 18, 7, '11:54:01.14', 10, 102, '-0.00187500', '0.00000000', 5, 60),
(118, 14, 8, '11:54:01.17', 10, 106, '0.00087500', '0.00000000', 5, 60),
(119, 16, 9, '11:54:01.20', 9, 96, '0.00000000', '0.00337500', 5, 60),
(120, 4, 10, '11:54:01.24', 10, 101, '0.00150260', '0.00150260', 5, 60),
(121, 9, 1, '11:54:01.76', 10, 109, '-0.00008839', '0.00008839', 6, 60),
(122, 1, 2, '11:54:01.80', 10, 101, '0.00000000', '0.00212500', 6, 60),
(123, 3, 3, '11:54:01.83', 9, 98, '-0.00287500', '0.00000000', 6, 60),
(124, 6, 4, '11:54:01.87', 9, 98, '0.00000000', '-0.00287500', 6, 60),
(125, 2, 5, '11:54:01.91', 9, 95, '-0.00362500', '0.00000000', 6, 60),
(126, 10, 6, '11:54:01.94', 10, 105, '0.00079550', '0.00079550', 6, 60),
(127, 18, 7, '11:54:01.98', 9, 99, '0.00185616', '0.00185616', 6, 60),
(128, 14, 8, '11:54:02.01', 10, 103, '0.00114905', '0.00114905', 6, 60),
(129, 16, 9, '11:54:02.05', 10, 106, '-0.00087500', '0.00000000', 6, 60),
(130, 4, 10, '11:54:02.08', 9, 98, '0.00203293', '0.00203293', 6, 60);

-- --------------------------------------------------------

--
-- Table structure for table `teams`
--

CREATE TABLE `teams` (
  `id` int(11) NOT NULL,
  `shooter` int(11) NOT NULL,
  `team` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `teams`
--

INSERT INTO `teams` (`id`, `shooter`, `team`) VALUES
(1, 9, 'Viborg'),
(2, 1, 'Aalborg'),
(3, 16, 'Viborg'),
(4, 3, 'ÅRK'),
(5, 4, 'Viborg'),
(6, 6, 'ÅRK'),
(7, 2, 'Viborg'),
(8, 10, 'TKL'),
(9, 18, 'Viborg'),
(10, 14, 'BPI');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `competitions`
--
ALTER TABLE `competitions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `disciplines`
--
ALTER TABLE `disciplines`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `events`
--
ALTER TABLE `events`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `names`
--
ALTER TABLE `names`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `nations`
--
ALTER TABLE `nations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `series`
--
ALTER TABLE `series`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `shooters`
--
ALTER TABLE `shooters`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `shots`
--
ALTER TABLE `shots`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `teams`
--
ALTER TABLE `teams`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `competitions`
--
ALTER TABLE `competitions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `disciplines`
--
ALTER TABLE `disciplines`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `events`
--
ALTER TABLE `events`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `names`
--
ALTER TABLE `names`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `nations`
--
ALTER TABLE `nations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `series`
--
ALTER TABLE `series`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `shooters`
--
ALTER TABLE `shooters`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `shots`
--
ALTER TABLE `shots`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=131;

--
-- AUTO_INCREMENT for table `teams`
--
ALTER TABLE `teams`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
