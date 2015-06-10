from bottle import response, route, run, template

@route('/store/<version>/<event>')
def store(version, event):
	try:
		f = open('aggregator_event_store.txt', 'a')
		import time
		f.write(str(time.time()) + ":" + version + ":" + event + "\n")
		f.flush()
		f.close()
		return {"success": True}
	except:
		return {"success": False}

run(host='localhost', port=3006)