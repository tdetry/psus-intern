let test: any = 4
console.log(test, typeof(test))
test = 'Hi'
console.log(test, typeof(test))

const dummy:number = 5
console.log(dummy, typeof(dummy))

let list = [1,2,3,4,5]
console.log(list, typeof(list))

let list1:number[] = [1,2,3,4,5]
console.log(list1, typeof(list1))

let list2:Array<number> = [1,2,3,4,5]
console.log(list2, typeof(list2))

enum Color { Red, Green, Blue };
let c: Color = Color.Green;
console.log(c, typeof(c), Color[c], typeof(Color), typeof(Color[c]))

function bigHorribleAlert():void {
  alert("I'm a little annoying box!");
}
// bigHorribleAlert()

var x:void = null
console.log(x,typeof(x))

let squareFunc = (i) => { return i * i }
console.log(squareFunc(5))

interface Person {
  name: string;
  age: number;
}

var p:Person = {name: 'name', age:25}
console.log(p)

var p2:Person = {name:'name2'}
console.log(p2)

interface Person1 {
  readonly name: string;
  readonly age: number;
}

var p3: Person1 = { name: "myname"};
console.log(p3)
p3.age=25
console.log(p3)

p3.age=50
console.log(p3)

type burger = "black-bean" | "hash-brown";
type veggies = "lettuce" | "cucumber" | "tomato" | "onion" |" ";
type food = `A ${burger} ${veggies} burger`;

let food1:food = "A black-bean cucumber burger"
console.log(food1)

let food2:food = "A hash-brown   burger"
console.log(food2)

interface Cash {
  readonly val: "cash";
}

interface Card {
  readonly val: "card";
  ccno: string;
  cvvno: string;
}

type payment = Cash|Card

function paymentInfo(paymentType: payment){
  console.log(paymentType)
}

var pay1:payment = {val:"cash"}

paymentInfo(pay1)

var pay2:payment = {val:"card", ccno:"1234 5678 9000 1234", cvvno:"XYZ"}

paymentInfo(pay2)

