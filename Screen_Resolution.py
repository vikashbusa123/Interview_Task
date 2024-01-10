#import win32api
import win32api
from win32api import GetSystemMetrics


#Create variable


screen_width=GetSystemMetrics(0)
scren_height=GetSystemMetrics(1)

print("Your Screen's Width is:",screen_width)
print("Your screen's Height is:",scren_height)