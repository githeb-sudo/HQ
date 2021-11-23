<?php

/*
To avoid the "Missing mandatory params" error, we can use the required attribute
To avoid the "Invalid page size requested", we can use the min and max attributes
*/

class Invalid_node_id_Exp extends Exception
{
    public function invalid_node_id_fun()
    {
        $invalid_node_id = "<b>Invalid node id</b>: " . $this->getMessage() . ' is not found.';
        return $invalid_node_id;
    }
}
class Missing_mandatory_params_Exp extends Exception
{
    public function missing_mandatory_params_fun()
    {
        $missing_mandatory_params = "<b>Missing mandatory params<b>: " . $this->getMessage() . " is a required input parameter.<br> Ergo, its value must not be empty or null.";
        return $missing_mandatory_params;
    }
}
class Invalid_page_number_requested_Exp extends Exception
{
    public function invalid_page_number_requested_fun()
    {
        $invalid_page_number_requested = "<b>Invalid page number requested<b>: " . $this->getMessage() . ' is not a valid 0-based index.';
        return $invalid_page_number_requested;
    }
}
class Invalid_page_size_requested_Exp extends Exception
{
    public function invalid_page_size_requested_fun() {
        //error message
        $invalid_page_size_requested = "<b>Invalid page size requested<b>: ".$this->getMessage().' is out of range.';
        return $invalid_page_size_requested;
    }
}
$search_keyword=htmlspecialchars($_GET['search_keyword']);
$nodeid=htmlspecialchars($_GET['nodeid']);
$page_num=htmlspecialchars($_GET['page_num']);
$page_size=htmlspecialchars($_GET['page_size']);

include('connexionPDO.php');
$reponse=$bdd->query('SELECT idNode FROM node_tree WHERE idNode= \''.$nodeid.'\'');
try {
    if (implode($_GET['language']) == ' ' or $nodeid=='')
    {
        throw new Missing_mandatory_params_Exp(($nodeid=='')?"node ID":"language");
    }

    elseif (!($data=$reponse->fetch()))
    {
        throw new Invalid_node_id_Exp($nodeid);
    }

    elseif (!(is_numeric($page_num) and ($page_num)>=0) and (($page_num)!=""))
    {
        throw new Invalid_page_number_requested_Exp($page_num);
    }
    elseif ((0>=$page_size or $page_size>1000) and ($page_size!=""))
    {
        throw new Invalid_page_size_requested_Exp($page_size);
    }
}
catch(Missing_mandatory_params_Exp $e)
{
    header('Location: errorInterface.php?errormsg='.$e->missing_mandatory_params_fun());
    exit();
}
catch(Invalid_node_id_Exp $e)
{
    header('Location: errorInterface.php?errormsg='.$e->invalid_node_id_fun());
    exit();
}
catch(Invalid_page_number_requested_Exp $e)
{
    header('Location: errorInterface.php?errormsg='.$e->invalid_page_number_requested_fun());
    exit();
}
catch(Invalid_page_size_requested_Exp $e)
{
    header('Location: errorInterface.php?errormsg='.$e->invalid_page_size_requested_fun());
    exit();
}

if($search_keyword!='') {
    $reponse = $bdd->query('SELECT node_tree.idNode,nodeName,ileft,iright FROM node_tree,node_tree_names WHERE 
                        node_tree.idNode=node_tree_names.idNode
                        and ileft >(SELECT ileft from node_tree where idNode= \'' . $nodeid . '\' )
                        and iright<(SELECT iright from node_tree where idNode= \'' . $nodeid . '\' )
                        and language in (\''.implode('\',\'',$_GET['language']).'\')
                        and nodeName like \'%'.$search_keyword.'%\' ');
    // like is case-insensitive by default
}
else{
    $reponse = $bdd->query('SELECT node_tree.idNode,nodeName,ileft,iright FROM node_tree,node_tree_names WHERE 
                        node_tree.idNode= \'' . $nodeid . '\' 
                        and node_tree.idNode=node_tree_names.idNode
                        and language in (\''.implode('\',\'',$_GET['language']).'\')
                        ');
}

$nodes=[];
while($data=$reponse->fetch())
{
    /*
    extract($data);
    $childCount=(int)(($iright-$ileft)/2);
    */

    $childCount=(int)(($data[3]-$data[2])/2);
    $idNode=$data[0];
    $nameNode=$data[1];
    array_push($nodes,compact("idNode","nameNode","childCount"));
}
$nodes=base64_encode(serialize($nodes));
$nodesEnc=urlencode($nodes);
$page_num=($page_num!='')?$page_num:0;
$page_size=($page_size!='')?$page_size:100;

header('Location: result.php?page_num='.$page_num.'&page_size='.$page_size.'&nodes='.$nodesEnc);
?>