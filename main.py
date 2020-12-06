from tkinter import *
import os
import convert
def resource_path(relative_path):
	try:
		base_path = os.path.join(sys._MEIPASS, 'data')
	except Exception:
		base_path = '...' # folder path of code
	return os.path.join(base_path, relative_path)

def main():
	root = Tk()
	root.title("Signed Calculator")
	root.resizable(width=False, height=False)
	root.geometry('500x440')
	root.iconbitmap(resource_path("logo_big.ico"))
	Label(root, text="Signed Calculator", font=("Tahoma", 20)).pack()
	Label(root, text="Decimal to Two's Complement:", font=("Tahoma", 10)).place(x=10, y=50)
	Label(root, text="Bit", font=("Tahoma", 10)).place(x=235, y=50)
	var = IntVar()
	var.set(4)
	spin = Spinbox(root, from_=0, to=100, width=3, font=("Tahoma", 10), textvariable=var)
	spin.place(x=200, y=50)
	str_var1 = StringVar()
	def Written_1(*args):
		entry_result_1.configure(state="normal")
		entry_result_1.delete(0, END)
		try:
			entry_result_1.insert(INSERT, convert.convert_to_bin(int(str_var1.get()), var.get()))
		except:
			if str_var1.get() != "":
				entry_result_1.insert(INSERT, "Error: Value error!")
			else:
				entry_result_1.insert(INSERT, "")
		entry_result_1.configure(state="readonly")
	var.trace("w", Written_1)
	str_var1.trace("w", Written_1)
	entry_1 = Entry(root, font=("Tahoma", 10), textvariable=str_var1, width=68)
	entry_1.place(x=10, y=80)
	Label(root, text="Result:", font=("Tahoma", 10)).place(x=10, y=110)
	entry_result_1 = Entry(root, font=("Tahoma", 10), width=50)
	entry_result_1.configure(state="readonly")
	entry_result_1.place(x=60, y=110)

	Label(root, text="Two's Complement to Decimal:", font=("Tahoma", 10)).place(x=10, y=140)
	Label(root, text="Bit", font=("Tahoma", 10)).place(x=235, y=140)
	var2 = IntVar()
	var2.set(4)
	spin2 = Spinbox(root, from_=0, to=100, width=3, font=("Tahoma", 10), textvariable=var2)
	spin2.place(x=200, y=140)
	str_var2 = StringVar()
	def Written_2(*args):
		entry_result_2.configure(state="normal")
		entry_result_2.delete(0, END)
		try:
			if str_var2.get() != "":
				entry_result_2.insert(INSERT, convert.convert_to_dec(str_var2.get()[len(str_var2.get())-var2.get():]))
			else:
				entry_result_2.insert(INSERT, "")
		except:
			if str_var2.get() != "":
				entry_result_2.insert(INSERT, "Error: Value error!")
			else:
				entry_result_2.insert(INSERT, "")
		entry_result_2.configure(state="readonly")
	var2.trace("w", Written_2)
	str_var2.trace("w", Written_2)
	entry_2 = Entry(root, font=("Tahoma", 10), textvariable=str_var2, width=68)
	entry_2.place(x=10, y=170)
	Label(root, text="Result:", font=("Tahoma", 10)).place(x=10, y=200)
	entry_result_2 = Entry(root, font=("Tahoma", 10), width=50)
	entry_result_2.configure(state="readonly")
	entry_result_2.place(x=60, y=200)

	Label(root, text="Two's Complement", font=("Tahoma", 10)).place(x=10, y=230)
	Label(root, text="Binary:", font=("Tahoma", 10)).place(x=10, y=260)
	str_var3 = StringVar()
	def Written_3(*args):
		entry_result_3.configure(state="normal")
		entry_result_3.delete(0, END)
		entry_result_4.configure(state="normal")
		entry_result_4.delete(0, END)
		entry_result_5.configure(state="normal")
		entry_result_5.delete(0, END)
		try:
			if str_var3.get() != "":
				entry_result_3.insert(INSERT, convert.convert_to_dec(str_var3.get()))
				entry_result_4.insert(INSERT, convert.two_complement(str_var3.get()))
				entry_result_5.insert(INSERT, convert.convert_to_dec(convert.two_complement(str_var3.get())))
			else:
				entry_result_3.insert(INSERT, "")
		except:
			if str_var3.get() != "":
				entry_result_3.insert(INSERT, "Error: Value error!")
			else:
				entry_result_3.insert(INSERT, "")
		entry_result_3.configure(state="readonly")
		entry_result_4.configure(state="readonly")
		entry_result_5.configure(state="readonly")
	str_var3.trace("w", Written_3)
	entry_3 = Entry(root, textvariable=str_var3, width=20)
	entry_3.place(x=60, y=260)
	Label(root, text=":", font=("Tahoma", 10)).place(x=180, y=260)
	entry_result_3 = Entry(root, font=("Tahoma", 10), width=5)
	entry_result_3.configure(state="readonly")
	entry_result_3.place(x=190, y=260)
	Label(root, text="<->", font=("Tahoma", 10)).place(x=220, y=260)
	entry_result_4 = Entry(root, font=("Tahoma", 10), width=20)
	entry_result_4.configure(state="readonly")
	entry_result_4.place(x=250, y=260)
	Label(root, text=":", font=("Tahoma", 10)).place(x=370, y=260)
	entry_result_5 = Entry(root, font=("Tahoma", 10), width=5)
	entry_result_5.configure(state="readonly")
	entry_result_5.place(x=380, y=260)

	Label(root, text="Calculator:", font=("Tahoma", 10)).place(x=10, y=290)
	entry_4 = Entry(root, font=("Tahoma", 10), width=10)
	entry_4.place(x=80, y=290)
	var3 = StringVar()
	var3.set("+")
	spin3 = Spinbox(root, values=("+", "-"), width=2, font=("Tahoma", 10), textvariable=var3)
	spin3.place(x=160, y=290)
	entry_5 = Entry(root, font=("Tahoma", 10), width=10)
	entry_5.place(x=195, y=290)
	Label(root, text="Bit:", font=("Tahoma", 10)).place(x=265, y=290)
	var4 = IntVar()
	var4.set(4)
	spin4 = Spinbox(root, from_=0, to=100, width=3, font=("Tahoma", 10), textvariable=var4)
	spin4.place(x=290, y=290)
	def calculate():
		entry_result_6.configure(state="normal")
		entry_result_6.delete(0, END)
		entry_result_7.configure(state="normal")
		entry_result_7.delete(0, END)
		entry_result_8.configure(state="normal")
		entry_result_8.delete(0, END)
		entry_result_9.configure(state="normal")
		entry_result_9.delete(0, END)
		entry_result_10.configure(state="normal")
		entry_result_10.delete(0, END)
		entry_result_11.configure(state="normal")
		entry_result_11.delete(0, END)
		entry_result_12.configure(state="normal")
		entry_result_12.delete(0, END)
		entry_result_13.configure(state="normal")
		entry_result_13.delete(0, END)
		entry_result_14.configure(state="normal")
		entry_result_14.delete(0, END)
		lab1.configure(text="%s" %var3.get())
		lab2.configure(text="(Bit %d)" %var4.get())
		if entry_4.get() != "" and entry_5.get() != "" and var3.get() == "+" or var3.get() == "-":
			try:
				con_bin_a = convert.convert_bin(entry_4.get(), var4.get())
				con_bin_b = convert.convert_bin(entry_5.get(), var4.get())
				con_to_dec_a = convert.convert_to_dec(con_bin_a)
				con_to_dec_b = convert.convert_to_dec(con_bin_b)
				entry_result_6.insert(INSERT, con_bin_a)
				entry_result_7.insert(INSERT, con_to_dec_a)
				entry_result_8.insert(INSERT, con_bin_b)
				entry_result_9.insert(INSERT, con_to_dec_b)
				if var3.get() == "+":
					entry_result_10.insert(INSERT, convert.convert_to_bin_signded(con_to_dec_a+con_to_dec_b, var4.get()))
					entry_result_11.insert(INSERT, con_to_dec_a+con_to_dec_b)
					entry_result_12.insert(INSERT, convert.convert_to_bin_signded(con_to_dec_a+con_to_dec_b, var4.get()))
					entry_result_13.insert(INSERT, convert.convert_to_bin_signded(con_to_dec_a+con_to_dec_b, var4.get())[len(convert.convert_to_bin_signded(con_to_dec_a+con_to_dec_b, var4.get()))-var4.get():])
					entry_result_14.insert(INSERT, convert.convert_to_bin_signded(con_to_dec_a+con_to_dec_b, var4.get())[len(convert.convert_to_bin_signded(con_to_dec_a+con_to_dec_b, var4.get()))-var4.get():])
					lab3.configure(text="%s" %convert.convert_to_dec(convert.convert_to_bin_signded(con_to_dec_a+con_to_dec_b, var4.get())[len(convert.convert_to_bin_signded(con_to_dec_a+con_to_dec_b, var4.get()))-var4.get():]))
				elif var3.get() == "-":
					entry_result_10.insert(INSERT, convert.convert_to_bin_signded(con_to_dec_a-con_to_dec_b, var4.get()))
					entry_result_11.insert(INSERT, con_to_dec_a-con_to_dec_b)
					entry_result_12.insert(INSERT, convert.convert_to_bin_signded(con_to_dec_a-con_to_dec_b, var4.get()))
					entry_result_13.insert(INSERT, convert.convert_to_bin_signded(con_to_dec_a-con_to_dec_b, var4.get())[len(convert.convert_to_bin_signded(con_to_dec_a-con_to_dec_b, var4.get()))-var4.get():])
					entry_result_14.insert(INSERT, convert.convert_to_bin_signded(con_to_dec_a-con_to_dec_b, var4.get())[len(convert.convert_to_bin_signded(con_to_dec_a-con_to_dec_b, var4.get()))-var4.get():])
					lab3.configure(text="%s" %convert.convert_to_dec(convert.convert_to_bin_signded(con_to_dec_a-con_to_dec_b, var4.get())[len(convert.convert_to_bin_signded(con_to_dec_a-con_to_dec_b, var4.get()))-var4.get():]))			
			except:
				lab3.configure(text="Error: Value error!")
		else:
			lab3.configure(text="Error: Value error!")
		entry_result_6.configure(state="readonly")
		entry_result_7.configure(state="readonly")
		entry_result_8.configure(state="readonly")
		entry_result_9.configure(state="readonly")
		entry_result_10.configure(state="readonly")
		entry_result_11.configure(state="readonly")
		entry_result_12.configure(state="readonly")
		entry_result_13.configure(state="readonly")
		entry_result_14.configure(state="readonly")
	Button(root, text="Calculate", fg="green", font=("Tahoma", 10), command=calculate).place(x=330, y=285)
	def clear():
		entry_4.delete(0, END)
		entry_5.delete(0, END)
		entry_result_6.configure(state="normal")
		entry_result_6.delete(0, END)
		entry_result_7.configure(state="normal")
		entry_result_7.delete(0, END)
		entry_result_8.configure(state="normal")
		entry_result_8.delete(0, END)
		entry_result_9.configure(state="normal")
		entry_result_9.delete(0, END)
		entry_result_10.configure(state="normal")
		entry_result_10.delete(0, END)
		entry_result_11.configure(state="normal")
		entry_result_11.delete(0, END)
		entry_result_12.configure(state="normal")
		entry_result_12.delete(0, END)
		entry_result_13.configure(state="normal")
		entry_result_13.delete(0, END)
		entry_result_14.configure(state="normal")
		entry_result_14.delete(0, END)
		entry_result_6.configure(state="readonly")
		entry_result_7.configure(state="readonly")
		entry_result_8.configure(state="readonly")
		entry_result_9.configure(state="readonly")
		entry_result_10.configure(state="readonly")
		entry_result_11.configure(state="readonly")
		entry_result_12.configure(state="readonly")
		entry_result_13.configure(state="readonly")
		entry_result_14.configure(state="readonly")
		lab3.configure(text="None")
	Button(root, text="Clear", fg="red", font=("Tahoma", 10), command=clear).place(x=400, y=285)
	Label(root, text="Step 1:", font=("Tahoma", 10)).place(x=10, y=320)
	entry_result_6 = Entry(root, font=("Tahoma", 10), width=10)
	entry_result_6.configure(state="readonly")
	entry_result_6.place(x=60, y=320)
	Label(root, text=":", font=("Tahoma", 10)).place(x=130, y=320)
	entry_result_7 = Entry(root, font=("Tahoma", 10), width=5)
	entry_result_7.configure(state="readonly")
	entry_result_7.place(x=140, y=320)
	lab1 = Label(root, text="%s" %var3.get(), font=("Tahoma", 10))
	lab1.place(x=180, y=320)
	entry_result_8 = Entry(root, font=("Tahoma", 10), width=10)
	entry_result_8.configure(state="readonly")
	entry_result_8.place(x=195, y=320)
	Label(root, text=":", font=("Tahoma", 10)).place(x=265, y=320)
	entry_result_9 = Entry(root, font=("Tahoma", 10), width=5)
	entry_result_9.configure(state="readonly")
	entry_result_9.place(x=275, y=320)
	Label(root, text="=", font=("Tahoma", 10)).place(x=315, y=320)
	entry_result_10 = Entry(root, font=("Tahoma", 10), width=10)
	entry_result_10.configure(state="readonly")
	entry_result_10.place(x=335, y=320)
	Label(root, text=":", font=("Tahoma", 10)).place(x=395, y=320)
	entry_result_11 = Entry(root, font=("Tahoma", 10), width=5)
	entry_result_11.configure(state="readonly")
	entry_result_11.place(x=405, y=320)

	Label(root, text="Step 2:", font=("Tahoma", 10)).place(x=10, y=350)
	entry_result_12 = Entry(root, font=("Tahoma", 10), width=10)
	entry_result_12.configure(state="readonly")
	entry_result_12.place(x=60, y=350)
	Label(root, text=":", font=("Tahoma", 10)).place(x=130, y=350)
	entry_result_13 = Entry(root, font=("Tahoma", 10), width=10)
	entry_result_13.configure(state="readonly")
	entry_result_13.place(x=140, y=350)
	lab2 = Label(root, text="(Bit %d)" %var4.get(), font=("Tahoma", 10))
	lab2.place(x=215, y=348)

	Label(root, text="Step 3:", font=("Tahoma", 10)).place(x=10, y=380)
	entry_result_14 = Entry(root, font=("Tahoma", 10), width=10)
	entry_result_14.configure(state="readonly")
	entry_result_14.place(x=60, y=380)
	Label(root, text="=", font=("Tahoma", 10)).place(x=135, y=380)
	lab3 = Label(root, text="None", fg="red", font=("Tahoma", 15))
	lab3.place(x=150, y=375)
	Label(root, text="Signed Calculator Powered by Surrussent (2018-2019) COMP SCI CMU :>", relief=SUNKEN, anchor=W, font=("Tahoma", 11)).pack(side=BOTTOM, fill=X)
	root.mainloop()

if __name__ == '__main__':
	main()