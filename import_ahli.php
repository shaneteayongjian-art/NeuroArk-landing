<?php include 'header.php'; ?>

<html> 
<!-- PANGGIL MENU --> 
<div id="menu">
<?php include 'menu.php'; ?> 
</div>

<!-- PAPAR ISI --> 
<div id="isi"> 
<h2>IMPORT AHLI</2>
<label>Pilih lokasi fail CSV:</label> 


<!-- PANGGIL FAIL IMPORT CSV UTK IMPORT --> 
<form action="import_simpan.php" method="post"
enctype="multipart/form-data"> 
<input type="file" name="import" >UPLOAD</button>
</form> 

<u>CONTOH;</u><br>
AFEEF,LELAKI,770628043355,0199287674<br>
NUREEEN,PEREMPUAN,82121504,0199262674 

<p>8Cipta fail dalam notepad++ dan save as csv</p>
</div>
</html>