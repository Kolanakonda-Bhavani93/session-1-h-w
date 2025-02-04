def mostFrequentWord(arr, n):
  
    # freq to store the freq of the most occurring variable
    freq = 0
    
    # res to store the most occurring string in the array of strings
    res = ""
    
    for i in range(0, n, 1):
        count = 0
        for j in range(i + 1, n, 1):
            if arr[j] == arr[i]:
                count += 1
        if count >= freq:
            res = arr[i]
            freq = count

    print("The word that occurs most is : " + str(res))
    print("No of times: " + str(freq))
arr = [ "geeks", "for", "geeks", "a", "portal", "to", "learn", "can", "be", "computer", "science", "zoom", "yup", "fire", "in", "be", "data", "geeks",]
n = len(arr)
mostFrequentWord(arr, n)

