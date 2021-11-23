
<!DOCTYPE HTML>

<html>

<head>
	<title>Attestation de présence</title>
	<meta charset="utf-8"/>
    <link rel="stylesheet" type="text/css" href="fillin.css" >
</head>

<body style="background-image:repeating-linear-gradient(to right,rgba(100,100,255,1),#4bbefe );">
	<div class="bloc_page">
		<a href="../index.php">ACCUEIL</a>
		<div class="title">Attestation de présence</div>
		<hr size="50" color="blue">
		
        <center>
			<?php if(isset($_POST['cin']))
			include("presencephp.php");
			echo '<br>';?>
            
			<h2>* = Champ obligatoire</h2>
			
            <form method="POST" action="presencephp.php"> <br>
				<label for="cin" class="fillinind"> Numéro du CIN* </label>
				<input type="text" name="cin" id="cin" placeholder="Ex:01234567" size="80%"  minlength="8"  maxlength="8" autofocus required><br><br>
				
				<label for="annee" class="fillinind" >Année scolaire*</label>
				<input type="text" name="annee" id="annee" placeholder="Ex:2020/2021" size="80%" pattern="20[0-9]{1}[0-9]{1}/20[0-9]{1}[0-9]{1}" required><br><br>
				
				<label for="date" class="fillinind">Le*</label>
				<input type="date" name="date" id="date" required>
				
				<p><input type="submit" value="  Valider " class="btn">
				<input type="reset" value="Mettre à zero" class="btn"></p>
			<form>
		</center>
	</div>
</body>
</html>