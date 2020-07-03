from .reqmethods import Req, Arrange

class FloatingIPs(Req, Arrange):
	slug = 'floating_ips'

	def __init__(self, token):
		self.setToken(token)

	def getAllFloatingIPs(self):
		data = self.get(self.slug)
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def assignDropletFloatingIPs(self,dropletId, key):
		body = {"droplet_id":f'{dropletId}'}
		data = self.post(self.slug, body)
		return data

	def assignRegionFloatingIPs(self,region, key):
		body = {"region":f'{region}'}
		data = self.post(self.slug, body)
		return data

	def getFloatingIPsByIp(self, floatIp):
		data = self.get(f'{self.slug}/{floatIp}')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def deleteFloatingIPs(self, floatIp):
		data = self.delete(f'{self.slug}/{floatIp}')
		return data