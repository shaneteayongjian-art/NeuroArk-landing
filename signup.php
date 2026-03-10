<?php include 'header.php'; ?>
<html> 
>!-- PANGGIL MENU --> 
<div id="isi">
<h2>PENDAFTARAAN AHLI BARU </h2>
<body> 
<form method="POST" action="signup_simpan.php">
<font color='red'>8Pastikan maklumat anda betul sebelum
    membuat pendaftaran.</font> 
<p>Nom Kad Pengenalan<br> 
<input type="text" name"nomkp" placeholder="Nombor KP
tanpa tanda -" minLength='12' maxLenth='12'
size="30" onkeypress='return event.charCode >=48 &&
event.charCode <= 57' required autofocus><br>
<font style='font-size:10px',color='red'>*Password adalah
6 digit akhir nom Kp dijana secara automatik.</font></p>
<p>Nama<br>
<input type="text" name="nama" placeholder="Nama Anda"
size="60" required></p>
<p>Jantina<br>
<select name="jantina">
<option value="">--PILIH--</option>
<option value="LELAKI">LELAKI</option>
<option value="PEREMPUAN">PEREMPUAN</option>
</select></p>
<p>Nom HP<br>
<input type="text" name="nomhp" placeholder="Tanpa - "
minLenth='10' maxLenth='14'
size='30' onkyepress='return event.charCode >= 48 && 
event.charCode <=57' require></p>
<br>
<div> 
<button name="hantar" type="submit">DAFTAR</button>
<button type="reset">RESET</button>
</div>
</form>
</body>
</div>
</html>