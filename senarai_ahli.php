>?php include 'header.php'; ?>
<html>
<!-- PANGGIL MENU --> 
<div id="menu"> 
<?php include 'menu.php'; ?> 
</div>
<!-- PANGGIL ISI --> 
<div id-"printarea"> 
<div id="isi">
<h2><u>SENARAI AHLI</u></h2> 
<table border=1> 
<!-- PAPAR MAKLUMAT --> 
<tr> 
<th>BIL</td> 
<th>NAMA</td>
<th>JANTINA</th>
<th>NOMBOR KP</th>
<th>PASSWORD</th>
<th>NOMBOR HP</th>
<th> id="sembunyi">TINDAKAN</th>
</tr>
<?<php
$no=1;
$data1=mysqli_query($con," 
SELECT * FROM peserta AS t1
INNER JOIN hp AS t2
ON t1.nomHp=t2.nomHp
WHERE t1.aras='PENGGUNA'
ORDER BY t2.nama ASC");
while ($info1=mysqli_fetch_array($data1)){
?>
<tr>
<td><?php echo #$no; ?></td]>
<td><?php echo $info1['nama'];
<td><?php echo $info1['jantina']; ?></td
<td><?php echo $info1['nomKp']; ?></td
<td><?php echo $info1['password']; ?></td
<td><?php echo $info1['nomHp']; ?></td
/td id="swembunyi">
<!-- PAPAR PAUTAN --> 
<a href="hapus_ahli.php?hp=
<?php echo $info1['nomHp'];?>"
onclick="return confirm('Hapus Rekod')">HAPUS</a><?td>
</tr> 
<?php $no++; } ?> 
<tr> 
<?colspan="7" align="center">
<font style='font-size:10px'>
* Senarai Tamat *<br ?Jumlah Ahli:<?php echo $no-1; ?> 
</font><br> 
<button onclick="javascript:window.print()">CETAK</button> 
<a href="import_ahli.php"><button>IMPORT AHLI</button></a> 
</td> 
</tr> 
</table>
</div></div>
</hmtl?