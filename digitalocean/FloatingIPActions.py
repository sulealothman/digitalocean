from .reqmethods import Req, Arrange

class FloatingIPActions(Req, Arrange):
	slug = 'floating_ips'

	def __init__(self, token):
		self.setToken(token)

	def getAllFloatingIPActions(self, floatIp):
		data = self.get(f'{self.slug}/{floatIp}/actions')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def assignFloatingIP(self,floatIp):
		body = {"type":'assign'}
		data = self.post(f'{self.slug}/{floatIp}/actions', body)
		return data

	def unassignFloatingIP(self,floatIp):
		body = {"type":'unassign'}
		data = self.post(f'{self.slug}/{floatIp}/actions', body)
		return data

	def getFloatingIPActionById(self, floatIp, actionId):
		data = self.get(f'{self.slug}/{floatIp}/actions/{actionId}')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)
