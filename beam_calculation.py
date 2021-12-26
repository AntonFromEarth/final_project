

class Case_1:
	def __init__(self, beam_length, force):
		self.beam_length = beam_length
		self.force = force
		self.reaction_force = None
		self.reaction_moment = None

		self.x_shear_force = []
		self.y_shear_force = []
		self.x_bend_moment = []
		self.y_bend_moment = []

	def calculation(self):
		self.reaction_force = self.force
		self.reaction_moment = self.force*self.beam_length

		#SHEAR FORCE CALCULATION
		self.x_shear_force = [i for i in range(self.beam_length+1)]
		#print(f"x_shear_force = {self.x_shear_force}, len = {len(self.x_shear_force)}") # MY CHECK
		self.y_shear_force = [self.reaction_force]*len(self.x_shear_force)
		#print(f"y_shear_force_1 = {self.y_shear_force}, len = {len(self.y_shear_force)}") # MY CHECK

		#BENDING MOMENT CALCULATION
		self.x_bend_moment = [i for i in range(self.beam_length+1)]
		#print(f"x_bend_moment = {self.x_bend_moment}, len = {len(self.x_bend_moment)}") # MY CHECK
		self.y_bend_moment = [round(-self.reaction_moment + i*self.reaction_force, 2) for i in self.x_bend_moment]
		#print(f"y_torque_1 = {self.y_bend_moment}, len = {len(self.y_bend_moment)}") # MY CHECK

		return self.x_shear_force, self.y_shear_force\
				, self.x_bend_moment, self.y_bend_moment


class Case_2:
	pass

class Case_3:
	pass

	
# MY CHECK
if __name__ == '__main__':
	c1 = Case_1(14, 10)
	c1.calculation()
	print("c1.calculation() = ", c1.calculation())
