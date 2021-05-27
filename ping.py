import os

with open("/tmp/ip_list") as file:
	dump=file.read()
	dump=dump.splitlines()

for ip in dump:
	res=os.popen(f"ping -c5 {ip}").read()
	f=open("/tmp/output.txt","a")
	f.write(str(res)+"\n")
	f.close()
	
