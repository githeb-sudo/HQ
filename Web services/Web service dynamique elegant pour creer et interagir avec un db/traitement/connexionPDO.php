<?php
	try
	{
		$bdd= new PDO("mysql:dbname=relevedesnotes;host=localhost",'root','Root1234',array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION)); 
    }
	catch(Exception $e)
	{
		echo "Erreur : ".$e->getMessage(); 
	}
?>