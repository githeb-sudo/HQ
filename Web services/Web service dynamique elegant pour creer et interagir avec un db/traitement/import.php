<!DOCTYPE HTML>

<html>

<head>
	<title>Import à partir un fichier CSV</title>
	<meta charset="utf-8"/>
    <link rel="stylesheet" type="text/css" href="fillin.css" >
</head>

<body style="background-image:repeating-linear-gradient(to right,rgba(100,100,255,1),#4bbefe );">
	<div class="bloc_page">
		<a href="../indexDbOp.php">ACCUEIL</a>
		<div class="title">Import à partir un fichier CSV</div>
		<hr size="50" color="blue">
		
        <center>
			<?php if(isset($_POST['cin']))
			include("importphp.php");
			echo '<br>';?>
            
			<h2>* = Champ obligatoire</h2>
			
            <form method="POST" action="importphp.php"> <br>
				<label class="fillinind">Choose a CSV File</label> 
				<p><input type="file" name="file" id="file" accept=".csv" autofocus required class="btn" style="width:500px"></p>

				<p><input type="submit" value="  Valider " class="btn">
				<input type="reset" value="Mettre à zero" class="btn"></p>
			<form>
		</center>
	</div>
</body>
</html>

