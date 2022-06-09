const person ={
    name:"Zodiac Hasbro",
    age:56
}

const greeting =`Hello, my name is ${person.name}`;

//Write concise object literal declarations using simple fields
const createPerson =(name2,age,gender) =>({name2,age,gender});
console.log(createPerson("david",22,"H"));

//Write concise declarative functions
const bike ={
    gear:2,
    setGear(newGear){
        this.gear =newGear;
    }
};

bike.setGear(3);
console.log(bike.gear);