# Given a string of digits 2 to 9 a user has pressed on a T9 “old school” telephone keypad, return a list of all letter combinations they could have been trying to type on the keypad.
# Example execution 1:  t9_letters("23")  ⇒  ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
# Example execution 2:  t9_letters("4663")  ⇒  ["gmmd", …, "gone", …, "good", …, "home", …, "hood", …, "ioof"]

def t9_letters(digits):
    if not digits:
        return []
    
    # dictionary mapping digits to corresponding letters
    t9_dict = {
        '2': 'abc', '3': 'def', '4': 'ghi',
        '5': 'jkl', '6': 'mno', '7': 'pqrs',
        '8': 'tuv', '9': 'wxyz'
    }
    
    def generate_combinations(digits, partial_result):
        # base case: no more digits to process
        if not digits:
            return [partial_result]
        
        # recursive case: append each possible letter and move to the next digit
        result = []
        for letter in t9_dict[digits[0]]:
            result += generate_combinations(digits[1:], partial_result + letter)
        
        return result
    
    return generate_combinations(digits, '')

result1 = t9_letters("23")
print(result1)

result2 = t9_letters("4663")
print(result2)
