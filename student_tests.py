from rps import is_move_good, is_round_winner

# Test case 1: Lowercase rock (valid input)
# Expected output: True
# Actual output: True
print(is_move_good("r"))

# Test case 2: Uppercase paper (valid input)
# Expected output: True
# Actual output: True
print(is_move_good("P"))

# Test case 3: An unrecognized letter (invalid input)
# Expected output: False
# Actual output: False
print(is_move_good("a"))

# Test case 4: A full word instead of one letter (invalid input)
# Expected output: False
# Actual output: False
print(is_move_good("rock"))

# Test case 5: An empty string (edge case, invalid input)
# Expected output: False
# Actual output: False
print(is_move_good(""))

# Test case 6: A single space (edge case, invalid input)
# Expected output: False
# Actual output: False
print(is_move_good(" "))

# Test case 7: Rock beats scissors (valid input)
# Expected output: True
# Actual output: True
print(is_round_winner("r", "s"))

# Test case 8: Scissors beats paper (valid input)
# Expected output: True
# Actual output: True
print(is_round_winner("s", "p"))

# Test case 9: Paper beats rock (valid input)
# Expected output: True
# Actual output: True
print(is_round_winner("p", "r"))

# Test case 10: Rock loses to paper (valid input)
# Expected output: False
# Actual output: False
print(is_round_winner("r", "p"))

# Test case 11: Same move with different capitalization (edge case)
# Expected output: False
# Actual output: False
print(is_round_winner("R", "r"))

# Test case 12: A winning pair with mixed capitalization (edge case)
# Expected output: True
# Actual output: True
print(is_round_winner("S", "p"))

# Reflection:
# All 12 test results matched the expected outputs, so no tests failed.
# The tests confirmed that single-letter moves work in either case, while
# full words, an empty string, and a space don't.
# They also confirmed that a tie is not a win and capitalization does not
# change the result of a round.
# Both functions worked as expected, so I did not need to modify them.
