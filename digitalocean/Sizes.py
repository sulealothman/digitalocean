from .reqmethods import Req, Arrange

class Size(Req, Arrange):
	slug = 'sizes/'

	def __init__(self, token):
		self.setToken(token)

	def getSizes(self):
		data = self.get(self.slug)
		if 'id' in data:
			return data
	
		return self.arrangeData(data)