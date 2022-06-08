interface ArrayConstructor {
    from(arrayLike: any, mapFn?: undefined, thisArg?: undefined): Array<any>;
}   

let display: HTMLDivElement = document.getElementById('display');

let buttons: Array<HTMLDivElement> = Array.from(document.getElementsByClassName('button'));


buttons.map( (button) => {
    button.addEventListener('click', (e: { target: { innerText: string; }; }) => {
        switch(e.target.innerText){
            case 'C':
                display.innerText = '';
                break;
            case '=':   
                try{
                    display.innerText = eval(display.innerText);
                } catch {
                    display.innerText = "Error"
                }
                break;
            case '←':
                if (display.innerText){
                   display.innerText = display.innerText.slice(0, -1);
                }
                break;
            default:
                display.innerText += e.target.innerText;
        }
    });
});