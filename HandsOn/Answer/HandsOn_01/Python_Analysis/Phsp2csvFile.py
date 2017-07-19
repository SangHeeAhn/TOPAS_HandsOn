with open('Output.phsp','r') as f:
	data=f.readlines()

d = open('Hist.csv','w')
for line in data:
	Phsp = line.split()
	#print Phsp
	Energy = Phsp[5] # 0 1 2 3 4 5(Energy) ... 
	d.write(Energy+"\n")
d.close()
