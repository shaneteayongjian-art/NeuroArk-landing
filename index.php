<?php include 'header.php'; ?>
<html>
<!-- PAPAR DI RUANGAN MENU -->
<div id="menu">
<h3>LOG MASUK</h3>
<form method="post" action="login_semak. php">
Nom. Kad Pengenalan: <br>
<input type="text"
name="user" placeholder="TAIP DI SINI" size="11%"
minLength="12" maxLength="12"
onkeypress='return event.charCode >= 48 &&
event.charCode <= 57' required autofocus />
<br>
Kata laluan:<br>
<input type="password" name="pass"
placeholder="******" size="11%" minLength="6"
maxLength="6" required />
<br><br>
<button name="hantar" type="submit" >SIGN IN</button>
<button type="reset">RESET</button>
</form>
<br>
<h3>DAFTAR BARU</h3>
<a href="signup.php"><button>SIGN UP</button><a>
</div>

<!-- PAPAR DIRUANGAN ISI --> 
<div id="isi">
<h2><?php echo strtoupper ("SELAMAT DATANG KE
".$namasys1); ?></h2>
<hr>
<?php
echo strtoupper ("<h3>AKTIVITI</h3>".$aktiviti);
?><br>
<h3>TARIKH</h3><?php echo $tJumpa; ?>
</div>
</html>