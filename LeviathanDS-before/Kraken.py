#!/usr/bin/ env python

for x in range(0,10000):
	with open("data/cluster_test_{}.txt".format(x),'w') as fileout:
		fileout.write("Clustering Test File {}".format(x))

	fileout.close()
