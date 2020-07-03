from .reqmethods import Req, Arrange

class Actions(Req, Arrange):
	slug = 'actions'

	def __init__(self, token):
		self.setToken(token)

	def getAllActions(self):
		data = self.get(f'{self.slug}')
		if 'id' in data:
			return data
		return self.arrangeData(data)

	def getAction(self, actionId):
		data = self.get(f'{self.slug}/{actionId}')
		if 'id' in data:
			return data
		return self.arrangeData(data)
