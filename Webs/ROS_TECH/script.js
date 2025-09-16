function AddTextContainer(text) {

    var newDiv = document.createElement("div");
    newDiv.classList.add("textContainer");
    newDiv.innerHTML = text;
    
    var mainDiv = document.querySelector(".content");
    mainDiv.appendChild(newDiv);

}

function ScrollToView(target) {
    var targetSection = document.getElementById(target);

    targetSection.scrollIntoView({ behavior: 'smooth' });
}