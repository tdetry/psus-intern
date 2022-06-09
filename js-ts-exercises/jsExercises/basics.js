//Comments

var number =5; //in line comment
/*
    multi
    line
    comment
*/

//Initialized variables
var a=2;
var b="b";
var c=true;
var d=[1,2,3];

//Uninitialized variables
var e;
var f;

//Basic Math
var sum =10+10;
var sub= 45-2;
var mult= 5*8;
var quotient = 66/33;

//Increment numbres
var myVar= 87;
myVar++;

//Decrement
myVar--;

//Decimals
var ourDecimal = 5.7;

var product= 2.0 *5.0;

//Remainder
var remainder;
remainder =11 % 3;

//Escaping literals quotes in strings
var myStr= "I am a\"double quoted\" string inside";

//Quoting strings with single quotes
var myStr2= '<a href="https:sdfasdf" target="asdfasdf">';
var myStr3 =``

//Concatenate strings
var ourStr = "1"+"2";

//Constructing strings with variables
var ourName ="David"
var test="my name is" +ourName;

//Appending variables to strings
var adjetivo="rojo"
var ourStr2= "el carro es";

ourStr2+=adjetivo;

//String length
console.log(ourStr2.length);

//Get character from index strings
console.log(ourStr2[0]);

//Arrays
var ourArray = ["David",23];
var myArray = ["Davidd",233,[2,4,6]];

//push
ourArray.push(["hola","si"]);

//pop
var removed =ourArray.pop();

//Shift removes first element and returns it
var removeWithSifth =ourArray.shift();

//unshift adds value to the beggining of the array
var unshifted =ourArray.unshift("platanos");

//Conditionals

if(1 == 1){
    console.log("si");
}else{
    console.log("no");
}

if(1 <= 1){
    console.log("si");
}else{
    console.log("no");
}
if(1 >= 1){
    console.log("si");
}else{
    console.log("no");
}
if(1 != 1){
    console.log("si");
}else{
    console.log("no");
}

if(1 === 1){
    console.log("si");
}else{
    console.log("no");
}
if(1 !== 1){
    console.log("si");
}else{
    console.log("no");
}
if(1 >1){
    console.log("si");
}else{
    console.log("no");
}

if(1 < 1){
    console.log("si");
}else{
    console.log("no");
}
if(1 == 1 && 1==2){
    console.log("si");
}else{
    console.log("no");
}

//Switch

function caseInSwitch(val){
    var answer ="";
    switch(val){
        case 1:
            answer="alpha";
            break;
        case 2:
            answer="beta";
            break;
        default:
            answer="no";

    }
    return answer;
}

//Siwtch with identical cases
function caseInSwitch(val){
    var answer ="";
    switch(val){
        case 1:
        case 2:
        case 3:
            answer="no";
        break;
    }
    return answer;
}

//Objects 
var ourDog ={
    "name": "Camper",
    "legs":4,
    "tails":1,
    "friends":["everything"]
};

//Acces object property dot notation
var nameVal =ourDog.name;

//Bracket notation
var legVal = ourDog["legs"];

//Adding new properties
ourDog.bark ="bow-wow";

//Delete properties from object
delete ourDog.friends;

//Check if an object has an specific property

if(ourDog.hasOwnProperty("name")){
    console.log("yes");
}

//Loops
while(i <10){
    console.log(i);
    i++;

}

for (let j = 0; j < 20; j++) {
    console.log(j);
}

//Iterate odd numbers
var ourArray =[]
for (let i = 0; i < 10; i+=2) {
    ourArray.push(i);
    
}
console.log(ourArray);


//Count backwards
for (let j = 10; j >0; j--) {
    ourArray.push(j);
}

console.log(ourArray);

//Nested for loop

for (let a = 0; a < 10; a++) {
    for (let b = 0; b < 20; b++) {
        console.log(a + b);
    }
}

//Do while loops

var num =10
do{
    console.log(num);
    num--;
}while(10>0);

//Ternary ops

function checkEquals(a,b){
    return a===b? true:false;
}

function checkSign(num){
    return num >0 ? "positive": num<0 ?"negative":"zero";
}
console.log(checkSign(10));

//let block scope
//var function scope
//const cant be reasigned

//Mutate an array declared as const

const s =[5,7,2];
function editInPlace(){
    "use strict";
    s[0]=2;

}
editInPlace();
console.log(s);

//Prevent mutating objects

function freezeObj(){
    const MATH_CONSTANTS ={
        PI:3.14
    }
    Object.freeze(MATH_CONSTANTS);
}