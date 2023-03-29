import tkinter as tk
import time


def btm_pomodoro_command():  # вызываем через функцию, чтобы избежать циклов вызовов
    from Screen_pomodoro import pomodoro_window
    root.destroy()
    pomodoro_window()

def start_info():
    global duration, start_time, flag
    duration = duration.get() * 60
    start_time = time.time()
    flag = True
    timer()

def timer():
    global duration, flag
    if flag:
        elapsed_time = time.time() - start_time
        duration = max(0, duration - elapsed_time)
        mins, secs = divmod(duration, 60)
        timer_label.configure(text="{:02d}:{:02d}".format(int(mins), int(secs)))
        if duration == 0:
            flag = False
        else:
            root.after(1000, timer)

def drop_timer():
    global flag, start_time, duration
    if flag:
        flag = False
        start_time = None
        timer_label.configure(text="00:00")
        duration = tk.IntVar()
        duration.set(0)

def timer_window():  # функция с оформлением окна
    global root, timer_label, duration
    root = tk.Tk()
    root.title("Timer")
    root.geometry("800x340+350+250")
    root.resizable(False, False)

    frm_left = tk.Frame(master=root)  # фрейм для приема информации
    duration = tk.IntVar()
    duration.set(0)
    ent_time = tk.Entry(master=frm_left, textvariable=duration)
    ent_time.grid(row=0, column=0, columnspan=3, sticky='we')

    btn_start = tk.Button(master=frm_left,  # погнали!
                          text='Start',
                          height=2,
                          width=18,
                          command=start_info)
    # подаем в функцию таймера значение времени и "изображение" с lbl
    btn_start.grid(row=1, column=0)

    #btn_stop = tk.Button(master=frm_left,
                         #text='Stop',
                         #height=2,
                         #width=18)
    #btn_stop.grid(row=1, column=1)  # кнопка стоп

    btn_drop = tk.Button(master=frm_left,
                         text='Drop',
                         height=2,
                         width=18, command=drop_timer)  # кнопка сброса
    btn_drop.grid(row=1, column=2)

    btn_pomodoro_again = tk.Button(master=frm_left, text='Pomodoro', command=btm_pomodoro_command)
    btn_pomodoro_again.grid(row=5, column=0, columnspan=3, sticky='we')

    frm_right = tk.Frame(master=root)  # фрейм для вывода времени

    timer_label = tk.Label(master=frm_right, text="--:--")
    timer_label.config(font=("Courier", 100))
    timer_label.pack()

    frm_left.pack(side=tk.LEFT)
    frm_right.pack(side=tk.RIGHT)

    root.mainloop()
