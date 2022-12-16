#! /usr/bin/python

import time
from optparse import OptionParser
import os
import sys

def make_list(i, d_dic):
	with open(i) as ir:
		for iLine in ir:
			i_chr = iLine.split("\t")[5]
			i_pos = iLine.split("\t")[6]
			i_name = iLine.split("\t")[0]
			i_pos = int(i_pos)

			for i in range(i_pos-151,i_pos+150):
				header = i_chr + "_" + str(i)

				try:
					d_dic[header]
					o_write.write(i_name+"\t"+i_chr+"\t"+str(format(i,','))+"\t"+d_dic[header]+"\n")
				except:
					continue
	o_write.close()

def make_dic(d):
	d_list=[]
	d_dic={}
	with open(d) as dr:
		print ('\033[91m'+"########## Start ##########")
		for dLine in dr:
			dLine = dLine.strip()
			d_chr = dLine.split("\t")[0]
			d_pos = dLine.split("\t")[1]
			d_depth = dLine.split("\t")[2]
			d_header = (d_chr+"_"+d_pos)
			d_dic[d_header]=d_depth
	return	d_dic

if __name__ == '__main__':
	if len(sys.argv) <= 1:
		print (	"  Usage: TAPE-seq_flanking_depth.py -h or --h \n\n  Created by Hyun Oh Lee in PHYZEN, 2021-08-12")
		sys.exit()

	use = "%prog -d [depth file] -r [Cas-OFfinder results] -o out.txt"
	parser = OptionParser(usage = use)
	parser.add_option("-d", dest = "depth", help = "depth")
	parser.add_option("-i", dest = "offinder", help = "cas-Offinder results")
	parser.add_option("-o", dest = "output", help = "output fie")
	options, args = parser.parse_args()

	d = options.depth
	i = options.offinder
	o = options.output
	o_write = open(o, 'w')
	o_write.write("Name\tChr.\tPosition\tDepth\n")

	if d == None:
		print ("input depth")
		sys.exit()
	if i == None:
		print ("input cas-Offinder results")
		sys.exit()
	start = time.time()
	d_dic = make_dic(d)
	make_list(i,d_dic)
	end = time.time()
	time_total = end - start
	time_sec = time_total % 60
	time_min = int(time_total / 60 % 60)

	print ("########## Running time: "+ str(time_min) + "m "+ str(round(time_sec, 0))+"s ##########")
	print ("########## Finished ##########")
