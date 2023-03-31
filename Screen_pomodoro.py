import tkinter as tk
import time

global lbl_main_time, lbl_second_time, lbl_amount, lbl_info, lbl_big_time, lbl_small_time, flag_stop, flag_drop
global time_format, root


def btm_timer_command():  # вызываем через функцию, чтобы избежать циклов вызовов
    from Screen_timer import timer_window
    root.destroy()
    timer_window()


def pomodoro_timer(main_time, second_time, amount):  # собираем, обрабатываем и распределяем
    global lbl_info, lbl_big_time, lbl_small_time, lbl_amount, flag_drop, flag_stop
    flag_drop = False
    flag_stop = False
    value_lst = [main_time, second_time, amount]
    value_lst = check_value(value_lst)
    main_time = value_lst[0]
    second_time = value_lst[1]
    amount = value_lst[2]
    main_duration = float(main_time) * 60  # сохраняем начальное значение времени
    second_duration = float(second_time) * 60
    for i in range(int(amount)):
        if (flag_drop is False) or (flag_stop is False):
            slices_format = "{:02d}".format(int(int(amount) - i))
            lbl_amount.configure(text=slices_format)
            period(main_duration)  # функция основного времени
            timeout(second_duration)  # функция перерыва
        if flag_stop or flag_drop:
            if flag_stop:
                return stop_to_go()
            if flag_drop:
                return total_drop()


def period(main_duration):  # функция основного времени
    global flag_stop, flag_drop, time_format
    flag_drop = False
    flag_stop = False
    start_time = time.time()
    while (flag_drop is False) or (flag_stop is False):
        elapsed_time_1 = time.time() - start_time
        remaining_time_1 = main_duration - elapsed_time_1
        if remaining_time_1 < 0:  # не даем уйти счетчику в минус
            lbl_big_time.configure(text="00:00")
            break
        mins, secs = divmod(remaining_time_1, 60)  # divmod находит остаток от деления и сам результат деления
        time_format = "{:02d}:{:02d}".format(int(mins), int(secs))
        lbl_big_time.configure(text=time_format)
        lbl_big_time.update()  # функция для обновления lbl
        time.sleep(0.1)


def timeout(second_duration):  # функция перерыва
    global flag_stop, flag_drop, time_format
    flag_drop = False
    flag_stop = False
    start_time = time.time()
    while (flag_drop is False) or (flag_stop is False):
        elapsed_time_2 = time.time() - start_time
        remaining_time_2 = second_duration - elapsed_time_2
        if remaining_time_2 < 0:  # не даем уйти счетчику в минус
            lbl_small_time.configure(text="00:00")
            break
        mins, secs = divmod(remaining_time_2, 60)  # divmod находит остаток от деления и сам результат деления
        time_format = "{:02d}:{:02d}".format(int(mins), int(secs))
        lbl_small_time.configure(text=time_format)
        lbl_small_time.update()  # функция для обновления lbl
        time.sleep(0.1)


def btm_drop_command():  # функция смены флага сброса времени
    global flag_drop
    flag_drop = True


def btm_stop_command():  # функция смены флага остановки времени
    global flag_stop
    flag_stop = True


def check_value(value):
    new_lst = []
    for y in value:
        if ',' in y:  # небольшая проверка и замена "," на "."
            y = y.replace(',', '.')
            new_lst.append(y)
        if y.isalpha():
            lbl_info.configure(text='Вы точно числа вводите? :)')
        else:
            new_lst.append(y)
    return new_lst


def stop_to_go():  # остановка времени
    global time_format, lbl_big_time, lbl_small_time
    lbl_big_time.configure(text=time_format)
    lbl_small_time.configure(text=time_format)


def total_drop():  # остановка времени
    global lbl_big_time, lbl_small_time, lbl_amount
    lbl_big_time.configure(text="00:00")
    lbl_small_time.configure(text="00:00")
    lbl_amount.configure(text="00:00")


def pomodoro_window():  # функция с оформлением окна
    global lbl_info, lbl_amount, lbl_main_time, lbl_second_time, lbl_big_time, lbl_small_time, root
    root = tk.Tk()
    root.title("Pomodoro")
    root.geometry("800x340+350+250")
    root.resizable(False, False)

    frm_left = tk.Frame(master=root)  # два фрейма для удобства: на левом виджеты которые собирают информацию
    frm_right = tk.Frame(master=root)  # на правом виджеты изображающее время

    # блок описывающий кнопки, поля ввода и вспомогательный текст для левого фрейма

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

    btn_start = tk.Button(master=frm_left, text='Старт', command=lambda: pomodoro_timer(ent_main.get(),
                                                                                        ent_second.get(),
                                                                                        ent_amount.get()))
    btn_start.grid(row=7, column=0, sticky='we')
    btn_stop = tk.Button(master=frm_left, text='Стоп', command=btm_stop_command)
    btn_stop.grid(row=7, column=1, sticky='we')
    btn_drop = tk.Button(master=frm_left, text='Сброс', command=btm_drop_command)
    btn_drop.grid(row=7, column=2, sticky='we')

    btn_timer = tk.Button(master=frm_left, text='Timer', command=btm_timer_command)
    btn_timer.grid(row=8, column=0, columnspan=3, sticky='we')

    # блок изображения времени на правом фрейме

    lbl_big_time = tk.Label(master=frm_right, text='--:--')
    lbl_small_time = tk.Label(master=frm_right, text='--:--')
    lbl_amount = tk.Label(master=frm_right, text='--')
    lbl_amount.config(font=("Courier", 50))
    lbl_big_time.config(font=("Courier", 70))
    lbl_small_time.config(font=("Courier", 70))
    lbl_amount.pack()
    lbl_big_time.pack()
    lbl_small_time.pack()

    frm_left.pack(side=tk.LEFT)
    frm_right.pack(side=tk.RIGHT)
    root.mainloop()
