const numbers = document.querySelectorAll(".number")
const currentOperand = document.querySelector(".current-operand")
const previousOperand = document.querySelector(".previous-operand")
const spanTwo = document.querySelector(".equal")
const operators = document.querySelectorAll(".operator")
let result = null
let operation = ""
console.log(spanTwo);
for (const number of numbers) {
    number.addEventListener("click", e =>{
        e.preventDefault()
        currentOperand.innerText = currentOperand.innerText+number.innerText
        console.log(number.innerText);
    })
    
}
for (const operator of operators) {
    operator.addEventListener("click", e =>{
        previousOperand.innerText = currentOperand.innerText + operator.innerText
        result = parseFloat(currentOperand.innerText)
        currentOperand.innerText = ""
        operation = operator.innerText
        console.log(operation);   
    })
    
}
spanTwo.addEventListener("click", e =>{
    e.preventDefault()

    switch (operation) {
        case '+':
                previousOperand.innerText += currentOperand.innerText 
                result += parseInt(currentOperand.innerText)
                currentOperand.innerText = result
            break;
        case '-':
            previousOperand.innerText += currentOperand.innerText 
            result -= parseInt(currentOperand.innerText)
            currentOperand.innerText = result
            break
        case '/':
            previousOperand.innerText += currentOperand.innerText 
            result /= parseInt(currentOperand.innerText)
            currentOperand.innerText = result
            break
        case '*':
            previousOperand.innerText += currentOperand.innerText 
            result *= parseInt(currentOperand.innerText)
            currentOperand.innerText = result
            break
        
        
    
        default:
            break;
    }
})

