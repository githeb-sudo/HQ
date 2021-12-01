<?php


$distribution_type=$_POST['distribution_type'];

$region=implode(",", $_POST['geo_objets_ids']??array());
$estate_type=implode("," , $_POST['typesbien']??array());

$nb_pieces=implode(",", $_POST['nb_pieces']??array());


$nb_chambres=implode(", ",$_POST['nb_chambres']??array());
$space=implode(", ",$_POST['surface']??array());
$price=implode(", ",$_POST['prix']??array());
$duree_2possession=implode(", ",$_POST['duree_2possession']??array());


$cmd="python C:\Apache24\htdocs\RealtyEagle\core\search.py -distribution_type=$distribution_type -region=[".$region."]  -estate_type=[".$estate_type."]  -nb_rooms=[".$nb_pieces."] -nb_bedrooms=$nb_chambres  -space=$space -price=$price -duree_2possession=$duree_2possession ";


$result=shell_exec($cmd);

$splitted=explode("\n",$result);
function isempty($var) {
    return (isset($var) And ($var == true )) Or ($var=='0') ;
}
$region_names=array("Ile-de-France","Champagne Ardenne","Picardie","Haute Normandie","Centre","Basse Normandie","Bourgogne","Nord Pas de Calais","Lorraine","Alsace","Franche Comte","Pays de la Loire","Bretagne","Poitou Charentes","Aquitaine","Midi Pyrenees","Limousin","Rhone Alpes","Auvergne","Languedoc Roussillon","Provence Alpes Cote d'Azur","Corse");


?>



<html lang="fr-FR" data-lt-installed="true">

<head>
	<meta name="viewport" content="width=device-width">
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">




	<title>RealtyEagle: IA pour optimiser les investissements immobiliers</title>
	<meta name="description" content="RealtyEagle: IA pour optimiser les investissements immobiliers. Consultez des milliers d'annonces immobilières sur toute la France selon vos préférences et minutieusement sélectionnées pour optimiser votre retour sur investissement >>>">

	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fancyapps/fancybox@3.5.7/dist/jquery.fancybox.min.css" integrity="sha256-Vzbj7sDDS/woiFS3uNKo8eIuni59rjyNGtXfstRzStA=" crossorigin="anonymous">
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/owl.carousel@2.3.4/dist/assets/owl.carousel.min.css" integrity="sha256-UhQQ4fxEeABh4JrcmAJ1+16id/1dnlOEVCFOxDef9Lw=" crossorigin="anonymous">
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/owl.carousel@2.3.4/dist/assets/owl.theme.default.min.css" integrity="sha256-kksNxjDRxd/5+jGurZUJd1sdR2v+ClrCl3svESBaJqw=" crossorigin="anonymous">

	<link rel="stylesheet" href="style.css">
	<link rel="stylesheet" href="style_icon.css">
</head>
<body>
<a href="index.php">ACCUEIL</a><br><br>

<header>

	<div class="brand-box">
		<a href="./index.php" class="logo"><span class="hidden">RealtyEagle</span></a>
	</div>
      
	<nav class="topnav">
		<div class="dropdown">
			<button class="btn btn-indigo">Historique</button>
			<div>
				<a href="Recently closed" onclick="gtag('event', 'Recently closed', {'event_category': 'HEADER', 'event_label': 'Menu'});">Recently closed</a>
				<a href="Bookmarked" onclick="gtag('event', 'Bookmarked', {'event_category': 'HEADER', 'event_label': 'Menu'});">Bookmarked</a>
			</div>
		</div>
      

		<div class="dropdown">
			<button>Outils utiles</button>
			<div>
				<a href="useful" onclick="gtag('event', 'Acceder Contrats', {'event_category': 'HEADER', 'event_label': 'Menu'});">Calculateur d'int�r�t</a>
			</div>
		</div>
	</nav>

</header>
<div id="pages-list">
<div class="row row-large-gutters page-item" data-infinite-params="{&quot;pageView&quot;:&quot;\/annonce\/vente\/liste\/ile-de-france\/no-typebien&quot;,&quot;smartads&quot;:&quot;?&quot;}">

 <?php

 for($i=1;$i<sizeof($splitted)-2;$i++)
	{
	    $offer=explode(" ",$splitted[$i]);
	    $offer=array_values(array_filter($offer,"isempty"));

	    $price=$offer[1];
	    $estate_type=$offer[2] ; 
	    $distribution_type=$offer[3];  
	    $space=$offer[4];   
	    $id_solo=$offer[5];  
	    $photos_nb=$offer[6];
	    $floor_nb=$offer[7];
	    $nb_rooms=$offer[8];
	    $nb_bedrooms=$offer[9];
	    $estate_postalcode=$offer[10];
	    $url2post=$offer[11];
	    
	    $region=$region_names[$offer[12]];
	    $gain=$offer[14];
	    $gain_max=$offer[15];
	    $worthit=$offer[16];
	?>
				
<div class="col-1-3 ">
<div class="search-list-item-alt">
<div class="owl-carousel owl-loaded owl-drag" data-owl-carousel="{&quot;items&quot;:1, &quot;loop&quot;:true, &quot;nav&quot;:true}">
											
												
												
<div class="owl-stage-outer"><a href=<?php echo $url2post."?mea=alaune1&disableNav=true"; ?>  class="item-thumb-link" onclick="gtag('event', 'Consulter', {'event_category': 'LISTE VENTE', 'event_label': 'Resume Visuel'});" style="width: 387px;"></a>
  
<div class="owl-stage" style="transform: translate3d(0px, 0px, 0px); transition: all 0s ease 0s; width: 6574px;">
<div class="owl-item cloned" style="width: 346px;">
<div class="img-liquid imgLiquid_bgSize imgLiquid_ready" style="display: block; background-image: url(&quot;https://mmf.logic-immo.com/mmf/ads/photo-prop-640x480/fc6/5/569fb5df-d37b-48c2-97ef-d30d9d37e486.jpg&quot;); background-size: cover; background-position: center center; background-repeat: no-repeat;">
</div> </div></div>
 </div>
                          
                          
<div class="owl-nav">
<button type="button" role="presentation" class="owl-prev">
<span aria-label="Previous">‹</span>
</button>
<button type="button" role="presentation" class="owl-next">
<span aria-label="Next">›</span>
</button>
</div>
<div class="owl-dots owl-dots-count-9 owl-dots-active-2">
<button role="button" class="owl-dot">
<span></span></button>
<button role="button" class="owl-dot active">
<span></span></button>
<button role="button" class="owl-dot">
<span></span></button>
<button role="button" class="owl-dot">
<span></span></button>
<button role="button" class="owl-dot">
<span></span></button>
<button role="button" class="owl-dot">
<span></span></button>
<button role="button" class="owl-dot">
<span></span></button>
<button role="button" class="owl-dot">
<span></span></button>
<button role="button" class="owl-dot">
<span></span></button>
</div>
<div class="owl-thumbs"></div>
</div>
				
			
		<a href="#dialog-enregistrer-email" class="btn-add-favorite tooltip tooltipstered" data-annonce="{&quot;id&quot;:439902098,&quot;active&quot;:false}">
				<span class="icon icon-heart"></span>
		</a>

					<div class="item-tag">
				<span>Annonce à la une</span>
			</div>
			
				<div class="item-tag-alt">
			<span class="icon icon-leaf tooltip tooltipstered"></span>
		</div>
		
		<div class="item-body">
			<a class="item-title" href=<?php echo $url2post; ?> name=<?php echo $id_solo; ?> onclick="gtag('event', 'Consulter', {'event_category': 'LISTE VENTE', 'event_label': 'Resume Titre'});">
				<span class="h1"><?php  echo $region." (".$estate_postalcode.')'; ?>
								</span>
				<ul class="item-tags">
											<li><?php echo $nb_rooms;?> pi�ces</li>
											<li><?php echo $nb_bedrooms;?> chambre(s)</li>
											<li><?php echo $space;?> <small>m<sup>2</sup></small></li>
										</ul>
										<span class="item-price"><?php echo $price;?>&nbsp;€</span>
										<br><span class="item-price"><?php echo "Un gain potentiel de ".number_format($gain,0,".",",");?>&nbsp;€</span>
										<br><span class="item-price"><?php echo "Le gain, dans un cas optimiste, est plus que ".number_format($gain_max,0,".",",");?>&nbsp;€</span>

			</a>
			<p class="item-description" data-gaq="{&quot;category&quot;:&quot;LISTE VENTE&quot;,&quot;action&quot;:&quot;Consulter&quot;,&quot;label&quot;:&quot;Resume Description&quot;}">
					description...	</p>
		</div>
	</div>
</div>

<?php

}

?>

</body>  
</html>
  
