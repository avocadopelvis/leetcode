# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Use sliding window 
# If duplicate found, start shrinking sliding window from left until duplicate is removed

# Use dictionary (seen) to detect duplicates.

# CODE:
# Two pointers - left & right
# Left remains stationary until we find a duplicate. 
# If duplicate is found on right, we remove left character in the set & shift left. (reducing sliding window)
# Right keeps moving forward & we add characters to our set.

# Get the length of seen every iteration & get the max.

# • Time complexity is O(n) since we iterate through the whole string
# • Space complexity is O(n) because potentially every character in the string can be unique & so add all of them to our set. 

