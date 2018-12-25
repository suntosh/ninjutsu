from actions.GetApps import GetApps
from actions.GetBlueprints import GetBlueprints

import sys

def main():
	if sys.version_info > (2, 7, 17):
		raise Exception ("Only python version 2.7.17 or lower supported")
	apis = { "1" : "Get Blueprints", "2" :"Get Apps"}
	var ="0"
	while True:
		for key in apis:
			print key," ",apis[key]
		var = raw_input("Please enter a number\n\r")
		if var not in apis.keys():
			print "Invalid Selection.. Exiting"
			break
		else:
			continue



if __name__ == "__main__":
	prints = GetApps()
	prints.fetch()
	#main()
