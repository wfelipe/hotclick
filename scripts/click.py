class Click:
	x = 0
	y = 0
	url = ''

	def __init__(self, attrs=None):
		for attr in attrs:
			if hasattr(self, attr):
				setattr(self, attr, attrs[attr])

if __name__ == "__main__":
	attrs = dict()
	attrs['x'] = 123
	attrs['y'] = 123
	attrs['url'] = 'http://www.uol.com.br/'

	clk = Click(attrs)
