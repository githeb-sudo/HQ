<?php

include('connexionPDO.php');
$reponse=$bdd->query('SELECT numCIN FROM etudiant WHERE numCIN= \''.$_POST['cin'].'\' ');

if(!($donnee=$reponse->fetch()))
	{
	$reponseEtudiant=$bdd->query('INSERT INTO etudiant VALUES(\''.$_POST['cin'].'\' , \''.$_POST['nom'].'\' , \''.$_POST['prenom'].'\' , \''.$_POST['niveau'].'\' , \''.$_POST['groupe'].'\' , \''.$_POST['session'].'\') ');
	$reponseEtudiant->closeCursor();
    $reponse->closeCursor();
	header("Location: add_ok.php");
	}
else
	{
	echo 'Mise à jour avec succés pour l\'étudiant(e) de cin '.$_POST['cin'].'. ';
	$reponseEtudiant=$bdd->query('UPDATE etudiant SET codeG= \''.$_POST['groupe'].'\' , codeNiv=\''.$_POST['niveau'].'\' where numCIN= \''.$_POST['cin'].'\' ');
	$reponseEtudiant->closeCursor();
    $reponse->closeCursor();
	header("Location: maj_ok.php");
    }

?>
