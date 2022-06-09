const magic =()=> new Date();


//With parameters
const myConcat =(arr1,arr2)=> arr1.concat(arr2);

console.log(myConcat([1,2,3],[2,2]))

//Higher order functions
const realNumberArray =[4,5.6,-9,3.14]
const squareList =(arr)=>{
    const squaredIntegers = arr.filter(num => Number.isInteger(num) && num >0).map(x => x*x);
    return squaredIntegers;
}

const increment =(function(){
    return function increment(number,value){
        return number+value;

    }
})();

//Rest operator

const sum =(function(){
    return function sum(...args){
        return args.reduce((a,b)=> a+b,0);
    }
});

//Spread operator
const arr3= ['JAN','FEB','MAR']
let arr4;
(function(){
    arr4=[...arr3];
    arr3[0]='potato';
})();

