class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack

# Create an instance of the Solution class
obj = Solution()

# Taking user input
user_input = '(){}'

# Pass it to the class
is_valid = obj.isValid(user_input)

# Print the result
print(is_valid)
