from .reqmethods import Req, Arrange

class Account(Req, Arrange):
	slug = 'account'
	def __init__(self, token):
		self.setToken(token)

	def account(self):
		data = self.get(self.slug)
		if 'id' in data:
			return data
		return self.arrangeData(data)
