//Two sum 

//Testcases
var arr1 = [6, 3, 4];
var target1 = 10;

var arr2 = [3, 5, 2, 7, 4, 5];
var target2 = 12;

var arr3 = [3, 6, 2, 9];
var target3 = 100;

var arr4 = [];
var target4 = 0;


console.log(twoSum(arr1, target1)); //expecting [0, 2]
console.log(twoSum(arr2, target2)); //expecting [1, 3]
console.log(twoSum(arr3, target3)); //expecting []
console.log(twoSum(arr4, target4)); //expecting []

//Function
function twoSum(arr, target){
    var subTargets = {};
    for (var i = 0; i < arr.length; i++){
        var currElement = arr[i]
        var currDiff = target - currElement;
        if (currElement in subTargets){
            return [subTargets[currElement], i];
        } else {
            subTargets[currDiff] = i;
        }
    }
    return [];
}