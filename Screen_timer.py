import tkinter as tk
import time

global flagTest, root, lbl_info


def btm_pomodoro_command():  # вызываем через функцию, чтобы избежать циклов вызовов
    from Screen_pomodoro import pomodoro_window
    root.destroy()
    pomodoro_window()


def end(timer_label):
    return timer_label.configure(text="00:00")


def timer(value, timer_label):  # основная функция
    global flagTest, lbl_info
    flagTest = False
    if ',' in value:  # небольшая проверка и замена "," на "."
        value = value.replace(',', '.')
    for i in value:
        if i.isalpha():
            lbl_info.configure(text='Нужно число')

    duration = float(value) * 60  # сохраняем начальное значение времени
    start_time = time.time()
    while flagTest is False:
        elapsed_time = time.time() - start_time
        remaining_time = duration - elapsed_time
        if remaining_time < 0:                  # не даем уйти счетчику в минус
            timer_label.configure(text="00:00")
            break
        if flagTest:  # проверка для сброса времени кнопка drop
            break
        mins, secs = divmod(remaining_time, 60)  # divmod находит остаток от деления и сам результат деления
        time_format = "{:02d}:{:02d}".format(int(mins), int(secs))
        timer_label.configure(text=time_format)
        timer_label.update()  # функция для обновления lbl
        time.sleep(0.1)
    end(timer_label)  # по нажатию drop вызываем функцию завершения


def btm_drop_command():  # функция сброса времени
    global flagTest
    flagTest = True


def timer_window():  # функция с оформлением окна
    global root, lbl_info
    root = tk.Tk()
    root.title("Timer")
    root.geometry("800x340+350+250")
    root.resizable(False, False)

    frm_left = tk.Frame(master=root)  # фрейм для приема информации
    lbl_info = tk.Label(master=frm_left, text='количество минут')
    lbl_info.config(font=("Courier", 13))
    lbl_info.grid(row=0, column=0)
    ent_time = tk.Entry(master=frm_left)
    ent_time.grid(row=1, column=0, columnspan=3, sticky='we')
    btn_start = tk.Button(master=frm_left,  # погнали!
                          text='Start',
                          height=2,
                          width=18,
                          command=lambda: timer(ent_time.get(), timer_label))
    # подаем в функцию таймера значение времени и "изображение" с lbl
    btn_start.grid(row=2, column=0, sticky='we')
    btn_drop = tk.Button(master=frm_left,
                         text='Drop',
                         height=2,
                         width=18, command=btm_drop_command)  # кнопка сброса
    btn_drop.grid(row=2, column=1)

    btn_pomodoro_again = tk.Button(master=frm_left, text='Pomodoro', command=btm_pomodoro_command)
    btn_pomodoro_again.grid(row=5, column=0, columnspan=3, sticky='we')

    frm_right = tk.Frame(master=root)  # фрейм для вывода времени
    timer_label = tk.Label(master=frm_right, text="--:--")
    timer_label.config(font=("Courier", 100))
    timer_label.pack()
    frm_left.pack(side=tk.LEFT)
    frm_right.pack(side=tk.RIGHT)
    root.mainloop()
