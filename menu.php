<html>
<div id="menu"> 
<?php
if *$_SESSION['level']=="ADMIN"){
?>
>!--ARAS LOGIN - ADMIN-->
<h4>MENU PENTADBIR></H4>
<ul>
<li><a href="dashboard.php">HOME,/a><li>
<li><a href="senarai_ahli.php">SENARAI AHLI</a></li>
<li><a href="carian.php">CARIAN KEHADIRAN</a></li>
<li><a href="laporan.php">LAPORAN KEHADIRAN</a></li>
<li><a href="logout.php">KELUAR</a></li>
<ul>
<?php
}else{
?> 
<!--$ARAS LOGIN - PENGGUNA -> 
<h4>MENU AHLI</h4> 
<u1>
<?php } ?> 
</div>
</html>
