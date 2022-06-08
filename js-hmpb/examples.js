// number examples
console.log(0.1 + 0.2);
var number = 10;
console.log(number);

number += 5;
console.log(number);

number -= 2;
console.log(number);

number *= 2;
console.log(number);

number /= 2;
console.log(number);

number %= 2; // remainder
console.log(number);


// string examples
var string = "hello";
console.log(string);

string += " world";
console.log(string);

console.log(string.length);
console.log(string.toUpperCase());
console.log(string.toLowerCase());
console.log(string[0]);

// boolean examples
var boolean = true;
console.log(boolean);

console.log(!boolean);

// array examples
var array = [1, 2, 3];
console.log(array);
console.log(array[0]);
console.log(array.length)
array.push(4);
console.log(array);
array.forEach(item => console.log(item)); // iterate over array(callback)
var poped = array.pop();
console.log(array);

var shifted = array.shift(); // removes first element
console.log(array);

array.unshift(10); // adds element to the beginning of the array
console.log(array);

