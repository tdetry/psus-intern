function push(array, ...items) {
	console.log(typeof array) // object, not array
	items.forEach(function (item) {
		array.push(item)
	})
}

//spread syntax & type annotation
function push2(array: Array<String>, ...items) {
	items.forEach(function (item) {
		array.push(item + 2)
	})
}

const a = [9, 10, 11]
push(a, 1, 2, 3, 4, 5, 6)
console.log(a)

const a2 = ['9', '10', '11']
push2(a2, 1, 2, 3, 4, 5, 6)
console.log(a2)

//function overloading
function reverse(x: number): number
function reverse(x: string): string
function reverse(x: number | string): number | string | void {
	if (typeof x === 'number') {
		return Number(x.toString().split('').reverse().join(''))
	} else if (typeof x === 'string') {
		return x.split('').reverse().join('')
	}
}
function sum() {
	let args: {
		[index: number]: number
		length: number
		callee: Function
	} = arguments
}

//Optional & default argument
function buildName(
	firstName: string,
	lastName?: string,
	midName: string = 'Default'
) {
	if (lastName) {
		return firstName + ' ' + lastName
	} else {
		return firstName
	}
}
let tomcat = buildName('Tom', 'Cat')
let tom = buildName('Tom')

export {}
