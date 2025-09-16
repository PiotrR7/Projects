const CreateBlock = (image_path, description_text) => {
    const container = document.createElement("div");
    const image = document.createElement("div");
    const description = document.createElement("div");

    container.classList.add("container");
    image.classList.add("image");
    description.classList.add("description");

    container.appendChild(image);
    container.appendChild(description);

    description.innerHTML = description_text;
    image.style.cssText = `
        background: url(` + image_path + `);
    `;

    const content = document.querySelector(".content");
    content.appendChild(container);
}