from .reqmethods import Req, Arrange

class CDNEndpoints(Req, Arrange):
	slug = 'cdn/endpoints'

	def __init__(self, token):
		self.setToken(token)

	def storeCDN(self, origin, certId, customDomain, ttl):
		body = {"origin":f'{orign}', 'certificate_id' : f'{certId}', 'custom_domain' : f'{customDomain}', 'ttl' : f'{ttl}'}
		data = self.post(self.slug, body)
		return data

	def updateCDN(self, cdnId, body):
		data = self.put(f'{self.slug}/{cdnId}', body)
		return data

	def getAllCDN(self):
		data = self.get(self.slug)
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def getCDNById(self, cdnId):
		data = self.get(f'{self.slug}/{cdnId}')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def deleteCDN(self, cdnId):
		data = self.delete(f'{self.slug}/{cdnId}')
		return data

	def purgeCDN(self, cdnId, files):
		body = {"files": files}
		data = self.delete(f'{self.slug}/{cdnId}/cache', files)
		return data