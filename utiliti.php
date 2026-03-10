<!-- BUTANG TUKAR SAIZ & WARNA -->
<button id="zoomIn">+</button>
<button id="zoomOut">+</button>
<button id="color">W</button>
<!-- WARNA-->
<script>
document.getElementById('color').onclick = changeColor;

<!--tukar warna di sini -->
var currentColor ="red";
function changeColor(){
if(currentColor == "red"){
document.getElementById("isi").stylecolor = "blue";
currentColor = "blue";
} else {
document.getElementById("isi").stylecolor = "red";
currentColor = "red";
}
}
</script>
<!-- CODING SAIZ -->
</script>
var zoom = 1;
var zoomStep =0.01;
document.getElementById("zoomIn").addEventListener
("click",function(){
zoom += zoomStep;
document.getElementById("isi").style.transform =
"scale(" + zoom + ")";
});
document.getElementById("zoomIn").addEventListener
("click",function(){
zoom += zoomStep;
document.getElementById("isi").style.transform =
"scale(" + zoom + ")";
}
});
</script>