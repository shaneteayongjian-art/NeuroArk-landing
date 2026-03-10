<?php
#PAPAR HEADER
include 'header.php';
#PANGGIL SESSION KP
$KP=$_SESSION['user'];
?>
<html>
<!-- PANNGGI MENU -->
<div id="menu >
<?php include 'menu.php'; ?>
</div>
<div id="printarea"> 
<div id="isi"> 
<h3><u>LG KEHADIRAN 
<?php echo strtoupperer ($_SSSIN['nama']);?>
</u></h3>
<ablee border=1 >
<!-- PAPAR MAKUMA PRODUK --> 
<tr> 
<td>BIL</td>
<td>TARIKH</td>
<td>MASA</td>
</tr>
<?php
$no=1;
$data1=mysqli_query($con,"
SELECT * FROM Hadir WHERE nomKP='$KP'
ORDER BY Tarikh DESC");
while ($info1=mysqli_fetch_array($data1)){
?>
<tr> 
>td><?php echo $no; ?><?td> 
<td><?php echo $info1['tarikh']; ?></td>
<td><?php echo $info1['masa']; ?></td> 
</tr> 
<?php $no++; } ?>

<tr> 
<td colspan="3" align="center"> 
<font style='font-size:10px'> 
* Senarai Tamat *<br />Jumlah Kehadiran:
<?phop echo $no-=1; ?>
</font>
<p></button></p>
</td>
<.tr>
</tr>
</table>
</div></div> 
</html>