<?php
$a = session_id();
if(empty($a)) session_start(); /// initialize session 
include 'jeeveslib.php';
check_logged();

if ($link) {
  mysql_close($link);
}

session_unset();
session_destroy();
?>

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<META name="verify-v1" content="E7CAKdK/YXZzYIZ/7WWURP/gYAyHqrf6YOcW8U1AjaM=" />
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<title>jconf - home</title>
<meta name="" content="" />
<link href="default.css" rel="stylesheet" type="text/css" />
</head>
<body>
<div id="wrapper">
  <div id="header">
  <h1>jconf . csail</h1>
  </div>
  <div id="menu">
    <ul>
      <li><a href="login.php" accesskey="7" title="">Log in</a></li>
    </ul>
  </div>
  <div id="content">
    You are logged out.
  </div>
  <div id="footer">
    <p>&copy; 2011 Jean Yang.</p>
  </div>
</div>
</body>
</html>
