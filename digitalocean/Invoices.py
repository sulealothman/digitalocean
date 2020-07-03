from .reqmethods import Req, Arrange

class Invoices(Req, Arrange):
	slug = 'customers/my/invoices'
	def __init__(self,token):
		self.setToken(token)

	def getAllInvoices(self):
		data = self.get(self.slug)
		if 'id' in data:
			return data
		return self.arrangeData(data)

	def getInvoiceByUuid(self, uuid):
		data = self.get(f'{self.slug}/{uuid}')
		if 'id' in data:
			return data
		return self.arrangeData(data)

	def getInvoiceSummary(self, uuid):
		data = self.get(f'{self.slug}/{uuid}/summary')
		if 'id' in data:
			return data
		return self.arrangeData(data)