-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: tahlel2
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `addanalyst`
--

DROP TABLE IF EXISTS `addanalyst`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `addanalyst` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `price` int DEFAULT NULL,
  `category` varchar(45) DEFAULT NULL,
  `sub_category` varchar(45) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `unit` text,
  `defult` text,
  `results` varchar(455) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=88 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addanalyst`
--

LOCK TABLES `addanalyst` WRITE;
/*!40000 ALTER TABLE `addanalyst` DISABLE KEYS */;
INSERT INTO `addanalyst` VALUES (5,'Random  blood sugar',2,'عدد','bio','2021-04-20 04:55:06','mg/dl','random def',''),(6,'Blood Urea',3,'عدد','bio','2021-02-22 23:11:50','mg2/dl','def2,g',NULL),(7,'S. Creatinin',3,'عدد','bio','2021-02-22 23:13:53',NULL,NULL,NULL),(8,'S. Uric acid',3,'عدد','bio','2021-02-22 23:14:50',NULL,NULL,NULL),(9,'S. Cholesterol',3,'عدد','bio','2021-02-22 23:15:47',NULL,NULL,NULL),(10,'S. Triglycerid',3,'عدد','bio','2021-02-22 23:16:20',NULL,NULL,NULL),(11,'Total serum Bilirubin',3,'عدد','bio','2021-02-22 23:17:26',NULL,NULL,NULL),(12,'S.Calcium',3,'عدد','bio','2021-02-22 23:18:14',NULL,NULL,NULL),(13,'Vitamin D',10,'عدد','bio','2021-02-22 23:18:58',NULL,NULL,NULL),(14,'Color:GSE',0,'خيارات','Full GSE','2021-02-22 23:20:34',NULL,NULL,'\'yallow\', \'brown\', \'green\', \'milk\''),(15,'Consistency',0,'خيارات','Full GSE','2021-02-22 23:22:08',NULL,NULL,'\'Solid\', \'Liquid\', \'Semi solid\', \'Semi liquid\', \'Mucoid\''),(16,'R.B.Cs:GSE',0,'خيارات','Full GSE','2021-02-22 23:22:58',NULL,NULL,'\'1 - 2\', \'1 - 3\', \'2 - 3\', \'2 - 4\', \'0 - 1\', \'0 - 2\', \'3 - 5\', \'4 - 6\', \'5 - 6\','),(17,'Pus cells:GSE',0,'خيارات','Full GSE','2021-02-22 23:23:17',NULL,NULL,'\'1 - 2\', \'1 - 3\', \'2 - 3\', \'2 - 4\', \'0 - 1\', \'0 - 2\', \'3 - 5\', \'4 - 6\', \'5 - 6\','),(18,'E. Histolytica',0,'خيارات','Full GSE','2021-02-22 23:23:41',NULL,NULL,'\'Cyst\', \'Trophozoite\''),(19,'G. Lembilia',0,'خيارات','Full GSE','2021-02-22 23:24:19',NULL,NULL,'\'Cyst\', \'Trophozoite\''),(20,'Ova',0,'خيارات','Full GSE','2021-02-22 23:24:56',NULL,NULL,'\'Nill\''),(21,'Other:GSE',0,'خيارات','Full GSE','2021-02-22 23:25:22',NULL,NULL,NULL),(22,'Appearance',0,'خيارات','Full GUE','2021-02-22 23:26:16',NULL,NULL,'\'Turbid\', \'Clear\''),(23,'Reaction:GUE',0,'خيارات','Full GUE','2021-02-22 23:26:37',NULL,NULL,'\'Acidic\', \'Alkaline\''),(24,'Albumin',0,'خيارات','Full GUE','2021-02-22 23:26:57',NULL,NULL,'\'Nil\', \'+\', \'++\', \'+++\', \'Trace\''),(25,'Sugar',0,'خيارات','Full GUE','2021-02-22 23:27:30',NULL,NULL,'\'Nil\', \'+\', \'++\', \'+++\', \'Trace\''),(26,'RBCs:GUE',0,'خيارات','Full GUE','2021-02-22 23:28:04',NULL,NULL,'\'1 - 2\', \'1 - 3\', \'2 - 3\', \'2 - 4\', \'0 - 1\', \'0 - 2\', \'3 - 5\', \'4 - 6\', \'5 - 6\','),(27,'Pus cells:GUE',0,'خيارات','Full GUE','2021-02-22 23:28:29',NULL,NULL,'\'1 - 2\', \'1 - 3\', \'2 - 3\', \'2 - 4\', \'0 - 1\', \'0 - 2\', \'3 - 5\', \'4 - 6\', \'5 - 6\','),(28,'Epith .cells',0,'خيارات','Full GUE','2021-02-22 23:28:59',NULL,NULL,'\'Few\', \'+\', \'++\', \'+++\', \'++++\''),(29,'Crystals',0,'خيارات','Full GUE','2021-02-22 23:29:30',NULL,NULL,'\'Am.Urate\', \'Am.Phosphatase\', \'Uric Acid\', \'Ca.Oxalate\''),(30,'Casts',0,'خيارات','Full GUE','2021-02-22 23:30:06',NULL,NULL,'\'Granular cast +\', \'Granular cast ++\', \'Granular cast +++\''),(31,'Other:GUE',0,'خيارات','Full GUE','2021-02-22 23:30:39',NULL,NULL,NULL),(32,'Hb',3,'خيارات مع تعديل','hematology','2021-02-22 23:31:12',NULL,NULL,'4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18'),(33,'PCV',3,'عدد','hematology','2021-02-22 23:31:42',NULL,NULL,NULL),(34,'WBCs',3,'عدد','hematology','2021-02-22 23:32:10',NULL,NULL,NULL),(35,'E.S.R',3,'عدد','hematology','2021-02-22 23:32:33',NULL,NULL,'\'A (+ve)\', \'B (+ve)\', \'AB (+ve)\', \'O (+ve)\', \'O (-ve)\', \'A (-ve)\', \'B (-ve)\', \'AB (-ve)\''),(36,'Blood Group',3,'خيارات','hematology','2021-02-22 23:33:03',NULL,NULL,'\'yellow\',\'green\',\'red\''),(37,'Rh',3,'خيارات','hematology','2021-02-22 23:33:30',NULL,NULL,NULL),(38,'Pregnancy test  in urine',3,'خيارات','hematology','2021-02-22 23:34:12',NULL,NULL,'\'Positive (+ve)\', \'Negative (-ve)\', \'Weak Positive\''),(39,'Pregnancy test  in serum',3,'خيارات','hematology','2021-02-22 23:34:40',NULL,NULL,'\'Positive (+ve)\', \'Negative (-ve)\''),(40,'R.B.Sugar',2,'عدد','hematology','2021-02-22 23:35:07',NULL,NULL,NULL),(41,'Bl. Urea',3,'عدد','hematology','2021-02-22 23:35:28',NULL,NULL,NULL),(42,'Salmonella typhi  IgG',4,'خيارات','hematology','2021-02-22 23:35:50',NULL,NULL,'\'Positive (+ve)\', \'Negative (-ve)\''),(43,'Salmonella typhi  IgM',4,'خيارات','hematology','2021-02-22 23:36:16',NULL,NULL,'\'Positive (+ve)\', \'Negative (-ve)\''),(44,'Rose-Bengal test',3,'خيارات','hematology','2021-02-22 23:36:34',NULL,NULL,'\'Positive (+ve)\', \'Negative (-ve)\''),(45,'T3',7,'عدد','هرمونات مشترك','2021-02-23 23:10:14',NULL,NULL,NULL),(46,'T4',7,'عدد','هرمونات مشترك','2021-02-23 23:11:06',NULL,NULL,NULL),(47,'TSH',7,'عدد','هرمونات مشترك','2021-02-23 23:11:36',NULL,NULL,NULL),(48,'LH',10,'عدد','هرمونات مشترك','2021-02-23 23:12:03',NULL,NULL,NULL),(49,'FSH',10,'عدد','هرمونات مشترك','2021-02-23 23:12:41',NULL,NULL,NULL),(50,'Prolactin',10,'عدد','هرمونات مشترك','2021-02-23 23:13:23',NULL,NULL,NULL),(51,'Testosterone',10,'عدد','هرمونات مشترك','2021-02-23 23:13:55',NULL,NULL,'\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\','),(52,'Toxoplasma IgG',10,'خيارات','هرمونات مشترك','2021-02-23 23:38:11',NULL,NULL,'\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\','),(53,'Toxoplasma IgM',10,'خيارات','هرمونات مشترك','2021-02-23 23:38:29',NULL,NULL,'\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\','),(54,'Cytomegalo Virus IgG',10,'خيارات','هرمونات مشترك','2021-02-23 23:40:00',NULL,NULL,'\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\','),(55,'Cytomegalo Virus IgM',10,'خيارات','هرمونات مشترك','2021-02-23 23:40:25',NULL,NULL,'\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\','),(56,'Rubella IgG',10,'خيارات','هرمونات مشترك','2021-02-23 23:40:45',NULL,NULL,'\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\','),(57,'Rubella IgM',10,'خيارات','هرمونات مشترك','2021-02-23 23:36:56',NULL,NULL,'\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\','),(58,'Anti - Phspholipin IgG',10,'خيارات','هرمونات مشترك','2021-02-23 23:41:17',NULL,NULL,'\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\','),(59,'Anti - Phspholipin  IgM',10,'خيارات','هرمونات مشترك','2021-02-23 23:41:44',NULL,NULL,'\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\','),(60,'Anti - Cardiolipin  IgG',10,'خيارات','هرمونات مشترك','2021-02-23 23:41:58',NULL,NULL,'\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\','),(61,'Anti - Cardiolipin  IgM',10,'خيارات','هرمونات مشترك','2021-02-23 23:42:14',NULL,NULL,'\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\','),(62,'Herps   IgG',10,'خيارات','هرمونات مشترك','2021-02-23 23:42:34',NULL,NULL,'\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\','),(63,'Herpes  IgM',10,'خيارات','هرمونات مشترك','2021-02-23 23:42:50',NULL,NULL,'\'0.5 Negative\', \'0.6 Negative\', \'0.7 Negative\', \'0.8 Negative\', \'1.1 Positive\', \'1.1 Positive\','),(65,'Volume',0,'خيارات','Full SFA',NULL,NULL,NULL,'\'0.5\', \'0.6\', \'0.7\''),(66,'Reaction:SFA',0,'خيارات','Full SFA',NULL,NULL,NULL,'\'Acidic\', \'Alkaline\''),(67,'Colour:SFA',0,'خيارات','Full SFA',NULL,NULL,NULL,'\'yallow\', \'brown\', \'green\', \'milk\''),(68,'Liquefaction',0,'خيارات','Full SFA',NULL,NULL,NULL,'\'5\', \'10\', \'15\', \'20\', \'25\', \'30\', \'35\', \'40\', \'45\''),(69,'Count',0,'عدد','Full SFA',NULL,NULL,NULL,NULL),(70,'Motility:Active',0,'خيارات','Full SFA',NULL,NULL,NULL,'\'5\', \'10\', \'15\', \'20\', \'25\', \'30\', \'35\', \'40\', \'45\', \'50\', \'55\', \'60\', \'65\', \'70\', \'75\', \'80\','),(71,'Motility:Sluggish',0,'خيارات','Full SFA',NULL,NULL,NULL,'\'5\', \'10\', \'15\', \'20\', \'25\', \'30\', \'35\', \'40\', \'45\', \'50\', \'55\', \'60\', \'65\', \'70\', \'75\', \'80\','),(72,'Motility:Dead',0,'خيارات','Full SFA',NULL,NULL,NULL,'\'5\', \'10\', \'15\', \'20\', \'25\', \'30\', \'35\', \'40\', \'45\', \'50\', \'55\', \'60\', \'65\', \'70\', \'75\', \'80\','),(73,'Morphology:Normal',0,'خيارات','Full SFA',NULL,NULL,NULL,'\'5\', \'10\', \'15\', \'20\', \'25\', \'30\', \'35\', \'40\', \'45\', \'50\', \'55\', \'60\', \'65\', \'70\', \'75\', \'80\','),(74,'Morphology:Abnormal',0,'خيارات','Full SFA',NULL,NULL,NULL,'\'5\', \'10\', \'15\', \'20\', \'25\', \'30\', \'35\', \'40\', \'45\', \'50\', \'55\', \'60\', \'65\', \'70\', \'75\', \'80\','),(75,'Morphology:Pus cells',0,'خيارات','Full SFA',NULL,NULL,NULL,'\'5\', \'10\', \'15\', \'20\', \'25\', \'30\', \'35\', \'40\', \'45\', \'50\', \'55\', \'60\', \'65\', \'70\', \'75\', \'80\','),(76,'Other:SFA',0,'خيارات','Full SFA',NULL,NULL,NULL,NULL),(77,'HBS Ag',5,'خيارات','hematology',NULL,NULL,NULL,NULL),(78,'HCV Ab',5,'خيارات','hematology',NULL,NULL,NULL,NULL),(79,'HIV',5,'خيارات','hematology',NULL,NULL,NULL,NULL),(80,'Bacteria:GSE',0,'خيارات','Full GSE',NULL,NULL,NULL,'\'Few\', \'+\', \'++\', \'+++\', \'++++\''),(81,'Monillia:GSE',0,'خيارات','Full GSE',NULL,NULL,NULL,'\'Few\', \'+\', \'++\', \'+++\', \'++++\''),(82,'Fatty drop:GSE',0,'خيارات','Full GSE',NULL,NULL,NULL,'\'Few\', \'+\', \'++\', \'+++\', \'++++\''),(83,'Bacteria:GUE',0,'خيارات','Full GUE',NULL,NULL,NULL,'\'Few\', \'+\', \'++\', \'+++\', \'++++\''),(84,'Monillia:GUE',0,'خيارات','Full GUE',NULL,NULL,NULL,'\'Few\', \'+\', \'++\', \'+++\', \'++++\''),(85,'Mucuse:GUE',0,'خيارات','Full GUE',NULL,NULL,NULL,'\'Few\', \'+\', \'++\', \'+++\', \'++++\''),(87,'new2',6,'خيارات مع تعديل','bio','2021-04-15 20:30:02','none','no','\'gg\', \' hello\', \' hi\'');
/*!40000 ALTER TABLE `addanalyst` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `addbuys`
--

DROP TABLE IF EXISTS `addbuys`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `addbuys` (
  `id` int NOT NULL AUTO_INCREMENT,
  `item_name` varchar(255) DEFAULT NULL,
  `signal_item_price` int DEFAULT NULL,
  `total_price` int DEFAULT NULL,
  `buys_type` varchar(255) DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addbuys`
--

LOCK TABLES `addbuys` WRITE;
/*!40000 ALTER TABLE `addbuys` DISABLE KEYS */;
INSERT INTO `addbuys` VALUES (1,'ali',21,100,'--------------',16,'2000-01-01 00:00:00'),(3,'item_name',10,100,'item_type',18,'2021-02-12 18:12:14');
/*!40000 ALTER TABLE `addbuys` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `addclient`
--

DROP TABLE IF EXISTS `addclient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `addclient` (
  `id` int NOT NULL AUTO_INCREMENT,
  `client_name` varchar(255) DEFAULT NULL,
  `client_age` int DEFAULT NULL,
  `client_genus` varchar(255) DEFAULT NULL,
  `client_doctor` varchar(255) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1354 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addclient`
--

LOCK TABLES `addclient` WRITE;
/*!40000 ALTER TABLE `addclient` DISABLE KEYS */;
INSERT INTO `addclient` VALUES (1,'alia',12,'ذكر','hj','2021-02-23 22:32:45'),(1228,'aliii',20,'انثى','عدوية شمس سعيد','2021-04-16 03:04:28'),(1229,'aliii',20,'انثى','عدوية شمس سعيد','2021-04-16 03:04:29'),(1230,'aliii',20,'انثى','عدوية شمس سعيد','2021-04-16 03:04:30'),(1231,'aliii',20,'انثى','عدوية شمس سعيد','2021-04-16 03:04:30'),(1232,'aliii',20,'انثى','عدوية شمس سعيد','2021-04-16 03:04:31'),(1233,'aliii',20,'انثى','عدوية شمس سعيد','2021-04-16 03:04:32'),(1234,'aliii',20,'انثى','عدوية شمس سعيد','2021-04-16 03:04:32'),(1235,'aliii',20,'انثى','عدوية شمس سعيد','2021-04-16 03:04:33'),(1236,'aliii',20,'انثى','عدوية شمس سعيد','2021-04-16 03:04:33'),(1237,'aliii',20,'انثى','عدوية شمس سعيد','2021-04-16 03:04:34'),(1238,'aliii',20,'انثى','عدوية شمس سعيد','2021-04-16 03:04:35'),(1239,'aliii',20,'انثى','عدوية شمس سعيد','2021-04-17 01:36:38'),(1240,'احمد جديد 100',25,'ذكر','عدوية شمس سعيد','2021-04-19 02:47:46'),(1241,'احمد جديد 100',25,'ذكر','عدوية شمس سعيد','2021-04-19 02:47:47'),(1242,'احمد جديد 100',25,'ذكر','عدوية شمس سعيد','2021-04-19 02:47:47'),(1312,'',20,'انثى','عدوية شمس سعيد','2021-04-20 06:04:39'),(1313,'',20,'انثى','عدوية شمس سعيد','2021-04-20 06:07:40'),(1314,'',20,'انثى','عدوية شمس سعيد','2021-04-20 06:07:44'),(1315,'new',20,'ذكر','عدوية شمس سعيد','2021-04-20 06:33:27'),(1316,'new',20,'ذكر','عدوية شمس سعيد','2021-04-20 06:33:28'),(1317,'new',20,'ذكر','عدوية شمس سعيد','2021-04-20 06:34:09'),(1318,'new',20,'ذكر','عدوية شمس سعيد','2021-04-20 06:34:10'),(1319,'new',20,'ذكر','عدوية شمس سعيد','2021-04-20 06:37:00'),(1320,'new',20,'ذكر','عدوية شمس سعيد','2021-04-20 06:37:01'),(1321,'kmkmdklmd',20,'انثى','عدوية شمس سعيد','2021-04-20 06:43:47'),(1322,'kmkmdklmd',20,'انثى','عدوية شمس سعيد','2021-04-20 06:43:48'),(1323,'kmkmdklmd',20,'انثى','عدوية شمس سعيد','2021-04-20 06:49:27'),(1324,'kmkmdklmd',20,'انثى','عدوية شمس سعيد','2021-04-20 06:50:36'),(1325,'kmkmdklmd',20,'انثى','عدوية شمس سعيد','2021-04-20 06:50:37'),(1326,'kmkmdklmd',20,'انثى','عدوية شمس سعيد','2021-04-20 06:53:39'),(1327,'kmkmdklmd',20,'انثى','عدوية شمس سعيد','2021-04-20 06:53:40'),(1328,'kmkmdklmd',20,'انثى','عدوية شمس سعيد','2021-04-20 06:56:32'),(1329,'kmkmdklmd',20,'انثى','عدوية شمس سعيد','2021-04-20 07:18:46'),(1330,'',20,'انثى','عدوية شمس سعيد','2021-04-20 07:31:12'),(1331,'',20,'انثى','عدوية شمس سعيد','2021-04-20 07:31:13'),(1332,'',20,'انثى','عدوية شمس سعيد','2021-04-20 07:31:13'),(1333,'',20,'انثى','عدوية شمس سعيد','2021-04-20 07:31:14'),(1334,'',20,'انثى','عدوية شمس سعيد','2021-04-20 07:31:15'),(1335,'',20,'انثى','عدوية شمس سعيد','2021-04-20 07:31:16'),(1336,'',20,'انثى','عدوية شمس سعيد','2021-04-20 07:31:16'),(1337,'',20,'انثى','عدوية شمس سعيد','2021-04-20 07:31:17'),(1338,'',20,'انثى','عدوية شمس سعيد','2021-04-20 07:31:18'),(1339,'',20,'انثى','عدوية شمس سعيد','2021-04-20 07:31:19'),(1340,'',20,'انثى','عدوية شمس سعيد','2021-04-20 07:31:20'),(1341,'',20,'انثى','عدوية شمس سعيد','2021-04-20 07:31:40'),(1342,'',20,'انثى','عدوية شمس سعيد','2021-04-20 07:31:40'),(1343,'',20,'انثى','عدوية شمس سعيد','2021-04-20 07:31:41'),(1344,'',20,'انثى','عدوية شمس سعيد','2021-04-20 07:31:42'),(1345,'',20,'انثى','عدوية شمس سعيد','2021-04-20 07:31:44'),(1346,'',20,'انثى','عدوية شمس سعيد','2021-04-20 07:31:45'),(1347,'',20,'انثى','عدوية شمس سعيد','2021-04-20 07:31:45'),(1348,'',20,'انثى','عدوية شمس سعيد','2021-04-20 07:31:46'),(1349,'',20,'انثى','عدوية شمس سعيد','2021-04-20 07:31:47'),(1350,'',20,'انثى','عدوية شمس سعيد','2021-04-20 07:31:48'),(1351,'',20,'انثى','عدوية شمس سعيد','2021-04-20 07:31:49'),(1352,'',20,'انثى','عدوية شمس سعيد','2021-04-20 07:31:50'),(1353,'kmkmdklmd',20,'انثى','عدوية شمس سعيد','2021-04-20 19:57:27');
/*!40000 ALTER TABLE `addclient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `addnewitem`
--

DROP TABLE IF EXISTS `addnewitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `addnewitem` (
  `id` int NOT NULL AUTO_INCREMENT,
  `client_name` varchar(255) NOT NULL,
  `client_id` int DEFAULT NULL,
  `client_age` int DEFAULT NULL,
  `genus` varchar(255) NOT NULL,
  `doctor_name` varchar(255) NOT NULL,
  `notes` text,
  `analyst_name` varchar(255) NOT NULL,
  `analyst_result` varchar(255) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `total_price` varchar(45) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1323 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addnewitem`
--

LOCK TABLES `addnewitem` WRITE;
/*!40000 ALTER TABLE `addnewitem` DISABLE KEYS */;
INSERT INTO `addnewitem` VALUES (1,'alia',1,12,'ذكر','hj','jh','Random  blood sugar ','13',0,'0','2021-02-23 22:32:45'),(1197,'aliii',1228,20,'انثى','عدوية شمس سعيد','','Color:GSE','yallow',0,'0','2021-04-16 03:04:28'),(1198,'aliii',1228,20,'انثى','عدوية شمس سعيد','','Consistency','Solid',0,'0','2021-04-16 03:04:29'),(1199,'aliii',1228,20,'انثى','عدوية شمس سعيد','','R.B.Cs:GSE','1 - 2',0,'0','2021-04-16 03:04:30'),(1200,'aliii',1228,20,'انثى','عدوية شمس سعيد','','Pus cells:GSE','1 - 2',0,'0','2021-04-16 03:04:30'),(1201,'aliii',1228,20,'انثى','عدوية شمس سعيد','','E. Histolytica','Cyst',0,'0','2021-04-16 03:04:31'),(1202,'aliii',1228,20,'انثى','عدوية شمس سعيد','','G. Lembilia','Cyst',0,'0','2021-04-16 03:04:32'),(1203,'aliii',1228,20,'انثى','عدوية شمس سعيد','','Ova','Nill',0,'0','2021-04-16 03:04:32'),(1204,'aliii',1228,20,'انثى','عدوية شمس سعيد','','Other:GSE','',0,'0','2021-04-16 03:04:33'),(1205,'aliii',1228,20,'انثى','عدوية شمس سعيد','','Bacteria:GSE','Few',0,'0','2021-04-16 03:04:34'),(1206,'aliii',1228,20,'انثى','عدوية شمس سعيد','','Monillia:GSE','Few',0,'0','2021-04-16 03:04:34'),(1207,'aliii',1228,20,'انثى','عدوية شمس سعيد','','Fatty drop:GSE','Few',0,'0','2021-04-16 03:04:35'),(1208,'aliii',1228,20,'انثى','عدوية شمس سعيد','','Random  blood sugar','3',2,'2','2021-04-17 01:36:38'),(1209,'احمد جديد 100',1240,25,'ذكر','عدوية شمس سعيد','نو','S. Cholesterol','0',3,'3','2021-04-19 02:47:46'),(1210,'احمد جديد 100',1240,25,'ذكر','عدوية شمس سعيد','نو','Vitamin D','0',10,'10','2021-04-19 02:47:47'),(1211,'احمد جديد 100',1240,25,'ذكر','عدوية شمس سعيد','نو','Pus cells:GUE','',0,'0','2021-04-19 02:47:48'),(1281,'',1301,20,'انثى','عدوية شمس سعيد','','Random  blood sugar','',2,'2','2021-04-20 06:04:40'),(1282,'',1301,20,'انثى','عدوية شمس سعيد','','Blood Group','green',3,'3','2021-04-20 06:07:40'),(1283,'',1301,20,'انثى','عدوية شمس سعيد','','Blood Group','green',3,'3','2021-04-20 06:07:44'),(1284,'new',1315,20,'ذكر','عدوية شمس سعيد','','Random  blood sugar','',2,'2','2021-04-20 06:33:27'),(1285,'new',1315,20,'ذكر','عدوية شمس سعيد','','Random  blood sugar','',2,'2','2021-04-20 06:33:28'),(1286,'new',1315,20,'ذكر','عدوية شمس سعيد','','Blood Urea','',3,'3','2021-04-20 06:34:09'),(1287,'new',1315,20,'ذكر','عدوية شمس سعيد','','Blood Urea','',3,'3','2021-04-20 06:34:10'),(1288,'new',1315,20,'ذكر','عدوية شمس سعيد','','S. Creatinin','',3,'3','2021-04-20 06:37:00'),(1289,'new',1315,20,'ذكر','عدوية شمس سعيد','','S. Creatinin','',3,'3','2021-04-20 06:37:01'),(1290,'kmkmdklmd',1321,20,'انثى','عدوية شمس سعيد','','Blood Urea','',3,'3','2021-04-20 06:43:47'),(1291,'kmkmdklmd',1321,20,'انثى','عدوية شمس سعيد','','Blood Urea','',3,'3','2021-04-20 06:43:48'),(1292,'kmkmdklmd',1321,20,'انثى','عدوية شمس سعيد','','S. Creatinin','',3,'3','2021-04-20 06:49:27'),(1293,'kmkmdklmd',1321,20,'انثى','عدوية شمس سعيد','','S. Triglycerid','',3,'3','2021-04-20 06:50:37'),(1294,'kmkmdklmd',1321,20,'انثى','عدوية شمس سعيد','','S. Triglycerid','',3,'3','2021-04-20 06:50:37'),(1299,'',1301,20,'انثى','عدوية شمس سعيد','','Color:GSE',' green',0,'0','2021-04-20 07:31:12'),(1300,'',1301,20,'انثى','عدوية شمس سعيد','','Consistency','Solid',0,'0','2021-04-20 07:31:13'),(1301,'',1301,20,'انثى','عدوية شمس سعيد','','R.B.Cs:GSE','1 - 2',0,'0','2021-04-20 07:31:14'),(1302,'',1301,20,'انثى','عدوية شمس سعيد','','Pus cells:GSE','1 - 2',0,'0','2021-04-20 07:31:14'),(1303,'',1301,20,'انثى','عدوية شمس سعيد','','E. Histolytica','Cyst',0,'0','2021-04-20 07:31:15'),(1304,'',1301,20,'انثى','عدوية شمس سعيد','','G. Lembilia','Cyst',0,'0','2021-04-20 07:31:16'),(1305,'',1301,20,'انثى','عدوية شمس سعيد','','Ova','Nill',0,'0','2021-04-20 07:31:16'),(1306,'',1301,20,'انثى','عدوية شمس سعيد','','Other:GSE','None',0,'0','2021-04-20 07:31:17'),(1307,'',1301,20,'انثى','عدوية شمس سعيد','','Bacteria:GSE','Few',0,'0','2021-04-20 07:31:18'),(1308,'',1301,20,'انثى','عدوية شمس سعيد','','Monillia:GSE','Few',0,'0','2021-04-20 07:31:19'),(1309,'',1301,20,'انثى','عدوية شمس سعيد','','Fatty drop:GSE',' +++',0,'0','2021-04-20 07:31:20'),(1310,'',1301,20,'انثى','عدوية شمس سعيد','','Volume','0.5',0,'0','2021-04-20 07:31:40'),(1311,'',1301,20,'انثى','عدوية شمس سعيد','','Reaction:SFA','Acidic',0,'0','2021-04-20 07:31:41'),(1312,'',1301,20,'انثى','عدوية شمس سعيد','','Colour:SFA','yallow',0,'0','2021-04-20 07:31:42'),(1313,'',1301,20,'انثى','عدوية شمس سعيد','','Liquefaction','5',0,'0','2021-04-20 07:31:43'),(1314,'',1301,20,'انثى','عدوية شمس سعيد','','Count','',0,'0','2021-04-20 07:31:44'),(1315,'',1301,20,'انثى','عدوية شمس سعيد','','Motility:Active','5',0,'0','2021-04-20 07:31:45'),(1316,'',1301,20,'انثى','عدوية شمس سعيد','','Motility:Sluggish','5',0,'0','2021-04-20 07:31:45'),(1317,'',1301,20,'انثى','عدوية شمس سعيد','','Motility:Dead','5',0,'0','2021-04-20 07:31:46'),(1318,'',1301,20,'انثى','عدوية شمس سعيد','','Morphology:Normal','5',0,'0','2021-04-20 07:31:47'),(1319,'',1301,20,'انثى','عدوية شمس سعيد','','Morphology:Abnormal','5',0,'0','2021-04-20 07:31:48'),(1320,'',1301,20,'انثى','عدوية شمس سعيد','','Morphology:Pus cells','5',0,'0','2021-04-20 07:31:49'),(1321,'',1301,20,'انثى','عدوية شمس سعيد','','Other:SFA','',0,'0','2021-04-20 07:31:50');
/*!40000 ALTER TABLE `addnewitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `adduser`
--

DROP TABLE IF EXISTS `adduser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `adduser` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(255) NOT NULL,
  `user_password` varchar(255) NOT NULL,
  `user_mail` varchar(255) NOT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adduser`
--

LOCK TABLES `adduser` WRITE;
/*!40000 ALTER TABLE `adduser` DISABLE KEYS */;
INSERT INTO `adduser` VALUES (3,'ali','5','a',NULL),(4,'ameer','5','a',NULL);
/*!40000 ALTER TABLE `adduser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor`
--

DROP TABLE IF EXISTS `doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor` (
  `id` int NOT NULL AUTO_INCREMENT,
  `uid` varchar(255) DEFAULT NULL,
  `action` varchar(45) DEFAULT NULL,
  `table` varchar(45) DEFAULT NULL,
  `date` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor`
--

LOCK TABLES `doctor` WRITE;
/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;
INSERT INTO `doctor` VALUES (1,'1','1','1','datetime.datetime.now()');
/*!40000 ALTER TABLE `doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `his`
--

DROP TABLE IF EXISTS `his`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `his` (
  `id` int NOT NULL AUTO_INCREMENT,
  `uid` int DEFAULT NULL,
  `action` int DEFAULT NULL,
  `tabled` int DEFAULT NULL,
  `dates` datetime DEFAULT NULL,
  `def` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1257 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `his`
--

LOCK TABLES `his` WRITE;
/*!40000 ALTER TABLE `his` DISABLE KEYS */;
INSERT INTO `his` VALUES (1249,4,6,1,'2021-04-20 19:56:06',1),(1250,4,6,1,'2021-04-20 19:56:32',1),(1251,4,6,1,'2021-04-20 19:56:33',1),(1252,4,6,1,'2021-04-20 19:56:34',1),(1253,4,3,1,'2021-04-20 19:57:27',1),(1254,4,6,1,'2021-04-20 19:57:49',1),(1255,4,6,1,'2021-04-20 20:07:37',1),(1256,4,6,1,'2021-04-20 20:08:17',1);
/*!40000 ALTER TABLE `his` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paths`
--

DROP TABLE IF EXISTS `paths`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paths` (
  `id` int NOT NULL AUTO_INCREMENT,
  `file_path` varchar(255) DEFAULT NULL,
  `save_file_path` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paths`
--

LOCK TABLES `paths` WRITE;
/*!40000 ALTER TABLE `paths` DISABLE KEYS */;
INSERT INTO `paths` VALUES (1,'F:\\برنامج التحليلات\\word','F:\\برنامج التحليلات');
/*!40000 ALTER TABLE `paths` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report`
--

DROP TABLE IF EXISTS `report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `report` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `report_type` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report`
--

LOCK TABLES `report` WRITE;
/*!40000 ALTER TABLE `report` DISABLE KEYS */;
/*!40000 ALTER TABLE `report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userper`
--

DROP TABLE IF EXISTS `userper`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userper` (
  `id` int NOT NULL AUTO_INCREMENT,
  `add_sale_item_page` int NOT NULL,
  `analyst_page` int NOT NULL,
  `clients_page` int NOT NULL,
  `history_page` int NOT NULL,
  `settings_page` int NOT NULL,
  `show_analyst` int NOT NULL,
  `add_analyst` int NOT NULL,
  `edit_analyst` int NOT NULL,
  `delete_analyst` int NOT NULL,
  `change_theme` int NOT NULL,
  `add_buys` int NOT NULL,
  `report` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userper`
--

LOCK TABLES `userper` WRITE;
/*!40000 ALTER TABLE `userper` DISABLE KEYS */;
/*!40000 ALTER TABLE `userper` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-20 20:10:03
