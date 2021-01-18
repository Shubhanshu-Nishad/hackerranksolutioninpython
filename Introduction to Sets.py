def average(array):
    # your code goes here
    set1=set(arr)
    sum1=sum(set1)
    n = len(set1)
    return float(sum1/n)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
