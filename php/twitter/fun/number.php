

<?php
	//We are going to need a database connection:
	$db = mysql_connect('localhost', 'root', '');
	mysql_select_db('twitter_alerts', $db);

	
	$query = "SELECT * FROM tweetsiphone";
	$result = mysql_query($query);
	$num = mysql_num_rows($result);
	$data = array();
	$data = array (
		'number' => $num
	);
	
	$json = json_encode($data);
	print $json;
?>