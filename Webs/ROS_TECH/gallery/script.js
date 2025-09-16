const img1 = "images/img-1.jpg";
const img2 = "images/img-2.jpg";
const img3 = "images/img-3.jpg";
const img4 = "images/img-4.jpg";

const images = [img1, img2, img3, img4];

let i = 0;
const ChangeImage = (value) => {
    const slider = document.querySelector(".gallery-container");
    
    i = i + value;
    if (i > images.length - 1) {
        i = 0;
    }
    if (i < 0) {
        i = images.length - 1;
    }

    if (slider.style.display == "flex") {
        slider.style.cssText = `
            display: flex;

            background-image: url(` + images[i] +`);
            background-size: cover;
            background-clip: border-box;
            background-repeat: no-repeat;
            background-position: center;
            
        `;
    } else {
        slider.style.cssText = `
            background-image: url(` + images[i] +`);          
        `;
    }

}
ChangeImage(0);