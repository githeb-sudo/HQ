<!DOCTYPE HTML>

<html>

<head>
	<title>Ajout par CIN</title>
	<meta charset="utf-8"/>
    <link rel="stylesheet" type="text/css" href="fillin.css" >
</head>

<body style="background-image:repeating-linear-gradient(to right,rgba(100,100,255,1),#4bbefe );">
	<div class="bloc_page">
		<a href="../indexDbOp.php">ACCUEIL</a>
		<div class="title">Ajout par CIN</div>
		<hr size="50" color="blue">
		
        <center>
			<?php if(isset($_POST['cin']))
			include("addphp.php");
			echo '<br>';?>
            
			<h2>* = Champ obligatoire</h2>
			
            <form method="POST" action="addphp.php"> <br>
				<label for="cin" class="fillinind"> Numéro du CIN* </label>
				<input type="text" name="cin" id="cin" placeholder="Ex:01234567" minlength="8"  maxlength="8" autofocus required><br><br>

				<label for="nom" class="fillinind"> Nom* </label>
				<input type="text" name="nom" id="nom" placeholder="Ex:Gueller"size="80%" required><br><br>

				<label for="prenom" class="fillinind"> Prenom* </label>
				<input type="text" name="prenom" id="prenom" placeholder="Ex:Ross"size="80%" required ><br><br>
				
				<label for="session" class="fillinind"> Session_ID* </label>
				<input type="text" name="session" id="session" placeholder="Ex:1" size="80%" required ><br><br>

			   <label for="niveau" class="fillinind">Niveau*</label>
			   <select name="niveau" id="niveau" class="selectbtn" required>
					<option value=""> </option>
					<option value="1">1</option>
					<option value="2">2</option>
					<option value="2">3</option>
				</select><br><br>

			   <label for="groupe" class="fillinind">Groupe*</label>
			   <select name="groupe" id="groupe" class="selectbtn" required>
					<option value=""> </option>
					<option value="A">A</option>
					<option value="B">B</option>
					<option value="C">C</option>
				</select><br><br>

				<p><input type="submit" value="  Valider " class="btn">
				<input type="reset" value="Mettre à zero" class="btn"></p>
			<form>
		</center>
	</div>
</body>
</html>

