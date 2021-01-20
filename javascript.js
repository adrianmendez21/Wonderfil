var myVar;
var currentOz = 0.0;
var elem = document.getElementById('bar');
var dispenseAmount = 0.0;

function clickFunc16()
{
    document.getElementById("button16").style.visibility = "hidden";
    document.getElementById("button18").style.visibility = "hidden";
    document.getElementById("button24").style.visibility = "hidden";
    dispenseAmount = 16.0;

    document.getElementById("dispensing").innerHTML = "Dispensing...";
    var percent = 0.0
    myVar = setInterval(ifCheck, 1000);
}

function clickFunc18()
{
    document.getElementById("button16").style.visibility = "hidden";
    document.getElementById("button18").style.visibility = "hidden";
    document.getElementById("button24").style.visibility = "hidden";
    dispenseAmount = 18.0;

    document.getElementById("dispensing").innerHTML = "Dispensing...";
    var percent = 0.0
    myVar = setInterval(ifCheck, 1000);
}

function clickFunc24()
{
    document.getElementById("button16").style.visibility = "hidden";
    document.getElementById("button18").style.visibility = "hidden";
    document.getElementById("button24").style.visibility = "hidden";
    dispenseAmount = 24.0;

    document.getElementById("dispensing").innerHTML = "Dispensing...";
    var percent = 0.0
    myVar = setInterval(ifCheck, 1000);
}

function ifCheck()
{
    if(currentOz + 0.28178333 > dispenseAmount) // using 500 mL per minute
    {
        currentOz = currentOz + (dispenseAmount - currentOz);
        var div = currentOz/dispenseAmount;
        percent = (div)*100;
        var roundedP = percent.toFixed(2);
        var roundedO = currentOz.toFixed(2);
        document.getElementById("num").innerHTML = roundedP + "%";
        document.getElementById("ounces").innerHTML = roundedO + "oz";
        elem.style.width = percent + "%";
        document.getElementById("dispensing").innerHTML = "Complete!";
        alert('Thank you! Have a Wonderfil day!');
        clearInterval(myVar);
    }

    else
    {
        currentOz = currentOz + 0.28178333;
        var div = currentOz/dispenseAmount;
        percent = (div)*100;
        var roundedP = percent.toFixed(2);
        var roundedO = currentOz.toFixed(2);
        document.getElementById("num").innerHTML = roundedP + "%";
        document.getElementById("ounces").innerHTML = roundedO + "oz";
        elem.style.width = percent + "%";
    }
}