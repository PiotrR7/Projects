class MenuButton {
    constructor(btn_class, content_class, display_type) {
        this.button = document.querySelector(btn_class);
        this.content_class = document.querySelector(content_class);
        this.display_type = display_type;
    }
}

const mBtn1 = new MenuButton(".mbtn1", ".about-us-box", "flex");
const mBtn2 = new MenuButton(".mbtn2", ".services-container", "flex");
const mBtn3 = new MenuButton(".mbtn3", ".gallery-container", "flex");
const mBtn4 = new MenuButton(".mbtn4", ".contact-box", "flex");

const buttons = [mBtn1, mBtn2, mBtn3, mBtn4];


const ButtonON = (button) => {
    // change button css style
    button.button.style.cssText = `
        background-image: linear-gradient(126deg, rgba(27,174,112,1) 23%, rgba(60,60,60,1) 100%);
        color: white;
    `;

    // show button content
    button.content_class.style.display = button.display_type;
}

const ButtonOFF = (button) => {
    // change button css style
    button.button.style.cssText = `
            background-color: white;
            color: gray;
    `;

    // hide button content
    button.content_class.style.display = "none";
}

ButtonON(mBtn1);

const Main = (button) => {
    for (let i = 0; i < buttons.length; i++) {
        if (buttons[i] != button) {
            ButtonOFF(buttons[i]);
        }
    }

    ButtonON(button);
}