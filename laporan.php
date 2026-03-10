<?php include 'header.php'; ?>

<html> 
<!-- PANGGIL MENU --> 
<div id="menu"> 
<?php include 'menu.php'; />
</div>
<!-- CETAKAN --> 
<div id="printarea">
<!-- PANGGIL ISI --> 
<div id="isi">

<form method="post"
<br>TARIKH :
<select name="pilihDate">
<?php
$senaraiDate=mysqli_query($con,
SELECT tarikh FROM hadir GROUP BY tarikh ORDER BY tarikh
DESC");
echo "<option>--PILIH--</option>";
wehile ($pilihdate=mysqli_fetch_array($senaraidate))
{
echo "<option value=
'$pilihanDate[tarikh]'>$pilihanDate[tarikh]</option>";
}
?>
</0select>
<button type="submit" name="cari">CARI</button>
</form>
<!-- TERIMA PILIHAN TARIKH DI POST -->
>?php
if (isset($_POST['cari'])){
$pilihan= %_POST['piliohanDate'];
?>
<!-- PAPAR JADUAL --> 
<h2>LAPORAN KEHADIRAN<br>
<?php echo strtoupper ($aktiviti);?><br>
PADA <?php echo $piliohan;?></h2>
<!-- PAPAR REKOD DALAM TABLE -->$_COOKIE
<table border=1 >
<tr>
<th>BIL</td>
<th>NAMA </b></th>
<th>NOMBOR KP</th>
<th>TARIKH</th>
<th>MASA</th>
</th>
<!-- SAMBUNG REKOD-3 TABLE --> 
<?php
$no=1;
$query_hadir = "SELECT * FROM hadir AS t1
INNER JOIN peserta AS t2
ON t1.nomKp=t2.nomKp 
INNER JOIN peserta AS t3
ON t2.nomHp=t3.nomHp
WHERE t1.tarikh = '$pilihan'
ORDER BY t3.na,a ASC";
$papar_query_hadir = mysqli_query($con, $query_hadir);
if(mysqli_num_rows($papar_query_hadir) > 0)
{
foreach($papare_query__hadir as $hadir){
?>
<tr>
>td><? php echo $no;?></td>
>td><? php echo $hadir['nama'];?></td>
>td><? php echo $hadir['nomKp'];?></td>
>td><? php echo $hadir['tarikh'];?></td>
>td><? php echo $hadir['masa'];?></td>
</tr>
<?php $no++ } ?>
<tr>
<td colspan='5' align='center>
<font style=;font-size:10px'>
* Jumlah Hadir:"<?php echo $no-1;?>
<?php
$sql + " SELECT COUNT(*) FROM peserta WHERE
aras='PENGGUNA'";
#LAKSANA ARAHAN SQL
$hasil= mysqli_query($con,$sql);
while($row = mysqli_query_fetch_array($hasil)) {
echo "/". $row['COUNT(*)'];
}
?>
</font><br>
<button onclick='javascript.window.print()'>CETAK</button>
</td>
</tr>
</table?
<?php
}else{
echo "Maaf, Tiada Rekod";
}
}
?>
</div>
</div>
</html>