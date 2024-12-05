'''Task 1'''
#Iterative
def edit_distance_iterative(s1,s2):
    m = len(s1)
    n = len(s2)
    if m == 0:
        return n
    if n == 0:
        return m
    i , count, j = 0,0,0
    while(i < m or j < n):
        if i >= m:
            count = count + n - j
            return count
        if j >= n:
            count = count + m - i
            return count
        if(s1[i] == s2[j]):
            i +=1
            j +=1
        else:
            count +=1
            i +=1
            j +=1
    return count
#Drive code
s1 = 'Dog'
s2 = 'hzkl'
s1 = s1.lower()
s2 = s2.lower()
print(edit_distance_iterative(s1, s2))
# Recursion
def edit_distance_recursion(s1 , s2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if (s1[m-1] == s2[n-1]):
        return edit_distance_recursion(s1, s2, m-1, n-1)
    return 1+min(edit_distance_recursion(s1, s2, m-1, n),# Insertion
                 edit_distance_recursion(s1, s2, m, n-1),# Remove
                 edit_distance_recursion(s1, s2, m-1, n-1))# Replace
def edit_distance(s1,s2):
    m = len(s1)
    n = len(s2)
    return edit_distance_recursion(s1, s2, m, n)
#Driver Code
s1 = 'Dog'
s2 = 'dig'
s1 = s1.lower()
s2 = s2.lower()
print(edit_distance(s1, s2))

#Recursion(Memoization)
def edit_distance_memoization(s1, s2, memo, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if memo[m][n] is not None:
        return memo[m][n]
    if (s1[m-1] == s2[n-1]):
        return edit_distance_memoization(s1, s2, memo, m-1, n-1)
    else:
        insert = edit_distance_recursion(s1, s2, memo, m-1, n) # insert
        remove = edit_distance_memoization(s1, s2, memo, m, n-1)# Remove
        replace = edit_distance_memoization(s1, s2, memo, m-1, n-1)# Replace
        memo[m][n] = 1 + min(insert, remove, replace)
        return memo[m][n]
def edit_distance_memo(s1,s2):
    m = len(s1)
    n = len(s2)
    memo = [[None] *(n+1) for _ in range(m+1)]
    return edit_distance_memoization(s1, s2, memo, m, n)
#Driver Code
s1 = 'Dog'
s2 = 'dighg'
s1 = s1.lower()
s2 = s2.lower()
print(edit_distance(s1, s2))    

#iterative(Tabulation)
def edit_distance_tabulation(s1,s2):
    m = len(s1)
    n = len(s2)
    dp = [[0] *(n+1) for _ in range(m+1)] 
    for i in range(m+1):
        dp[m][0] = i
    for j in range(n+1):
        dp[0][n] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if(s1[i-1] == s2 [j-1]):
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
    return dp[m][n]
#driver code
s1 = 'Dog'
s2 = 'dig'
s1 = s1.lower()
s2 = s2.lower()     
print(edit_distance_tabulation(s1, s2))
'''Task 2'''
#iterative Version
def unbalanced_brackets_stack(sequence):
    stack = []
    for char in sequence:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)
    return '(' * stack.count(')') + sequence + stack.count('(') * ')'
#driver code
s = "a+b)((c+d"
balanced = unbalanced_brackets_stack(s)
print(balanced)

#Recursive version
def unbalanced_brackets_recursive(sequence, index = 0, open_count = 0, close_count = 0):
    if len(sequence) == index:
        return '(' * close_count + sequence + ')' * open_count
    char = sequence[index]
    if char == '(':
        return unbalanced_brackets_recursive(sequence, index + 1, open_count + 1, close_count)
    elif char == ')':
        if open_count > 0:
            return unbalanced_brackets_recursive(sequence, index + 1, open_count - 1, close_count )
        else:
            return unbalanced_brackets_recursive(sequence, index + 1, open_count , close_count+ 1)
    else:
        return unbalanced_brackets_recursive(sequence, index + 1, open_count, close_count)
#Driver code
s = "xy) + (z"
balanced = unbalanced_brackets_recursive(s)
print(balanced)