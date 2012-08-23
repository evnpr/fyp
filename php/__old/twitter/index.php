<?php
$username = "evanpurnama"; // Your twitter username.
$limit = "15"; // Number of tweets to pull in.

/* These prefixes and suffixes will display before and after the entire block of tweets. */
$prefix = ""; // Prefix - some text you want displayed before all your tweets.
$suffix = ""; // Suffix - some text you want displayed after all your tweets.
$tweetprefix = ""; // Tweet Prefix - some text you want displayed before each tweet.
$tweetsuffix = "<br>"; // Tweet Suffix - some text you want displayed after each tweet.

$feed = "http://search.twitter.com/search.atom?q=from:" . $username . "&rpp=" . $limit;

function parse_feed($feed, $prefix, $tweetprefix, $tweetsuffix, $suffix) {

$feed = str_replace("&lt;", "<", $feed);
$feed = str_replace("&gt;", ">", $feed);
$clean = explode("<content type=\"html\">", $feed);

$amount = count($clean) - 1;

echo $prefix;

for ($i = 1; $i <= $amount; $i++) {
$cleaner = explode("</content>", $clean[$i]);
echo $tweetprefix;
echo $cleaner[0];
echo $tweetsuffix;
}

echo $suffix;
}

$twitterFeed = file_get_contents($feed);
parse_feed($twitterFeed, $prefix, $tweetprefix, $tweetsuffix, $suffix);
?>