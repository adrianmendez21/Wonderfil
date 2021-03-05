var myVar;
var currentOz = 0.0;
var elem = document.getElementById('bar');
var dispenseAmount = 0.0;
var cost = 0.0;
var pricePerOunce = 0.0;
var currCost = 0.0;
var abort = false;

function clickFunc16()
{
    myVar;
    currentOz = 0.0;
    elem = document.getElementById('bar');
    dispenseAmount = 0.0;
    cost = 0.0;
    pricePerOunce = 0.0;
    currCost = 0.0;
    abort = false;
    document.getElementById("button16").style.display = "none";
    document.getElementById("button18").style.display = "none";
    document.getElementById("button24").style.display = "none";
    document.getElementById("stop").style.display = "inline";
    dispenseAmount = 16.0;
    cost = 7.99;
    pricePerOunce = cost/dispenseAmount;

    document.getElementById("select").innerHTML = "To stop dispensing, click the stop button";
    document.getElementById("dispensing").innerHTML = "Dispensing...";
    var percent = 0.0
    myVar = setInterval(ifCheck, 1000);
}

function clickFunc18()
{
    myVar;
    currentOz = 0.0;
    elem = document.getElementById('bar');
    dispenseAmount = 0.0;
    cost = 0.0;
    pricePerOunce = 0.0;
    currCost = 0.0;
    abort = false;
    document.getElementById("button16").style.display = "none";
    document.getElementById("button18").style.display = "none";
    document.getElementById("button24").style.display = "none";
    document.getElementById("stop").style.display = "inline";
    dispenseAmount = 18.0;
    cost = 9.99;
    pricePerOunce = cost/dispenseAmount;

    document.getElementById("select").innerHTML = "To stop dispensing, click the stop button";
    document.getElementById("dispensing").innerHTML = "Dispensing...";
    var percent = 0.0
    myVar = setInterval(ifCheck, 1000);
}

function clickFunc24()
{
    myVar;
    currentOz = 0.0;
    elem = document.getElementById('bar');
    dispenseAmount = 0.0;
    cost = 0.0;
    pricePerOunce = 0.0;
    currCost = 0.0;
    abort = false;
    document.getElementById("button16").style.display = "none";
    document.getElementById("button18").style.display = "none";
    document.getElementById("button24").style.display = "none";
    document.getElementById("stop").style.display = "inline";
    dispenseAmount = 24.0;
    cost = 13.99;
    pricePerOunce = cost/dispenseAmount;

    document.getElementById("select").innerHTML = "To stop dispensing, click the stop button";
    document.getElementById("dispensing").innerHTML = "Dispensing...";
    var percent = 0.0
    myVar = setInterval(ifCheck, 1000);
}

function ifCheck()
{
    if(abort)
    {
        document.getElementById("button16").style.display = "inline";
        document.getElementById("button18").style.display = "inline";
        document.getElementById("button24").style.display = "inline";
        document.getElementById("stop").style.display = "none";
        document.getElementById("select").innerHTML = "Please select the amount you'd like to dispense.";
        document.getElementById("dispensing").innerHTML = "Stopped!";
        clearInterval(myVar);
    }

    else
    {
        if(currentOz + 0.28178333 > dispenseAmount) // using 500 mL per minute
        {
            var leftOver = dispenseAmount - currentOz;
            currentOz = currentOz + leftOver;
            currCost = currCost + (leftOver * pricePerOunce);
            var div = currentOz/dispenseAmount;
            percent = (div)*100;
            var roundedP = percent.toFixed(2);
            var roundedO = currentOz.toFixed(2);
            var roundedCost = currCost.toFixed(2);
            document.getElementById("num").innerHTML = roundedP + "%";
            document.getElementById("ounces").innerHTML = roundedO + "oz";
            document.getElementById("price").innerHTML = "$" + roundedCost;
            elem.style.width = percent + "%";
            document.getElementById("dispensing").innerHTML = "Complete!";
            alert('Thank you! Have a Wonderfil day!');
            clearInterval(myVar);
        }
    
        else
        {
            currentOz = currentOz + 0.28178333;
            currCost = currCost + (0.28178333 * pricePerOunce);
            var div = currentOz/dispenseAmount;
            percent = (div)*100;
            var roundedP = percent.toFixed(2);
            var roundedO = currentOz.toFixed(2);
            var roundedCost = currCost.toFixed(2);
            document.getElementById("num").innerHTML = roundedP + "%";
            document.getElementById("ounces").innerHTML = roundedO + "oz";
            document.getElementById("price").innerHTML = "$" + roundedCost;
            elem.style.width = percent + "%";
        }
    }
}