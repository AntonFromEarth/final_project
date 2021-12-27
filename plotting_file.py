import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import beam_calculation as bc

class GraphPloter:

	def __init__(self, x_sh_force=None, y_sh_force=None, x_bend_moment=None, y_bend_moment=None):
		self.x_sh_force = x_sh_force
		self.y_sh_force = y_sh_force 
		self.x_bend_moment = x_bend_moment 
		self.y_bend_moment = y_bend_moment

	'''
	def plot_tables(self):

		plt.subplot(2, 1, 1)
		plt.title("SHARE FORCE", fontsize=16, fontweight='bold', color='blue')
		plt.xlabel('Lenght', fontsize=14,color='blue')
		plt.ylabel('Share force [N]', fontsize=14,color='blue')
		plt.grid()
		#plt.legend()
		plt.plot(self.x_sh_force, self.y_sh_force, label='Share Force', linewidth=1)
		plt.fill_between(self.x_sh_force, self.y_sh_force, color = 'green') #заливка графика
		plt.legend()

		plt.subplot(2, 1, 2)
		plt.title("Bending", fontsize=16, fontweight='bold', color='red')
		plt.xlabel('Lenght', fontsize=14,color='red')
		plt.ylabel('Bending moment [N*m]', fontsize=14,color='red')
		plt.grid()
		#plt.legend()
		plt.plot(self.x_bend_moment, self.y_bend_moment, '--r', label='Torque', linewidth=1)
		#"легенда" или перечисление имен графиков в отдельном окошке. важно поставить его после графиков
		plt.fill_between(self.x_bend_moment, self.y_bend_moment, color = 'red') #заливка графика
		plt.legend()
		# отображение графика

		#изменение фона графика
		#ax = plt.gca()
		#ax.set_facecolor('green')

		plt.show()

	'''

	# MAIN!
	def plot_tables_wind(self, window):


		fig1 = Figure(figsize=(6, 2.4), dpi=100)
		fig2 = Figure(figsize=(6, 2.4), dpi=100)
		
		ax1 = fig1.add_subplot()
		ax1.set_title('Shear Force')
		ax1.set_xlabel("beam length [m]")
		ax1.set_ylabel("Force [N]")
		#ax1.set_xlim([-len(self.x_sh_force), len(self.x_sh_force)]) # задание и ограничение диапазона значений графика
		ax1.set_ylim([-len(self.y_sh_force), len(self.y_sh_force)*1.4])
		ax1.plot(self.x_sh_force, self.y_sh_force, linewidth=3)
		#ax1.stem(self.x_sh_force, self.y_sh_force, linefmt="g-", markerfmt=".", bottom=0) # заливка вертикальными линиями
		#ax1.fill_between(self.x_sh_force, self.y_sh_force, hatch = '||')
		ax1.fill_between(self.x_sh_force, self.y_sh_force, color = 'green') #заливка графика
		ax1.grid(True)
		fig1.tight_layout() # раздвигает графики что бы не накладывлись друг на друга


		ax2 = fig2.add_subplot()
		ax2.set_title('Bending Moment')
		ax2.set_xlabel("beam length [m]")
		ax2.set_ylabel("Moment [Nm]")
		ax2.plot(self.x_bend_moment, self.y_bend_moment)
		ax2.fill_between(self.x_bend_moment, self.y_bend_moment, color = 'red') #заливка графика
		fig2.tight_layout() # 

		canvas1 = FigureCanvasTkAgg(fig1, master=window)  # A tk.DrawingArea.
		canvas2 = FigureCanvasTkAgg(fig2, master=window)
		
		#canvas1.draw()
		#canvas2.draw()

		#canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
		canvas1.get_tk_widget().grid(row=4, column=0, stick='we', columnspan = 3)
		canvas2.get_tk_widget().grid(row=5, column=0, stick='we', columnspan = 3)

	def plotter_windows(self, window):
		pass


'''
#def plot_tables(x_shear_force, y_shear_force, x_torque, y_torque):
def plot_tables(x_shear_force, y_shear_force, x_torque, y_torque):	
	
	plt.subplot(2, 1, 1)
	plt.title("SHARE FORCE", fontsize=16, fontweight='bold', color='blue')
	plt.xlabel('Lenght', fontsize=14,color='blue')
	plt.ylabel('Share force [N]', fontsize=14,color='blue')
	plt.grid()
	#plt.legend()
	plt.plot(x_shear_force, y_shear_force, label='Share Force', linewidth=1)
	plt.fill_between(x_shear_force, y_shear_force, color = 'green') #заливка графика
	plt.legend()

	plt.subplot(2, 1, 2)
	plt.title("Bending", fontsize=16, fontweight='bold', color='red')
	plt.xlabel('Lenght', fontsize=14,color='red')
	plt.ylabel('Bending moment [N*m]', fontsize=14,color='red')
	plt.grid()
	#plt.legend()
	plt.plot(x_torque, y_torque, '--r', label='Torque', linewidth=1)
	#"легенда" или перечисление имен графиков в отдельном окошке. важно поставить его после графиков
	plt.fill_between(x_torque, y_torque, color = 'red') #заливка графика
	plt.legend()
	# отображение графика

	#изменение фона графика
	#ax = plt.gca()
	#ax.set_facecolor('green')

	plt.show()

'''

if __name__ == '__main__':
	c1 = bc.Case_1(beam_length = 14, force = 100)
	c1.calculation()
	print("c1.calculation() = ", c1.calculation())
	#plot_tables(*c1.calculation())

	gp1 = GraphPloter(*c1.calculation())
	gp1.plot_tables()
