import tkinter as tk

class my_custum_frame(tk.Frame):
    def __init__(self,parent,bg="white"):
        super().__init__(parent,bg=bg)
        self.my_label = tk.Label(self, text="coucou")
        self.my_label.place(x=20, y=50)


def main():
    my_window = tk.Tk()
    my_window.geometry("500x500")
    
    my_frame = my_custum_frame(my_window)
    my_frame.pack(fill='both',expand=True)

    my_window.mainloop()

if __name__ == "__main__":
    main()