if(localStorage.getItem("thema") == "light" || localStorage.getItem("thema") == null){
    applyLightMode();
    localStorage.setItem("isLightMode", "true");
}
else{
    applyDarkMode();
    localStorage.setItem("isLightMode", "false");
}

document.querySelector("#icon-button").addEventListener("click", toggleMode);

function toggleMode(){
    if(localStorage.getItem("isLightMode")=="true")
    {
        applyDarkMode();
        localStorage.setItem("isLightMode", "false");
    }
    else
    {
        applyLightMode();
        localStorage.setItem("isLightMode", "true");
    
    }
   
}

function applyDarkMode() {
    localStorage.setItem("thema", "dark");

    document.querySelector("#navbar").setAttribute("class","navbar  navbar-expand-lg navbar-dark")
   
    document.querySelector("#navbar").setAttribute("style","transition: 2s ease");

    document.querySelector("#thema-link").setAttribute("href","/static/css/darkMode.css%20");

    document.querySelector("#themaicon").setAttribute("class","fa-solid fa-sun");

}

function applyLightMode() {
    localStorage.setItem("thema","light");
    
    document.querySelector("#navbar").setAttribute("class","navbar navbar-expand-lg navbar-light");
    document.querySelector("#navbar").setAttribute("style","background-color: #e3f2fd");

    document.querySelector("#thema-link").setAttribute("href","/static/css/lightMode.css%20");

    document.querySelector("#themaicon").setAttribute("class","fa-solid fa-moon");


}
