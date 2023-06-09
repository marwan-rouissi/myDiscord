-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: mydiscord
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `pseudo` varchar(255) DEFAULT NULL,
  `message` text,
  `date` varchar(255) DEFAULT NULL,
  `id_chanel` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,'Ironman','message Test\n','29/03/2023 11:47',1),(2,'Ironman','Salut \n','29/03/2023 11:48',1),(3,'Ironman','aze\n','29/03/2023 12:49',1),(4,'Ironman','Hello\n','29/03/2023 15:37',1),(5,'Ironman','lol\n','29/03/2023 15:37',1),(6,'Ironman','hey\n','29/03/2023 15:39',1),(7,'Ironman','hey\n','29/03/2023 15:40',1),(8,'Ironman','u, who r u ? \n','29/03/2023 15:41',1),(9,'Ironman','Hello\n','30/03/2023 08:04',1),(10,'Ironman','new test\n','30/03/2023 08:04',1),(11,'Ironman','New try\n','30/03/2023 08:08',1),(12,'Ironman','Hello world\n','30/03/2023 08:09',1),(13,'Ironman','Hello\n','30/03/2023 08:13',1),(14,'Ironman','Hola mundo\n','30/03/2023 08:18',1),(15,'Ironman','Hola quetal\n','30/03/2023 09:33',1),(16,'Ironman','Hello Spidey\n','30/03/2023 09:38',1),(17,'Ironman','Hola mundo\n','30/03/2023 10:47',1),(18,'Ironman','Hola mundo\n','30/03/2023 10:52',1),(19,'Ironman','Hey Spidey\n','30/03/2023 10:53',1),(20,'Ironman','Hey Spidey\n','30/03/2023 10:55',1),(21,'Ironman','Hola mundo\n','30/03/2023 10:56',1),(22,'Ironman','Hola mundo\n','30/03/2023 10:57',1),(23,'Ironman','Hey there\n','30/03/2023 11:03',1),(24,'Ironman','Hey there\n','30/03/2023 11:07',1),(25,'Ironman','Hello there\n','30/03/2023 11:11',1),(26,'Ironman','Hello there\n','30/03/2023 11:12',1),(27,'Ironman','Hey there\n','30/03/2023 11:13',1),(28,'Ironman','Hola mundo\n','30/03/2023 11:15',1),(29,'Ironman','hola mundo\n','30/03/2023 11:26',1),(30,'Ironman','Hola mundo\n','30/03/2023 11:28',1),(31,'Ironman','Hola mundo\n','30/03/2023 11:33',1),(32,'Ironman','Hey\n','30/03/2023 11:35',1),(33,'Ironman','Hello world\n','30/03/2023 11:35',1),(34,'Ironman','Hello world\n','30/03/2023 11:36',1),(35,'Ironman','Hello there\n','30/03/2023 11:38',1),(36,'Ironman','Hello there\n','30/03/2023 11:39',1),(37,'Ironman','Hello there\n','30/03/2023 11:40',1),(38,'Ironman','Hello there\n','30/03/2023 11:41',1),(39,'Ironman','Hello there\n','30/03/2023 11:43',1),(40,'Ironman','Hello there\n','30/03/2023 11:48',1),(41,'Ironman','Hello there\n','30/03/2023 11:49',1),(42,'Ironman','Hello there\n','30/03/2023 11:51',1),(43,'Ironman','Hola mundo\n','30/03/2023 11:52',1),(44,'Ironman','Hola mundo\n','30/03/2023 11:53',1),(45,'Ironman','Hola mundo\n','30/03/2023 11:54',1),(46,'Ironman','Hello there\n','30/03/2023 11:55',1),(47,'Ironman','Hey hey hey\n','30/03/2023 11:56',1),(48,'Spiderman','Hello there ','30/03/2023 12:01:',1),(49,'Ironman','Hey ','30/03/2023 12:01:',1),(50,'Ironman','Hey ','30/03/2023 12:07:',1),(51,'Spiderman','','30/03/2023 12:07:',1),(52,'Spiderman','Hey ','30/03/2023 12:09:',1),(53,'Ironman','test ','30/03/2023 12:10:',1),(54,'Spiderman','','30/03/2023 12:18:',1),(55,'Spiderman','fail ','30/03/2023 12:18:',1),(56,'Ironman','Hello ','30/03/2023 12:22:',1),(57,'Spiderman','ok ok ','30/03/2023 12:24:',1),(58,'Brayne','Hey ','30/03/2023 12:28:',1),(59,'Ironman','What\'s up ?! ','30/03/2023 12:44:',1),(60,'Ironman','Hey ','31/03/2023 08:10:',1),(61,'Ironman','hey ','01/04/2023 10:15:',1),(62,'Ironman','good morning ','01/04/2023 10:30:',1),(63,'Spiderman','hello ','01/04/2023 10:32:',1),(64,'Ironman','hey ','01/04/2023 11:10:',1);
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) DEFAULT NULL,
  `prenom` varchar(255) DEFAULT NULL,
  `pseudo` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `passwd` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Wick','John','JoWick','john.wick@laplateforme.io','babayaga'),(2,'Wayne','Bruce','Brayne','bruce.wayne@laplateforme.io','imbatman'),(3,'Kent','Clark','Clent','clark.kent@laplateforme.io','imsuperman'),(4,'Stark','Tony','Ironman','tony.stark@laplateforme.io','imironman'),(5,'Parker','Peter','Spiderman','peter.parker@laplateforme.io','imspiderman');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-01 11:18:04
