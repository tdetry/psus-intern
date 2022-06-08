// strings

let greeting = "hello";
let person = "John";

console.log(greeting,person);
console.log(person.length);
console.log(person[0])
console.log(person[person.length - 1])

function wordBlanks(Noun, Adjective, Verb, Adverb) {
    let result = "The " + Adjective + " " + Noun + " " + Verb + " " + Adverb + ".";
    return result
}

console.log(wordBlanks("Dog", "fast", "ran", "quick"));

// arrays

let array = ["apple", "banana"];
let nestedArray = [["John", "Dog"],["Cat"]];

array[0] = "pineapple";

array.push("apple");
array.unshift("watermelon");

console.log(array.pop());
console.log(array.shift());

// functions

function addFive(num) {
    return num + 5;
}

console.log(addFive(3));

function isTrue(a) {
    if (a) {
        console.log("The expresstion was true.");
    } 
    else {
        console.log("The expression was false.");
    }
}

isTrue(true);

// equality

console.log(3=="3");
console.log(3==="3");

// switch

function switchFunction(a) {
    switch (a) {
        case 1:
            return "One";
        case 2:
            return "Two";
        case 3:
            return "Three";
        default:
            return "Unknown";
    }
}

console.log(switchFunction(1));

// objects

dog = {
    "name": "Remy",
    "sound": "bark",
    "age": 5
};

console.log(dog.sound);

dog.activity = "walks";

console.log(dog.activity);

delete(dog.activity);

let whileArray = [];

let i = 0;
while (i<4){
    whileArray.push(i);
    i++;
}

console.log(whileArray);

forArray = [];

for (let i = 0; i<4; i++){
    forArray.push(i);
}

console.log(forArray);

doWhileArray = [];

do {
    doWhileArray.push(i);
    i++;
} while (i < 6);

console.log(doWhileArray);

// ternary operator

console.log("a" == "a" ? "good" : "bad");

// arrow function

const addSeven = (num) => num + 7;

console.log(addSeven(5));

// default parameters

function increment(num, step = 1) {
    return num += step;
}

console.log(increment(5));
console.log(increment(7, 3));

// destructuring

let argsObj = {
    "max" : 10,
    "min" : 1
};

function getRange({max, min}){
    return max - min;
}

console.log(getRange(argsObj));

// template literal

let personName = "John";

console.log(`Hello, ${personName}`);

// simple fields

const createPerson = (name, age) => ({name, age});

console.log(createPerson("John", 3));

// classes

class Food {
    constructor(name){
        this.name = name;
        this._status = "uneaten";
    }
    get status() {
        return this._status;
    }
    set status(status){
        this._status = status;
    }


}

let pizza = new Food("pizza");

console.log(pizza.name);