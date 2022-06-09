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