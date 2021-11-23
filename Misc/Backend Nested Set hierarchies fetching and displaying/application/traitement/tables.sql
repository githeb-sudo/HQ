CREATE DATABASE if not exists `organizationalchart`;

USE `organizationalchart`;

/* Table structure for table `node_tree` */


CREATE TABLE IF NOT EXISTS `node_tree` (
    `idNode` int(8) NOT NULL COMMENT 'Node ID',
    `level`  int(8) NOT NULL COMMENT 'Node level',
    `ileft`  int(8) NOT NULL COMMENT 'Node level',
    `iright` int(8) NOT NULL COMMENT 'Node level',
    PRIMARY KEY (`idNode`),
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


/*Table structure for table `node_tree_names` */

CREATE TABLE IF NOT EXISTS `node_tree_names` (
    `idNode` int(8) NOT NULL COMMENT 'Node ID',
    `language` varchar(20) NOT NULL COMMENT 'Language',
    `nodeName` varchar(30) NOT NULL COMMENT 'Node Name',
    foreign key (`idNode`) references `node_tree`(`idNode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
