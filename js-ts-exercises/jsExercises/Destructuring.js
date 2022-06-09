var voxel ={x:3.6,y:7.4,z: 6.54};

var AVG_TEMP ={
    today:77,
    tomorrow:70

}

function getTempOfTmrw(avgTemp){
    const {tomorrow:tempOfTomorrow} =avgTemp;
    return tempOfTomorrow;
   

}
console.log(getTempOfTmrw(AVG_TEMP));


//Destructuring with nested objects
const LOCAL_FORECAST ={
    today: {min:72,max:83},
    tomorrow:{min:73.3,max:84.6}
};

function getMaxOfTmrw(forecast){
    "use strict";
    const {tomorrow : {max: maxOfTomorrow}} =forecast;
    return maxOfTomorrow;
}

console.log(getMaxOfTmrw(LOCAL_FORECAST));

//To asign variables from array
const [z,x,,y] =[1,2,3,4,5,6];
let a =8,b=6;
(()=>{
    [a,b] =[b,a];
})();

//Use destructuring assignment with the rest operator
const source = [1,2,3,4,5,6,7,8,9]
function removeFirstTwo(list){
    const [, ,...arr ]=list;
    return arr;

}

const arr =removeFirstTwo(source);

//Use destructuring assignment to pass an object as a functions parameters
const stats ={
    max:56.78,
    starndard_deviation: 4.34,
    median:23.87,
    min:-0.56
}

const half =(function(){
    return function half({max,min}){
        return (max+min)/2.0;
    }
})