-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 23, 2024 at 03:33 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `distribusi_bansos`
--

-- --------------------------------------------------------

--
-- Table structure for table `bansos`
--

CREATE TABLE `bansos` (
  `id` int(11) NOT NULL,
  `nama_bansos` varchar(255) DEFAULT NULL,
  `tanggal` date DEFAULT NULL,
  `jumlah` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bansos`
--

INSERT INTO `bansos` (`id`, `nama_bansos`, `tanggal`, `jumlah`) VALUES
(1, 'BLT', '0000-00-00', 100000),
(2, 'BALSEM', NULL, 20000),
(3, 'dagadg', NULL, 56356),
(4, 'adfdaf', NULL, 123123),
(5, 'cbzdcv', NULL, 12312),
(6, 'asdasf', NULL, 123124),
(7, 'asfasf', NULL, 0),
(8, 'gsdgsd', NULL, 124124),
(9, 'Prakerja', NULL, 200000);

-- --------------------------------------------------------

--
-- Table structure for table `transaksi`
--

CREATE TABLE `transaksi` (
  `id` int(11) NOT NULL,
  `id_warga` int(11) DEFAULT NULL,
  `id_jenis_bansos` int(11) DEFAULT NULL,
  `tanggal_penerimaan` date DEFAULT NULL,
  `jumlah_terima` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `transaksi`
--

INSERT INTO `transaksi` (`id`, `id_warga`, `id_jenis_bansos`, `tanggal_penerimaan`, `jumlah_terima`) VALUES
(1, 4, 3, '0000-00-00', 56356),
(2, 4, 6, '0000-00-00', 123124),
(3, 2, 2, '2024-02-23', 20000),
(4, 5, 9, '2024-02-20', 200000);

-- --------------------------------------------------------

--
-- Table structure for table `warga`
--

CREATE TABLE `warga` (
  `id` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `alamat` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `warga`
--

INSERT INTO `warga` (`id`, `nama`, `alamat`) VALUES
(1, 'testing', 'testing'),
(2, 'testing2', 'jalan'),
(3, 'aham', 'jajaj'),
(4, 'testing', 'testing'),
(5, 'test', 'jkahskjdh'),
(6, 'kjahsdkj', 'jakshjdk'),
(7, 'safa', 'sdfgsg'),
(8, 'ssfasf', 'asfas'),
(9, 'fasfas', 'asfasf'),
(10, 'dasd', 'asdas'),
(11, 'udin', 'jahskjd'),
(12, 'jkhakjsda', 'klajlsdas'),
(13, 'asgad', 'adgad'),
(14, 'hgdhdg', 'dghgfh'),
(15, 'safas', 'asfaf'),
(16, 'asfasdfas', '12442');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bansos`
--
ALTER TABLE `bansos`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `warga`
--
ALTER TABLE `warga`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bansos`
--
ALTER TABLE `bansos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `transaksi`
--
ALTER TABLE `transaksi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `warga`
--
ALTER TABLE `warga`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
