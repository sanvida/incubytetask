import re
import unittest

""" 
first I have to create StringCalculator class 
inside that class need to create a add method to add all the numbers
so first i need to check each cases like - 
- if input string is emprty
- if inpurt string is separated by comma or new line
- if input string contains custom delimeter
- if input string contains negative numbers

-add function will return the sum of all the positive numbers
"""

class StringCalculator:
    @staticmethod
    def add(numbers: str) -> int:
        # return 0 if the string is empty
        if not numbers:
            return 0
        
        # Default delimiter is comma or newline
        delimiter = ',|\n'
        
        # Need to check if there is a custom delimiter
        if numbers.startswith('//'):
            # Split the input in order to get the delimiter and number
            parts = numbers.split('\n', 1)

            # extract the custom delimiter
            delimiter = re.escape(parts[0][2:])
            numbers = parts[1]
        
        # split the numbers string using the delimiters
        number_list = re.split(delimiter, numbers)
        result = 0
        negatives = []
        
        # loop through the list of number strings
        for number in number_list:
            if number:
                num = int(number)
                if num < 0:
                    # storing all the negative numbers to raise an exception later
                    negatives.append(num)
                result += num  # finally add the positive number to the result
        
        # there are negative numbers, raise an exception with their details
        if negatives:
            raise ValueError(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")
        
        # finally return the sum of the numbers
        return result
    

# manually tested all the cases by direcltly calling the add function
# obj = StringCalculator()
# print(obj.add(""))
# print(obj.add("1"))
# print(obj.add("1,2"))
# print(obj.add("10,30"))
# print(obj.add("1\n2,3"))
# print(obj.add("//|\n10|20|30"))
# print(obj.add("1,-2,3,-4"))
# print(obj.add("//;\n1;-2;3;-4"))


# unit test for each case
class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(StringCalculator.add(""), 0)
    
    def test_single_number(self):
        self.assertEqual(StringCalculator.add("1"), 1)
        self.assertEqual(StringCalculator.add("5"), 5)
    
    def test_two_numbers(self):
        self.assertEqual(StringCalculator.add("1,2"), 3)
        self.assertEqual(StringCalculator.add("10,20"), 30)
    
    def test_multiple_numbers(self):
        self.assertEqual(StringCalculator.add("1,2,3"), 6)
        self.assertEqual(StringCalculator.add("10,20,30,40"), 100)
    
    def test_new_lines_between_numbers(self):
        self.assertEqual(StringCalculator.add("1\n2,3"), 6)
        self.assertEqual(StringCalculator.add("10\n20\n30,40"), 100)
    
    def test_custom_delimiter(self):
        self.assertEqual(StringCalculator.add("//;\n1;2"), 3)
        self.assertEqual(StringCalculator.add("//|\n10|20|30"), 60)
    
    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            StringCalculator.add("1,-2,3,-4")
        self.assertTrue("Negative numbers not allowed: -2, -4" in str(context.exception))
    
    def test_custom_delimiter_with_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            StringCalculator.add("//;\n1;-2;3;-4")
        self.assertTrue("Negative numbers not allowed: -2, -4" in str(context.exception))

if __name__ == '__main__':
    unittest.main()