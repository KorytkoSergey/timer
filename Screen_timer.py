import tkinter as tk
import time

global flag_drop, root_t, lbl_info, flag_stop, time_format, timer_label

#check
def btm_pomodoro_command():  # вызываем через функцию, чтобы избежать циклов вызовов
    from Screen_pomodoro import pomodoro_window
    root_t.destroy()
    pomodoro_window()


def end():
    global timer_label
    return timer_label.configure(text="00:00")


def timer(value):  # основная функция
    global flag_drop, lbl_info, flag_stop, time_format, timer_label
    flag_drop = False
    flag_stop = False
    if ',' in value:  # небольшая проверка и замена "," на "."
        value = value.replace(',', '.')
    for i in value:
        if i.isalpha():
            lbl_info.configure(text='Нужно число')
    duration = float(value) * 60  # сохраняем начальное значение времени
    start_time = time.time()
    while (flag_drop is False) or (flag_stop is False):
        elapsed_time = time.time() - start_time
        remaining_time = duration - elapsed_time
        if remaining_time < 0:                  # не даем уйти счетчику в минус
            timer_label.configure(text="00:00")
            break
        if flag_drop:  # проверка для сброса времени кнопка drop
            break
        if flag_stop:
            return stop_to_go()
        mins, secs = divmod(remaining_time, 60)  # divmod находит остаток от деления и сам результат деления
        time_format = "{:02d}:{:02d}".format(int(mins), int(secs))
        timer_label.configure(text=time_format)
        timer_label.update()  # функция для обновления lbl
        time.sleep(0.1)
    end()  # по нажатию drop вызываем функцию завершения


def stop_to_go():  # остановка времени
    global time_format, timer_label
    timer_label.configure(text=time_format)
    # mins, secs = time_format.split(':') подумать, как сделать перезапуск с последним значением
    # mins = int(mins)
    # secs = int(secs)
    # value = mins + (secs / 60)
    # btn_start = tk.Button(command=lambda: timer(value, timer_label))


def btm_drop_command():  # функция смены флага сброса времени
    global flag_drop
    flag_drop = True


def btm_stop_command():  # функция смены флага остановки времени
    global flag_stop
    flag_stop = True


def timer_window():  # функция с оформлением окна
    global root_t, lbl_info, timer_label
    root_t = tk.Tk()
    root_t.title("Timer")
    root_t.geometry("800x340+350+250")
    root_t.resizable(False, False)

    frm_left = tk.Frame(master=root_t)  # фрейм для приема информации
    lbl_info = tk.Label(master=frm_left, text='количество минут')
    lbl_info.config(font=("Courier", 13))
    lbl_info.grid(row=0, column=0)
    ent_time = tk.Entry(master=frm_left)
    ent_time.grid(row=1, column=0, columnspan=3, sticky='we')
    btn_start = tk.Button(master=frm_left,  # погнали!
                          text='Start',
                          height=2,
                          width=10,
                          command=lambda: timer(ent_time.get()))
    # подаем в функцию таймера значение времени и "изображение" с lbl
    btn_start.grid(row=2, column=0, sticky='we')
    btn_stop = tk.Button(master=frm_left,  # погнали!
                         text='Stop',
                         height=2,
                         width=10,
                         command=btm_stop_command)
    btn_stop.grid(row=2, column=1, sticky='we')
    btn_drop = tk.Button(master=frm_left,
                         text='Drop',
                         height=2,
                         width=10, command=btm_drop_command)  # кнопка сброса
    btn_drop.grid(row=2, column=2)

    btn_pomodoro_again = tk.Button(master=frm_left, text='Pomodoro', command=btm_pomodoro_command)
    btn_pomodoro_again.grid(row=5, column=0, columnspan=3, sticky='we')
    root_t.grid_columnconfigure(0, minsize=10)
    root_t.grid_columnconfigure(1, minsize=10)
    root_t.grid_columnconfigure(2, minsize=10)
    frm_right = tk.Frame(master=root_t)  # фрейм для вывода времени
    timer_label = tk.Label(master=frm_right, text="--:--")
    timer_label.config(font=("Courier", 100))
    timer_label.pack()
    frm_left.pack(side=tk.LEFT)
    frm_right.pack(side=tk.RIGHT)
    root_t.mainloop()
