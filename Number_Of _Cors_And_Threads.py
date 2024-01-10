#import psutil
import psutil

#Get Number Of Cores From psutil
Cores=psutil.cpu_count()

#print the number of cores
print(Cores)