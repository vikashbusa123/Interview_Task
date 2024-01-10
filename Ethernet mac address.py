#import psutil
import psutil

#get the Data 
for interface in psutil.net_if_addrs():
    #chech data using if statement
        if psutil.net_if_addrs()[interface][0].address:
            print("Your MAC Address Is:",psutil.net_if_addrs()[interface][0].address)
            break
           