<?php
	include('connexionPDO.php');
    $csv = array_map('str_getcsv', file($_POST['file']));
	for ($i=1;$i<count($csv);$i++)
    {
		$reponse0=$bdd->query('SELECT etudiant.numCIN FROM etudiant,matiere WHERE etudiant.numCIN= \''.$csv[$i][0].'\' and matiere.nomMat= \''.$_POST['nomMat'].'\' and etudiant.codeNiv=matiere.niveauMat');
		if(($donnee0=$reponse0->fetch()))
        {
			$reponse=$bdd->query('SELECT numCIN,nomMat FROM note WHERE numCIN= \''.$csv[$i][0].'\' and nomMat= \''.$_POST['nomMat'].'\' ');
			if(!($donnee=$reponse->fetch()))
				{
				$reponseEtudiant=$bdd->query('INSERT INTO note VALUES(\''.$csv[$i][0].'\' , \''.$_POST['nomMat'].'\' , \''.$csv[$i][1].'\') ');
				$reponseEtudiant->closeCursor();
				$reponse->closeCursor();
				}
			else
				{
				$reponseEtudiant=$bdd->query('UPDATE note SET noteVal=\''.$csv[$i][1].'\' where numCIN= \''.$csv[$i][0].'\' and nomMat= \''.$_POST['nomMat'].'\' ');
				$reponseEtudiant->closeCursor();
				$reponse->closeCursor();
				}
		}
        $reponse0->closeCursor();
		header("Location: op_ok.php");
    }	
?>