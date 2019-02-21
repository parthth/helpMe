import urllib.parse, hashlib


def identicon_generation(email):
	default = "identicon"
	size = 40
	# construct the url
	gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(email.lower().encode('utf-8')).hexdigest() + "?"
	gravatar_url += urllib.parse.urlencode({'d': default, 's': str(size)})
	return gravatar_url