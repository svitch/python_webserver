def wsgi_application(environ, start_response):
	status = '200 OK'
	headers = [
		('Content-Type', 'text/plain')
	]
	
	body = []
	for key in env['QUERY_STRING'].split('&'):
		data = key + "\n"
		body.append(data)

	start_response(status, headers)
	return [body]
