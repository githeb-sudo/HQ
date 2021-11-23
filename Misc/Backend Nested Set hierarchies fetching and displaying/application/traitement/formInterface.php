<?php
include('connexionPDO.php');
$reponse=$bdd->query("select language from node_tree_names group by language ");
$donnee=array();
while($donnee1=$reponse->fetch(PDO::FETCH_ASSOC))
{
    array_push($donnee,implode($donnee1));
}

?>
<!DOCTYPE HTML>

<html>

<head>
	<title>Form interface</title>
	<meta charset="utf-8"/>
    <link rel="stylesheet" type="text/css" href="fillin.css" >
</head>

<body>
	<div class="bloc_page">
		<a href="../api.php">Home</a>
		<div class="title">Form</div>
		<hr size="50" color="blue">
		
        <center>

            
			<b style="font: bold 25px garamond; display:block; margin:7px;">* =Required Field</b>
			<b style="font: bold 25px garamond;">Hold <div class="ctrl">ctrl</div> for a multiple selection</b>


            <form method="GET" action="apicore.php"> <br>
				<label for="nodeid" class="fillinind"> Node ID* </label>
				<input type="text" name="nodeid" id="nodeid" placeholder="Ex:10"  autofocus pattern="[0-9]+" ><br>



				<label for="search_keyword" class="fillinind" >Search keyword</label>
				<input type="text" name="search_keyword" id="search_keyword" placeholder="Ex:Developers" pattern="[a-zA-Z]+" "><br>

				<label for="page_num" class="fillinind">Page number</label>
				<input type="text" name="page_num" id="page_num" pattern="[0-9|-]+" placeholder="0"> <br>

                <label for="page_size" class="fillinind">Page size</label>
                <input type="text" name="page_size" id="page_size" pattern="[0-9]+" placeholder="1-1000"><br>

                <label for="language" class="fillinind"> Language(s)* </label>
                <select multiple="multiple" name="language[]" id="language" size="3" style="display: block;width: 40%;" >
                    <option value=" " hidden selected="selected"></option>
                    <?php for($i=0;$i<count($donnee);$i++) {?>
                        <option value="<?php echo $donnee[$i]; ?>"><?php echo ucfirst($donnee[$i]); ?></option>
                    <?php } ?><br>
				</select>
                <p><input type="submit" value=" Validate  " class="btn">
				<input type="reset" value=" Reset " class="btn"></p>
			<form>
		</center>
	</div>
</body>
</html>