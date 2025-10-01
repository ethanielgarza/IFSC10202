S = input("Enter a String: ")
splitpoint = (len(S) + 1) // 2
firsthalve = S[:splitpoint]
secondhalve = S[splitpoint:]
New_S = secondhalve + firsthalve
print(New_S)