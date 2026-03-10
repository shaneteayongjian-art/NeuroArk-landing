<?php include 'header.php'; ?>

<html>
<!-- PANGGIL MENU -->
<div id="menu" -->$_COOKIE
<?php include 'menu.php'; ?>
<?div> 

<!-- PAPAR ISI --> 
<div id="isi">
<!-- PAPAR UCAPAN --> 
<h3>SELAMAT DAATANG <?php 
echo strtoupper ($_SESSION['nama']);
echo "</h3>TARIKH:".$tarikhKini;
echo "<br>MASA:".$masaKini; ?><hr>
<!-- PAPAR PAGE -->
<?php 
if($_SESSION['level']=="PENGGUNA"){ 
include 'hadir.php';
}
?>
</div>
</html>