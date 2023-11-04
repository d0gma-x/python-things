class Convert:
	def __init__(self):
		self.temp = ' '
		self.mass = ' '
		self.speed = ' '
		
	def dataConv(self):
		self.select_conv = str(input('select type of conv (temp, mass or speed): ')).lower()
		if self.select_conv == 'temp':
			self.temp = int(input('input cent to farhen: '))
			self.cent_to_ferhen = self.temp*1.8+32
			print('is {} farhen degrees'.format(self.cent_to_ferhen))
			print('-----------------------------')

		elif self.select_conv == 'mass':
			self.mass = int(input('input kg to lb: '))
			self.kg_to_lb = self.mass*2.205
			print('is {} lb'.format(self.kg_to_lb))
			print('-----------------------------')
			
		elif self.select_conv == 'speed':
			self.speed = int(input('input mi to kl: '))
			self.mi_to_kl = self.speed*1.609
			print('is {} k'.format(self.mi_to_kl))
			print('-----------------------------')
			
		else:
			print('not valid option')
			print('-----------------------------')
			
	def convertCont(self):
		while True:
			self.cont = input('Otro??? y/n >>> ').lower()
			print('-----------------------------')
			if self.cont == 'n':
				break
			else:
				self.dataConv()
				
if __name__=='__main__':
	conv = Convert()
	conv.dataConv()
	conv.convertCont()