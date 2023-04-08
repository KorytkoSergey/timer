import tkinter as tk
import time


class WindowMaker:
    form, label_info, timer_label, flag_stop, flag_drop, another_timer, ent_time = None, None, None, None, None, \
        None, None
    break_timer_label, amount_label, ent_second = None, None, None

    def __init__(self, another_timer_name, is_pomodoro):
        self.another_timer_name = another_timer_name
        self.is_pomodoro = is_pomodoro

    def timer(self):
        self.flag_stop = False
        self.flag_drop = False
        ent_time = self.ent_time.get()
        break_time = None
        if not self.check_time(ent_time):
            return
        if self.is_pomodoro:
            break_time = self.ent_second.get()
            if not self.check_time(break_time):
                return

        self.main_timer(ent_time, self.timer_label)
        if self.is_pomodoro:
            self.main_timer(break_time, self.break_timer_label)

    def check_time(self, in_time):
        if ',' in in_time:
            in_time = in_time.replace(',', '.')
        for i in in_time:
            if i.isalpha():
                self.label_info.configure(text='Нужно число')
                return False
        return True

    def main_timer(self, time_count, timer_label):
        time_format = None

        duration = float(time_count) * 60  # сохраняем начальное значение времени
        start_time = time.time()
        while self.flag_drop is False and self.flag_stop is False:
            elapsed_time = time.time() - start_time
            remaining_time = duration - elapsed_time
            if remaining_time < 0:
                timer_label.configure(text="00:00")
                break
            if self.flag_drop:
                break
            elif self.flag_stop:
                timer_label.configure(text=time_format)
                self.break_timer_label.configure(text=time_format)
                break

            mins, secs = divmod(remaining_time, 60)  # divmod находит остаток от деления и сам результат деления
            time_format = "{:02d}:{:02d}".format(int(mins), int(secs))
            timer_label.configure(text=time_format)
            timer_label.update()  # функция для обновления lbl
            time.sleep(0.1)

    def stop_command(self):
        self.flag_stop = True

    def drop_command(self):
        self.flag_drop = True
        self.timer_label.configure(text="00:00")
        if self.is_pomodoro:
            self.break_timer_label.configure(text="00:00")
            self.amount_label.configure(text="00:00")

    def pomodoro_command(self):
        self.form.destroy()
        self.another_timer.draw_form()

    def draw_form(self):
        is_pomodoro = self.is_pomodoro

        self.form = tk.Tk()
        self.form.title("Timer")
        self.form.geometry("800x340+350+250")
        self.form.resizable(False, False)

        row_number = 0
        frm_left = tk.Frame(master=self.form)
        self.label_info = tk.Label(master=frm_left, text='количество минут')
        self.label_info.config(font=("Courier", 18))
        self.label_info.grid(row=row_number, column=0)
        row_number += 1
        if is_pomodoro:
            lbl_main_time = tk.Label(master=frm_left, text='Длительность основного времени')
            lbl_main_time.grid(row=row_number, column=0)
            row_number += 1
        self.ent_time = tk.Entry(master=frm_left)
        if is_pomodoro:
            self.ent_time.grid(row=row_number, column=0)
        else:
            self.ent_time.grid(row=1, column=0, columnspan=3, sticky='we')
        row_number += 1

        if is_pomodoro:
            lbl_second_time = tk.Label(master=frm_left, text='Длительность перерыва')
            lbl_second_time.grid(row=row_number, column=0)
            row_number += 1
            self.ent_second = tk.Entry(master=frm_left)
            self.ent_second.grid(row=row_number, column=0)
            row_number += 1
            lbl_amount = tk.Label(master=frm_left, text='Количество')
            lbl_amount.grid(row=row_number, column=0)
            ent_amount = tk.Entry(master=frm_left)
            row_number += 1
            ent_amount.grid(row=row_number, column=0)
            row_number += 1

        button_start = tk.Button(master=frm_left,
                                 text='Start',
                                 height=2,
                                 width=10,
                                 command=self.timer)

        button_start.grid(row=row_number, column=0, sticky='we')
        button_stop = tk.Button(master=frm_left,  # погнали!
                                text='Stop',
                                height=2,
                                width=10,
                                command=self.stop_command)
        button_stop.grid(row=row_number, column=1, sticky='we')
        button_drop = tk.Button(master=frm_left,
                                text='Drop',
                                height=2,
                                width=10, command=self.drop_command)
        button_drop.grid(row=row_number, column=2)
        row_number += 1

        button_another_timer = tk.Button(master=frm_left, text=self.another_timer_name, command=self.pomodoro_command)
        button_another_timer.grid(row=row_number, column=0, columnspan=3, sticky='we')
        self.form.grid_columnconfigure(0, minsize=10)
        self.form.grid_columnconfigure(1, minsize=10)
        self.form.grid_columnconfigure(2, minsize=10)

        frm_right = tk.Frame(master=self.form)
        self.timer_label = tk.Label(master=frm_right, text="--:--")
        self.timer_label.config(font=("Courier", 100))
        self.timer_label.pack()
        if is_pomodoro:
            self.break_timer_label = tk.Label(master=frm_right, text="--:--")
            self.break_timer_label.config(font=("Courier", 100))
            self.break_timer_label.pack()
            self.amount_label = tk.Label(master=frm_right, text='--')
            self.amount_label.config(font=("Courier", 50))
            self.amount_label.pack()
        frm_left.pack(side=tk.LEFT)
        frm_right.pack(side=tk.RIGHT)
        self.form.mainloop()
