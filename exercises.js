function myFunction(){
    var x = 1
    return x;
}
console.log(x) //Error

{
    y=5
}
console.log(y)

//anonymous function
(function(){
    var temporary = 20;
    console.log(temporary)
    window.permanent = temporary; // any variable or object from the global scope has to be updated to be able to access anonyous functions
})();

console.log(temporary)
console.log(permanent)

// closure
function closure() {
    let x = 'Hi';
    function innerFunciton() {
        console.log(x);
    }
    return innerFunciton;
}
let hi = closure();
hi();

// Objects and scopes
myObj = {
    myString: "Hello world!",
    myFunc: function(){
        return this.myString; // if this keyword is not used, it will search global scope for mystring variable when the function is invoked
    }
};
myObj.myFunc()

// speicfying context using call and apply
var tempfunction = function(){
    return this.tempvar
}

tempObj = {tempvar: 'lol'}

tempfunction.call(tempObj) // just specify the context and it will return the tempvar variable in that scope of the context

// Prototype

protoObj = {testKey: 'testval'}
myObj.__proto__ = protoObj // its cascading to lower levels
console.log(myObj.testKey)

for (var x in myObj){ // searches all levels of prototypes until a null prototype is reached
    console.log(myObj[x]);
}