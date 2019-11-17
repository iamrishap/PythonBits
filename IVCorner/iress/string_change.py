'''
You will be given 2 strings and need to make the changes below based on the words “nice” and “niece” and others.  
String 1- if its nice = insert because you’re putting in an extra e to make niece 
String 2- niece to nice = delete the extra e
String 3: form to from = swap
String 4: if its identical
String 5: impossible
'''

def solution(S, T):
    # write your code in Python 3.6
    if S == T:
        return "NOTHING"
    elif abs(len(S) - len(T)) > 1:
        return "IMPOSSIBLE"
    else:
        swap_str = None
        if len(S) == len(T):
            # Try swapping a character
            skip_i = len(S)   # RISHAP ADDED LATER. SKIP I.
            for i in range(len(S)):
                if S[i] != T[i] and skip_i != i:  # All values can't be same. So we are just considering the different values  # RISHAP ADDED LATER. SKIP I.
                    if i < len(S)-1 and S[i+1] == T[i] and swap_str is None and S[i] == T[i+1]:  # Check limits of array
                        swap_str = "SWAP " + S[i] + " " + S[i+1]
                        skip_i = i+1  # RISHAP ADDED LATER. SKIP I.
                    else:
                        return "IMPOSSIBLE"
            return swap_str
        elif len(S) > len(T):
            # Try deleting a character
            chance = 0  # Only one chance to reedem(delete)
            j = 0
            for i in range(len(S)):
                if j < len(S):  # Checking that j is still in bounds of array length
                    if S[j] == T[i]:
                        j += 1
                    elif S[j] != T[i] and S[j+1] == T[i] and chance == 0:
                        c_del = S[j]
                        j += 2
                        chance = 1
                    else:
                        return "IMPOSSIBLE"
            return "DELETE " + c_del  # If so far it hasn't been impossible, it is possible with deletion
        else:
            # Try inserting a character
            chance = 0  # Only one chance to reedem(insert)
            j = 0
            for i in range(len(S)):
                if j < len(S):
                    if S[i] == T[j]:
                        if i == len(S) - 1:
                            return "INSERT " + T[i+1]  # To handle cases like 'nice' -> 'nicee'
                        j += 1
                    elif S[j] != T[i] and S[j] == T[i + 1] and chance == 0:
                        c_ins = T[i]
                        j += 2
                        chance = 1
                    else:
                        return "IMPOSSIBLE"
            return "INSERT " + c_ins  # If so far it hasn't been impossible, it is possible with insertion
    return "IMPOSSIBLE"

print(solution('form', 'from'))
print(solution('form', 'format'))
print(solution('front', 'font'))
print(solution('alex', 'alexa'))
print(solution('olx', 'olax'))
print(solution('olax', 'olax'))