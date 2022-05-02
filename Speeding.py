#Cormac Wilson
#110603274
#12 02 22
#Project 1 - Speeding

def readExistingCarData():
  with open('carData.csv','r') as existingCarData:
    for each in existingCarData.readlines():
      each = each[0:-1]
      temp = each.split(',')
      carAges.append(int(temp[0]))
      carSpeedResults.append(int(temp[1]))
  existingCarData.close()
# This function will read the existing car data held in file
# The data will be stored in parallel arrays ages[] and carSpeedResults[]
  return carAges, carSpeedResults

def gatherData(carAges, carSpeedResults):
# This function will loop asking the user to enter the car data
# until the value 999 is entered and append the data to the arrays
# age[] and carSpeedResults[]

  inputValue = 0
  while inputValue != 999:
    inputValue = int(input("Please enter in the cars age: "))
    if inputValue != 999:
      carAges.append(inputValue)
      carSpeed = int(input("Please enter in the car speeding indicator: "))
      carSpeedResults.append(carSpeed)
    
  return carAges, carSpeedResults

def carsPercentages(carSpeedResults):
# This function will calculate the percentage of cars speeding (1) and
# the percentage of cars not speeding (0)
  countSpeeding = 0
  for index in range(len(carSpeedResults)):
    if carSpeedResults[index] == 1:
      countSpeeding = countSpeeding + 1

  pSpeeding = countSpeeding / len(carSpeedResults)*100
  pNotSpeeding = 100 - pSpeeding
  
  return pSpeeding, pNotSpeeding

def countSpeedingOccur(carSpeedResults):
  count = 0
  for index in range(len(carSpeedResults)):
    if carSpeedResults[index] == 1:
      count = count + 1

  return count

#Main program
carAges = []
carSpeedResults = []
pSpeeding = 0
pNotSpeeding = 0
countCarsSpeeding = 0

carAges, carSpeedResults = readExistingCarData()
carAges, carSpeedResults = gatherData(carAges, carSpeedResults)
pSpeeding, pNotSpeeding = carsPercentages(carSpeedResults)
print(round(pSpeeding,2), round(pNotSpeeding,2))
countCarsSpeeding = countSpeedingOccur(carSpeedResults)
print("There were",countCarsSpeeding, "occurrences of cars speeding.")