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
	<title>Import des notes</title>
	<meta charset="utf-8"/>
    <link rel="stylesheet" type="text/css" href="fillin.css" >
</head>

<body style="background-image:repeating-linear-gradient(to right,rgba(100,100,255,1),#4bbefe );">
	<div class="bloc_page">
		<a href="../indexDbOp.php">ACCUEIL</a>
		<div class="title">Import des notes</div>
		<hr size="50" color="blue">
		
        <center>
            
			<h2>* = Champ obligatoire</h2>

            <form method="POST" action="importnotephp.php"> <br>
				<label class="fillinind">Choose a CSV File*</label> 
				<p><input type="file" name="file" id="file" accept=".csv" autofocus required class="btn" style="width:500px"></p>

				<label for="nomMat" class="fillinind"> Matiére* </label>
				<select name="nomMat" id="nomMat" style="display:block" required>
                <option value="">
				<?php for($i=0;$i<count($donnee);$i++) {?>
				<option value="<?php echo $donnee[$i]; ?>"><?php echo $donnee[$i]; ?></option> 
				<?php } ?>   
				
				<p><input type="submit" value="  Valider " style="margin-top:1vh" class="btn">
				<input type="reset" value=" Mettre à zero " style="margin-top:1vh" class="btn"></p>           
			<form>
           		</center>
	</div>
</body>
</html>

