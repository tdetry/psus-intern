function isPalindrome(str){
    var pointer1 = 0;
    var pointer2 = str.length - 1;
    while (pointer2 >= pointer1){
        if (str.charAt(pointer2) != str.charAt(pointer1)){
            return false;
        }
        pointer1++;
        pointer2--;
    }
    return true;
}


var test1 = "kayak"
var test2 = "odoo"
var test3 = "solos"
var test4 = "saippuakivikauppias"
var test5 = ""

console.log(isPalindrome(test1));
console.log(isPalindrome(test2));
console.log(isPalindrome(test3));
console.log(isPalindrome(test4));
console.log(isPalindrome(test5));