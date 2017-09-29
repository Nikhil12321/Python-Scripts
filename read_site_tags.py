# Reads website's source code and does stuff
# according to <td> tag



from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class Parser(HTMLParser):

	def __init__(self):
		HTMLParser.__init__(self)
		self.inTd = 0
		self.element = 0
		self.desc_save = ""
		self.desc_or_data = 0
		self.code_save = 0
		self.write_to_file = open('data', 'wr')

	def handle_starttag(self, tag, attributes):

		if tag == "td":
			self.inTd = 1

	def handle_endtag(self, tag):

		if tag == "td":
			self.inTd = 0

	def handle_data(self, data):

		if self.inTd == 1:
			
			if self.desc_or_data == 1:
				if self.desc_save == "Code":
					self.write_to_file.write("(\""+str(data)+"\", ")
					self.code_save = str(data)
				elif self.desc_save == "Description":
					self.write_to_file.write("\""+str(data)+"\", ")
				elif self.desc_save == "PKG/Box":
					self.write_to_file.write(str(data)+", ")
				elif self.desc_save == "MRP (Per Pc.)":
					self.write_to_file.write(str(data)+"f , R.drawable.wisdom_"+self.code_save+")\n")

				self.desc_or_data = 0

			# Not a description
			if data == "Code":
				self.desc_save = data
				self.desc_or_data = 1
			elif data == "Description":
				self.desc_save = data
				self.desc_or_data = 1
			elif data == "MRP (Per Pc.)":
				self.desc_save = data
				self.desc_or_data = 1
			elif data == "PKG/Box":
				self.desc_save = data
				self.desc_or_data = 1




#Description MRP (Per Pc.) Code PKG/Box
f = open('toparse', 'r')
s = f.read()
parser = Parser()
parser.feed(s)