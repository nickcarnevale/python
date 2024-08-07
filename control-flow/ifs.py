# If statements don't need parentheses or curly braces
# Indentation is used to show what should happen after an if or else

n = 1
if n > 2: 
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2

# Multi-line conditions need parentheses
# and = &&
# or = ||

n, m = 1, 2
if((n > 2 and 
    n != m) or n == m):
    n += 1

if n > 2 and n != m or n == m: 
    n -= 1 





