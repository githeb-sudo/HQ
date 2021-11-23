<!DOCTYPE HTML>

<html>
<head>
    <link rel="stylesheet" type="text/css" href="result.css" >
</head>
<body>
	
	<div class="bloc_page">
		<center>

			
			<?php 
			function sanitize($s) { return htmlspecialchars($s);}
			$nodes=$_GET['nodes'];
			$nodesUnserialized=unserialize(base64_decode(urldecode($nodes)));
			array_walk_recursive($nodesUnserialized,"sanitize");
			$page_size=htmlspecialchars($_GET['page_size']);
			$page=htmlspecialchars($_GET['page_num']);
			$total=count($nodesUnserialized);
			$pages = ceil($total / $page_size)-1;
			$current_first=$page*$page_size;
			
			$current_page=array_slice($nodesUnserialized,$current_first,$page_size);
			// We don't need a specific process to manage the last page in case its elements' count is less than $page_size.

			$nextpage=$page+1;
			$prevpage=$page-1;
            $prevlink = ($page > 0) ? "<a href='?page_num=0&page_size=$page_size&nodes=$nodes' title='First page'><div class='navigationBtn'>&laquo;</div></a>
            <a href='?page_num=$prevpage&page_size=$page_size&nodes=$nodes' title='Previous page'><div class='navigationBtn'>&lsaquo;</div></a>"
            : '<span class="disabled">&laquo;</span> <span class="disabled">&lsaquo;</span>';
            $nextlink = ($page < $pages) ?"<a href='?page_num=$nextpage&page_size=$page_size&nodes=$nodes' title='Next page'><div class='navigationBtn'>&rsaquo;</div></a>
            <a href='?page_num=$pages&page_size=$page_size&nodes=$nodes' title='Last page'><div class='navigationBtn'>&raquo;</div></a>"
            : '<span class="disabled">&rsaquo;</span> <span class="disabled">&raquo;</span>';
                        ?>
            <div class="result" ><?php echo "<pre>".json_encode($current_page,JSON_PRETTY_PRINT)."<pre>"; ?></div>
            <div class="pagination" >
            <?php
            if($page<=$pages){
            echo $prevlink, ' Page ', $page+1, ' of ', $pages+1, ' page(s), displaying ', $current_first+1, '-', min($current_first+$page_size,$total), ' of ', $total, ' result(s) ', $nextlink;
            }
            else {echo $prevlink.'The requested page is out of range';} ?>
            </div>
            
            <!-- We can pass the nodeId and search_keyword using $_GET to make a more detailed PDF -->
            <!-- It is possible to add the "download current page only" feature -->
            
            <a href=<?php echo "downloadResultPDF.php?nodes=".$nodes; ?> target="_self" ><div class="btn" >Download as PDF</div></a>
            <a href="formInterface.php" target="_self" ><div class="btn" >Search again</div></a>
            <a href="../api.php" target="_self" ><div class="btn" >Home</div></a>
		</center>
	</div>
</body>
</html>
