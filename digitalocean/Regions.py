from .reqmethods import Req, Arrange

class Regions(Req, Arrange):
	slug = 'regions/'

	def __init__(self, token):
		self.setToken(token)

	def getRegions(self):
		data = self.get(self.slug)
		if 'id' in data:
			return data
		return self.arrangeData(data)