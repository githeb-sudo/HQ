<!DOCTYPE HTML>

<html>

<head>
	<title>Ajout d&apos;une matière</title>
	<meta charset="utf-8"/>
    <link rel="stylesheet" type="text/css" href="fillin.css" >
</head>

<body style="background-image:repeating-linear-gradient(to right,rgba(100,100,255,1),#4bbefe );">
	<div class="bloc_page">
		<a href="../indexDbOp.php">ACCUEIL</a>
		<div class="title">Ajout d&apos;une matière</div>
		<hr size="50" color="blue">
		
        <center>
			<?php if(isset($_POST['cin']))
			include("addMphp.php");
			echo '<br>';?>
            
			<h2>* = Champ obligatoire</h2>
			
            <form method="POST" action="addMphp.php"> <br>
				<label for="nomMat" class="fillinind"> Nom matiére* </label>
				<input type="text" name="nomMat" id="nomMat" placeholder="Ex:xxxx" minlength="8" autofocus maxlength="20" required><br><br>

				<label for="codeMat" class="fillinind"> Code du matiére* </label>
				<input type="text" name="codeMat" id="codeMat" placeholder="Ex:xx"size="80%" required><br><br>

			   <label for="niveau" class="fillinind">Niveau*</label>
			   <select name="niveau" id="niveau" class="selectbtn" required>
					<option value=""> </option>
					<option value="1">1</option>
					<option value="2">2</option>
					<option value="3">3</option><br><br>
				</select>
			
				<p><input type="submit" value="  Valider " class="btn">
				<input type="reset" value="Mettre à zero" class="btn"></p>
			<form>
		</center>
	</div>
</body>
</html>

