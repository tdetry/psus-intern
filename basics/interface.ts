interface Person {
	name: string
	age?: number
	move(): void
}

// Object that implements the "Person" interface
// Can be treated as a Person since it has the name and move properties
let p: Person = { name: 'Bobby', move: () => {} }
// Objects that have the optional property:
let validPerson: Person = { name: 'Bobby', age: 42, move: () => {} }
// Is not a person because age is not a number
// let invalidPerson: Person = { name: 'Bobby', age: true }
