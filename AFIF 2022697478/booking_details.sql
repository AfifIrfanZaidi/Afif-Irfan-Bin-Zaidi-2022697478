-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 04, 2024 at 11:04 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `futsal_booking`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking_details`
--

CREATE TABLE `booking_details` (
  `NAME` text NOT NULL,
  `START` int(1) NOT NULL,
  `END` int(1) NOT NULL,
  `DATE` varchar(30) NOT NULL,
  `DURATION PRICE` varchar(30) NOT NULL,
  `HOURS` int(1) NOT NULL,
  `PLACE` text NOT NULL,
  `PLAYING TIME` int(1) NOT NULL,
  `PRICE` int(2) NOT NULL,
  `TOTAL PRICE` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `booking_details`
--

INSERT INTO `booking_details` (`NAME`, `START`, `END`, `DATE`, `DURATION PRICE`, `HOURS`, `PLACE`, `PLAYING TIME`, `PRICE`, `TOTAL PRICE`) VALUES
('MUHAMMAD HANIF AIMAN BIN KAMARUZAMAN', 3, 5, '6 February 2024', 'PM RM70 per hour', 2, 'WNS Futsal', 2, 70, 140),
('Muhammad Izzat Bin Jamal', 6, 8, '20 February 2024', 'AM RM50 per hour', 2, 'WNS Futsal', 2, 50, 100),
('IRFAN', 8, 10, '6 February 2024', 'PM RM70 per hour', 2, 'Derga Futsal', 2, 70, 140),
('SALSABILA', 4, 6, '13 February 2024', 'PM RM70 per hour', 2, 'D Futsal', 2, 70, 140),
('muaz', 1, 3, '2 March 2024', 'PM RM70 per hour', 2, 'D Futsal', 2, 70, 140);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
