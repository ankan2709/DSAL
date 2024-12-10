def letterCombinations(digits):

    KEYBOARD = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
    }   
    
    res = []

    def backtrack(start__index, temp):
        if start__index == len(digits):
            res.append(''.join(temp[:]))
            return
        
        next_num = digits[start__index]
        for letter in KEYBOARD[next_num]:
            temp.append(letter)
            backtrack(start__index + 1, temp)
            temp.pop()

    backtrack(0, [])
    return res


print(letterCombinations("56"))