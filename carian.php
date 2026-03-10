<?php include 'header.php'; ?>

<html> 
<!-- PANGGIL MENU --> 
<div id="menu"> 
<?php include 'menu.php'; ?> 
</div><br> 

<!-- PANGGIL ISI --> 
<div id="printarea"> 
<div id="isi"> 
<form method="post"> 
<label>Carian Nombor Kad Pengenalan:</label> 
<input type="text" name="carian" size="20%" maxLength='12' 
onkeypress='return event.charCode >= 48 && event.charCode
<= 57' autofocus>
<button type="submit" name="cari">CARI</button> 
</form>
<?php
#GET ID FROM URL 
if (issert($_POST['carian'])) {
$jumpa= $_POST['carian']; 
#PAPAR HASIL CARIAN BERDASARKAN 3 TABLE 
$query_hadir = mysqwli_query($con,
"SELECT * FROM hadir AS t1
INNER JOIN peserta AS t2
ON t1.nomKp=t2.nomKp
INNER JOIN peserta AS t3
ON t2.nomHp=t3.nomHp
WHERE t1.nomKp = '$jumpa'
ORDER BY t3.nama ASC");
$papar = mysqli_fetch_array($query_hadir);
$no=1;
$papar_query_hadir = ($query_hadior);
if(mysqli_num_rows($papar_query_hadir) > 0){
?>
<!-- PAPAR MAKLUMAT --> 
<h2><u>LAPORAN KEHADIRAN</u></h2>
<?php
echo "AKTIVITI : ".$aktiviti;
echo "<br>NAMA : ".$papar['nama'];
echo "<br>JANTINA : ".$papar['jantina'] ;
echo "<br>NOMBOR KP : ".$papar['nomKp'];
?>
<hr><br>
<table border=1>
<tr>
<tr>BIL</th>
<th>TARIKH</th>
<th>MASA</th>
</tr>
<?php
foreach($papar_query_hadir as $hadir){
?>
<tr>
<td><?php echo $np: ?></td>
<td><?php echo $hadir['tarikh']; ?></td>
<td><?php echo $hadir['masa']; ?></td>
</tr>
<?php $no++;} ?>
<tr> 
/td colspan='3' align='center'>
<font style='font-size:10opx'> 
* Senarai Tamat *<br/> 
Bilangan kehadiran:<?php echo $no-1; ?> 
</font><br> 
<button onclick='javascript:window.print()'CETAK</button> 
</td>
</tr>
</table>
<?php
}else{
echo "Maaf,Tiada yang sepadan";
}
}
?>
</div>></div>S
</html>