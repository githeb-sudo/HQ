
<head>
    <link rel="stylesheet" type="text/css" href="fillin0.css" >
</head>
	
<meta charset="utf-8"/>
	
	<?php

		include('connexionPDO.php');
		if(implode($_POST['nomMat'])==' ')
        {
		$reponse=$bdd->query('SELECT numCIN,UPPER(nomEtud) ,UPPER(prenomEtud),codeNiv,codeG  FROM etudiant
						  WHERE 
                          codeNiv in (\''.implode('\',\'',$_POST['niveau']).'\')  and codeG in (\''.implode('\',\'',$_POST['codeg']).'\')');           
        }
        else
        {
		$reponse=$bdd->query('SELECT etudiant.numCIN,UPPER(nomEtud)  AS nom ,UPPER(prenomEtud) AS prenom, matiere.nomMat, noteVal  FROM etudiant,matiere,note
						  WHERE etudiant.numCIN=note.numCIN and matiere.nomMat=note.nomMat and
                          codeNiv in (\''.implode('\',\'',$_POST['niveau']).'\')  and codeG in (\''.implode('\',\'',$_POST['codeg']).'\')
                          and matiere.nomMat in (\''.implode('\',\'',$_POST['nomMat']).'\')');  
		}							
	
    
    ?>
		<body>
		<center>
			<a href="indexDbOp.php">ACCUEIL</a>
			<table cellspacing="0">
					<caption><div class="title">Liste des Etudiants</div></caption>
					 <br/>
					 <tr>
						<th style="color:rgb(0,0,100)">CIN</th>
						<th style="color:rgb(0,0,100)">Nom</th>
						<th style="color:rgb(0,0,100)">Prénom</th>
                        <th style="color:rgb(0,0,100)">
                        <?php if(implode($_POST['nomMat'])==' '){echo "Niveau";} else {echo "Matière";} ?></th>
                        <th style="color:rgb(0,0,100)">
                        <?php if(implode($_POST['nomMat'])==' '){echo "Groupe";} else {echo "Note";} ?></th>
					 </tr>
				 <?php
				 
					while($donnee=$reponse->fetch())
					{
						
					?>	
						<tr>
						<td align="center" ><?php echo $donnee[0] ?></td>
						<td align="center" ><?php echo $donnee[1]?></td>
						<td align="center" ><?php echo $donnee[2]?></td>
                        <td align="center" ><?php echo $donnee[3]?></td>
                        <td align="center" ><?php echo $donnee[4]?></td>
						</tr>
					<?php
					}
				 
				 ?>
			</table> 
		</center>
        <body>
		
		<?php
		$reponse->closeCursor();
		?>