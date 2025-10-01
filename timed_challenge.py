# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!
"""

TIMED CHALLENGE - 30 MINUTES

Problem: Balanced Symbols (Group 4: Last-In, First-Out Logic)

Check if the brackets in a string are balanced.

Input: "{[()]}"
Output: True

Input: "{[(])}"
Output: False

Rules:
- Opening brackets must be closed by the same type of bracket
- Opening brackets must be closed in the correct order
- Every closing bracket must have a corresponding opening bracket
"""

def is_balanced(string):
    """
    Check if brackets in a string are balanced.
    
    Justification:
    I chose a stack because this problem requires Last-In-First-Out (LIFO) behavior.
    When we encounter an opening bracket, we push it onto the stack O(1). When we
    encounter a closing bracket, we pop from the stack O(1) and verify it matches.
    This gives us O(n) overall time complexity with O(n) space complexity, which is
    optimal for bracket matching problems.
    """
    # Stack to keep track of opening brackets
    stack = []
    
    # Dictionary to map closing brackets to their opening counterparts
    matching = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    # Iterate through each character in the string
    for char in string:
        # If it's an opening bracket, push to stack
        if char in '({[':
            stack.append(char)
        
        # If it's a closing bracket
        elif char in ')}]':
            # Check if stack is empty (no matching opening bracket)
            if not stack:
                return False
            
            # Pop from stack and check if it matches
            top = stack.pop()
            if top != matching[char]:
                return False
    
    # If stack is empty, all brackets were matched
    # If stack has items, there are unmatched opening brackets
    return len(stack) == 0


# Test cases
def test_balanced_symbols():
    print("Testing Balanced Symbols...")
    
    # Test case 1: Basic balanced
    assert is_balanced("{[()]}") == True
    print("✓ Test 1 passed: {[()]}")
    
    # Test case 2: Basic unbalanced
    assert is_balanced("{[(])}") == False
    print("✓ Test 2 passed: {[(])}")
    
    # Test case 3: Empty string (edge case)
    assert is_balanced("") == True
    print("✓ Test 3 passed: empty string")
    
    # Test case 4: Only opening brackets (edge case)
    assert is_balanced("{{{") == False
    print("✓ Test 4 passed: only opening brackets")
    
    # Test case 5: Only closing brackets (edge case)
    assert is_balanced("}}}") == False
    print("✓ Test 5 passed: only closing brackets")
    
    # Test case 6: Single pair
    assert is_balanced("()") == True
    print("✓ Test 6 passed: single pair ()")
    
    # Test case 7: Nested same type
    assert is_balanced("((()))") == True
    print("✓ Test 7 passed: nested same type")
    
    # Test case 8: Multiple types balanced
    assert is_balanced("()[]{}") == True
    print("✓ Test 8 passed: multiple types balanced")
    
    # Test case 9: Wrong order
    assert is_balanced("([)]") == False
    print("✓ Test 9 passed: wrong order ([)]")
    
    # Test case 10: Complex balanced
    assert is_balanced("{[()]}(){}") == True
    print("✓ Test 10 passed: complex balanced")
    
    # Test case 11: Single opening bracket
    assert is_balanced("(") == False
    print("✓ Test 11 passed: single opening bracket")
    
    # Test case 12: Single closing bracket
    assert is_balanced(")") == False
    print("✓ Test 12 passed: single closing bracket")
    
    # Test case 13: Mismatched types
    assert is_balanced("(]") == False
    print("✓ Test 13 passed: mismatched types (]")
    
    print("\nAll tests passed! ✓")


# Run tests
test_balanced_symbols()


"""
REFLECTION (200-300 words)

Structure Choice and Reasoning:
I chose a stack data structure to solve the balanced symbols problem because it 
perfectly matches the Last-In-First-Out (LIFO) nature of bracket matching. When 
parsing the string, each opening bracket must be closed by its corresponding closing 
bracket in reverse order - exactly how a stack operates. The stack allows me to 
push opening brackets with O(1) complexity and pop them when encountering closing 
brackets, also in O(1) time.

Impact of Time Limit:
The 30-minute constraint significantly influenced my approach. I immediately 
recognized this as a classic stack problem from the "Last-In, First-Out Logic" 
category, which allowed me to start coding within the first 2-3 minutes. I didn't 
spend time considering alternative data structures like queues or lists because 
I knew stack was optimal. This instant recognition saved valuable time that I could 
allocate to testing and edge cases.

Trade-offs and Compromises:
Under time pressure, I prioritized getting a working solution quickly over potential 
optimizations. I used Python's built-in list as a stack rather than implementing a 
custom Stack class, which is perfectly acceptable and more practical. I also created 
a matching dictionary upfront rather than using conditional logic, trading a small 
amount of space for cleaner, more readable code.

My main compromise was in the testing strategy. While I tested 13 different cases 
including edge cases (empty strings, single brackets, mismatched types), I could 
have tested with strings containing non-bracket characters. However, the problem 
statement implied we'd only receive bracket characters, so I focused on the core 
matching logic instead.

The time limit taught me to trust pattern recognition and implement proven solutions 
rather than overthinking. In a real interview, demonstrating you know standard 
approaches and can execute them correctly is more valuable than finding a novel 
solution.

Time taken: Approximately 28 minutes
"""
