let binaryLiteral: number = 0b1010
let octalLiteral: number = 0o744
let decLiteral: number = 6
let hexLiteral: number = 0xf00d

enum Color {
	Red,
	Green,
	Blue,
}
let c: Color = Color.Blue

let name: string = 'Runoob'
let years: number = 5
let words: string = `name: ${name} years + 1 = : ${years + 1} `

console.log(words)

let x: [string, number]
x = ['Runoob', 1]
// x = [1, 'Runoob'];    // error
console.log(x[0]) // Runoob

// When it's impossible to know, there is the "Any" type
let notSure: any = 4
notSure = 'maybe a string instead'
notSure = false // okay, definitely a boolean
console.log(typeof notSure)
let anyObj: any
console.log('10 ' + typeof anyObj)

function hello(): void {
	alert('Hello')
}
function sayHello(person: string) {
	return 'Hello, ' + person
}

let arr: number[] = [1, 2]

function test(a: number, b: number, c: string) {
	console.log(typeof arguments)
}
test(1, 3, 'TESTING')
interface Animal {
	name: string
}
interface Cat {
	name: string
	run(): void
}

function testAnimal(animal: Animal): Cat {
	return animal as Cat
}
function testCat(cat: Cat) {
	return cat as Animal
}

export {}
