//Rest operator
const sum = (function()
{
 return function sum(...args) {
    //  const args = [x,y,z];
     return args.reduce((a,b)=> a+b,0);
 };
})();
console.log(sum(1,2,3,4)); 

// Spread operator 
const arr1 = ['Jan','Feb','Mar','Apr','May'];
let arr2;
(function(){
    // arr2 = arr1 does not work
    arr2 = [...arr1];
    arr1[0] = 'potato'

})();
console.log(arr2)
console.log(arr1)


//Desctructuring assignment
const avg_temp = {
    today: 30,
    tomorrow: {min:20, max:40}
};
function getTomorrowTemp(avgTemp)
{

    const {tomorrow : {max: tomorrow_temp }} = avgTemp;
    return tomorrow_temp;

}

console.log(getTomorrowTemp(avg_temp));