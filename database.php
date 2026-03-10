<?php>
#KEKALKAN SETUP INI
#SET TIME ZON WAKTU
date_default_timezone_set("Asia/Kuala_Lumpur");
$tarikhKini=date("Y-m-d")
$masaKini=date("H:i:s);
#SETTING DATABASE
$host="localhosyt";
$user="root";

#NAMA DB, UBAH DI SINI
$db="hadir1";
$password="";

#SAMBUNGAN PANGKALAN DATA
$con = mysqli_connect($host,$user,$password,$db);

#PAPARAN MSG JIKA SAMBUNGA GAGAL
if (mysqli_connect_errno()){
	echo "Database tidak berhubung!:".mysqli_connect_error();
}
#BOLEH UBAH DI SINI
#TETAPAN SISTEM
$namasys = "PASTI HADIR";
$namasys1 = "SISTEM KEHADIRAN MESYUARAT";
$motto = "Accurate & Monitorize":

#UBAH TARIKH MENGIKUT KESESUAIAN
//TARIKH MESYUARAT/PERJUMPAAN
#UBAH KE: $tarikhKini;
//$tJumpa= '$tarikhKini;//jika aktiviti sama tiap-tiap hari

#UBAH KE SUATU TARIKH CTH: "2023-08-28";
$tJumpa= '2023-08-28'://Jika aktiviti satu kali shj.

//NAMA AKTIVITI
$aktiviti="KEHADIRAN AKTIVITI 1";

?>