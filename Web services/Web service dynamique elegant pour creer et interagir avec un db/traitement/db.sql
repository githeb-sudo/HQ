/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`relevedesnotes` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `relevedesnotes`;

/*Table structure for table `Etudiant` */


CREATE TABLE IF NOT EXISTS `etudiant` (
  `numCIN` int(8) NOT NULL COMMENT 'numero du CIN',
  `nomEtud` varchar(25) DEFAULT NULL COMMENT 'nom de l''etudiant',
  `prenomEtud` varchar(25) DEFAULT NULL COMMENT 'prenom de l''etudiant',
  `codeNiv` int(1) DEFAULT NULL COMMENT 'Code du niveau' ,
  `codeG` varchar(1) DEFAULT NULL COMMENT 'Code du groupe',
  `sessionid` int(8) NOT NULL COMMENT 'numero du session',
  PRIMARY KEY (`numCIN`),
  check (`codeNiv` between 1 and 3) ,
  check (`codeG` in ('A','B','C'))  
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `etudiant` (`numCIN`, `nomEtud`, `prenomEtud`,`codeNiv`,`codeG`,`sessionid`) VALUES
('20160011', 'a1', 'a1', 1,'A',1),
('20160012', 'a2', 'a2', 1,'B',1),
('20160013', 'a3', 'a3', 3,'C',1),
('20160014', 'a4', 'a4', 2,'A',1),
('20160010', 'a5', 'a5', 2,'A',1);

/*Table structure for table `matiere` */

CREATE TABLE IF NOT EXISTS `matiere` (
  `nomMat` varchar(8) NOT NULL COMMENT 'nom du matiere',
  `codeMat` varchar(3) DEFAULT NULL COMMENT 'le code de la matiere',
  `niveauMat` int(2) DEFAULT NULL COMMENT 'le niveau de la matiere',
  primary key(`nomMat`),
  check (`niveauMat` between 1 and 3)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `matiere` (`nomMat`, `codeMat`, `niveauMat`) VALUES
('x', 'x', '2');


/*Table structure for table `Note` */

CREATE TABLE IF NOT EXISTS `note` (
  `numCIN` int(8) NOT NULL COMMENT 'numero du CIN',
  `nomMat` varchar(8) NOT NULL COMMENT 'nom du matiere',
  `noteVal` int(2) DEFAULT NULL COMMENT 'la note',
  foreign key (`numCIN`) references `etudiant`(`numCIN`),
  foreign key (`nomMat`) references `matiere`(`nomMat`),
  check (`noteVal` between 0 and 20) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `note` (`numCIN`,`nomMat`,`noteVal`) VALUES ('20160011','x','19');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
