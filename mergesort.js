/**
 * Implement the solution in this function
 *
 * @param {number[]} arr1 First sorted array
 * @param {number[]} arr2 Second sorted array
 * @returns {number[]} Merged and sorted array
 */
function merge (arr1, arr2) {
 var arr = [];
 var i = 0;
 var j = 0;
 while (i < arr1.length & j < arr2.length) {
   if (arr1[i] < arr2[j]) {
       arr.push(arr1[i]);
       i += 1;
   } else {
       arr.push(arr2[j]);
       j += 1;
   }
 }
 while (i < arr1.length) {
     arr.push(arr1[i])
     i += 1;
 }
  while (j < arr2.length) {
     arr.push(arr2[j])
     j += 1;
 }
 return arr;
}
