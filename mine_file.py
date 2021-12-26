import tkinter as tk

import beam_calculation as bc
import plotting_file as pf

main_window_height = 412
main_window_width = 320

sub_window_height = 70
sub_window_width = 220


def submit():
	#print('hello!')
	if var.get() == 1:
		print("first")
		case_1()
	elif var.get() == 2:
		print("second")

def case_1():

	def send():
		beam_lenght = int(wc1_entry_1.get())
		force = int(wc1_entry_2.get())
		print(beam_lenght)
		print(force)

		c1 = bc.Case_1(beam_length = beam_lenght, force = force)
		#c1.calculation()

		#gp1 = pf.GraphPloter(*c1.calculation())
		#gp1.plot_tables()
		sub_window_height = 480
		sub_window_width = 600
		wind_case_1.geometry(f"{sub_window_width}x{sub_window_height}+200+100")
	

		gp2 = pf.GraphPloter(*c1.calculation())
		gp2.plot_tables_wind(wind_case_1)


	print(var.get())
	wind_case_1 = tk.Toplevel()
	wind_case_1.title('Case 1')
	wind_case_1.geometry(f"{sub_window_width}x{sub_window_height}+200+100")
	wc1_label_1 = tk.Label(wind_case_1, text='Lenght of Beam:').grid(row=1, column=0, stick='w')
	wc1_label_2 = tk.Label(wind_case_1, text='Force [kN]:').grid(row=2, column=0, stick='w')
	#wind_case_1['bg'] = 'grey'
	#wind_case_1.overrideredirect(True)
	wc1_entry_1 = tk.Entry(wind_case_1)
	wc1_entry_1.grid(row=1, column=1)
	wc1_entry_2 = tk.Entry(wind_case_1)
	wc1_entry_2.grid(row=2, column=1)

	wc1_button_1 = tk.Button(wind_case_1, text='submit', command=send).grid(row=3, column=0, stick='we', columnspan = 2)


	#tk.Label(wind_case_1, text="About this").pack(expand=2)
	#wind_case_1.after(5000, lambda: wind_case_1.destroy())

def case_2():
	print(var.get())





root = tk.Tk() # создание окна
root.title('ОКНО') # заголовок название окна
root.geometry(f"{main_window_width}x{main_window_height}+100+50") # размер окна и пасполоение относительно верхнего правого угла "длина х ширина + пксели в право + пиксели вниз"


#var = tk.BooleanVar()
var = tk.IntVar()
#var = tk.DoubleVar()
#var = tk.StringVar()

label = tk.Label(root, text = 'Choise beam bending case', font=("Arial",
                 18, "bold")).grid(row=0, column=0, stick='we', columnspan = 2)


image_1 = tk.PhotoImage(file = 'pict//1.1.png')
image_1 = image_1.subsample(1,1)

image_2 = tk.PhotoImage(file = 'pict//2.1.png')
image_2 = image_2.subsample(1,1)



#rb_1 = tk.Radiobutton(root, command = case_1, variable = var,
#               value = 1, indicator = False, image = image_1).grid(row=1, column=1, stick='we')

rb_1 = tk.Radiobutton(root, variable = var,
                value = 1, indicator = False, image = image_1).grid(row=1, column=0, stick='we')

#rb_1 = tk.Radiobutton(root, text = 'text1', variable = var,
#                value = 1, indicator = 0).grid(row=1, column=1)
#rb_2 = tk.Radiobutton(root, text = 'text2', variable = var,
#                value = 2, indicator = 0).pack(fill = tk.X, ipady = 6)
rb_2 = tk.Radiobutton(root, command = case_2, variable = var,
                value = 2, indicator = False, image = image_2).grid(row=2, column=0, stick='we')




# после того как вариант нагрузки выбран эта кнопка должна
# запускать окно с окошками заполнения дфнных и запуском решения
choice_button = tk.Button(root, text='SUBMIT', command=submit).grid(row=5, column=0, stick='we')



root.mainloop() # запуск петли событий