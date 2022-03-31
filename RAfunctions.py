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
            FischerLists.append([0]*numFeatures+2)
            FischerLists[row][0] = num1
            FischerLists[row][1] = num2
            meanDiff = meanList[index1] - meanList[index2]
            for featureNum in range(numFeatures-1):
                FischerLists[row][2+featureNum] = meanDiff[featureNum+1]
            row = row + 1





    a = 1
    # First the amount of columns of the features are computed:

    a = 2

    ratioScores = 1

    return ratioScores

    # vector to save the size of the panda
    pdSize = [0]
    pdSize.append(int(IrisPanda.shape[0]/3))
    pdSize.append(int(2*IrisPanda.shape[0]/3))
    pdSize.append(int(IrisPanda.shape[0]))

    #First the mean by each class is computed
    # setosa mean
    setosaMean = []
    setosaMean.append(IrisPanda[pdSize[0]:pdSize[1]]["sepal_length"].mean())
    setosaMean.append(IrisPanda[pdSize[0]:pdSize[1]]["sepal_width"].mean())
    setosaMean.append(IrisPanda[pdSize[0]:pdSize[1]]["petal_length"].mean())
    setosaMean.append(IrisPanda[pdSize[0]:pdSize[1]]["petal_width"].mean())
    # versicolor mean
    versicolorMean = []
    versicolorMean.append(IrisPanda[pdSize[1]:pdSize[2]]["sepal_length"].mean())
    versicolorMean.append(IrisPanda[pdSize[1]:pdSize[2]]["sepal_width"].mean())
    versicolorMean.append(IrisPanda[pdSize[1]:pdSize[2]]["petal_length"].mean())
    versicolorMean.append(IrisPanda[pdSize[1]:pdSize[2]]["petal_width"].mean())
    # virginica mean
    virginicaMean = []
    virginicaMean.append(IrisPanda[pdSize[2]:pdSize[3]]["sepal_length"].mean())
    virginicaMean.append(IrisPanda[pdSize[2]:pdSize[3]]["sepal_width"].mean())
    virginicaMean.append(IrisPanda[pdSize[2]:pdSize[3]]["petal_length"].mean())
    virginicaMean.append(IrisPanda[pdSize[2]:pdSize[3]]["petal_width"].mean())
    
    #Standard deviation for each class is computed
    # setosa mean
    setosaStd = []
    setosaStd.append(IrisPanda[pdSize[0]:pdSize[1]]["sepal_length"].std())
    setosaStd.append(IrisPanda[pdSize[0]:pdSize[1]]["sepal_width"].std())
    setosaStd.append(IrisPanda[pdSize[0]:pdSize[1]]["petal_length"].std())
    setosaStd.append(IrisPanda[pdSize[0]:pdSize[1]]["petal_width"].std())
    # versicolor mean
    versicolorStd = []
    versicolorStd.append(IrisPanda[pdSize[1]:pdSize[2]]["sepal_length"].std())
    versicolorStd.append(IrisPanda[pdSize[1]:pdSize[2]]["sepal_width"].std())
    versicolorStd.append(IrisPanda[pdSize[1]:pdSize[2]]["petal_length"].std())
    versicolorStd.append(IrisPanda[pdSize[1]:pdSize[2]]["petal_width"].std())
    # virginica mean
    virginicaStd = []
    virginicaStd.append(IrisPanda[pdSize[2]:pdSize[3]]["sepal_length"].std())
    virginicaStd.append(IrisPanda[pdSize[2]:pdSize[3]]["sepal_width"].std())
    virginicaStd.append(IrisPanda[pdSize[2]:pdSize[3]]["petal_length"].std())
    virginicaStd.append(IrisPanda[pdSize[2]:pdSize[3]]["petal_width"].std())

    # The fischer discrimination ratio is computed by pair of species 

    #Setosa  - Versicolor 
    xSetosaVersicolor = np.array(IrisPanda.iloc[pdSize[0]:pdSize[1]])
    xSetosaVersicolor[:,:-1]
    MeanDifSetosaVersicolor = np.array(setosaMean) - np.array(versicolorMean)
    MeanDifSetosaVersicolor = np.multiply(MeanDifSetosaVersicolor,MeanDifSetosaVersicolor)
    StdSumSetosaVersicolor = np.multiply(setosaStd,setosaStd) + np.multiply(versicolorStd,versicolorStd)
    ratioScoreSetosaVersicolor = np.divide(MeanDifSetosaVersicolor,StdSumSetosaVersicolor)

    #Versicolor  - Virginica 
    xVersicolorVirginica = np.array(IrisPanda.iloc[pdSize[1]:pdSize[3]])
    xVersicolorVirginica[:,:-1]
    MeanDifVersicolorVirginica = np.array(versicolorMean) - np.array(virginicaMean)
    MeanDifVersicolorVirginica = np.multiply(MeanDifVersicolorVirginica,MeanDifVersicolorVirginica)

    StdSumVersicolorVirginica = np.multiply(versicolorStd,versicolorStd) + np.multiply(virginicaStd,virginicaStd)

    ratioScoreVersicolorVirginica = np.divide(MeanDifVersicolorVirginica,StdSumVersicolorVirginica)


    #Setosa  - Virginica 
    SetVirginIndex = list(range(pdSize[0],pdSize[1])) + list(range(pdSize[2],pdSize[3]))
    xSetosaVirginica = np.array(IrisPanda.iloc[SetVirginIndex])
    xSetosaVirginica[:,:-1]
    MeanDifSetosaVirginica = np.array(setosaMean) - np.array(virginicaMean)
    MeanDifSetosaVirginica = np.multiply(MeanDifSetosaVirginica,MeanDifSetosaVirginica)

    StdSumSetosaVirginica = np.multiply(setosaStd,setosaStd) + np.multiply(virginicaStd,virginicaStd)

    ratioScoreSetosaVirginica = np.divide(MeanDifSetosaVirginica,StdSumSetosaVirginica)

    ratioScores = [ratioScoreSetosaVersicolor,ratioScoreVersicolorVirginica,ratioScoreSetosaVirginica]

    return ratioScores