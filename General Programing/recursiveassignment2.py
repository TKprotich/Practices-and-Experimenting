def fact(n):
    #base case
    if n == 0:
        return 1
    #recursive case
    return n*(n-1)
def main():
    print(fact(100))
if __name__ =="__main__":
    main()
