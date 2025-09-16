const prompt = require("prompt-sync")({ sigint: true });

const number = Math.floor(Math.random()*100)
const checkNumber = () => {
    const getNumber = prompt("Podaj liczbe: ")
    if (getNumber != number) {
        if (getNumber > number) {
            console.log("Za duża liczba!\n")
            checkNumber()
        }
        else {
            console.log("Za mała liczba!\n")
            checkNumber()
        }
    }
    else {
        console.log("Liczba odgadnięta")
    }
}

const game = () => {
    console.log("Zgadnij liczbe 1-100");
    checkNumber()
}

game()