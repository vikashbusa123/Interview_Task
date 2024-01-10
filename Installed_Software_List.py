#import subprocess
import subprocess


#Get Data Using Subprocess
Data=subprocess.check_output(['wmic','product','get','name'])

#convert Data Into String By String Casting
a=str(Data)


#get The data from variable "a" using for loop
try:
    for i in range(len(a)):
        print(a.split("\\r\\r\\n")[6:][i])
except IndexError as e:
    print("All Done")