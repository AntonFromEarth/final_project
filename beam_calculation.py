import numpy as np

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
		#self.x_shear_force = [i for i in range(self.beam_length+1)]
		#[round(i, 2) for i in np.linspace(0, 100, 10)]
		self.x_shear_force = [round(i, 2) for i in np.linspace(0, self.beam_length, 50)]
		#print(f"x_shear_force = {self.x_shear_force}, len = {len(self.x_shear_force)}") # MY CHECK
		self.y_shear_force = [self.reaction_force]*len(self.x_shear_force) # в данном случае умножаем одиночный список на количество членов в списке Х и таким образов создаем сисок с одинаковыми числами в количестве как в списке Х
		#print(f"y_shear_force_1 = {self.y_shear_force}, len = {len(self.y_shear_force)}") # MY CHECK

		#BENDING MOMENT CALCULATION
		#self.x_bend_moment = [i for i in range(self.beam_length+1)]
		self.x_bend_moment = [round(i, 2) for i in np.linspace(0, self.beam_length, 50)]
		print(f"x_bend_moment = {self.x_bend_moment}, len = {len(self.x_bend_moment)}") # MY CHECK
		self.y_bend_moment = [round(-self.reaction_moment + i*self.reaction_force, 2) for i in self.x_bend_moment]
		print(f"y_torque_1 = {self.y_bend_moment}, len = {len(self.y_bend_moment)}") # MY CHECK

		return self.x_shear_force, self.y_shear_force\
				, self.x_bend_moment, self.y_bend_moment


class Case_2:
	pass

class Case_3:
	def __init__(self, l_beam_length, w_distributed_force):
		self.l_beam_length = l_beam_length
		self.w_distributed_force = w_distributed_force
		self.reaction_force = None
		self.reaction_moment = None

		self.x_shear_force = []
		self.y_shear_force = []
		self.x_bend_moment = []
		self.y_bend_moment = []

	def calculation(self):
		self.reaction_force = self.w_distributed_force * self.l_beam_length
		self.reaction_moment = self.reaction_force * self.l_beam_length / 2

		#SHEAR FORCE CALCULATION
		self.x_shear_force = [round(i, 2) for i in np.linspace(0, self.l_beam_length, 50)]
		print(f"x_shear_force = {self.x_shear_force}, len = {len(self.x_shear_force)}") # MY CHECK
		self.y_shear_force = [round(self.w_distributed_force * (self.l_beam_length - i), 2) for i in self.x_shear_force]
		print(f"y_shear_force = {self.y_shear_force}, len = {len(self.y_shear_force)}") # MY CHECK

		#BENDING MOMENT CALCULATION
		self.x_bend_moment = [round(i, 2) for i in np.linspace(0, self.l_beam_length, 50)]
		#print(f"x_bend_moment = {self.x_bend_moment}, len = {len(self.x_bend_moment)}") # MY CHECK
		self.y_bend_moment = [round(- self.w_distributed_force * pow((self.l_beam_length - i), 2) / 2, 2) for i in self.x_bend_moment]
		#print(f"y_bend_moment = {self.y_bend_moment}, len = {len(self.y_bend_moment)}") # MY CHECK

		return self.x_shear_force, self.y_shear_force\
				, self.x_bend_moment, self.y_bend_moment

class Case_4:
	pass

class Case_5:
	pass

class Case_6:
	def __init__(self, l_beam_length, a_distance, force):
		self.l_beam_length = l_beam_length
		self.force = force
		self.a_distance = a_distance
		self.reaction_force_left = None
		self.reaction_force_right = None

		self.x_shear_force = []
		self.y_shear_force = []
		self.x_bend_moment = []
		self.y_bend_moment = []

	def calculation(self):
		#REACTION FORCES CALCULATION
		self.reaction_force_left = round(self.force * (self.l_beam_length - self.a_distance)/self.l_beam_length, 2)
		self.reaction_force_right = round(self.force * self.a_distance / self.l_beam_length, 2)

		#SHEAR FORCE CALCULATION
		self.x_shear_force_1 = [i for i in range(self.a_distance+1)]
		#print(f"x_shear_force_1 = {self.x_shear_force_1}, len = {len(self.x_shear_force_1)}") # MY CHECK
		self.y_shear_force_1 = [self.reaction_force_left] * len(self.x_shear_force_1)
		##print(f"y_shear_force_1 = {self.y_shear_force_1}, len = {len(self.y_shear_force_1)}") # MY CHECK
		
		self.x_shear_force_2 = [i for i in range(self.a_distance, self.l_beam_length+1)]
		#print(f"x_shear_force_2 = {self.x_shear_force_2}, len = {len(self.x_shear_force_2)}")
		self.y_shear_force_2 = [self.reaction_force_left - self.force] * len(self.x_shear_force_2)
		#print(f"y_shear_force_2 = {self.y_shear_force_2}, len = {len(self.y_shear_force_2)}")
		
		self.x_shear_force = self.x_shear_force_1+self.x_shear_force_2
		#print(f"x_shear_force = {self.x_shear_force}, len = {len(self.x_shear_force)}")
		self.y_shear_force = self.y_shear_force_1+self.y_shear_force_2
		#print(f"y_shear_force = {self.y_shear_force}, len = {len(self.y_shear_force)}")


		#BENDING MOMENT CALCULATION
		self.x_bend_moment_1 = [i for i in range(self.a_distance+1)] 
		#print(f"x_bend_moment_1 = {self.x_bend_moment_1}, len = {len(self.x_bend_moment_1)}") # MY CHECK
		self.y_bend_moment_1 = [round(i*self.reaction_force_left, 2) for i in self.x_bend_moment_1]
		#print(f"y_bend_moment_1 = {self.y_bend_moment_1}, len = {len(self.y_bend_moment_1)}") # MY CHECK

		self.x_bend_moment_2 = [i for i in range(self.a_distance, self.l_beam_length+1)]
		#print(f"x_bend_moment_2 = {self.x_bend_moment_2}, len = {len(self.x_bend_moment_2)}")
		self.y_bend_moment_2 = [round((self.reaction_force_left - self.force) * i + self.force * self.a_distance) for i in self.x_bend_moment_2]
		#print(f"y_bend_moment_2 = {self.y_bend_moment_2}, len = {len(self.y_bend_moment_2)}")

		self.x_bend_moment = self.x_bend_moment_1 + self.x_bend_moment_2
		print(f"x_bend_moment = {self.x_bend_moment}, len = {len(self.x_bend_moment)}")
		self.y_bend_moment = self.y_bend_moment_1 + self.y_bend_moment_2
		print(f"y_bend_moment = {self.y_bend_moment}, len = {len(self.y_bend_moment)}")


		return self.x_shear_force, self.y_shear_force\
				, self.x_bend_moment, self.y_bend_moment


class Case_7:
	pass


# MY CHECK
if __name__ == '__main__':
	'''
	c1 = Case_1(14, 10)
	c1.calculation()
	print("c1.calculation() = ", c1.calculation())
	'''

	c3 = Case_3(10, 2)
	c3.calculation()
	#print("c3.calculation() = ", c3.calculation())
	

	'''
	c6 = Case_6(10, 4, 14)
	c6.calculation()
	print("c1.calculation() = ", c6.calculation())
	'''
