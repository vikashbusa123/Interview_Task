#import gputil
import GPUtil

#get information of gpu from gputil
GPU_Details=GPUtil.getGPUs()

#Gett the name of gpu
GPU_Name=GPU_Details.name

print("Your GPU Name Is:",GPU_Name)