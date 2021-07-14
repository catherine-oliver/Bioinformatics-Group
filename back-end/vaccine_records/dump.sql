-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: vaccine_records
-- ------------------------------------------------------
-- Server version	8.0.25

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
-- Table structure for table `pfizer_records`
--

DROP TABLE IF EXISTS `pfizer_records`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pfizer_records` (
  `jurisdiction` varchar(255) NOT NULL,
  `week_of_allocations` varchar(255) NOT NULL,
  `1st_dose_allocations` varchar(255) NOT NULL,
  `2nd_dose_allocations` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pfizer_records`
--

LOCK TABLES `pfizer_records` WRITE;
/*!40000 ALTER TABLE `pfizer_records` DISABLE KEYS */;
/*!40000 ALTER TABLE `pfizer_records` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `total_vaccinations`
--

DROP TABLE IF EXISTS `total_vaccinations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `total_vaccinations` (
  `date` varchar(255) NOT NULL,
  `location` varchar(255) NOT NULL,
  `distributed` varchar(255) NOT NULL,
  `distributed_Janssen` varchar(255) NOT NULL,
  `distributed_Moderna` varchar(255) NOT NULL,
  `distributed_Pfizer` varchar(255) NOT NULL,
  `distributed_per_100k` varchar(255) NOT NULL,
  `distributed_per_100k_12Plus` varchar(255) NOT NULL,
  `distributed_per_100k_18Plus` varchar(255) NOT NULL,
  `distributed_per_100k_65Plus` varchar(255) NOT NULL,
  `administered` varchar(255) NOT NULL,
  `administered_12Plus` varchar(255) NOT NULL,
  `administered_18Plus` varchar(255) NOT NULL,
  `administered_65Plus` varchar(255) NOT NULL,
  `administered_Janssen` varchar(255) NOT NULL,
  `administered_Moderna` varchar(255) NOT NULL,
  `administered_Pfizer` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `total_vaccinations`
--

LOCK TABLES `total_vaccinations` WRITE;
/*!40000 ALTER TABLE `total_vaccinations` DISABLE KEYS */;
INSERT INTO `total_vaccinations` VALUES ('07/12/2021','PA','15,853,755','1,060,700','6,746,020','8,047,035','123,838','143,065','155,928','662,405','14,139,778','14,135,675','13,485,505','4,371,079','548,949','5,846,511','7,743,852'),('07/13/2021','LA','4116760','238100','1819220','2059440','88555','104931','115602','555552','3454831','3454630','3363824','1164833','129072','1560147','1764403'),('07/13/2021','GA','11326585','599200','4807680','5919705','106679','126018','139601','746666','8607149','8605294','8258767','2392383','227871','3636187','4742153'),('7/13/2021','NJ','11737785','606300','4796520','6334965','132150','154072','169044','795493','10053662','10052992','9479392','2413132','380647','4052763','5620223'),('07/13/2021','UT','3276300','172400','1384720','1719180','102194','126388','144027','895477','2902966','2902407','2713569','609395','126663','1172765','1603538'),('07/13/2021','MN','6595710','349300','2635640','3610770','116953','138041','152098','716627','5957434','5938144','5596618','1584711','264866','2326498','3365425'),('07/13/2021','SD','972075','59400','436980','475695','109881','131699','145617','640066','830727','830702','795925','261991','26646','361325','442743'),('07/13/2021','MT','1121325','69600','499800','551925','104917','122202','133461','543180','953213','953078','915697','323685','39073','426581','486905'),('07/13/2021','CT','4783785','250000','1938380','2595405','134177','154020','168571','759037','4481997','4480383','4199556','1161624','178817','1723569','2579044');
/*!40000 ALTER TABLE `total_vaccinations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-14 15:20:38
