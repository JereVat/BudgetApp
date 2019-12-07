function configureVars() {
    var result = document.getElementById("result-h4").textContent;
    var netIncome = document.getElementById("netIncome").value;
    var savingTime = document.getElementById("savingTime").value;
    var targetWealth = document.getElementById("targetWealth").value;
    var beginningWealth = document.getElementById("beginningWealth").value;
    var targetInterest = document.getElementById("targetInterest").value;

    var overUnder = netIncome - result;
    if (overUnder == 0) {
        overUnder = 0
    } else {
        overUnder = overUnder.toFixed(2);
    }

    document.getElementById("totalOverUnder").value = overUnder;
}

function reCalculate() {
    var result = document.getElementById("result-h4").textContent;
    var netIncome = document.getElementById("netIncome").value;
    var savingTime = document.getElementById("savingTime").value;
    var targetWealth = document.getElementById("targetWealth").value;
    var beginningWealth = document.getElementById("beginningWealth").value;
    var targetInterest = document.getElementById("targetInterest").value;
    var living = document.getElementById("living").value;
    var food = document.getElementById("food").value;
    var car = document.getElementById("car").value;
    var insurances = document.getElementById("insurances").value;
    var mobileSubscription = document.getElementById("mobileSubscription").value;
    var electricity = document.getElementById("electricity").value;
    var internet = document.getElementById("internet").value;
    var hobbies = document.getElementById("hobbies").value;
    var other = document.getElementById("other").value;

    var expenses = Number(living) + Number(food) + Number(car) + Number(insurances) + Number(mobileSubscription)
    + Number(electricity) + Number(internet) + Number(hobbies) + Number(other);

    var overUnder = netIncome - result - expenses;

    document.getElementById("totalOverUnder").value = overUnder.toFixed(2);
}

