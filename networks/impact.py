# Reference: https://integrations.impact.com/impact-publisher/reference/authentication

from .network import Network

class Impact(Network):

	def check_connection(self):
		return True
