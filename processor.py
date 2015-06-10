from bottle import route, run, template

@route('/pageview_created')
def process():
	
	data_by_minute = {}
	
	import time
	current_min = time.localtime(time.time()).tm_min
	with open('pageviews.txt') as views:
	   for line in views:   	
	   	min = time.localtime(float(line)).tm_min
	   	if current_min > min:
			min = str(min)
		   	if not min in data_by_minute:
		   		data_by_minute[min] = 0
	   		data_by_minute[min] += 1
	
	return {"success": True, "data": data_by_minute}

run(host='localhost', port=3003)