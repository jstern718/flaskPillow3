function clickFunctionOpen() {
    console.log("open script running");
    const openAccordion = document.getElementById("open-accordion");
    const closedAccordion = document.getElementById("closed-accordion");
    closedAccordion.classList.remove("open");
    closedAccordion.classList.add("closed");
    openAccordion.classList.remove("closed");
    openAccordion.classList.add("open");
}

function clickFunctionClose() {
    console.log("close script running");
    const openAccordion = document.getElementById("open-accordion");
    const closedAccordion = document.getElementById("closed-accordion");
    openAccordion.classList.remove("open");
    openAccordion.classList.add("closed");
    closedAccordion.classList.remove("closed");
    closedAccordion.classList.add("open");
}

