<pre>
import netifaces

interfaces = netifaces.interfaces()
print ""
print ("All interfaces in this computer:") 
print ""
print interfaces	
print ""
inter = raw_input("Name of interface: ")
x = netifaces.ifaddresses(inter)
y = x[netifaces.AF_INET]
print ""
print y 
print ""

</pre>