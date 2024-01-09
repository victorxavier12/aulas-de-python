import tkinter as tk

janela = tk.Tk()
label = tk.Label(janela, text='OLA MUNDO')
label2 = tk.Label(janela, text='OLA MUNDO')
label.grid(row=0, column=0)
label2.grid(row=1, column=10)
# label.pack()
# label2.pack()

janela.mainloop()

