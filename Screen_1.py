import tkinter as tk


def btn_timer_command():  # вызываем через функцию, чтобы избежать зациклиности вызовов
    from Screen_timer import timer_window
    window_1.destroy()
    timer_window()

####################
def btn_pomodoro_command():  # вызываем через функцию, чтобы избежать циклов вызовов
    from Screen_pomodoro import pomodoro_window
    window_1.destroy()
    pomodoro_window()


window_1 = tk.Tk()
window_1.title("Timer or Pomodoro")
window_1.geometry("400x140+550+350")
window_1.resizable(False, False)

frm_btn = tk.Frame(master=window_1, padx=0, pady=34)  # фрейм кнопок

btn_timer = tk.Button(master=frm_btn,
                      text='Timer',
                      height=2,
                      width=18,
                      command=btn_timer_command)  # кнопка таймер
btn_timer.pack(side=tk.LEFT, fill=tk.BOTH)
btn_pomodoro = tk.Button(master=frm_btn,
                         text='Pomodoro',
                         height=2,
                         width=18,
                         command=btn_pomodoro_command)  # кнопка pomodoro
btn_pomodoro.pack(side=tk.RIGHT, fill=tk.BOTH)

frm_btn.pack(ipadx=12, ipady=12)


window_1.mainloop()
