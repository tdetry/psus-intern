// ';' at end of line is good code style
var a; // declaration
var b = 4; // assignment

var c = 5;
c = "value" // value types can change for var

// variable keywords:
/* var   : mutable, can be re-declared
   let   : mutable, can't be re-declared
   const : immutable, can't be re-declared */

var camelCase = 1; // camel case convention
let camelCase2 = 2; // for mutable variables
const CAMEL_CASE_3 = 1; // all caps for immutable

b++; // equivalent to 'b = b + 1;' similarly 'b--;' for 'b = b - 1;'
b += 5; // equivalent to 'b = b + 5;'
/* can use with other operators, -, * and / */

c = "Use \\ as an escape char in strings for special chars \\n or \\'";
console.log(c); // prints passed in variable

var myStr = "test";
myStr += "ing"; // unlike python, '+' operator on strings don't add a space
var strLen = myStr.length; // string acts as 'list' of characters
myStr[0] // index starts at 0

const multiDim = [[1, 2], [3, 4]] // nested arrays are allowed
multiDim[0] = 1; // arrays are mutable even if var itself is const
multiDim[0] = [1, 2];
multiDim[0][1] = 3; // unpacking multidim array, var[row][col]

var exList = [1, 2, 3, 4, 5, 6, 7]
var lastVal = exList.pop() // pop() removes last element, shift() removes first
exList.push(7) // push() adds element at last index, unshift() at first index

function exFunc(num1, num2) {
   var num3 = num1 + num2; // local var, scope only to function
   num3 += b; // can access global vars in same file
   return num3;
}

a = exFunc(1, 3);
console.log(a);