function clickFunctionOpen() {

    console.log("open script running");
    const openAccordion = document.getElementsByClassName("openLi");
    for (let i = 0; i < openAccordion.length; i++) {
        openAccordion[i].classList.toggle("closed");
    }

    const openClass = document.getElementsByClassName("open-class")[0];
    openClass.classList.toggle("closed");


    const closedClass = document.getElementsByClassName("closed-class")[0];
    closedClass.classList.toggle("closed");


}
