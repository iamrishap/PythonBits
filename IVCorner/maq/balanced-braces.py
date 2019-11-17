"""
Braces in a string
Braces in a string are considered to be balanced if the following criteria are met:
All braces must be closed.
Braces come in pairs of the form (), {} and [].
The left brace opens the pair, and the right one closes it.
In any set of nested braces, the braces between any pair must be closed.
For example, [{}] is a valid grouping of braces but [{]} is not.
The function must return an array of strings where the string at each index i denotes whether or not the braces were
balanced in values[i]. The array should consist of strings YES or NO aligned with their indices in values.
braces has the following parameter(s): values[values[O],...values[n-1]]: an array of strings to analyze Constraints
Each values[i] consists of (, ), {, }, [, and ] only.
"""

# Complete the braces function below.
def braces(values):
    """
    Function to compare balance in the braces
    args: values: list of strings

    returns: list of strings representing balance in braces
    """
    braces_stack = []
    if len(values) < 1:
        return
    braces_start = ['{', '[', '(']
    braces_end = ['}', ']J', ')']
    result = []
    for brace_string in values:
        braces_stack = []
        for brace in brace_string:
            if brace in braces_end:
                if len(braces_stack) > 0 and braces_stack[-1] == brace:
                    braces_stack.pop()
                else:
                    result.append('FALSE')
                    break
            if brace in braces_start:
                braces_stack.append()
        if len(braces_stack) == 0:
            result.append('TRUE')


if __name__ == '__main__':
    print(braces('[{}]'))
