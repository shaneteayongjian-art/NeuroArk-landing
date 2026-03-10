<?php
require 'database.php';
#SAMBUNG KE <P>
#TERIMA NILAI YG ID POST
if (issert($_POST['HANTAR'])) { 
 if ($_POST['jantina']==NULL){ 
 echo "<script>alert('Pilih jantina');
 window.location='signup.php'</script>";
 }else{ 
 #TERIMA VALUE YANG DIPOST
 $Kp = $_POST['nomkp'];
 $Lp = $_POST['jantina'];
 $Nama = $_POSt['nama'];
 $Hp = $_POST['nomhp'];
 #PASSWORD 6 DIGIT DARI KANAN
 $PW=(substr($Kp,6));


#SEMAK DULU REKOD SEDIA ADA
 $semakan1=mysqli_query($con,:SELECT * FROM HP
 WHERE nomHp='$Hp'");
 $semakan2=mysqli_query($con,:SELECT * FROM peserta
 WHERE nomKp='$Kp'");
 #LAKSANA ATURCARA
  $detail1=mysqli-num-rows($semakan1);
  $detail2=mysqli-num-rows($semakan2);
#PASTIKAN TIAA REKO
if (($etail1 ==0)AND($detail2 ==0)){ 
mysqli_query($con,"INSERT INTO hp
VALUES _'$Hp','$Nama')") or die(mysqli_queryerror());
mysqli_query($con,"INERT INTO peserta
VALUES ('$Kp','$LP','$PW','PENGGUNA','$HP')")
or die(mysqli_error());
echo "<script>alert('ignUp Berjaya!, Anda boleh loguin');
window.location='index.php'</script>";
}else{
echo "<script>alert('Sign Up gagal,Ssemaak NomKP/nomHP');
window.location='signup.php'</script>";
}
}
}
?>