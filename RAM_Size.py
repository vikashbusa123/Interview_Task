#import psutil
import psutil

#get Memory Details from psutil
Memory=psutil.virtual_memory()

#get Information of total memory

Memory_Size_In_Bytes=Memory.total

#convert memory size in GB
Memory_Size=Memory_Size_In_Bytes/1000000000
print("Your RAM Size is:",Memory_Size)
