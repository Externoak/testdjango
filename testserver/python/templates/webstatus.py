<pre>
#!/usr/bin/env python
import sys
import httplib

site = raw_input("\nSite you wish too check. Ex: www.google.com: ")

for site_name in [site]:

    try:
        conn = httplib.HTTPConnection(site_name)
        conn.request("HEAD", "/")
        r1 = conn.getresponse()
        conn.close()
        website_return = r1.status
    
        if website_return == 200 or website_return == 301:
            print site_name + " is working as correctly"
           
        else:
            print "Problem with " + site_name
           
      
    except Exception as e:
        print "No response from server " + site_name
</pre>
