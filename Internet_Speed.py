#import speedtest
import speedtest

#Create Variable For Speed
st=speedtest.Speedtest()

option=int(input('''what speed you want to test:
                 (1)Download Speed
                 (2)Upload Speed
                 (3)Ping
                 Your Choice:'''))

#Get Speed according to choice
if option==1:
    print("Your Downloading Speed Is:",st.download())
elif option==2 :
    print("Your uploading Speed Is:",st.upload())
elif option==3:
    servernames=[]
    st.get_servers(servernames)
    print("Your Ping speed Is:",st.results.ping)
else:
    print("Please Enter The Correct Choice!")
    