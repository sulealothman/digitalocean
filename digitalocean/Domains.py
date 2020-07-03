from .reqmethods import Req, Arrange

class Domains(Req, Arrange):
	slug = 'domains'
	def __init__(self, token):
		self.setToken(token)

	def storeDomain(self, domain, ip_address):
		body = {"name":f'{domain}', 'ip_address': f'{ip_address}'}
		data = self.post(self.slug, body)
		return data

	def getDomain(self, domain):
		data = self.get(f'{self.slug}/{domain}')
		if 'id' in data:
			return data
		return self.arrangeData(data)

	def getAllDomains(self):
		data = self.get(self.slug)
		if 'id' in data:
			return data

		return self.arrangeData(data)

	def deleteDomain(self, domain):
		data = self.delete(f'{self.slug}/{domain}')
		return data