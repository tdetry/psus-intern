function clearScreen(): void {
    let result: HTMLInputElement = document.querySelector(
        '#result'
    ) as HTMLInputElement;
    result.value = '';
}

function display(value: 'string'): void {
    let result: HTMLInputElement = document.querySelector(
        '#result'
    ) as HTMLInputElement;
    result.value += value;
}

function calculate(): void {
    let result: HTMLInputElement = document.querySelector(
        '#result'
    ) as HTMLInputElement;
    result.value = eval(result.value);
}
