
class filterList(object):
	
	def __init__(self, paramName, list_toBeIncluded, list_toBeExcluded):

		self.paramName = paramName
		self.list_toBeIncluded = list_toBeIncluded
		self.list_toBeExcluded = list_toBeExcluded


	def transferItem(self, item_ToBeTransfered, dest_list):
		
		if dest_list == "included":

			self.list_toBeExcluded.remove(item_ToBeTransfered)
			self.list_toBeIncluded.append(item_ToBeTransfered)

		elif dest_list == "excluded":

			self.list_toBeIncluded.remove(item_ToBeTransfered)
			self.list_toBeExcluded.append(item_ToBeTransfered)

		else:

			raise RuntimeError("Please select 'included' or 'excluded' as the dest_list parameter")