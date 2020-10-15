def lengthstr(s, l =0):
    if s == "":
        return 0
    nl = 1 +  lengthstr(s[1:], l)
    return nl 

def main():
    stri = input("Please enter a string: ")
    print(lengthstr(stri))
if __name__ =="__main__":
    main()
