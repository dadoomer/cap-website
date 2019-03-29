<?php 
$a = session_id();
if(empty($a)) {
  session_start(); /// initialize session 
}
include("jeeveslib.php"); 
check_variables();

if ($_POST["ac"]=="log") { /// do after login form is submitted  
  // If submitted username and password are valid, then go straight to the 
  // index.
  if (password_authenticate("jconf", $_POST["username"], $_POST["password"])) {
    set_session_user($_POST["username"]);
  }
};
if (array_key_exists($_SESSION["logged"],$USERS)) { //// check if user is logged or not  
  header( 'Location: index.php' ); 
} else { //// if not logged show login form 
  include("login_screen.php");
}; 
?>
