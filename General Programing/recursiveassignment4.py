def swap(s):
    if s=="":
        return ""
    return s[1]+s[0] + swap(s[2:])
def main():
    #print(swap("abcdefgh"))
    print(swap("kiprotichtimothy"))
if __name__ =="__main__":
    main()
