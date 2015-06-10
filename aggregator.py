# from bottle import route, run, template

# @route('/create_pageview')
# def create_pageview():
# 	import time
# 	try:
# 		ts = time.time()
# 		f = open('pageviews.txt', 'a')
# 		f.write(str(float(ts)) + "\n")
# 		f.flush()
# 		f.close()
# 		return {"success": True}
# 	except:
# 		return {"success": False}

	

# run(host='localhost', port=3002)

import os, time, urllib2, urllib, json

try:
	line_count = open("last_read_line.txt", "r")
	last_read_line = int(line_count.readline())
	line_count.close()
except:
	last_read_line = 0

print "Starting from line: " + str(last_read_line)
while True:
	new_events_detected = False
	print("Processing...")
	
	try:
		events = open('aggregator_event_store.txt', 'r')
		for i, line in enumerate(events):
			if last_read_line <= i:
				print("New events found.")
				new_events_detected = True
				last_read_line = i + 1
				event_time, event_version, event = line.split(":")
				f = open('pageviews.txt', 'a')
				f.write(event_time + "\n")
				f.flush()
				f.close()
			
		events.close()
		line_count = open("last_read_line.txt", "w")
		line_count.write(str(last_read_line))
		line_count.flush()
		line_count.close()
	
		if new_events_detected:
			print("Pageviews created.")
			response = urllib2.urlopen("http://localhost:3003/pageview_created").read()
			data = json.loads(response)
		
			if data["success"]:
				print("Creating view with processed pageview.")
				response = urllib2.urlopen("http://localhost:3004/pageview_processed", data=urllib.urlencode(data["data"])).read()
	except:
		print("Event source not found.")

	time.sleep(1)

print("Service started.")


