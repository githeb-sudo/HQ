<?php

	include('connexionPDO.php');
    $reponse=$bdd->query('SELECT nomMat FROM matiere WHERE nomMat= \''.$_POST['nomMat'].'\' ');
  
	if(!($donnee=$reponse->fetch()))
		{
        $reponseEtudiant=$bdd->query('INSERT INTO matiere VALUES(\''.$_POST['nomMat'].'\' , \''.$_POST['codeMat'].'\' , \''.$_POST['niveau'].'\') ');
        $reponseEtudiant->closeCursor();
        $reponse->closeCursor();
        header("Location: add_ok.php");
		}
	else
		{
		$reponseEtudiant=$bdd->query('UPDATE matiere SET niveauMat=\''.$_POST['niveau'].'\' where nomMat= \''.$_POST['nomMat'].'\' ');
		$reponseEtudiant->closeCursor();
        $reponse->closeCursor();
        header("Location: maj_ok.php");
        }
	
    
      
  
?>