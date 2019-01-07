---------------------------------
### PROJECT: WEB SITE BLOCKER ###
---------------------------------
import time
from datetime import datetime as dt

#setting up the hosts path, local IP and blocked website list
#host file should be copied from "C:\Windows\System32\drivers\etc" to script file folder due to aministrative rights issues
hosts_temp = r"C:\Users\Nikola\Desktop\python\3website_blocker\hosts"
microsoft_hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirected_IP = "127.0.0.1"
blocked_website_list = ["www.facebook.com", "facebook.com", "www.instagram.com", "instagram.com"]

while True:
    #comparing if the datetime.now is between 8h-16h
    if dt(dt.now().year, dt.now().month, dt.now().day, 1) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        #Working hours:8-16
        #opening a host file in read and append mode
        with open(microsoft_hosts_path, "r+") as file:
            host_content = file.read()
            for website in blocked_website_list:
                if website in host_content:
                    pass
                else:
                    file.write(redirected_IP + " " + website + "\n")
    else:
        #Fun hours
        #opening a host file in read and append mode
        with open(microsoft_hosts_path, "r+") as file:
            host_content = file.readlines()
            #setting the pointer at the beggining of the file
            file.seek(0)
            for line in host_content:
                #rewriting the lines in file if the line doesn't have a website in it
                if not any(website in line for website in blocked_website_list):
                    file.write(line)
                #truncate function is dropping everything below the current pointer
                file.truncate()
    time.sleep(5)
