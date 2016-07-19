# dkdkdkdk
import re

ip = raw_input("input your Ip:")
print "hello"
print repr(ip)
def checkip(ip):
    print ip  
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')  
    print ip
    if p.match(ip):
        print "yes"
        return True    
    else:
        print "no"       
        return False
checkip(ip)
