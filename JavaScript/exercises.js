console.log("JavaScript")
var global_variable = "var => Global Variable"
let local_variable = "let => Local Variable"
const constant_variable = "const => Constant Variable"
console.log(global_variable, local_variable, constant_variable)
console.log("concatinating two stirngs: " + "this si the second string!")
console.log('Using the "double quotes" inside of the console.log statement')
console.log("Printing this on the \nNew line")
console.log("Printing the first character of the string 'Hello': ", "Hello"[0])
console.log("Printing the last character of the string 'Hello': ", "Hello"["Hello".length-1])

const arrayOperating = (array) => {
    console.log("Printing the first element of the below array using a function in JavaScript:")
    console.log(array)
    array.map((ele) => {console.log(ele[0])})
}
let array = [["A", 1], ["B", 2], ["C", 3], ["D", 4]]
arrayOperating(array)
array[0][0] = "Z"
console.log("Modifying the first element of the first element of the given array to Z: ", array)
array.push(["M", 13])
console.log("Pushing a value to the end of the array: ", array)
array.pop()
console.log("Removing the last entry from the array: ", array)
array.shift()
console.log("Removing the first entry from the array: ", array)
array.unshift(["N", 14])
console.log("Adding an element at the start of the array: ", array)

const adder = (a, b) => {
    return a+b;
}

console.log("Created a function to add 2 numbers, Let's add 3 and 5: ", adder(3, 5))

const scopeChecker = () => {
    let newOne = "This is a let variable"
    var newTwo = "This is a var variable"
    console.log("Trying to understand the scope of variables, local variable: ", newOne, ", global variable: ", newTwo)
}
scopeChecker()

console.log("For array operations, important functions are: shift(), unshift(), pop(), push()")
let checker1 = 3 === '3'
let checker2 = 3 == '3'
console.log("Difference between == and ===: 3 === '3': ", checker1, " and 3 == '3': ", checker2)

function switchCaseChecker(val) {
    let answer = "";
    switch(val) {
        case 1:
            answer = "yolo"
            break;
        case 2:
            answer = "polo";
            break;
    }
    return answer;
}
console.log("Switch statement: ", switchCaseChecker(2))
var myObject = {
    "name": "Odoo",
    "city": "Buffalo"
}
console.log("The name of the object is: ", myObject.name)
myObject.name = "New Name Now"
console.log("Changed name of the object is: ", myObject.name)
myObject.newVar = "New Var"
console.log("Adding a property of myObject: ", myObject)
var checker3 = myObject.hasOwnProperty('city')
var checker4 = myObject.hasOwnProperty('state')
console.log("Checking if the object has a city property: ", checker3)
console.log("Checking if the object has a state property: ", checker4)
console.log("Generating a random number: ", Math.random())
console.log("Generating a random integer: ", Math.floor(Math.random()*10))
var checker5 = parseInt("50")
console.log("Converting a string number ('50') into integer type: ", checker5)
var checker6 = parseInt("1010010", 2)
console.log("Converting a binary number into integer type: ", checker6)
console.log(true ? "print this when true" : "Else print this using the ternary operator")
const arr = [0, 1, 2]
console.log("The array: ", arr)
console.log("Updating a const array using indexes and not by directly redefining the array: ")
arr[0] = 100
console.log("The new array is: ", arr)
console.log(`Using the template literals by 
printing ${checker5} and ${checker6}, and guess what, this works so much like python!!`)
const obj = {
    id: 1,
    idGenerator() {
        return Math.floor(Math.random()*5)
    }
}
console.log("Printing form a function defined in an object: ", obj.idGenerator())
console.log("Concatinating strings with numbers: 1, 2, 3, " + 4)
checker7 = "String"
console.log("Printing the first letter of the String: ", checker7.charAt(0))
console.log("Array: ", arr)
console.log("Removing 2 elements from the array and adding 5 more elements, removed this: ", arr.splice(0, 2, 9, 8, 7, 6, 5))
console.log("The new array is: ", arr)