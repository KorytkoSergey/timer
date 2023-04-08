import tkinter as tk
from Screen_timer import ScreenTimer
from Screen_pomodoro import pomodoro_window


class FormWorker:
    root_t, lbl_info, timer_label = None
    window_1 = tk.Tk()
    screen_timer = ScreenTimer()


    def draw_main_from(self):
        self.window_1.title("Timer or Pomodoro")
        self.window_1.geometry("400x140+550+350")
        self.window_1.resizable(False, False)

        frm_btn = tk.Frame(master=self.window_1, padx=0, pady=34)  # фрейм кнопок

        btn_timer = tk.Button(master=frm_btn,
                              text='Timer',
                              height=2,
                              width=18,
                              command=self.btm_timer_command)  # кнопка таймер
        btn_timer.pack(side=tk.LEFT, fill=tk.BOTH)
        btn_pomodoro = tk.Button(master=frm_btn,
                                 text='Pomodoro',
                                 height=2,
                                 width=18,
                                 command=self.btm_pomodoro_command)  # кнопка pomodoro
        btn_pomodoro.pack(side=tk.RIGHT, fill=tk.BOTH)

        frm_btn.pack(ipadx=12, ipady=12)

        self.window_1.mainloop()
    def btm_timer_command(self):  # вызываем через функцию, чтобы избежать зациклиности вызовов
        self.window_1.destroy()
        self.timer_window()

    def btm_pomodoro_command(self):  # вызываем через функцию, чтобы избежать циклов вызовов
        self.window_1.destroy()
        pomodoro_window()

    def timer_window(self):  # функция с оформлением окна

        timer = tk.Tk()
        timer.title("Timer")
        timer.geometry("800x340+350+250")
        timer.resizable(False, False)

        frm_left = tk.Frame(master=timer)  # фрейм для приема информации
        lbl_info = tk.Label(master=frm_left, text='количество минут')
        lbl_info.config(font=("Courier", 13))
        lbl_info.grid(row=0, column=0)
        ent_time = tk.Entry(master=frm_left)
        ent_time.grid(row=1, column=0, columnspan=3, sticky='we')
        btn_start = tk.Button(master=frm_left,  # погнали!
                              text='Start',
                              height=2,
                              width=10,
                              command=lambda: self.screen_timer.timer(ent_time.get()))
        # подаем в функцию таймера значение времени и "изображение" с lbl
        btn_start.grid(row=2, column=0, sticky='we')
        btn_stop = tk.Button(master=frm_left,  # погнали!
                             text='Stop',
                             height=2,
                             width=10,
                             command=self.screen_timer.btm_stop_command())
        btn_stop.grid(row=2, column=1, sticky='we')
        btn_drop = tk.Button(master=frm_left,
                             text='Drop',
                             height=2,
                             width=10, command=self.screen_timer.btm_stop_command())  # кнопка сброса
        btn_drop.grid(row=2, column=2)

        btn_pomodoro_again = tk.Button(master=frm_left, text='Pomodoro', command=self.screen_timer.btm_stop_command())
        btn_pomodoro_again.grid(row=5, column=0, columnspan=3, sticky='we')
        timer.grid_columnconfigure(0, minsize=10)
        timer.grid_columnconfigure(1, minsize=10)
        timer.grid_columnconfigure(2, minsize=10)
        frm_right = tk.Frame(master=timer)  # фрейм для вывода времени
        timer_label = tk.Label(master=frm_right, text="--:--")
        timer_label.config(font=("Courier", 100))
        timer_label.pack()
        frm_left.pack(side=tk.LEFT)
        frm_right.pack(side=tk.RIGHT)
        timer.mainloop()



