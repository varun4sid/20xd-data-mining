import csv
import math

def getDataFromCSV(filename):
    with open(filename,"r") as file:
        reader = csv.reader(file)
        data = []
        for row in reader:
            data.append(row)
    table = []
    cf = 0
    for row in data:
        cf += int(row[2])
        obj = {
            "start" : int(row[0]),
            "end" : int(row[1]),
            "frequency" : int(row[2]),
            "cf": cf
        }
        table.append(obj)    
        
    return table


def getTotalFrequency(table):
    freqSum = 0
    for row in table:
        freqSum += row["frequency"]
    return freqSum


def getMean(table):
    rowSum = 0
    freqSum = 0
    for row in table:
        rowSum += (row["start"]+row["end"])/2 * row["frequency"]
        freqSum += row["frequency"]
    
    return rowSum/freqSum


def getMedian(table):
    n = getTotalFrequency(table)
    half = n/2

    medianClass = None
    for obj in table:
        if obj["cf"] >= half:
            medianClass = obj
            break
            
    if medianClass is None:
        raise ValueError("No median class found. Check the data.")
            
    L = medianClass["start"]
    w = medianClass["end"] - L + 1
    B = medianClass["cf"]
    G = medianClass["frequency"]
    
    return L + ((half-B)/G) * w


def getMode(table):
    modalClasses = []
    maxVal = 0
    
    for obj in table:
        if obj["frequency"] > maxVal:
            maxVal = obj["frequency"]

    for index, obj in enumerate(table):
        if obj["frequency"] == maxVal:
            if index != 0:
                obj["f0"] = table[index-1]["frequency"]
            else:
                obj["f0"] = 0
            if index != len(table)-1:
                obj["f2"] = table[index+1]["frequency"]
            else:
                obj["f2"] = 0
            modalClasses.append(obj)
    modes = []
    for obj in modalClasses:
        mode = obj["start"] + (obj["frequency"] - obj["f0"])/(2*obj["frequency"] - obj["f2"] - obj["f0"])
        modes.append(mode)
        
    return modes


def checkEmpiricalRule(data):
    mean = getMean(data)
    median = getMedian(data)
    mode = getMode(data)[0]
    
    print(f"{3*median} = {2*mean} + {mode}")
    if 3*median == 2*mean + mode:
        return True
    else:
        return False


if __name__ == "__main__":
    filename = "q2.csv"
    data = getDataFromCSV(filename)
    print("Mean : ", getMean(data))
    print("Median : ", getMedian(data))
    print("Mode : ", getMode(data))
    print(f"Empirical rule : {"Satisfied" if checkEmpiricalRule(data) else "Not satisfied"}")