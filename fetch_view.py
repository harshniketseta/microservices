from bottle import response, route, run, template

@route('/')
def results():
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
	import json
	
	try:
		f = open('by_minute.txt', 'r')
		return json.loads(f.read())
	except (ValueError, IOError):
		return {}


run(host='localhost', port=3005)