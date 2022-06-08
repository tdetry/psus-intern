//TypeScript crash course

let isDone: boolean = false;
let lines: number = 42;
let pname: string = "Anders";

//if variables drawn from explicit literals we can ommit type annotation
let flag = false;

//not sure?
let notSure: any = 4;
notSure = "maybe str"
notSure = false;

const numberOfMonths = 12;
//numberOfMonths = 10 -> error

//typed arrays vs generic arrays (theyre completely equiv)
let list: number[] = [1,2,3,4];
let list2: Array<number> = [1,2,3,4];


//enumerations
enum Color {Red, Green, Blue};
let c: Color = Color.Green;
//c is now 1
//... cross reference to the Color enum
console.log(Color[c]);

// Lastly, "void" is used in the special case of a function returning nothing
function bigHorribleAlert(): void {
  alert("I'm a little annoying box!");
}

//some equiv function syntax
let f1 = function(i: number):number {
  return i*i;
}

// here the return type is inferred
let f2 = function(i:number) {
  return i*i;
}

//fat arrow syntax supported
let f3 = (i:number): number => {
  return i*i;
}
//... with return type inferred
let f4 = (i:number) => {
  return i*i;
}

//no return type needed
let f5 = (i: number) => i*i;

//interfaces!
interface Person {
  name: string;
  //optional attributes
  age?: number;
  move(): void;
}

//without specifying age attribute
let p: Person = {
  name: "Yann", move: () => {}
}

//all of the attr specified
let vPerson: Person = {name: "Yorch", age: 30, move: () => { } };

// they can also describe a function type
interface SearchFunc {(source:string, subString: string): boolean;}

let mySearch: SearchFunc;
mySearch = function(src: string, sub:string) {
  return src.search(sub) != -1;
}

//call it with mySearch("<src>", "<sub>");

let named = "damian";
//use backticks for template strings
let greet = `Hello ${named}, how are you?`;


//readonly in interfaces
//interface Person{
//  readonly age: string;
//  readonly name: string;
//} 
//
//let p1: Person = { name: "Damian", age = 40 };
//p1.age = 30; -> throws an error


/// arrays and redonly arrays
let numberArray: Array<number> = [0, 1, 2, 3, 4];
let readOnlyNumbers: ReadonlyArray<number> = numberArray;

// readOnlyNumbers.push(3); -> throws error, elements read only
