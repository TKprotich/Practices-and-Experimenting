def add(seq):
    seqType = type(seq)
    emptySeq = seqType()
    if seq == emptySeq:
        return 0
    return seq[0] + add(seq[1:])
def main():
    print(add([45,444444, 45,444444, 45,444444]))
if __name__ == "__main__":
    main()
