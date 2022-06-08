function clearScreen() {
    var result = document.querySelector('#result');
    result.value = '';
}
function display(value) {
    var result = document.querySelector('#result');
    result.value += value;
}
function calculate() {
    var result = document.querySelector('#result');
    result.value = eval(result.value);
}
