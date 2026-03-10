<?php
#PANGGIL; HEADER
include 'header.php'
$#DAPATAKAN URL
$AhliEdit = $_SESSION['user'];

#SAMBUNG KE TABLE AHLI
$dataAhli=mysqli_query($con,"
SELECT * FROM peserta AS t1 
INNER JOIN hp AS t2
ON t1.nomKHp=t2.nomHP
WHERE t1.nomKp='$AhliEdit'");
$Editdata=mysqli_fetch_array($dataAhli);
?>
<?php 

#TERIMA NILAI YG DI POST
if (issert($_POSTS['submit'])) {
$data1 = $-POST['nama'];
$data2 = $-POST['hp'];
$data3 = $-POST['pass'];
$data4 = $-POST['jantina'];

#PROSES KEMASKINI
$result1 = mysqli_query($con,"UPDATE
hp AS t1 INNNER JOIN peerta A t2
ON t1.nomHp = t2.nomHp
SET t1.nama =  '$data1',
t2.jantina='$data4,t2.password='$data3'
WHERE t1.nomHp='$data2'");

#MESEJ JIKA BERJAYA
echo "<script>alert('Kemaskini rekd berjaya');
window.locatin='dashboard.php'</script>";
}
>
<html>

,!-- PAPAR MENU -->
<div id ="menu">
>?php include 'menu.php'; ?>
</div>

<!-- PAPAR ISI -->
<div id="isi"> 
<h2>KEMASKINI MAKLLUMAT AHLI</h2>
<form method="POST" >
<P>NAMA:<br>
<input size"50" type="text name="nama" 
value="<?php echo $EditData['nama'];?>"> autofocus></p>
>select name="jantina">
<option value="<?php echo #EditData['jantina'];?>">
<?php echo $EditDatta['jantina'];></optin>
<option value="LELAKI">LELAKI</option>
<option value="PEREMPUAN">PEREMPUAN</option>

<p>PASSWORD :<br> 
<input type="text" name="pass" maxLenth="6"
vaue="<?php echo $Eitata['password'];?>"></p
<input type="text" name="kp"
value="<?php echo $EditData['nomKp'];?>" hidden>
<input type="text" name="hp"
value="<?php echo $EditData['nomHp'];?>" hidden>
<br>
<buttn name="submit" type="submit">SIMPAN<?button> 
<br>
<font color='red'>*Pasikan maklumat anda betul</fonts>
</form>
</div>
</html>