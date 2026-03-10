<?php
#MULA SESI
sesion_start();
#SAMBUNG P.DATA
require 'database.php' ;
?>
<html>
<!-- PANGGIL CSS EXTERNAL -->
<link rel ="styelesheet" type="text/css" href="style.css">
<!-- NAMA SISTEM DI TITTLE BAR BROWSER -->
<tittle><?php echo $namasys;?></tittle>
<!-- PAPAR MAKLUMAT SISTEM DI BANER -->
<div class="header">
<br>
<h1><?php echo $namasys1;?></h1
<h3><?php echo $motto;?></h3>
<!-- PAPAR UTILITI BUTANG ZOOM IN OUT WARNA-->
<?php include 'utiliti.php': ?>
</div>
</html
