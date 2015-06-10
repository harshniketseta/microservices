from bottle import response, route, request, run

@route('/pageview_processed', method='POST')
def pageview_processed():

	try:
		f = open('by_minute.txt', 'w')
		import json
		data_by_minute = {}
		for minute in request.forms:
			data_by_minute[minute] = request.forms[minute]
		f.write(json.dumps(data_by_minute))
		f.flush()
		f.close()
		return {"success": True}
	except:
		return {"success": False}

run(host='localhost', port=3004)