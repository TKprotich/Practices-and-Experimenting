plain_text = "This is a test. ABC abc"
 
for c in plain_text:
    x = ord(c)
    x = x + 1
    c2 = chr(x)
    print(c2, end="")
print()
encripted = "Uijt!jt!b!uftu/!BCD!bcd"
decoded = ''
for c in encripted:
    x = ord(c)
    x = x - 1
    c2 = chr(x)
    decoded +=c2
print(decoded, end="")
