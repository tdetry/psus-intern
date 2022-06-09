

function fact(n){
    if (n == 1 || n == 0){
        return 1;
    }
    return n * fact(n - 1);
}

function main(outputNum){
    for(let i =0 ;i < outputNum; i++){
        console.log(i,'factorial =',fact(i));
    }
}

main(10);

console.log('5' == 5, '5' === 5);
console.log('this is a string'.charAt(10));
console.log('this is a string'.substring(0,9));
console.log('this is a string'.length);

null;      // used to indicate a deliberate non-value
undefined; // used to indicate a value is not currently present (although 'undefined' is actually a value itself)

// Variables are declared with the `var` keyword. JavaScript is dynamically
// typed, so you don't need to specify type. Assignment uses a single `=`
// character.
var someVar = 5;

// If you leave the var keyword off, you won't get an error...
someOtherVar = 10;

// ...but your variable will be created in the global scope, not in the scope
// you defined it in.

var arr = [32,false,"js",12,56,90];
console.log(arr);

arr = arr.join(";"); 
console.log(arr);

arr = arr.slice(0,5);
console.log(arr);

var dict = {k1: "Hello", k2: "World"};

console.log(dict.k1, dict["k2"]);

