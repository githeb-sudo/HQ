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
    $this->Image('images/logo2.png',300,20,50);
    $this->Image('images/logo3.jpg',500,20,50);
    $this->SetFont('Arial','B',15);
    $this->Cell(80);
    $this->text(220,150,'ATTESTATION DE REUSSITE',1,0,'C');
    $this->Ln(20);
}

// Pied de page
function Footer()
{
   
    $this->SetY(-15);
    $this->SetFont('Arial','I',8);
    $this->Cell(0,10,'Page '.$this->PageNo().'/{nb}',0,0,'C');
}
}
$pdf = new PDF("P","pt","A4"); 
$pdf ->AddPage();
$pdf ->SetFont('Times','',14);
$pdf ->SetXY(70, 200);  
$pdf ->Cell(0,10, "Le Secr".utf8_decode("é")."taire G".utf8_decode("é")."n".utf8_decode("é")."ral de l'Ecole XXX, certifie que l'".utf8_decode("é")."tudiant(e):\n"); 
$pdf ->SetXY(80, 240); 
$pdf ->SetFont('Times','B',14); 
$pdf ->Cell(0,10,"M(Mme): ".Ucfirst($donnee[1])." ".Ucfirst($donnee[0])); 
$pdf ->SetXY(50, 280); 
$pdf ->SetFont('Times','',14);
if($donnee[2]=='1')
{$pdf ->Cell(0,10,"a suivi avec succ".utf8_decode("é")."s les examens de la ".$donnee[2]." ".utf8_decode("é")."re ann".utf8_decode("é")."e du Cycle de Formation"); }
else{$pdf ->Cell(0,10,"a suivi avec succ".utf8_decode("é")."s les examens de la ".$donnee[2]." ".utf8_decode("é")."me ann".utf8_decode("é")."e du Cycle de Formation"); }
$pdf ->SetXY(80, 310); 
$pdf ->SetFont('Times','B',14);
$pdf ->Cell(0,10," D'INGENIEURS DE TELECOMMUNICATIONNS");
$pdf ->SetXY(50, 340); 
$pdf ->SetFont('Times','',14);
$pdf ->Cell(0,10,"Ann".utf8_decode("é")."e universitaire ".$_POST['annee']);
$pdf ->SetXY(50, 380); 
$pdf ->Cell(0,10,"Session ".$_POST['session']." : ".$_POST['annee']);
$pdf ->SetXY(70, 420);
$pdf ->Cell(0,10," La pr".utf8_decode("é")."sente attestation est delivr".utf8_decode("é")."e ".utf8_decode("é")." l'int".utf8_decode("é")."ress".utf8_decode("é")."(e) sur sa demande pour valoire et servir");
$pdf ->SetXY(50, 440);
$pdf ->Cell(0,10,"ce que de droit");
$pdf ->SetXY(400, 550);
$pdf ->Cell(0,10,"Tunis, Le ".$_POST['date']);
$pdf ->SetXY(430, 600);
$pdf ->Cell(0,10,"Le Secr".utf8_decode("é")."taire General");
$pdf ->SetXY(50, 700);
$pdf ->SetFont('Times','B',11);
$pdf ->Cell(0,10,"NB: Cette attestation  n'est delivr".utf8_decode("é")."e qu'une seule fois");
$pdf ->Output(); 	
ob_end_flush();

?>