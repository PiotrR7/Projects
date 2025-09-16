let randomNumber = Math.floor(Math.random()*100+1)

function sprawdzLiczbe(){
    let pobranaLiczba = parseInt(document.getElementById('podajLiczbe').value)


    if (pobranaLiczba > randomNumber){
        let informacja = "Twoja liczba jest za duża"
        document.getElementById('tekstKonsola').innerHTML=(informacja)
    }
    if (pobranaLiczba < randomNumber){
        let informacja = "Twoja liczba jest za mała"
        document.getElementById('tekstKonsola').innerHTML=(informacja)
    }
    if (pobranaLiczba == randomNumber){
        let informacja = "Liczba została odkryta!"
        document.getElementById('tekstKonsola').innerHTML=(informacja)
    }
        


}