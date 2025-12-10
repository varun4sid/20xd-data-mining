from q1 import getMean, getMedian, getMode

def getStandardDeviation(data):
    N = len(data)
    M = getMean(data)
    
    sum = 0
    for num in data:
        sum += (num - M)**2
        
    return (sum/N)**0.5


if __name__ == "__main__":
    g1 = [10, 15, 17, 25, 14, 76, 89, 190, 50]
    g2 = [18, 28, 5, 10, 28, 97, 156, 89, 55]
    g3 = [65, 15, 48, 55, 20, 67, 187, 28, 1]

    print("Mean of g1 : ", getMean(g1))
    print("Mean of g2 : ", getMean(g2))
    print("Mean of g3 : ", getMean(g3))

    print("Standard Deviation of g1 : ", getStandardDeviation(g1))
    print("Standard Deviation of g2 : ", getStandardDeviation(g2))
    print("Standard Deviation of g3 : ", getStandardDeviation(g3))