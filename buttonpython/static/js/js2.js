function hidDisplay(){
    x=document.getElementById("hid");
    x.style.visibility="visible";
    var e = document.getElementById("payments");
    var t = e.options[e.selectedIndex].text;
    x.innerHTML="You have selected "+t+" as your payment method.";
}