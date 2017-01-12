<pre>
 #!/usr/bin/env python
import nmap                        
nm = nmap.PortScanner()             
nm.scan('127.0.0.1', '1-9999')      
nm.command_line()                   
nm.scaninfo()                       
nm.all_hosts()                      
nm['127.0.0.1'].hostname()          
nm['127.0.0.1'].hostnames()         
                                    
nm['127.0.0.1'].hostname()          
nm['127.0.0.1'].state()             
nm['127.0.0.1'].all_protocols()     
nm['127.0.0.1']['tcp'].keys()       
nm['127.0.0.1'].all_tcp()           
nm['127.0.0.1'].all_udp()           
nm['127.0.0.1'].all_ip()            
nm['127.0.0.1'].all_sctp()          
nm['127.0.0.1'].has_tcp(22)         
nm['127.0.0.1']['tcp'][22]          
nm['127.0.0.1'].tcp(22)             
nm['127.0.0.1']['tcp'][22]['state'] 


# a more usefull example :
for host in nm.all_hosts():
    print('--------Open Ports on LocalHost-------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())

    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)

        lport = nm[host][proto].keys()
        lport.sort()
        for port in lport:
            print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

print('---------------Specify Network Ex:192.168.1.0/24-------------------')

ip = raw_input("Network range: ")

print ("Trying with:" + ip)

print('-------------Scanning specified networking-------------------------')
nm.scan(hosts= ip , arguments='-n -sP -PE -PA21,23,80,3389')
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
for host, status in hosts_list:
    print('{0}:{1}'.format(host, status))

print ('-----------------------Finished NMAP-------------------------------')

</pre>
