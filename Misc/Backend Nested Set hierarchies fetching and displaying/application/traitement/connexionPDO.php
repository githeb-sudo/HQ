<?php
	try
	{
		$bdd= new PDO("mysql:dbname=organizationalchart;host=localhost",'DoceboDeveloper','password1234',array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION));
    }
	catch(Exception $e)
	{
		echo "Erreur : ".$e->getMessage(); 
	}
?>