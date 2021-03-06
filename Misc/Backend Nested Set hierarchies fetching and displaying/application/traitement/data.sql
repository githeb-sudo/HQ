use organizationalchart;

INSERT INTO `node_tree` (`idNode`, `level`, `ileft`,`iright`) VALUES
('1', '2', '2', '3'),
('2', '2', '4', '5'),
('3', '2', '6', '7'),
('4', '2', '8', '9'),
('5', '1', '1', '24'),
('6', '2', '10', '11'),
('7', '2', '12', '19'),
('8', '3', '15', '16'),
('9', '3', '17', '18'),
('10', '2', '20', '21'),
('11', '3', '13', '14'),
('12', '2', '22', '23');

INSERT INTO `node_tree_names` (`idNode`,`language`,`nodeName`) VALUES
('1','english','Marketing'),
('2','english','Helpdesk'),
('3','english','Managers'),
('4','english','Customer Account'),
('5','english','Docebo'),
('6','english','Accounting'),
('7','english','Sales'),
('8','english','Italy'),
('9','english','Europe'),
('10','english','Developers'),
('11','english','North America'),
('12','english','Quality Assurance'),
('1','italian','Marketing'),
('2','italian','Supporto tecnico'),
('3','italian','Managers'),
('4','italian','Assistenza Cliente'),
('5','italian','Docebo'),
('6','italian','Amministrazione'),
('7','italian','Supporto Vendite'),
('8','italian','Italia'),
('9','italian','Europa'),
('10','italian','Sviluppatori'),
('11','italian','Nord America'),
('12','italian','Controllo Qualità');