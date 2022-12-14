CREATE DATABASE  IF NOT EXISTS `bbdd_bienes_raices_future` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bbdd_bienes_raices_future`;
-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: bbdd_bienes_raices_future
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `propiedad`
--

DROP TABLE IF EXISTS `propiedad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `propiedad` (
  `Id_Propiedad` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) NOT NULL,
  `Direccion` varchar(45) NOT NULL,
  `Contacto` varchar(45) NOT NULL,
  `Id_Tipo` int DEFAULT NULL,
  `Id_Estado` int DEFAULT NULL,
  `Id_Operatoria_Comercial` int DEFAULT NULL,
  `Id_Propietario` int DEFAULT NULL,
  PRIMARY KEY (`Id_Propiedad`),
  UNIQUE KEY `Direccion_UNIQUE` (`Direccion`),
  UNIQUE KEY `id_Propiedad_UNIQUE` (`Id_Propiedad`) /*!80000 INVISIBLE */,
  KEY `Id_Tipo_idx` (`Id_Tipo`),
  KEY `Id_Estado_idx` (`Id_Estado`),
  KEY `Id_Operacion_Comercial_idx` (`Id_Operatoria_Comercial`),
  KEY `Id_Propietario_idx` (`Id_Propietario`),
  CONSTRAINT `Id_Estado` FOREIGN KEY (`Id_Estado`) REFERENCES `estado` (`Id_Estado`),
  CONSTRAINT `Id_Operacion_Comercial` FOREIGN KEY (`Id_Operatoria_Comercial`) REFERENCES `operatoriacomercial` (`Id_Operatoria_Comercial`),
  CONSTRAINT `Id_Propietario` FOREIGN KEY (`Id_Propietario`) REFERENCES `propietario` (`Id_Propietario`),
  CONSTRAINT `Id_Tipo` FOREIGN KEY (`Id_Tipo`) REFERENCES `tipo` (`Id_Tipo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `propiedad`
--

LOCK TABLES `propiedad` WRITE;
/*!40000 ALTER TABLE `propiedad` DISABLE KEYS */;
/*!40000 ALTER TABLE `propiedad` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-25 21:58:54
