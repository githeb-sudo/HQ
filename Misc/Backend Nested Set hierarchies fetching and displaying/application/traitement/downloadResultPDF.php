<?php
$result=json_encode(unserialize(base64_decode((urldecode($_GET['nodes'])))),JSON_PRETTY_PRINT);
$result=str_replace("{","\n{",$result);


require("fpdf/fpdf.php");

class PDF extends FPDF
{
    function Header()
    {
        $this->SetFont('Arial','B',15);
        $this->text(220,150,"Report",1,0,'C');
    }
    
    function Footer()
    {
        
        $this->SetY(-15);
        $this->SetFont('Arial','I',8);
        $this->Cell(0,10,'Page '.$this->PageNo(),0,0,'C');
        $this->Cell(0,10,date("r"),0,0,'R');
    }
}

$pdf = new PDF("P","pt","A4");
$pdf ->AddPage();
$pdf->Image('images/logo.png',50,20,50);
$pdf->Image('images/docebo.png',500,35,50);
$pdf ->SetXY(70, 200);
$pdf ->SetFont('Times','B',14);
$pdf ->Cell(0,10,"Search result ");
$pdf ->SetXY(80, 240);
$pdf ->Multicell(0,10, $result);
$pdf ->Output();
ob_end_flush();

?>
