-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: Library
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `ADM_ID` varchar(40) NOT NULL,
  `ADM_NAME` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ADM_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES ('admin','admin');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book_class`
--

DROP TABLE IF EXISTS `book_class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_class` (
  `class_name` varchar(20) DEFAULT NULL,
  `class_id` varchar(20) NOT NULL,
  PRIMARY KEY (`class_id`),
  KEY `idx_class` (`class_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_class`
--

LOCK TABLES `book_class` WRITE;
/*!40000 ALTER TABLE `book_class` DISABLE KEYS */;
INSERT INTO `book_class` VALUES ('军事','123'),('娱乐','3123342'),('学术','3123'),('悲剧','555'),('教育','312312'),('文学','75675'),('烂漫','13124'),('爱情','520'),('现实','321'),('经济','12313'),('艺术','1231312');
/*!40000 ALTER TABLE `book_class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `BOOK_ID` varchar(20) NOT NULL,
  `BNAME` varchar(40) DEFAULT NULL,
  `publisher` varchar(40) DEFAULT NULL,
  `AUTHOR` varchar(40) DEFAULT NULL,
  `CDATE` date DEFAULT NULL,
  `CLASS` varchar(30) DEFAULT NULL,
  `FLAG` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`BOOK_ID`),
  KEY `CLASS` (`CLASS`),
  CONSTRAINT `CLASS` FOREIGN KEY (`CLASS`) REFERENCES `book_class` (`class_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES ('10000','葬爱','人民出版社','花心','3913-08-21','爱情',0),('1001','葬爱','人民出版社','花心','2022-03-02','爱情',0),('1002','葬爱','人民出版社','花心','2022-03-02','爱情',0),('1011','活着','清华出版社','MIke','2003-03-02','现实',1),('1012','活着','清华出版社','MIke','2003-03-02','现实',0),('1013','活着','清华出版社','MIke','2003-03-02','现实',1),('1021','百年孤独','哈工大出版社','laohuang','2003-03-01','悲剧',1),('1022','百年孤独','哈工大出版社','laohuang','2003-03-01','悲剧',1),('1023','百年孤独','哈工大出版社','laohuang','2003-03-01','悲剧',1),('1031','平凡的世界','哈工大出版社','John','2005-03-02','烂漫',0),('1032','平凡的世界','哈工大出版社','John','2005-03-02','烂漫',0),('123234','真的','哈工大出版社','假的','2022-03-04','文学',1),('1233','我不爱这个世界只爱你捏','小i出版社','只！','9999-09-09','爱情',1),('9999','玫瑰花','清华出版社','小u','2021-03-21','文学',1);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `borrow_record`
--

DROP TABLE IF EXISTS `borrow_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `borrow_record` (
  `R_ID` int NOT NULL AUTO_INCREMENT,
  `STU_ID` varchar(40) DEFAULT NULL,
  `BOOK_ID` varchar(40) DEFAULT NULL,
  `BDATE` date DEFAULT NULL,
  PRIMARY KEY (`R_ID`),
  KEY `STU_ID` (`STU_ID`),
  KEY `BOOK_ID` (`BOOK_ID`),
  CONSTRAINT `borrow_record_ibfk_1` FOREIGN KEY (`STU_ID`) REFERENCES `users` (`STU_ID`),
  CONSTRAINT `borrow_record_ibfk_2` FOREIGN KEY (`BOOK_ID`) REFERENCES `books` (`BOOK_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `borrow_record`
--

LOCK TABLES `borrow_record` WRITE;
/*!40000 ALTER TABLE `borrow_record` DISABLE KEYS */;
INSERT INTO `borrow_record` VALUES (11,'2021110751','1001','2023-11-11'),(14,'2021110751','1021','2023-11-11'),(15,'2021110751','1022','2023-11-11'),(16,'1','1011','2023-11-11'),(17,'2021110751','1012','2023-11-11'),(18,'2021110751','1013','2023-11-11'),(19,'2021110751','1001','2023-11-11'),(22,'2021110751','1001','2023-11-11'),(23,'2021110751','1011','2023-11-11'),(24,'2021110751','1031','2023-11-11'),(25,'2021110751','1032','2023-11-11'),(28,'2021110751','1012','2023-11-11'),(30,'2021110751','1031','2023-11-11'),(31,'2021110751','1032','2023-11-11'),(33,'2021110751','1021','2023-11-11'),(38,'2021110751','1011','2023-11-11'),(40,'2021110751','123234','2023-11-12'),(41,'2021110751','1031','2023-11-19'),(42,'2021110751','1011','2023-11-19'),(43,'2021110751','1011','2023-11-19'),(44,'2021110751','1031','2024-05-13'),(45,'2021110751','1032','2024-05-13');
/*!40000 ALTER TABLE `borrow_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `borrowed_book`
--

DROP TABLE IF EXISTS `borrowed_book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `borrowed_book` (
  `BOOK_ID` varchar(20) NOT NULL,
  `STU_ID` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`BOOK_ID`),
  KEY `STU_ID` (`STU_ID`),
  CONSTRAINT `borrowed_book_ibfk_1` FOREIGN KEY (`STU_ID`) REFERENCES `users` (`STU_ID`),
  CONSTRAINT `borrowed_book_ibfk_2` FOREIGN KEY (`BOOK_ID`) REFERENCES `books` (`BOOK_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `borrowed_book`
--

LOCK TABLES `borrowed_book` WRITE;
/*!40000 ALTER TABLE `borrowed_book` DISABLE KEYS */;
INSERT INTO `borrowed_book` VALUES ('1001','1'),('1012','2021110751'),('1031','2021110751'),('1032','2021110751');
/*!40000 ALTER TABLE `borrowed_book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `send_record`
--

DROP TABLE IF EXISTS `send_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `send_record` (
  `S_ID` int NOT NULL AUTO_INCREMENT,
  `STU_ID` varchar(40) DEFAULT NULL,
  `BOOK_ID` varchar(40) DEFAULT NULL,
  `BDATE` date DEFAULT NULL,
  PRIMARY KEY (`S_ID`),
  KEY `STU_ID` (`STU_ID`),
  KEY `BOOK_ID` (`BOOK_ID`),
  CONSTRAINT `send_record_ibfk_1` FOREIGN KEY (`STU_ID`) REFERENCES `users` (`STU_ID`),
  CONSTRAINT `send_record_ibfk_2` FOREIGN KEY (`BOOK_ID`) REFERENCES `books` (`BOOK_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `send_record`
--

LOCK TABLES `send_record` WRITE;
/*!40000 ALTER TABLE `send_record` DISABLE KEYS */;
INSERT INTO `send_record` VALUES (11,'2021110751','1022','2023-11-11'),(17,'2021110751','1021','2023-11-11'),(18,'2021110751','1013','2023-11-11'),(34,'1','1233','2023-11-12'),(35,'2021110751','1031','2023-11-19'),(36,'2021110751','1011','2023-11-19'),(37,'2021110751','1011','2023-11-19'),(38,'2021110751','123234','2024-05-13');
/*!40000 ALTER TABLE `send_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `SNAME` varchar(40) NOT NULL,
  `STU_ID` varchar(40) NOT NULL,
  `sex` varchar(2) NOT NULL,
  `birth` date DEFAULT NULL,
  PRIMARY KEY (`STU_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('1','1','男','2023-11-11'),('2','2','女','2022-02-04'),('lx','2021110751','男','2001-09-19');
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

-- Dump completed on 2024-05-13 16:23:01
