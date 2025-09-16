const days_in_month = new Array(31,28,31,30,31,30,31,31,30,31,30,31)
const date = new Date()

const dniDoKoncaRoku = () => {
    var iloscDni = date.getDate()
    var iloscDniWroku = 365

    for (var i = 0; i <= date.getMonth()-1; i++) {
        iloscDni += days_in_month[i]
    }

    if (date.getFullYear() % 4 == 0) {
        if (date.getFullYear() % 100 != 0) {
            iloscDni += 1
            iloscDniWroku += 1
        }
    } else if (date.getFullYear() % 400 == 0) {
        iloscDni += 1
        iloscDniWroku += 1
    }

    console.log("Do końca roku pozostało: ", iloscDniWroku - iloscDni, "dni")
}

dniDoKoncaRoku()