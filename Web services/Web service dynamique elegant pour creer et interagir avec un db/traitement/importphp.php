<?php
	include('connexionPDO.php');
    $csv = array_map('str_getcsv', file($_POST['file']));
	for ($i=1;$i<count($csv);$i++)
    {
		$reponse=$bdd->query('SELECT numCIN FROM etudiant WHERE numCIN= \''.$csv[$i][0].'\' ');
		if(!($donnee=$reponse->fetch()))
			{
			$reponseEtudiant=$bdd->query('INSERT INTO etudiant VALUES(\''.$csv[$i][0].'\' , \''.$csv[$i][1].'\' , \''.$csv[$i][2].'\' , \''.$csv[$i][3].'\' , \''.$csv[$i][4].'\' , \''.$csv[$i][5].'\') ');
			$reponseEtudiant->closeCursor();
			$reponse->closeCursor();
			}
		else
			{
			$reponseEtudiant=$bdd->query('UPDATE etudiant SET codeG= \''.$csv[$i][4].'\' , codeNiv=\''.$csv[$i][3].'\' where numCIN= \''.$csv[$i][0].'\' ');
			$reponseEtudiant->closeCursor();
			$reponse->closeCursor();
			}
		header("Location: op_ok.php");
    }	
?>