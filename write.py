# algorithm to filter if its ip, interface or rName
import re
patternList = [r'\b(?:\d{1,3}\.){3}\d{1,3}\b', r'\b(router1|rt1)\b', r'\bf\d\S*|g\d\S*|s\d\S*']
arrList = ["interfaceArr", "routerNameArr", "ipAdressesArr"]
arrElementsList = ["interface", "routername", "ipAdresses"]
r2eIP = []
r2rIP = []
path = "test.txt"

def readFile(path):
    f = open(path)
    fileContent = f.readlines()
    f.close()
    return fileContent

def filterIP(ip):
    if ip.find("s") != -1:
        r2rIP.append(ip)
    else:
        r2eIP.append(ip)

def regexFind(strings, patternIndex, array, itemOfArray):
    for line in strings:
        itemOfArray = re.findall(patternList[patternIndex], line.lower())
        for i in itemOfArray:
            if itemOfArray != []:
                array.append(i)

def main():
    fileContent = readFile(path)

    # execute regexFind
    for i in range(len(arrList)):
        arrList[i] = []
        regexFind(fileContent, i, arrList[i], arrElementsList[i])

    for i in range(len(arrList[2])):
        filterIP(arrList[2][i])

    print(f"Routername: {arrList[1]}\nInterfaces: {arrList[2]}\nRouter2Ethernet: {r2eIP}\nRouter2Router: {r2rIP}")

if __name__ == "__main__":
    main()