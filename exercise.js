console.log("hi")
// is for comment 
var num = 5;
/*
Multi line comment 
multi line comment 
*/
//Data types and variables 
var num = null
var flag = false
var s = 'strung'
// var is used for variable declaration 
// let is another variable declaration 
// let has a scope limitation and var is for global 
// const declaration cann't be changes
let x =5 
const y = 5
 // y = 6 // will throw an error 
 // variable assignment 
 var a ;
var b =5
a = b;
console.log(a)
// declaration and initialization can be done at the same time.
// variable names are case sensitive 
var a  = 5 
var A = 6 
console.log(a)
console.log(A)
// use camel casing in JS 
// Arithmetic operators 
var s = 4+5;
console.log(s)
var b = 42-12
var prod = 4*5 
var div = 54/23;
//increment by 1 
a++;
a--;
var dec = 5.564
var mod = 5%2;
// escaping literals in a string
var s = "I am  \"Kusal\" "
//  use single quotes to escape all characters by default
var s = 'sadasd "asda" '
// string concatination 
var str = "I am "+"kusal"
console.log(str)
str+= ",Hi!"
console.log(str)
// length of the length 
console.log(str.length)
console.log(str[str.length-1])
var arr = ["example",2]
var arr1 = [[1,2],[35,654]]
console.log(arr[1])
console.log(arr1[0][1])
//Arrays are immutable and can hold non homogenous data 
arr[1]=5
arr.push(arr1)
console.log(arr)
// Can remove an element using pop      
var removed = arr.pop()
console.log(arr)
//  shift is used to remove the first element instead of the last element 
var first_elem = arr.shift()
console.log(arr)
arr.unshift(first_elem)
console.log(arr)
// Function declarations in javascript 
function demoFunction(a ,b){
    console.log("demo function")
    console.log(a*b)
}
demoFunction(3,5);
//Scope of a variable 
var global_var = 10
function func(){
    console.log(global_var)
    ex1 = 5;
}
// local and global variables can have the same name. 

function func1(){
    var global_var = 6
    console.log(global_var)
}
func1()
// if a function doesnot have a return value it reurns undefined 
console.log(func1())

//Queue sumulation 
function nextInLine(arr,item){
    arr.push(item)
    var first = arr.shift()
    return first
}
var q = [1,2,3,4,5,6];
console.log(JSON.stringify(q))
console.log(nextInLine(q,7))
console.log(JSON.stringify(q))
// control flow using conditional stations 
var flag = false
if ( flag){
    console.log("It is True")
}else{
    console.log("It is false")
}

// switch case 
function switch_case(key){
    switch(key){
        case 1 : 
        console.log("value is 1"); break;
        case 2 : 
        console.log("value is 2"); break;
        case 3 : 
        console.log("value is 3"); break;
        default:
            console.log("Reached default block")

    }
}
switch_case(4)
function objectManipulations(){
    var exObj = {
        "name": "example",
        "hat": "red"
    }
    exObj.hat = "blue"
    exObj.shirt = "red"
    delete exObj.hat
    console.log(exObj)
    console.log(exObj["name"])
    if (exObj.hasOwnProperty('name')){
        console.log("has name")
    }
    
    // Objects are similar to dict in python
    // we can store multiple objects in an array, this is similar to JSON notation


}
function iterators(){
    var i = 0
    while(i <5){
        console.log(i++)
    }
    for(var i =0;i<5;i++){
        console.log(i)
    }
    var arr = [1,2,3,4,5,6]
    for(var i = 0 ;i<arr.length;i++){
        console.log(arr[i])
    }
    // Inbuilt lambda foreach function to iterate over every element in the array
    arr.forEach(element => {
        console.log(element)
    });
    var flag = false;
    do{
        console.log("does this once even though flag is false")
    }while(flag)

}
objectManipulations()
iterators()

function math_lib(){
    console.log(Math.random())// will return a decimal b/w 0,1
    console.log(Math.floor(Math.random()*10))     
    var max = 5
    var min =0
    // Get random number in a range
    console.log(Math.floor(Math.random()*(max - min+1)))+min
}
math_lib()

console.log(parseInt("3.2")) // Will typecast to int even if we give float
function ternary_operator(a,b){
    return a >b ? "a is greater than b":a>0? "a is positive":"a is  not  positive"
}
console.log(ternary_operator(0,2))

function var_vs_let(){

    let a = 5;
    // var a = 6;
    let b = 3;
    //let b = 4; // This will throw an error
    // the scope of let will be at the block scpoe
    if(true){
        let a = 9;
        console.log(a)

    }
    console.log(a)
    // const cannot be reassigned
    const x = 6;
    //x = 9;
    //always try to use let in the code to maintain proper scoping
    const y = [1,2,3]
    y[0]=1 /// this works as we are not changing the instance of the variable to avoid this use Object.freeze 
    Object.freeze(y)
}
var_vs_let();
function anonymous_function(){
    let dt = ()=> new Date();
    return dt;

}

anonymous_function()
/// variable arguments 
function rest_operator(...arr){
    console.log(arr)
}
rest_operator(1,2,4)
