import json
import urllib2

import matplotlib.pyplot as plt

import numpy as np

url = "http://ppm15-demo.cisco.com:4440/ppm/rest/reports/Availability/Interfaces/Interface++Availability?FQDN=Node=ems7606b.cisco.com&outputType=jsonv2"

print ("pidiendo a: " + url)

reports = json.load(urllib2.urlopen(url))

data = reports["report"]["data"]

interfaces = []
interface_uptime = []

n_groups = 0

for i in data:
    n_groups += 1
    interfaces.append(i[0])
    interface_uptime.append( int(i[2]))
    if (n_groups == 10):
	break

print interface_uptime

index = np.arange(n_groups)
bar_width = 0.3

rects1 = plt.bar(index, interface_uptime, bar_width)

plt.xticks(index + bar_width, interfaces)
plt.xlabel('Intf')
plt.ylabel('% Uptime')
plt.title('Interface  Availability')

plt.show()
