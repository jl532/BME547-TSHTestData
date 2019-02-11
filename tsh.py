# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 20:54:03 2019

@author: Mars
"""


def nameParser(inputDictionary, inputString):
    firstAndLast = inputString.split(" ")
    inputDictionary["First Name:"] = firstAndLast[0]
    inputDictionary["Last Name: "] = firstAndLast[1]
    return inputDictionary


def ageParser(inputDictionary, inputString):
    inputDictionary["Age"] = int(inputString.rstrip())
    return inputDictionary


def genderParser(inputDictionary, inputString):
    inputDictionary["Gender"] = inputString
    return inputDictionary


def testDataParser(inputDictionary, inputString):
    testDataSplit = inputString.split(",")
    testDataTagRm = testDataSplit[1:]
    newData = []
    for eachEntry in testDataTagRm:
        newData.append(float(eachEntry))
    inputDictionary["TSHData"] = sorted(newData)
    return inputDictionary


def fileParser(fileName):
    fileData = open(fileName,"r")
    listOfPatients = []
    lineNumber = 0
    for eachLine in fileData:
        if lineNumber%4 == 0:
            if eachLine != "END":
                person = {}
                person = nameParser(person, eachLine.rstrip())
        if lineNumber%4 == 1:
            person = ageParser(person, eachLine.rstrip())
        if lineNumber%4 == 2:
            person = genderParser(person, eachLine.rstrip())
        if lineNumber%4 == 3:
            person = testDataParser(person, eachLine.rstrip())
            listOfPatients.append(person)
        lineNumber = lineNumber + 1
    fileData.close()
    return listOfPatients

def saveData(outFile, inputDictionary):
    import json
    fileWriter = open(outFile,"w")
    for eachPatient in inputDictionary:
        json.dump(eachPatient, fileWriter)
    fileWriter.close()
    
def diagnoseTSH(inputPatients):
    for eachPatient in inputPatients:
        tshData = eachPatient["TSHData"]
        if any(tshReading > 4 for tshReading in tshData):
            eachPatient["TSH Diagnosis"] = "hypothyroidism"
        if any(tshReading < 1 for tshReading in tshData):
            eachPatient["TSH Diagnosis"] = "hyperthyroidism"
        else:
            eachPatient["TSH Diagnosis"] = "normal thyroid function"
    return inputPatients

def main():
    patients = fileParser("test_data.txt")
    patients = diagnoseTSH(patients)
    outFile = "patients.json"
    saveData(outFile, patients)

if __name__ == "__main__":
    main()
    