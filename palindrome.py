def isPalindrome(word):
    pointer1 = 0
    pointer2 = len(word) - 1
    while pointer2 >= pointer1:
        if word[pointer1] != word[pointer2]:
            return False
        pointer1 += 1
        pointer2 -= 1
    return True

    


test1 = "kayak"
test2 = "odoo"
test3 = "solos"
test4 = "saippuakivikauppias"
test5 = ""

print(isPalindrome(test1))
print(isPalindrome(test2))
print(isPalindrome(test3))
print(isPalindrome(test4))
print(isPalindrome(test5))