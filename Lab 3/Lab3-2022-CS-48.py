# Task 1: Edit Distance Implementations

# Iterative Version (Two Pointers Approach)
def edit_distance_iterative(s1, s2):
    m, n = len(s1), len(s2)
    
    if m == 0:
        return n
    if n == 0:
        return m
    
    i, j, count = 0, 0, 0
    
    while i < m or j < n:
        if i >= m:
            count += (n - j)  # Add remaining characters in s2
            break
        if j >= n:
            count += (m - i)  # Add remaining characters in s1
            break
        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            count += 1
            i += 1
            j += 1
            
    return count

# Driver code
s1 = 'Dog'
s2 = 'hzkl'
print(edit_distance_iterative(s1.lower(), s2.lower()))


# Recursive Version (Naive)
def edit_distance_recursive(s1, s2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if s1[m - 1] == s2[n - 1]:
        return edit_distance_recursive(s1, s2, m - 1, n - 1)
    
    return 1 + min(
        edit_distance_recursive(s1, s2, m - 1, n),     # Insertion
        edit_distance_recursive(s1, s2, m, n - 1),     # Deletion
        edit_distance_recursive(s1, s2, m - 1, n - 1)  # Replacement
    )

# Driver code
s1 = 'Dog'
s2 = 'dig'
print(edit_distance_recursive(s1.lower(), s2.lower(), len(s1), len(s2)))


# Memoized Version (Recursion + Memoization)
def edit_distance_memoization(s1, s2, memo, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if memo[m][n] is not None:
        return memo[m][n]
    
    if s1[m - 1] == s2[n - 1]:
        memo[m][n] = edit_distance_memoization(s1, s2, memo, m - 1, n - 1)
    else:
        insert_op = edit_distance_memoization(s1, s2, memo, m - 1, n)
        delete_op = edit_distance_memoization(s1, s2, memo, m, n - 1)
        replace_op = edit_distance_memoization(s1, s2, memo, m - 1, n - 1)
        memo[m][n] = 1 + min(insert_op, delete_op, replace_op)
    
    return memo[m][n]

def edit_distance_memo(s1, s2):
    m, n = len(s1), len(s2)
    memo = [[None] * (n + 1) for _ in range(m + 1)]
    return edit_distance_memoization(s1, s2, memo, m, n)

# Driver code
s1 = 'Dog'
s2 = 'dighg'
print(edit_distance_memo(s1.lower(), s2.lower()))


# Iterative Version (Tabulation / DP)
def edit_distance_tabulation(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases for filling first row and column
    for i in range(m + 1):
        dp[i][0] = i  # Deletion
    for j in range(n + 1):
        dp[0][j] = j  # Insertion
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
    return dp[m][n]

# Driver code
s1 = 'Dog'
s2 = 'dig'
print(edit_distance_tabulation(s1.lower(), s2.lower()))


# Task 2: Balancing Brackets

# Iterative Version Using Stack
def balance_brackets_stack(sequence):
    stack = []
    for char in sequence:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()  # Correct pair found, pop it
            else:
                stack.append(char)  # Mismatched closing bracket
    
    # Add necessary parentheses to balance
    return '(' * stack.count(')') + sequence + ')' * stack.count('(')

# Driver code
s = "a+b)((c+d"
print(balance_brackets_stack(s))


# Recursive Version
def balance_brackets_recursive(sequence, index=0, open_count=0, close_count=0):
    if index == len(sequence):
        # Return corrected sequence with extra parentheses if needed
        return '(' * close_count + sequence + ')' * open_count
    
    char = sequence[index]
    if char == '(':
        return balance_brackets_recursive(sequence, index + 1, open_count + 1, close_count)
    elif char == ')':
        if open_count > 0:
            return balance_brackets_recursive(sequence, index + 1, open_count - 1, close_count)
        else:
            return balance_brackets_recursive(sequence, index + 1, open_count, close_count + 1)
    else:
        return balance_brackets_recursive(sequence, index + 1, open_count, close_count)

# Driver code
s = "xy) + (z"
print(balance_brackets_recursive(s))