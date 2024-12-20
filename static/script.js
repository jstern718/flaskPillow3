function clickFunctionOpen() {

    console.log("open script running");
    const openAccordion = document.getElementsByClassName("openLi");
    for (let i = 0; i < openAccordion.length; i++) {
        openAccordion[i].classList.toggle("closed");
    }

}
