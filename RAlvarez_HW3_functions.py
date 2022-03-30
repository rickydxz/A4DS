#######################################################################
#                      Algorithms for Data Science                    #
#                             Homework # 3                            #
#                      Ricardo Alvarez - ralvar16                     #
#######################################################################

# This is the main background code of the Homework # 3
# of Algorithms for Data Science.
# The objective of this code is to define the functions that will be
# used for the development of the assignment in the Jupyter Notebook
# RAlvarezHW3.ipynb

# Feature ranking function
# input: Panda file with the features by columns
# output ranking of the features
import pandas as pd

# Definition fo the feature ranking function 
# [input]: panda with the features matrix
# [output]: List of the feature ranking using the FDRs
def FeatureRanking(featuresPanda):

    # List of numbers in the data set, and sorted
    numbersList = pd.unique(featuresPanda[0])
    numbersList.sort()

    #amount of features
    numFeatures = featuresPanda.shape[1]-1

    # initializing empty lists for the mean and the standard deviation
    meanList = []
    stdList = []

    # the code then iterate over the whole data set to get the rows of 
    # each number and compute the mean for each feature
    for index in range(len(numbersList)):
        # initializing the mean and standard deviation list 
        meanList.append([0]*numFeatures)
        stdList.append([0]*numFeatures)

        # current number of the data set
        currentNumber = numbersList[index]

        currentNumPanda = featuresPanda[featuresPanda[0] == currentNumber]
        # the first value is the number, and the subsequent values are the 
        # mean values
        meanList[currentNumber] = currentNumPanda.mean(axis = 0)
        # standard deviation values
        stdList[currentNumber] = currentNumPanda.std(axis = 0)

    # The fischer discrimination ratio is computed by pair of numbers
    FischerLists = []
    # row from the table
    row = 0

    for index1 in range(len(numbersList)):
        num1 = numbersList[index1]
        numbersList2 = range(index1+1,len(numbersList))
        for index2 in numbersList2:
            numColumns = numFeatures + 2
            num2 = numbersList[index2]
            FischerLists.append([0]*numColumns)
            FischerLists[row][0] = num1
            FischerLists[row][1] = num2
            meanDiff = meanList[index1] - meanList[index2]
            for featureNum in range(numFeatures):
                FischerLists[row][2+featureNum] = meanDiff[featureNum+1]
            row = row + 1
    return FischerLists