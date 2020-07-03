from .reqmethods import Req, Arrange

class Billing(Req, Arrange):
	slug = 'customers/my/billing_history'
	def __init__(self,token):
		self.setToken(token)

	def getBilling(self):
		data = self.get(self.slug)
		if 'id' in data:
			return data
		return self.arrangeData(data)