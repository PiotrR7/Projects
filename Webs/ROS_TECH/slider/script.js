const CreateElementWithClass = (element_name, class_name) => {
  const element = document.createElement(element_name);
  element.classList.add(class_name);
  return element;
}

const ChangeSliderContent = (id) => {
  const logo = document.querySelector(".slider-logo");
  const title_box = document.querySelector(".title-box");
  const text_box = document.querySelector(".text-box");

  const btn1 = document.querySelector("#menu-button1");
  const btn2 = document.querySelector("#menu-button2");
  const btn3 = document.querySelector("#menu-button3");

  if (id == 1) {
    title_box.innerText = "Lorem ipsum 1";
    text_box.innerText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin elementum iaculis viverra. In hendrerit cursus enim, eget scelerisque quam scelerisque.";
    logo.style.cssText = `background-image: url("./images/slider-1.jpg");`;
    btn1.disabled = true;
    btn2.disabled = false;
    btn3.disabled = false;
  }
  if (id == 2) {
    title_box.innerText = "Lorem ipsum 2";
    text_box.innerText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin elementum iaculis viverra. In hendrerit cursus enim, eget scelerisque quam scelerisque.";
    logo.style.cssText = `background-image: url("./images/slider-2.jpg");`;
    btn1.disabled = false;
    btn2.disabled = true;
    btn3.disabled = false;
  }
  if (id == 3) {
    title_box.innerText = "Lorem ipsum 3";
    text_box.innerText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin elementum iaculis viverra. In hendrerit cursus enim, eget scelerisque quam scelerisque.";
    logo.style.cssText = `background-image: url("./images/slider-3.jpg");`;
    btn1.disabled = false;
    btn2.disabled = false;
    btn3.disabled = true;
  }
}

const CreateSlider = (title, text, image_path) => {
  // create html elements
  const logo = CreateElementWithClass("div", "slider-logo")
  const content = CreateElementWithClass("div", "slider-content")
  const text_content = CreateElementWithClass("div", "text-content")
  const buttons_menu = CreateElementWithClass("div", "buttons-menu")
  const title_box = CreateElementWithClass("div", "title-box");
  const text_box = CreateElementWithClass("div", "text-box");

  const menu_button1 = CreateElementWithClass("button", "menu-button");
    menu_button1.setAttribute("id", "menu-button1");
    menu_button1.onclick = function() {ChangeSliderContent(1)};
  const menu_button2 = CreateElementWithClass("button", "menu-button");
    menu_button2.setAttribute("id", "menu-button2");
    menu_button2.onclick = function() {ChangeSliderContent(2)};
  const menu_button3 = CreateElementWithClass("button", "menu-button");
    menu_button3.setAttribute("id", "menu-button3");
    menu_button3.onclick = function() {ChangeSliderContent(3)};

  // builid html child system
  content.appendChild(text_content);
  content.appendChild(buttons_menu);
  text_content.appendChild(title_box);
  text_content.appendChild(text_box);
  buttons_menu.appendChild(menu_button1);
  buttons_menu.appendChild(menu_button2);
  buttons_menu.appendChild(menu_button3);

  // add text into divs
  title_box.innerText = title || "";
  text_box.innerText = text || "";

  // css styles
  logo.style.cssText = `
    background-image: url(` + image_path + `);
  `;

  // put elements into html
  const HTMLcontent = document.querySelector(".slider-main");
  HTMLcontent.appendChild(logo);
  HTMLcontent.appendChild(content);

  ChangeSliderContent(1);
}