from .reqmethods import Req, Arrange

class DomainRecords(Req, Arrange):
	slug = 'domains'

	def __init__(self, token):
		self.setToken(token)

	def getAllDomainRecords(self, domain):
		data = self.get(f'{self.slug}/{domain}/records')
		if 'id' in data:
			return data
		return self.arrangeData(data)

	def storeDomainRecord(self, domain, tp, name, domainData, priority, port, ttl, weight, flags, tag):
		body ={"type":f'{tp}',"name":f'{name}',"data":f'{domainData}',"priority":f'{priority}',"port":f'{port}',"ttl": f'{ttl}',"weight":f'{weight}',"flags":f'{flags}',"tag":f'{tag}'}
		data = self.post(f'{self.slug}/{domain}/records', body)
		return data

	def updateDomainRecord(self, domain, recordId, body):
		data = self.put(f'{self.slug}/{domain}/records/{recordId}', body)
		return data

	def getDomainRecordById(self, domain, recordId):
		data = self.get(f'{self.slug}/{domain}/records/{recordId}')
		if 'id' in data:
			return data
	
		return self.arrangeData(data)

	def deleteDomainRecord(self, domain, recordId):
		data = self.delete(f'{self.slug}/{domain}/records/{recordId}')
		return data