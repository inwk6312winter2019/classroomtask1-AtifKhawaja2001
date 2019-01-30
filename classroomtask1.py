import os
def travers(dirname):
	for name in os.list(dirname):
		path = os.path.join(dirname, name)

	if os.path.isfile(path):
		print(path)
	else:
		walk(path)
	
