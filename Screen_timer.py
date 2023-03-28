import tkinter as tk
import time


def btm_pomodoro_command():  # вызываем через функцию, чтобы избежать циклов вызовов
    from Screen_pomodoro import pomodoro_window
    root.destroy()
    pomodoro_window()

def end():
    return timer_label.configure(text="00:00")

def timer(value, timer_label, flag):
    duration = int(value)  # сохраняем начальное значение времени
    start_time = time.time()
    a = 1
    while a != 0:  # используем бесконечный цикл для того, чтобы проверять флаги каждый раз
        elapsed_time = time.time() - start_time
        remaining_time = duration - elapsed_time
        if remaining_time < 0:
            timer_label.configure(text="00:00")  # изменяем время на нули по истечению времени
            break

        mins, secs = divmod(remaining_time, 60)  # divmod находит остаток от деления и сам результат деления
        time_format = "{:02d}:{:02d}".format(int(mins), int(secs))
        timer_label.configure(text=time_format)
        timer_label.update()  # функция для обновления lbl
        time.sleep(0.1)
        if flag == 2:  # если флаг сброса установлен
            a = 0  # изменяем время на нули по истечению времени
    end()



def btm_stop_command():  # добавляем аргумент флага остановки времени
    stop_flag = True  # устанавливаем флаг, чтобы функция timer остановила таймер
    timer(stop_flag)


def btm_drop_command():  # добавляем аргумент флага сброса времени
    drop_flag = True  # устанавливаем флаг, чтобы функция timer сбросила время
    timer_label.configure(text="00:00")  # сбрасываем значение на "00:00"
    timer(0, timer_label, 2)



def timer_window():  # функция с оформлением окна
    global root, timer_label
    root = tk.Tk()
    root.title("Timer")
    root.geometry("800x340+350+250")
    root.resizable(False, False)

    frm_left = tk.Frame(master=root)  # фрейм для приема информации

    ent_time = tk.Entry(master=frm_left)
    ent_time.grid(row=0, column=0, columnspan=3, sticky='we')

    btn_start = tk.Button(master=frm_left,  # погнали!
                          text='Start',
                          height=2,
                          width=18,
                          command=lambda: timer(ent_time.get(), timer_label, 0))
    # подаем в функцию таймера значение времени и "изображение" с lbl
    btn_start.grid(row=1, column=0)

    btn_stop = tk.Button(master=frm_left,
                         text='Stop',
                         height=2,
                         width=18,
                         command=btm_stop_command)
    btn_stop.grid(row=1, column=1)  # кнопка стоп

    btn_drop = tk.Button(master=frm_left,
                         text='Drop',
                         height=2,
                         width=18, command=btm_drop_command)  # кнопка сброса
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
