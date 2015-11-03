
def transform_Y2G(y2g):
	if y2g == 'G':
		return 0
	elif y2g in [None, ""]:
		return None
	else:
		return int(y2g)
		
def transform_down(d):
	if d == "" or d == None:
		return None
	else:
		return int(d)