import { question } from "readline-sync";

type Operator = '*' | '+' | '-' | '/';

function main(): void {
    const firstString: string = question("Enter first number: ");
    const operator: string = question("operator: ");
    const secondString: string = question("Enter second number: ");

    const input: boolean = isNumber(firstString) && isNumber(secondString) && isOperator(operator)

    if (input) {
        const firstNum : number = parseInt(firstString);
        const secondNum: number = parseInt(secondString);
        const result = calc(firstNum, operator as Operator, secondNum);
        console.log(result);
    }else {
        console.log('invalid data');
        main();
    }


    
}

function calc(firstNum: number, operator: Operator, secondNum: number): number {
    switch(operator) {
        case '+':
            return firstNum + secondNum;
        case '-':
            return firstNum - secondNum;
        case '*':
            return firstNum * secondNum;
        case '/':
            return firstNum / secondNum;
    }
}

function isOperator(op: string): boolean {
    switch (op){
        case '+':
        case '-':
        case '*':
        case '/':
            return true;
        default:
            return false;
    }
}

function isNumber(str: string): boolean {
    const num = parseInt(str);
    const isNum = !isNaN(num);

    return isNum;
}

main();