from .reqmethods import Req, Arrange

class Snapshots(Req, Arrange):
	slug = 'snapshots'
	def __init__(self, token):
		self.setToken(token)

	def getAllSnapshots(self):
		data = self.get(self.slug)
		return self.arrangeData(data)

	def getAllSnapshotsDroplet(self):
		data = self.get(f'{self.slug}?resource_type=droplet')
		return self.arrangeData(data)

	def getAllSnapshotsVolumes(self):
		data = self.get(f'{self.slug}?resource_type=volume')
		return self.arrangeData(data)

	def getSnapshotById(self, snapshotId):
		data = self.get(f'{self.slug}/{snapshotId}')
		return self.arrangeData(data)

	def deleteSnapshotById(self, snapshotId):
		data = self.delete(f'{self.slug}/{snapshotId}')
		return data