"""
Level 1
Write a program to find the length of the string "refrigerator" without using len function.
"""
str = "refrigerator"
cnt = 0

for i in str:
    cnt = cnt+1

print("Length of refrigerator:",cnt)