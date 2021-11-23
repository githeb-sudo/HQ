<!DOCTYPE HTML>

<html>

<head>
	<title>Supprimer</title>
	<meta charset="utf-8"/>
    <link rel="stylesheet" type="text/css" href="fillin.css" >
</head>

<?php
	
	include('connexionPDO.php');
	
	$reponse=$bdd->query('SELECT UPPER(nomEtud) ,UPPER(prenomEtud) AS prenom, codeNiv,codeG FROM etudiant WHERE numCIN= \''.$_POST['cin'].'\' ');
							  
	$donnee=$reponse->fetch();
	
	if($donnee)
	{
	?>
    <body style="background-image:repeating-linear-gradient(to right,rgba(100,100,255,1),#4bbefe );">
    <a href="../indexDbOp.php">ACCUEIL</a><br><br>
	<center>
		<div class='title'>INFORMATION DE <div style="display:block;color:rgb(0,0,100); text-decoration:underline double"><?php echo $donnee[0]," ", $donnee[1]?></div></div>
		<br><br>
		<table  align="center" cellspacing="15px" cellpadding="0">
			<tr>
				<td align="center"><div class="fillinind">CIN : </div></td>
				<td align="center"><div class="display"><?php echo $_POST['cin'] ?></div></td>
			</tr>
			
			<tr>
				<td align="center"><div class="fillinind">Nom : </div></td>
				<td align="center"><div class="display"><?php echo $donnee[0] ?></div></td>
			</tr>
			<tr>
				<td align="center"><div class="fillinind">Prenom : </div></td>
				<td align="center"><div class="display"><?php echo $donnee[1] ?></div></td>
			</tr>
				<td align="center"><div class="fillinind">Niveau : </div></td>
				<td align="center"><div class="display"><?php echo $donnee[2] ?></div></td>
			</tr>
			<tr>
				<td align="center"><div class="fillinind">Groupe : </div></td>
				<td align="center"><div class="display"><?php echo $donnee[3] ?></div></td>
			</tr>

		</table>
	</center>
    </body>
	<?php
	}
	else
		header('Location: rech_notok.php?cin='.$_POST['cin']);

	$reponse->closeCursor();

?>