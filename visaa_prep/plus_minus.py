def plusMinus(arr):
    positive_count=0
    negative_count=0
    zero_count=0
    n=len(arr)
    for num in arr:
        if num>0:
            positive_count+=1
        elif num<0:
            negative_count+=1
        else:
            zero_count+=1
    positive_ratio=positive_count/n
    negative_ratio=negative_count/n
    zero_ratio=zero_count/n
    
    print(f"{positive_ratio:.6f}")
    print(f"{negative_ratio:.6f}")
    print(f"{zero_ratio:.6f}")
            
