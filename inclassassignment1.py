lineList1 = [line.rstrip('\n') for line in open('//Users//arvinnatadihardja//Downloads//data//age')]
lineList2 = [line.rstrip('\n') for line in open('//Users//arvinnatadihardja//Downloads//data//city')]
lineList3 = [line.rstrip('\n') for line in open('//Users//arvinnatadihardja//Downloads//data//names')]
lineList4 = [line.rstrip('\n') for line in open('//Users//arvinnatadihardja//Downloads//data//phone')]
lineList5 = [line.rstrip('\n') for line in open('//Users//arvinnatadihardja//Downloads//data//state')]

myFile = open('InClass1.py', 'w')
# for i in range (len(lineList1)) :
for i in range(12) :
   myFile.write ( "age" , "," , "city", "," , "names" , "," , "phone" , "," , "state")
   myFile.write(lineList1[0], ", ", lineList2[0], "," , lineList3[0] , "," , lineList4 [0] , "," , lineList5[0])
   myFile.write(lineList1[1], ", ", lineList2[1], ",", lineList3[1], ",", lineList4[1], ",", lineList5[1])
   myFile.write(lineList1[2], ", ", lineList2[2], ",", lineList3[2], ",", lineList4[2], ",", lineList5[2])
   myFile.write(lineList1[3], ", ", lineList2[3], ",", lineList3[3], ",", lineList4[3], ",", lineList5[3])
   myFile.write(lineList1[4], ", ", lineList2[4], ",", lineList3[4], ",", lineList4[4], ",", lineList5[4])
   myFile.write(lineList1[5], ", ", lineList2[5], ",", lineList3[5], ",", lineList4[5], ",", lineList5[5])
   myFile.write(lineList1[6], ", ", lineList2[6], ",", lineList3[6], ",", lineList4[6], ",", lineList5[6])
   myFile.write(lineList1[7], ", ", lineList2[7], ",", lineList3[7], ",", lineList4[7], ",", lineList5[7])
   myFile.write(lineList1[8], ", ", lineList2[8], ",", lineList3[8], ",", lineList4[8], ",", lineList5[8])
   myFile.write(lineList1[9], ", ", lineList2[9], ",", lineList3[9], ",", lineList4[9], ",", lineList5[9])
   myFile.write(lineList1[10], ", ", lineList2[10], ",", lineList3[10], ",", lineList4[10], ",", lineList5[10])
   myFile.write(lineList1[11], ", ", lineList2[11], ",", lineList3[11], ",", lineList4[11], ",", lineList5[11])

   print (i)

   
