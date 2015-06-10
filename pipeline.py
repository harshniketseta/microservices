from bottle import response, route, run, template

@route('/do_pageview.js')
def pageview():
	import json
	import urllib2, urllib

	response = urllib2.urlopen("http://localhost:3006/store/v1/create_pageview").read()
	data = json.loads(response)

run(host='localhost', port=3001)