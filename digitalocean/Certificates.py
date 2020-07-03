from .reqmethods import Req, Arrange

class Certificates(Req, Arrange):
	slug = 'certificates'
	def __init__(self, token):
		self.setToken(token)

	def storeCertificate(self,body):
		data = self.post(self.slug, body)
		return data

	def getCertificate(self, certId):
		data = self.get(f'{self.slug}/{certId}')
		return self.arrangeData(data)

	def getAllCertificates(self):
		data = self.get(self.slug)
		return self.arrangeData(data)

	def deleteCertificate(self, certId):
		data = self.delete(f'{self.slug}/{certId}')
		return data