<!DOCTYPE HTML>

<html>

<head>
	<title>Supprimer</title>
	<meta charset="utf-8"/>
    <link rel="stylesheet" type="text/css" href="fillin.css" >
</head>

<body style="background-image:repeating-linear-gradient(to right,rgba(100,100,255,1),#4bbefe );">
	<div class="bloc_page">
		<a href="../indexDbOp.php">ACCUEIL</a>
		<div class="title">Suppression par CIN</div>
		<hr size="50" color="blue">
		
        <center>
			<?php if(isset($_POST['cin']))
			include("supprimerphp.php");
			echo '<br>';?>
            
			<h2>* = Champ obligatoire</h2>
			
            <form method="POST" action="supprimerphp.php"> <br>
				<label for="cin" class="fillinind"> Numéro du CIN* </label>
				<input type="text" name="cin" id="cin" placeholder="Ex:01234567" minlength="8"  maxlength="8" autofocus required><br><br>
				
				<p><input type="submit" value="Supprimer" class="btn">
				<input type="reset" value="Mettre à zero" class="btn"></p>
			<form>
		</center>
	</div>
</body>
</html>

