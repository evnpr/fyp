<?php
	include "tablename.php";
	//We are going to need a database connection:
	$db = mysql_connect('localhost', 'root', '');
	mysql_select_db('twitter_alerts', $db);
	//Now, two possibilities: if we don't have a start parameter, we print the last ten $tablename.
	//Otherwise, we print all the $tablename with IDs bigger than start, if any
	$start = mysql_real_escape_string($_GET['start']);
	if(! $start){
		$query = "SELECT * FROM (SELECT * FROM $tablename ORDER BY userid DESC LIMIT 0,10) AS last_ten ORDER BY userid ASC";
	}else{
		$query = "SELECT * FROM (SELECT * FROM $tablename WHERE userid>".$start." ORDER BY userid DESC LIMIT 0,10) AS new_tweets ORDER BY userid ASC";
	}
	
	$result = mysql_query($query);
	$data = array(); //Initializing the results array
    
	while ($row = mysql_fetch_assoc($result)){
		array_push($data, $row);
	}
	$json = json_encode($data);
	print $json;
?>