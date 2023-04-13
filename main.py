import tkinter as tk
import time


class Device:  # родительский класс в который упакованы дочерние Window и Machine

    def __init__(self):
        self.timer_label = None
        self.lbl_info = None
        self.time_format = None
        self.lbl_amount = None
        self.lbl_big_time = None
        self.lbl_small_time = None


class Window(Device):  # класс отрисовки

    def __init__(self):
        super().__init__()

    def timer_or_pomodoro(self):  # метод выбора типа таймера
        self.window_main = tk.Tk()
        self.window_main.title('timer or pomodoro')
        self.window_main.geometry("400x140+550+350")
        self.window_main.resizable(False, False)
        frm_btn = tk.Frame(master=self.window_main, padx=0, pady=34)
        btn_timer = tk.Button(master=frm_btn,
                              text='Timer',
                              height=2,
                              width=18,
                              command=lambda: self.cross_road('timer'))  # выбираем таймер
        btn_timer.pack(side=tk.LEFT, fill=tk.BOTH)
        btn_pomodoro = tk.Button(master=frm_btn,
                                 text='Pomodoro',
                                 height=2,
                                 width=18,
                                 command=lambda: self.cross_road('pomodoro'))  # выбираем pomodoro
        btn_pomodoro.pack(side=tk.RIGHT, fill=tk.BOTH)
        frm_btn.pack(ipadx=12, ipady=12)
        self.window_main.mainloop()

    def cross_road(self, road):  # метод навигации
        if road == 'timer':
            self.window_main.destroy()
            self.timer_window()
        elif road == 'pomodoro':
            self.window_main.destroy()
            self.pomodoro_window()
        elif road == 'timer_from_pomodoro':
            self.window_pomodoro.destroy()
            self.timer_window()
        elif road == 'pomodoro_from_timer':
            self.window_timer.destroy()
            self.pomodoro_window()

    def timer_window(self):  # отрисовка таймера
        self.window_timer = tk.Tk()
        self.window_timer.title('timer')
        self.window_timer.geometry("800x340+350+250")
        self.window_timer.resizable(False, False)
        frm_left = tk.Frame(master=self.window_timer)  # фрейм для приема информации
        lbl_info = tk.Label(master=frm_left, text='количество минут')
        lbl_info.config(font=("Courier", 13))
        lbl_info.grid(row=0, column=0)
        ent_time = tk.Entry(master=frm_left)
        ent_time.grid(row=1, column=0, columnspan=3, sticky='we')
        btn_start = tk.Button(master=frm_left,  # погнали!
                              text='Start',
                              height=2,
                              width=10, command=lambda: Machine.pre_timer(self, ent_time.get(), self.timer_label))
        btn_start.grid(row=2, column=0, sticky='we')
        btn_stop = tk.Button(master=frm_left,  # погнали!
                             text='Stop',
                             height=2,
                             width=10,
                             command=lambda: Machine.btm_stop_timer(self))
        btn_stop.grid(row=2, column=1, sticky='we')
        btn_drop = tk.Button(master=frm_left,
                             text='Drop',
                             height=2,
                             width=10,
                             command=lambda: Machine.btn_drop_timer(self))  # кнопка сброса
        btn_drop.grid(row=2, column=2)
        btn_pomodoro_again = tk.Button(master=frm_left, text='Pomodoro',
                                       command=lambda: self.cross_road('pomodoro_from_timer'))
        btn_pomodoro_again.grid(row=5, column=0, columnspan=3, sticky='we')
        self.window_timer.grid_columnconfigure(0, minsize=10)
        self.window_timer.grid_columnconfigure(1, minsize=10)
        self.window_timer.grid_columnconfigure(2, minsize=10)
        frm_right = tk.Frame(master=self.window_timer)
        self.timer_label = tk.Label(master=frm_right, text="--:--")
        self.timer_label.config(font=("Courier", 100))
        self.timer_label.pack()
        frm_left.pack(side=tk.LEFT)
        frm_right.pack(side=tk.RIGHT)
        self.window_timer.mainloop()

    def pomodoro_window(self):  # отрисовка pomodoro
        self.window_pomodoro = tk.Tk()
        self.window_pomodoro.title("Pomodoro")
        self.window_pomodoro.geometry("800x340+350+250")
        self.window_pomodoro.resizable(False, False)
        frm_left = tk.Frame(master=self.window_pomodoro)
        frm_right = tk.Frame(master=self.window_pomodoro)
        lbl_info = tk.Label(master=frm_left, text='Значения в минутах')
        lbl_info.config(font=("Courier", 18))
        lbl_info.grid(row=0, column=0)
        lbl_main_time = tk.Label(master=frm_left, text='Длительность основного времени')
        lbl_main_time.grid(row=1, column=0)
        ent_main = tk.Entry(master=frm_left)
        ent_main.grid(row=2, column=0)
        lbl_second_time = tk.Label(master=frm_left, text='Длительность перерыва')
        lbl_second_time.grid(row=3, column=0)
        ent_second = tk.Entry(master=frm_left)
        ent_second.grid(row=4, column=0)
        lbl_amount = tk.Label(master=frm_left, text='Количество')
        lbl_amount.grid(row=5, column=0)
        ent_amount = tk.Entry(master=frm_left)
        ent_amount.grid(row=6, column=0)
        btn_start = tk.Button(master=frm_left, text='Старт', command=lambda: Machine.pomodoro_timer(self,
                                                                                                    ent_main.get(),
                                                                                                    ent_second.get(),
                                                                                                    ent_amount.get()))
        btn_start.grid(row=7, column=0, sticky='we')
        btn_stop = tk.Button(master=frm_left, text='Стоп', command=lambda: Machine.btm_stop_pomodoro(self))
        btn_stop.grid(row=7, column=1, sticky='we')
        btn_drop = tk.Button(master=frm_left, text='Сброс', command=lambda: Machine.btn_drop_pomodoro(self))
        btn_drop.grid(row=7, column=2, sticky='we')
        btn_timer = tk.Button(master=frm_left, text='Timer', command=lambda: self.cross_road('timer_from_pomodoro'))
        btn_timer.grid(row=8, column=0, columnspan=3, sticky='we')
        self.lbl_big_time = tk.Label(master=frm_right, text='--:--')
        self.lbl_small_time = tk.Label(master=frm_right, text='--:--')
        self.lbl_amount = tk.Label(master=frm_right, text='--')
        self.lbl_amount.config(font=("Courier", 50))
        self.lbl_big_time.config(font=("Courier", 70))
        self.lbl_small_time.config(font=("Courier", 70))
        self.lbl_amount.pack()
        self.lbl_big_time.pack()
        self.lbl_small_time.pack()
        frm_left.pack(side=tk.LEFT)
        frm_right.pack(side=tk.RIGHT)
        self.window_pomodoro.mainloop()


class Machine(Device):  # класс механизма отсчета

    def __init__(self):
        super().__init__()
        self.flag_stop = None
        self.flag_drop = None
        self.value = None

    def check_value(self, value):  # метод проверки
        new_lst = []
        for y in value:
            if ',' in y:
                y = y.replace(',', '.')
                new_lst.append(y)
            else:
                new_lst.append(y)
        return new_lst

    def pre_timer(self, value, form_timer):  # метод подготовки значений таймера
        self.flag_drop = False
        self.flag_stop = False
        value = Machine.check_value(self, value)
        value = float(''.join(value)) * 60
        Machine.timer(self, value, form_timer)

    def timer(self, value, form_timer):  # общий метод для отчета
        if self.flag_drop or self.flag_stop:
            pass
        start_time = time.time()
        while self.flag_drop is False and self.flag_stop is False:
            elapsed_time = time.time() - start_time
            remaining_time = value - elapsed_time
            if remaining_time < 0:  # не даем уйти счетчику в минус
                form_timer.configure(text="00:00")
                break
            mins, secs = divmod(remaining_time, 60)  # divmod находит остаток от деления и сам результат деления
            time_format = "{:02d}:{:02d}".format(int(mins), int(secs))
            form_timer.configure(text=time_format)
            form_timer.update()  # функция для обновления lbl
            time.sleep(0.1)

    def pomodoro_timer(self, main_time, second_time, amount):  # метод подготовки значений pomodoro
        self.flag_drop = False
        self.flag_stop = False
        value_lst = [main_time, second_time, amount]
        value_lst = Machine.check_value(self, value_lst)
        main_time = value_lst[0]
        second_time = value_lst[1]
        amount = value_lst[2]
        main_duration = float(main_time) * 60
        second_duration = float(second_time) * 60
        for i in range(int(amount)):
            if (self.flag_drop is False) and (self.flag_stop is False):
                slices_format = "{:02d}".format(int(int(amount) - i))
                self.lbl_amount.configure(text=slices_format)
                Machine.timer(self, main_duration, self.lbl_big_time)
                Machine.timer(self, second_duration, self.lbl_small_time)

    def clear_timers(self, *timer_labels):  # сброс
        for label in timer_labels:
            label.configure(text="00:00")

    def stop_timers(self, *timer_labels):  # стоп
        for label in timer_labels:
            label.configure(text=label.cget("text"))

    def btn_drop_timer(self):  # меняем флаг для сброса таймера
        self.flag_drop = True
        Machine.clear_timers(self, self.timer_label)

    def btm_stop_timer(self):  # метод смены флага остановки времени
        self.flag_stop = True
        Machine.stop_timers(self, self.timer_label)

    def btn_drop_pomodoro(self):  # меняем флаг для сброса pomodoro
        self.flag_drop = True
        Machine.clear_timers(self, self.lbl_amount, self.lbl_big_time, self.lbl_small_time)

    def btm_stop_pomodoro(self):  # меняем флаг для сброса pomodoro
        self.flag_stop = True
        Machine.stop_timers(self, self.lbl_amount, self.lbl_big_time, self.lbl_small_time)


form_worker = Window()  # экземпляр window, который все запускает
form_worker.timer_or_pomodoro()
