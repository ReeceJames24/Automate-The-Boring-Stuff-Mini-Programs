# folder byte size counter

import os

totalByteSize = 0
print('Input absolute path of directory')
directoryAbsPath = str(input())

for file in os.listdir(directoryAbsPath):
    if not os.path.isfile(os.path.join(directoryAbsPath, file)):
        continue  #note that continue is used to skip to next iteration of loop
    totalByteSize = totalByteSize + os.path.getsize(os.path.join(directoryAbsPath, file))


directoryName = os.path.basename(directoryAbsPath)
print(str(directoryName) + ' has ' + str(totalByteSize) + ' bytes.')


    

                
    
