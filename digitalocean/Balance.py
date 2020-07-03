from .reqmethods import Req, Arrange

class Balance(Req, Arrange):
	slug = 'customers/my/balance'
	def __init__(self,token):
		self.setToken(token)

	def getBalance(self):
		data = self.get(self.slug)
		if 'id' in data:
			return data
		return self.arrangeData(data)