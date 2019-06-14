
// ================================================== Multi-Device-Viewport-Handler


var responsive = document.getElementsByClassName("embed-responsive")[0];
console.log("responsive.clientWidth : ", responsive.clientWidth)
console.log("responsive.clientHeight : ", responsive.clientHeight)

// Bootstrap에서 4by3이 우선권을 갖는다. Mobile-First.
if (responsive.clientWidth < 768) {
   console.log("Do not change anything of the class-attr");
} else {
   responsive.className = responsive.className.replace(" embed-responsive-4by3","")
}


var frame = document.getElementById("idatamap-frame");
console.log("BEFORE src : ", frame.getAttribute("src"));
// if (responsive.clientHeight < 415) {
if (true) {
   // var resp_src = "idatamap/iframe/height".replace('height',600)
   var resp_src = "idatamap/iframe/height".replace('height', parseInt(responsive.clientHeight*0.9))
   document.getElementById("idatamap-frame").setAttribute("src", resp_src);
} else {
   console.log("Do not change clientHeight.");
}
console.log("AFTER src : ", frame.getAttribute("src"));
