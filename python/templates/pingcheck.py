<pre>
import subprocess
import os

range = raw_input("Network range: ")
with open(os.devnull, "wb") as limbo:
        for n in xrange(1, 254):
               lista = range.split(".")
               lista[3] = str(n)
               ipfinal = ".".join(lista)
               result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ipfinal],
                       stdout=limbo, stderr=limbo).wait()
               if result:
                       print ipfinal, "inactive"
               else:
                       print ipfinal, "active"
</pre>
