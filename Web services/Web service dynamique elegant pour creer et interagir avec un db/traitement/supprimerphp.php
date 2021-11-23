<?php
     
	include('connexionPDO.php');
	
	 $reponse=$bdd->query('SELECT numCIN FROM etudiant WHERE numCIN = \''.$_POST['cin'].'\' ');
	 
	 
	 if($donnee=$reponse->fetch())
	 {
		$reponse3=$bdd->query('DELETE FROM note WHERE numCIN = \''.$_POST['cin'].'\' ');
		$reponse2 =$bdd->query('DELETE FROM etudiant WHERE numCIN = \''.$donnee[0].'\' ');		
		header('Location: supp_ok.php?cin='.$donnee[0]);
		$reponse2->closeCursor();
        $reponse3->closeCursor();
	 }
	 else
		header('Location: supp_notok.php?cin='.$_POST['cin']);
		$reponse->closeCursor();
	
?>