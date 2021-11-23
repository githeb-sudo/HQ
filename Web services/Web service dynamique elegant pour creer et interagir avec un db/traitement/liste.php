                <?php 
                include('connexionPDO.php');
                $reponse=$bdd->query("select nomMat from matiere");
                $donnee=array();
                while($donnee1=$reponse->fetch(PDO::FETCH_ASSOC))
                {
                array_push($donnee,implode($donnee1));
                }
                ?> 

<!DOCTYPE HTML>

<html>

<head>
	<title>Recherche avancée</title>
	<meta charset="utf-8"/>
    <link rel="stylesheet" type="text/css" href="fillin.css" >
</head>

<body style="background-image:repeating-linear-gradient(to right,rgba(100,100,255,1),#4bbefe );">
	<div class="bloc_page">
		<a href="../indexDbOp.php">ACCUEIL</a>
		<div class="title">Recherche avancée</div>
		<hr size="50" color="blue">
		
        <center>
			<?php if(isset($_POST['cin']))
			include("listephp.php");
			echo '<br>';?>
            
			<h2>* = Champ obligatoire</h2>
            <h2>Maintenir la touche <ctrl style="color:rgb(0,0,100); font: bold 28px/1 Caviar, sans-serif; text-decoration:underline double">ctrl</ctrl> pour une sélection multiple</h2>
            <h2> <ctrl style="color:rgb(0,0,100); font: bold 28px/1 Caviar, sans-serif; text-decoration:underline double">Laisser tomber la sélection des matières</ctrl><br>  pour faire une recherche des informations personnelles </h2>
						
            <form method="POST" action="listephp.php"> <br>
				<label for="niveau" class="fillinind"> Niveau* </label>
				<select multiple="multiple" name="niveau[]" id="niveau" style="display:block" autofocus required>
					<option value="1"> 1 </option>
					<option value="2"> 2 </option>
					<option value="3"> 3 </option>
				</select><br><br>

				<label  for="codeg" class="fillinind"> Groupe* </label>
				<select multiple="multiple" name="codeg[]" id="codeg" style="display:block" required>
					<option value="A"> A </option>
					<option value="B"> B </option>
					<option value="C"> C </option>
				</select>	<br><br>

				<label for="nomMat" class="fillinind"> Matiére </label>
				<select multiple="multiple" name="nomMat[]" id="nomMat" style="display:block" >
                <option value=" " hidden selected="selected"></option>
				<?php for($i=0;$i<count($donnee);$i++) {?>
				<option value="<?php echo $donnee[$i]; ?>"><?php echo $donnee[$i]; ?></option> 
				<?php } ?>   <br><br><br>
				
				<p><input type="submit" value="  Valider " class="btn">
				<input type="reset" value="Mettre à zero" class="btn"></p>           
			<form>
            <p><div class="fillinind">Pour rechercher un étudiant particulier <a href="rechercher.php"> cliquer ici</div></p>
		</center>
	</div>
</body>
</html>

