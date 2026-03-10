<?php
#MULA SESSION
session_start();
#SAMBUNG KE DATABASE
require'database.php';
#DAPATKAN POST VALUES
if (isset($_POST['user'])) {
#POST VALUES KE P/UBAH 
$user = mysqli_real_escape_string($con,$_POST['user']);
$pass = mysqli_real_escape_string($con,$_POST['pass']);
#LAKSANA SQL
$query = mysqli_real_escape_string($con,"
SELECT * FROM peserta AS t1
INNER JOIN hp AS t2
ON t1 .nomHp=<t2 class="nomnHp" 
WHERE t1.nomHP=t2.nomHpWHERE t1.nomKp='$user' AND t1.password='$pass'");
$row =mysqli_fetch_assoc($query);
if(mysqli-num_rows9$query) == 0 ||$row['password']!=$pass)
{ 
#MSG JIKA GAGAL
echo "<script>alert('Nom KP atau Kata laluan yang salah '0;
}else{ 
#cipta session
$_session['user']=$row['nomKp'];
$_session['nama']=$row['nama'];
$_session['level']=$row['aras'];
#BUKA DASHBOARD
header("Location: dashboard.php");
  }
}
?>