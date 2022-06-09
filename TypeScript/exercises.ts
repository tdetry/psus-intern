let notSure: any  = "Hey what's up";
console.log("Initializing a variable as a string: ", notSure)
notSure = false
console.log("Chnaging the value of the same variable to check if it works: ", notSure)
let tsAdder = (a: number, b: number) => a+b
console.log(tsAdder(10, 20))

type batsman = "left-handed" | "right-handed";
type bowler = "Spin" | "Fast";
type cricketer = `A ${batsman} ${bowler} bowler`;

let bowler1: cricketer = "A right-handed Fast bowler"
console.log(bowler1)