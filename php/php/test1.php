<?php
ini_set('memory_limit', '-1');
include "db.php";

$sql = "SELECT * FROM tweetsiphone WHERE text LIKE '%RT%' LIMIT 1000000";
$result = mysql_query($sql);

$twit = array();
$numberOfRT = array();
$childid = array();
$text = array();
$screenname = array();
$numberOfFollower = array();
$i = 0;

while($row = mysql_fetch_object($result)){
    $childid[$i] = $row->id;
    $text[$i] = $row->text;
    $screenname[$i] = $row->screen_name;
    $numberOfFollower[$i] = $row->followers_count;
    
    $dataid[$screenname[$i]] = $childid[$i];
    $datanumfol[$screenname[$i]] = $numberOfFollower[$i];
    $i++;
}



for($i=0;$i<1000000;$i++){
    
    $after = explode("RT @", $text[$i]);
    $after2 = $after[1];
    $parentname = explode(" ", $after2);
    $parentname2 = $parentname[0];
    $parentname3 = explode(":", $parentname2);
    $parentname4 = $parentname3[0];
    $parentname = $parentname4;
    
    $parentid = $dataid[$parentname];
    $parentnumfol = $datanumfol[$parentname];
    
    if($parentid==''){
        continue;
    }
    
    
    $t = $parentid;
    $n = $parentnumfol;
    
    $inp = "0 ".strval($t)." ".strval($n)." ".strval($parentname);
    if(in_array($inp,$twit)){
        $pos = array_search($inp,$twit);
        array_push($numberOfRT, $inp);
        $number = array_count_values($numberOfRT);
        $twit[$pos] = strval($number[$inp])." ".strval($t)." ".strval($n)." ".strval($parentname);
    }
    else if(in_array(strval($number[$inp])." ".strval($t)." ".strval($n)." ".strval($parentname), $twit)){
        $pos = array_search(strval($number[$inp])." ".strval($t)." ".strval($n)." ".strval($parentname),$twit);
        array_push($numberOfRT, $inp);
        $number = array_count_values($numberOfRT);
        $twit[$pos] = strval($number[$inp])." ".strval($t)." ".strval($n)." ".strval($parentname);
    }
    else{
        array_push($twit,$inp);
    }
    
    
}


foreach($twit as $itwit){
    echo $itwit;
    echo "\n";
}





