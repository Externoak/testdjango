<pre>
import os
import sys
ans=True

while ans:

    print(""" 
SYSADMIN Usefull scripts in python 
   """)


    print ("""
    1. Nmap script
    2. SpeedTest 
    3. Pingcheck
    4. Webstatus
    8. Exit/Quit
    9. Dependencies (INSTALL IF FIRST TIME!)
    """)
    ans=raw_input("What would you like to do? ") 
    if ans=="1": 
      print("\n Running Nmap script")
      os.system("\n python map.py")
      print("\n Nmap has finished")

    elif ans=="2":
      print("\n Running Speedtest") 
      os.system("\n python speedtest.py")
      print("\n Speedtest has finished")

    elif ans=="3":
      print("\n Network Pingcheck")
      os.system("\n python pingcheck.py")
      print("\n Pingcheck has finished") 

    elif ans=="4":
      print("\n Running WebStatus")
      os.system("\n python webstatus.py")
      print("\n WebStatus has finished") 

    elif ans=="8":
      print("\n Goodbye")
      sys.exit() 

    elif ans=="9":
      print("\n Dependencies")
      os.system("\n python dependencies.py")
      print("\n All dependencies installed correctly") 

    elif ans !="":
      print("\n Not Valid Choice Try again") 

</pre>
