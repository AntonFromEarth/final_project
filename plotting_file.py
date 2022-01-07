import matplotlib.pyplot as plt
import matplotlib.ticker as ticker # модуль управления "тиками" (делениями осей)
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import beam_calculation as bc

class GraphPloter:

	def __init__(self, x_sh_force=None, y_sh_force=None, x_bend_moment=None, y_bend_moment=None):
		self.x_sh_force = x_sh_force
		self.y_sh_force = y_sh_force 
		self.x_bend_moment = x_bend_moment 
		self.y_bend_moment = y_bend_moment


	# MAIN!
	def plot_tables_wind(self, window):


		fig1 = Figure(figsize=(6, 2.4), dpi=100)
		fig2 = Figure(figsize=(6, 2.4), dpi=100)
		
		# постройка графика силы
		ax1 = fig1.add_subplot()
		ax1.set_title('Shear Force')
		ax1.set_xlabel("Beam length [m]")
		ax1.set_ylabel("Force [N]")
		#ax1.set_xlim([-len(self.x_sh_force), len(self.x_sh_force)]) # задание и ограничение диапазона значений графика
		#ax1.set_ylim([-len(self.y_sh_force)*1.1, len(self.y_sh_force)*1.1])

		ax1.set_ylim([-abs(min(self.y_sh_force))*1.2, abs(max(self.y_sh_force))*1.2])  # задание и ограничение диапазона значений графика по шкале y
		ax1.plot(self.x_sh_force, self.y_sh_force, color = 'b', linewidth=2)
		#ax1.stem(self.x_sh_force, self.y_sh_force, linefmt="g-", markerfmt=".", bottom=0) # заливка вертикальными линиями
		#ax1.fill_between(self.x_sh_force, self.y_sh_force, hatch = '|')
		ax1.fill_between(self.x_sh_force, self.y_sh_force, color = 'green') #заливка графика

		#ax1.grid(True)
		ax1.minorticks_on() # подключение встроенных делений осей
		ax1.grid(which = 'major', color = 'k', linewidth = 0.5) # определение основной сетки
		ax1.grid(which = 'minor', color = 'b', linestyle = ':', linewidth = 0.5) # определения вспомогательной сетки

		#ax1.xaxis.set_major_locator(ticker.MultipleLocator(1))
		#ax1.xaxis.set_minor_locator(ticker.MultipleLocator(0.2))
		#ax1.yaxis.set_major_locator(ticker.MultipleLocator(100))
		#ax1.yaxis.set_minor_locator(ticker.MultipleLocator(50))

		ax1.hlines(0, 0, max(self.x_sh_force)*1, color = 'black') # задаем цветную горизонтальную линию
		ax1.vlines(0, -abs(min(self.y_sh_force))*1, abs(max(self.y_sh_force))*1, color = 'black') # задаем цветную вертикальную линию
		fig1.tight_layout() # раздвигает графики что бы не накладывлись друг на друга

		# постройка графика моментов
		ax2 = fig2.add_subplot()
		ax2.set_title('Bending Moment')
		ax2.set_xlabel("Beam length [m]")
		ax2.set_ylabel("Moment [Nm]")
		
		ax2.set_ylim([-abs(min(self.y_bend_moment))*1.2, abs(max(self.y_bend_moment))*1.2])  # задание и ограничение диапазона значений графика по шкале y
		ax2.plot(self.x_bend_moment, self.y_bend_moment)
		ax2.fill_between(self.x_bend_moment, self.y_bend_moment, color = 'red') #заливка графика
		
		ax2.minorticks_on() # подключение встроенных делений осей
		ax2.grid(which = 'major', color = 'k', linewidth = 0.5) # определение основной сетки
		ax2.grid(which = 'minor', color = 'b', linestyle = ':', linewidth = 0.5) # определения вспомогательной сетки

		ax2.hlines(0, 0, max(self.x_bend_moment)*1, color = 'black') # задаем цветную горизонтальную линию
		ax2.vlines(0, -abs(min(self.y_bend_moment))*1, abs(max(self.y_bend_moment))*1, color = 'black') # задаем цветную вертикальную линию
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


if __name__ == '__main__':
	c1 = bc.Case_1(beam_length = 14, force = 100)
	c1.calculation()
	print("c1.calculation() = ", c1.calculation())
	#plot_tables(*c1.calculation())

	gp1 = GraphPloter(*c1.calculation())
	gp1.plot_tables()
