var dzialanie
const console = document.querySelector("#console")

const numer0 = () => {
    console.value += 0
}

const numer1 = () => {
    console.value += 1
}

const numer2 = () => {
    console.value += 2
}

const numer3 = () => {
    console.value += 3
}

const numer4 = () => {
    console.value += 4
}

const numer5 = () => {
    console.value += 5
}

const numer6 = () => {
    console.value += 6
}

const numer7 = () => {
    console.value += 7
}

const numer8 = () => {
    console.value += 8
}

const numer9 = () => {
    console.value += 9
}

const plus = () => {
    console.value += "+"
}

const minus = () => {
    console.value += "-"
}

const mnoz = () => {
    console.value += "×"
}

const dziel = () => {
    console.value += "÷"
}

const del = () => {
    dzialanie = document.getElementById("console").value
    if (dzialanie.length > 0) {
        var newValue = dzialanie.slice(0, -1);
        console.value = newValue 
    }
}

const cl = () => {
    console.value = ""
}

const kropka = () => {
    console.value += "."
}

const wynik = () => {
    dzialanie = document.getElementById("console").value
    if (dzialanie.includes(" ")) {
        dzialanie = dzialanie.replace(" ", "");
    }
    if (dzialanie.includes("×")) {
        dzialanie = dzialanie.replace("×", "*");
    }
    if (dzialanie.includes("÷")) {
        dzialanie = dzialanie.replace("÷", "/");
    }
    console.value = eval(dzialanie)
}