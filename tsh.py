# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 20:54:03 2019

@author: Mars
"""


def nameParser(inputDictionary, inputString):
    """Splits full name string into First and Last name and parses into dict

    nameParser takes an input String with a full name ("First Last") and
    splits the string to a list of ["First","Last"]. This list is parsed
    into the inputDictionary patient dictionary. This updated dictionary is
    then returned.

    Args:
        inputDictionary (dict): patient dictionary
        inputString (String): patient's full name
    Returns:
        inputDictionary (dict): patient dictionary with first and last name
    """
    firstAndLast = inputString.split(" ")
    inputDictionary["First Name:"] = firstAndLast[0]
    inputDictionary["Last Name: "] = firstAndLast[1]
    return inputDictionary


def ageParser(inputDictionary, inputString):
    """typesets the input String into an int and records in patient dictionary

    Nothing special is done here... it just takes the input string, turns it
    into an int, and then makes the "age" entry in the patient dictionary.
    Then outputs the patient dictionary after the age is entered. Simple

    Args:
        inputDictionary (dict): patient dictionary
        inputString (String): patient's age
    Returns:
        inputDictionary (dict): patient dictionary populated with age data
    """
    inputDictionary["Age"] = int(inputString)
    return inputDictionary


def genderParser(inputDictionary, inputString):
    """Directly enters inputString of Gender into patient dictionary

    Nothing special done here either. Takes input string, and places "gender"
    entry into the patient dictionary. Then outputs the patient dictionary
    after the age is entered. Simplest.

    Args:
        inputDictinoary (dict): patient dictionary
        inputString (String): patient's gender
    Returns:
        inputDictionary (dict): patient dictionary populated with gender data
    """
    inputDictionary["Gender"] = inputString
    return inputDictionary


def testDataParser(inputDictionary, inputString):
    """ Parses TSH data line into a list for input into patient dictionary

    Splits the TSH data line by commas, ignoring the first entry "TSH" and
    appending all other entries between commas into a list. This list is then
    sorted (extra credit) and appended in the patient dictionary under
    "TSHData". The populated patient dictionary is then returned.

    Args:
        inputDictionary (dict): patient dictionary
        inputString (String): patient's TSH data unformatted
    Returns:
        inputDictinoary (dict): patient dictionary populated with TSH data
    """
    testDataSplit = inputString.split(",")
    testDataTagRm = testDataSplit[1:]
    newData = []
    for eachEntry in testDataTagRm:
        newData.append(float(eachEntry))
    inputDictionary["TSHData"] = sorted(newData)
    return inputDictionary


def fileParser(fileName):
    """Parses patient information from txt input into a list of dictionaries

    This file Parser opens the given text file and parses it line-by-line,
    which corresponds to the particular piece of patient information in order.
    The pre-determined order of data is as follows: First Name/Last Name, Age,
    Gender, and TSH test data. Given this order, the modulo command can be used
    with the lineNumber within the text file to send the line to the proper
    String parsing function. These functions append dictionary entries for
    each patient, in order. In the sequence, the first line corresponding to
    a new patient initializes a new dictionary, the lines of data are parsed in
    dictionary key/value pairs, and then the function appends the fully
    populated dictionary into the list of patients. This list of dictionaries
    with patient data is then returned.

    Args:
        fileName (String): name of the .txt file containing patient info

    Returns:
        listOfPatients (list): list of dictionaries with patient information
    """

    fileData = open(fileName, "r")
    listOfPatients = []
    lineNumber = 0
    for eachLine in fileData:
        if lineNumber % 4 == 0:
            if eachLine != "END":
                person = {}
                person = nameParser(person, eachLine.rstrip())
        if lineNumber % 4 == 1:
            person = ageParser(person, eachLine.rstrip())
        if lineNumber % 4 == 2:
            person = genderParser(person, eachLine.rstrip())
        if lineNumber % 4 == 3:
            person = testDataParser(person, eachLine.rstrip())
            listOfPatients.append(person)
        lineNumber = lineNumber + 1
    fileData.close()
    return listOfPatients


def saveData(outFile, inputDictionaries):
    """Generates the json formatted file including all patient data

    saveData takes the input list of dictionaries and dumps them in json format
    into the target "outFile" .json file.

    Args:
        outFile (String): file name of the json output file
        inputDictionaries (list): list including all patient dictionaries
    """
    import json
    fileWriter = open(outFile, "w")
    for eachPatient in inputDictionaries:
        json.dump(eachPatient, fileWriter)
    fileWriter.close()


def diagnoseTSH(inputPatients):
    """Runs the TSH data of each patient through predetermined diagnostic logic

    The function iterates through each patient in the input list, checking
    each TSH reading against the specifications for diagnostic cutoffs for
    Thyroid Stimulating Hormone (TSH). If a hit is found, the corresponding
    diagnosis is appended in the patient dictionary. Else, a normal status is
    appended. The full list of dictionaries with the diagnostic status is
    returned.

    Args:
        inputPatients (list): list of patient dictionaries
    Returns:
        inputPatients (list): list of patient dictionaries with diagnosis

    """
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
