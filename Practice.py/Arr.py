# To print first non repeating number in an array
def norepeat(arr):
    freq = {}
    for i in arr:
        freq[i] = freq.get(i, 0) + 1 
    for i in arr:
        if freq[i] == 1:
            return i 
        return 0
if __name__ == "__main__":
    arr = [-1, 2, -1, 4, 3, 4]
    print(norepeat(arr)) 

