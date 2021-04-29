var myVar;
var currentOz = 0.0;
var elem = document.getElementById('bar');
var dispenseAmount = 0.0;
var cost = 0.0;
var pricePerOunce = 0.0;
var currCost = 0.0;
var abort = false;
var prodNum = 0;
var prodName = "";
var prodDesc = "";
var ingredDesc = "";

function selectSize()
{
    document.getElementById("vals").style.display = "none";
    document.getElementById("product1").style.display = "none";
    document.getElementById(prodName).style.display = "none";
    document.getElementById(prodDesc).style.display = "none";
    document.getElementById("dispenseProd").style.display = "none";
    document.getElementById("ingredientList").style.display = "none";
    document.getElementById("button16").style.display = "inline";
    document.getElementById("button18").style.display = "inline";
    document.getElementById("button24").style.display = "inline";
    document.getElementById("select1").style.display = "block";
    document.getElementById("yes").style.display = "none";
    document.getElementById("no").style.display = "none";
}

function ingredients()
{
    ingredDesc = "ingredientDesc" + prodNum;
    document.getElementById("product1").style.display = "none";
    document.getElementById(prodName).style.display = "none";
    document.getElementById(prodDesc).style.display = "none";
    document.getElementById("dispenseProd").style.display = "none";
    document.getElementById("ingredientList").style.display = "none";
    document.getElementById("ingred").style.display = "block";
    document.getElementById(ingredDesc).style.display = "block";
    document.getElementById("backButton").style.display = "inline";
}

function goBack()
{
    document.getElementById("product1").style.display = "block";
    document.getElementById(prodName).style.display = "block";
    document.getElementById(prodDesc).style.display = "block";
    document.getElementById("dispenseProd").style.display = "inline";
    document.getElementById("ingredientList").style.display = "inline";
    document.getElementById("ingred").style.display = "none";
    document.getElementById(ingredDesc).style.display = "none";
    document.getElementById("backButton").style.display = "none";
}

function screen1f()
{
    prodNum = 1;
    prodName = "productName" + prodNum;
    prodDesc = "productDesc" + prodNum;
    document.getElementById("screen1").style.display = "none";
    document.getElementById("screen2").style.display = "none";
    document.getElementById("screen3").style.display = "none";
    document.getElementById("screen4").style.display = "none";
    document.getElementById("welc1").style.display = "none";
    document.getElementById("product1").style.display = "block";
    document.getElementById(prodName).style.display = "block";
    document.getElementById(prodDesc).style.display = "block";
    document.getElementById("dispenseProd").style.display = "inline";
    document.getElementById("ingredientList").style.display = "inline";
}

function screen2f()
{
    prodNum = 2;
    prodName = "productName" + prodNum;
    prodDesc = "productDesc" + prodNum;
    document.getElementById("screen1").style.display = "none";
    document.getElementById("screen2").style.display = "none";
    document.getElementById("screen3").style.display = "none";
    document.getElementById("screen4").style.display = "none";
    document.getElementById("welc1").style.display = "none";
    document.getElementById("product1").style.display = "block";
    document.getElementById(prodName).style.display = "block";
    document.getElementById(prodDesc).style.display = "block";
    document.getElementById("dispenseProd").style.display = "inline";
    document.getElementById("ingredientList").style.display = "inline";
}

function screen3f()
{
    prodNum = 3;
    prodName = "productName" + prodNum;
    prodDesc = "productDesc" + prodNum;
    document.getElementById("screen1").style.display = "none";
    document.getElementById("screen2").style.display = "none";
    document.getElementById("screen3").style.display = "none";
    document.getElementById("screen4").style.display = "none";
    document.getElementById("welc1").style.display = "none";
    document.getElementById("product1").style.display = "block";
    document.getElementById(prodName).style.display = "block";
    document.getElementById(prodDesc).style.display = "block";
    document.getElementById("dispenseProd").style.display = "inline";
    document.getElementById("ingredientList").style.display = "inline";
}

function screen4f()
{
    prodNum = 4;
    prodName = "productName" + prodNum;
    prodDesc = "productDesc" + prodNum;
    document.getElementById("screen1").style.display = "none";
    document.getElementById("screen2").style.display = "none";
    document.getElementById("screen3").style.display = "none";
    document.getElementById("screen4").style.display = "none";
    document.getElementById("welc1").style.display = "none";
    document.getElementById("product1").style.display = "block";
    document.getElementById(prodName).style.display = "block";
    document.getElementById(prodDesc).style.display = "block";
    document.getElementById("dispenseProd").style.display = "inline";
    document.getElementById("ingredientList").style.display = "inline";
}

function clickFunc16()
{
    document.getElementById("resultOz").innerHTML = "Total ounces: ";
    document.getElementById("resultPrice").innerHTML = "Total cost: ";
    document.getElementById("num").innerHTML = 0 + "%";
    document.getElementById("price").innerHTML = "";
    document.getElementById("ounces").innerHTML = "";
    elem.style.width = 0 + "%";

    document.getElementById("vals").style.display = "block";
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
    document.getElementById("select1").style.display = "none";
    document.getElementById("start").style.display = "inline";
    dispenseAmount = 16.0;
    cost = 7.99;
    pricePerOunce = cost/dispenseAmount;

    document.getElementById("select2").style.display = "block";
    var percent = 0.0
}

function clickFunc18()
{
    document.getElementById("resultOz").innerHTML = "Total ounces: ";
    document.getElementById("resultPrice").innerHTML = "Total cost: ";
    document.getElementById("num").innerHTML = 0 + "%";
    document.getElementById("price").innerHTML = "";
    document.getElementById("ounces").innerHTML = "";
    elem.style.width = 0 + "%";

    document.getElementById("vals").style.display = "block";
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
    document.getElementById("select1").style.display = "none";
    document.getElementById("start").style.display = "inline";
    dispenseAmount = 18.0;
    cost = 9.99;
    pricePerOunce = cost/dispenseAmount;

    document.getElementById("select2").style.display = "block";
    var percent = 0.0
}

function clickFunc24()
{
    document.getElementById("resultOz").innerHTML = "Total ounces: ";
    document.getElementById("resultPrice").innerHTML = "Total cost: ";
    document.getElementById("num").innerHTML = 0 + "%";
    document.getElementById("price").innerHTML = "";
    document.getElementById("ounces").innerHTML = "";
    elem.style.width = 0 + "%";

    document.getElementById("vals").style.display = "block";
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
    document.getElementById("select1").style.display = "none";
    document.getElementById("start").style.display = "inline";
    dispenseAmount = 24.0;
    cost = 13.99;
    pricePerOunce = cost/dispenseAmount;

    document.getElementById("select2").style.display = "block";
    var percent = 0.0
}

function startFunc()
{
    abort = false;
    document.getElementById("select2").style.display = "none";
    document.getElementById("select3").style.display = "block";
    document.getElementById("select4").style.display = "none";
    document.getElementById("stop").style.display = "inline";
    document.getElementById("start").style.display = "none";
    document.getElementById("yes").style.display = "none";
    document.getElementById("no").style.display = "none";
    document.getElementById("dispensing").innerHTML = "Dispensing...";
    myVar = setInterval(ifCheck, 1000);
}

function results()
{
    document.getElementById("thanks").style.display = "block";
    document.getElementById("vals").style.display = "none";
    document.getElementById("home").style.display = "inline";
    document.getElementById("yes").style.display = "none";
    document.getElementById("select4").style.display = "none";
    document.getElementById("no").style.display = "none";
    document.getElementById("dispensing").style.display = "none";
    document.getElementById("resultOz").style.display = "block";
    document.getElementById("resultPrice").style.display = "block";
    document.getElementById("resultOz").innerHTML = "Total ounces: " + currentOz.toFixed(2) + " oz";
    document.getElementById("resultPrice").innerHTML = "Total cost: $" + currCost.toFixed(2);
}

function home()
{
    document.getElementById("thanks").style.display = "none";
    document.getElementById("home").style.display = "none";
    document.getElementById("resultOz").style.display = "none";
    document.getElementById("resultPrice").style.display = "none";
    document.getElementById("screen1").style.display = "inline";
    document.getElementById("screen2").style.display = "inline";
    document.getElementById("screen3").style.display = "inline";
    document.getElementById("screen4").style.display = "inline";
    document.getElementById("welc1").style.display = "block";
}

function ifCheck()
{
    if(abort)
    {
        document.getElementById("stop").style.display = "none";
        document.getElementById("select3").style.display = "none";
        document.getElementById("select4").style.display = "block";
        document.getElementById("yes").style.display = "inline";
        document.getElementById("no").style.display = "inline";
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
            //alert('Thank you! Have a Wonderfil day!');
            // document.getElementById("button16").style.display = "inline";
            // document.getElementById("button18").style.display = "inline";
            // document.getElementById("button24").style.display = "inline";
            document.getElementById("stop").style.display = "none";
            document.getElementById("select3").style.display = "none";
            //document.getElementById("select1").style.display = "block";
            clearInterval(myVar);
            results();
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
