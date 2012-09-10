

<?php
	include "tablename.php";
	//We are going to need a database connection:
	include "db.php";

	
	$query = "SELECT * FROM $tablename";
	$result = mysql_query($query);
	$num = mysql_num_rows($result);
	$data = array();
	$data = array (
		'number' => $num
	);
	
	$json = json_encode($data);
	print $json;
?>
