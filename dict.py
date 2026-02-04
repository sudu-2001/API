server = {
    "hostname": "server-01",
    "ip": "192.168.1.10",
    "status": "running"
}

server["status"] = "critical"

print (server["ip"])

print (server.keys())

print (server.values())

print (server.items())

server["uptime"] = "stopped"

del server["ip"]

print (server.items())

for key,value in server.items():

	print(key, ":" ,value)
