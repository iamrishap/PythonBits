def palindromes(text):
    text = text.lower()
    results = []
    for i in range(len(text)):
        for j in range(0, i):
            chunk = text[j:i + 1] # Every possible chunk from size 1 to n
            if chunk == chunk[::-1]:
                results.append(chunk)
    return text.index(max(results, key=len)), results

print(palindromes('rishapahsir'))