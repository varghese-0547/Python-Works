'''
##print('Do you want to shutdon the system')
##Ans=input()
##if 'yes' in Ans:
##    import os
##    os.system('shutdown /s /t 1')
##elif 'Yes' in Ans:
##    import os
##    os.system('shutdown /s /t 1')
##elif 'Yah' in Ans:
##    import os
##    os.system('shutdown /s /t 1')
##elif 'yah' in Ans:
##    import os
##    os.system('shutdown /s /t 1')
##elif 'Ya' in Ans:
##    import os
##    os.system('shutdown /s /t 1')
##elif 'ya' in Ans:
##    import os
##    os.system('shutdown /s /t 1')
##elif 'Hmm' in Ans:
##    import os
##    os.system('shutdown /s /t 1')
##elif 'Yes' in Ans:
##    import os
##    os.system('shutdown /s /t 1')
##elif 'hmm' in Ans:
##    import os
##    os.system('shutdown /s /t 1')
##else :
##    print ("I think you don't want to shutdown the system")
'''




import os
import time

# Wait for 3 minutes (180 seconds)
time.sleep(170)

# Shutdown the system
os.system("shutdown /s /t 1")  # For Windows

# For Linux or macOS, use this instead:
# os.system("shutdown now")












