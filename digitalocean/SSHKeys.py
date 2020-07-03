from .reqmethods import Req, Arrange

class SSHKeys(Req, Arrange):
	slug = 'account/keys'
	def __init__(self, token):
		self.setToken(token)

	def storeKey(self,keyName, key):
		body = {"name":f'{keyName}', 'public_key' : key}
		data = self.post(self.slug, body)
		return data

	def updateKeyName(self,keyId, keyName):
		body = {"name":f'{keyName}'}
		data = self.put(f'{self.slug}/{keyId}', body)
		return data

	def getKey(self, keyId):
		data = self.get(f'{self.slug}/{keyId}')
		return self.arrangeData(data)

	def getAllKeys(self):
		data = self.get(self.slug)
		return self.arrangeData(data)

	def deleteKey(self, keyId):
		data = self.delete(f'{self.slug}/{keyId}')
		return data