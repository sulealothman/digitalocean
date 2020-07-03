from .reqmethods import Req, Arrange

class VPCs(Req, Arrange):
	slug = 'vpcs'
	def __init__(self, token):
		self.setToken(token)

	def storeVPC(self, vpcName, region, ipRange):
		body = {"name":f'{vpcName}', 'region' : f'{region}', 'ip_range': f'{ipRange}'}
		data = self.post(self.slug, body)
		return data

	def updateVPC(self, vpcId, vpcName, vpcDesc):
		body = {"name":f'{keyName}', 'name': f'{vpcName}', 'description': f'{vpcDesc}'}
		data = self.put(f'{self.slug}/{vpcId}', body)
		return data

	def updatePartVPC(self, vpcId, keyName, value):
		body = {f'{keyName}' : f'{value}'}
		data = self.patch(f'{self.slug}/{vpcId}', body)
		return data

	def getVPC(self, vpcId):
		data = self.get(f'{self.slug}/{vpcId}')
		return self.arrangeData(data)

	def getVPCMembers(self, vpcId):
		data = self.get(f'{self.slug}/{vpcId}/members')
		return self.arrangeData(data)

	def getAllVPCs(self):
		data = self.get(self.slug)
		return self.arrangeData(data)

	def deleteVPC(self, vpcId):
		data = self.delete(f'{self.slug}/{vpcId}')
		return data