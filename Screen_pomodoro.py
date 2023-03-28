import tkinter as tk
import time

def pomodoro_timer(value, lbl_big_time):
    duration = int(value)
    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time
        remaining_time = duration - elapsed_time

        if remaining_time < 0:
            lbl_big_time.configure(text="00:00")  # изменяем время на нули по истечению времени
            break

        mins, secs = divmod(remaining_time, 60)  # divmod находит остаток от деления и сам результат деления
        time_format = "{:02d}:{:02d}".format(int(mins), int(secs))
        lbl_big_time.configure(text=time_format)
        lbl_big_time.update()  # функция для обновления lbl
        time.sleep(0.1)

def pomodoro_window():  # функция с оформлением окна
    root = tk.Tk()
    root.title("Pomodoro")
    root.geometry("800x340+350+250")
    root.resizable(False, False)

    frm_left = tk.Frame(master=root)  # два фрейма для удобства: на левом виджеты которые собирают информацию
    frm_right = tk.Frame(master=root)  # на правом виджеты изображающее время

    # блок описывающий кнопки, поля ввода и вспомогательный текст для левого фрейма

    lbl_main_time = tk.Label(master=frm_left, text='Длительность основного времени')
    lbl_main_time.grid(row=0, column=0)

    ent_main_time = tk.Entry(master=frm_left)
    ent_main_time.grid(row=1, column=0)

    btn_main_time = tk.Button(master=frm_left, text='Ок', command=lambda: pomodoro_timer(ent_main_time.get(), lbl_big_time))
    btn_main_time.grid(row=1, column=1)

    lbl_second_time = tk.Label(master=frm_left, text='Длительность перерыва')
    lbl_second_time.grid(row=2, column=0)

    ent_second_time = tk.Entry(master=frm_left)
    ent_second_time.grid(row=3, column=0)

    btn_second_time = tk.Button(master=frm_left, text='Ок')
    btn_second_time.grid(row=3, column=1)

    btn_start = tk.Button(master=frm_left, text='Старт')
    btn_start.grid(row=4, column=0, sticky='we')

    btn_stop = tk.Button(master=frm_left, text='Стоп')
    btn_stop.grid(row=4, column=1, sticky='we')

    btn_drop = tk.Button(master=frm_left, text='Сброс')
    btn_drop.grid(row=4, column=2, sticky='we')

    btn_timer = tk.Button(master=frm_left, text='Timer')
    btn_timer.grid(row=5, column=0, columnspan=3, sticky='we')

    # блок изображения времени на правом фрейме

    lbl_big_time = tk.Label(master=frm_right, text='--:--')
    lbl_small_time = tk.Label(master=frm_right, text='--:--')
    lbl_big_time.config(font=("Courier", 100))
    lbl_small_time.config(font=("Courier", 100))
    lbl_big_time.pack()
    lbl_small_time.pack()

    frm_left.pack(side=tk.LEFT)
    frm_right.pack(side=tk.RIGHT)
    root.mainloop()
