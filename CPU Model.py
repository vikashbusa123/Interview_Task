#import cpuinfo
import cpuinfo

#Collect Information Of CPU From cpuinfo
cpu_details=cpuinfo.get_cpu_info()

cpu_model=cpu_details["brand_raw"]
print("Model Of Your CPU is:",cpu_model)