<?php


include('connexionPDO.php');
$reponse=$bdd->query('SELECT nomEtud,prenomEtud,codeNiv FROM etudiant WHERE numCIN= \''.$_POST['cin'].'\' ');
$donnee=$reponse->fetch();

ob_start();

require("fpdf/fpdf.php"); 
class PDF extends FPDF
{
// En-tête
function Header()
{
    $this->Image('images/logo1.png',50,20,50);
    $this->Image('images/logo2.png',375,20,50);
    $this->Image('images/logo3.jpg',750,20,50);

    $this->SetFont('Arial','B',20);
    $this->text(360,150,'DIPLOME',1,0,'C');
    $this->text(300,170,'NATIONAL D\'INGENIEUR',1,0,'C');
    $this->Ln(20);
}

// Pied de page
function Footer()
{
   
    $this->SetY(-15);
    $this->SetFont('Arial','I',8);
    $this->Cell(0,10,'Page '.$this->PageNo(),0,0,'C');
}
}
$pdf = new PDF("L","pt","A4"); 
$pdf ->AddPage();
$pdf ->SetFont('Times','',14);
$pdf ->SetXY(50, 200);  
$pdf ->Cell(0,10, "Vu le proc".utf8_decode("é")."s verbal de l'examen ".utf8_decode("é")."tabli le <".$_POST['date'].">"); 
$pdf ->SetXY(50, 220); 
$pdf ->Cell(0,10,"par le pr".utf8_decode("é")."sident du jury, examinateur,"); 
$pdf ->SetXY(50, 240); 
$pdf ->Cell(0,10,"le <Dipl".utf8_decode("ô")."me National d'ing".utf8_decode("é")."nieur en T".utf8_decode("é")."l".utf8_decode("é")."communications>"); 
$pdf ->SetXY(50, 280); 
$pdf ->Cell(0,10," est conf".utf8_decode("é")."r".utf8_decode("é")." ".utf8_decode("à")." <".Ucfirst($donnee[0])." ".Ucfirst($donnee[1]).">");
$pdf ->SetXY(80, 320); 
$pdf ->Cell(0,10," pour en jouir avec les droits et pr".utf8_decode("é")."rogatives qui y sont attach".utf8_decode("é")."s");
$pdf ->SetXY(100, 380); 
$pdf ->SetFont('Times','',11);
$pdf ->Cell(0,10,"Signature du titulaire");
$pdf ->SetXY(400, 380);
$pdf ->Cell(0,10,"Ministre de l'Enseignement Sup".utf8_decode("é")."rieur et de la Recherche Scientifique");
$pdf ->Output('download/1.pdf','I'); 	
ob_end_flush();

?>