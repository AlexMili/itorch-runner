# coding: utf-8
import sys, getopt
import os
import json
import datetime
from subprocess import call

current_date = str(datetime.datetime.now()).replace(' ', '!')
output_file_name = './tmp_itorch_exec-'+current_date+'.lua'

if __name__ == "__main__":
	if len(sys.argv) > 0:
		input_file = open(sys.argv[1], 'r')


		with input_file as json_file:
		    json_data = json.load(json_file)
		input_file.close()

		sources = []

		for item in json_data['cells']:
		    if item['cell_type'] == 'code' and len(item['source']) > 0:
		    	item['source'][-1] = item['source'][-1]+'\n'
		        sources = sources + item['source']

		output_file = open(output_file_name, 'w')
		output_file.writelines(sources)
		output_file.close()

		call(["th", output_file_name])

		os.remove(output_file_name)
