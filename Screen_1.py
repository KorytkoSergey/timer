import tkinter as tk
from WindowMaker import WindowMaker


class FormWorker:
    main_form = tk.Tk()
    screen_timer = WindowMaker("pomodoro", False)
    screen_pomodoro = WindowMaker("timer", True)
    screen_timer.another_timer = screen_pomodoro
    screen_pomodoro.another_timer = screen_timer

    def draw_main_form(self):
        self.main_form.title("Timer or Pomodoro")
        self.main_form.geometry("400x140+550+350")
        self.main_form.resizable(False, False)

        frame_button = tk.Frame(master=self.main_form, padx=0, pady=34)

        btn_timer = tk.Button(master=frame_button,
                              text='Timer',
                              height=2,
                              width=18,
                              command=self.btm_timer_command)  # кнопка таймер
        btn_timer.pack(side=tk.LEFT, fill=tk.BOTH)
        btn_pomodoro = tk.Button(master=frame_button,
                                 text='Pomodoro',
                                 height=2,
                                 width=18,
                                 command=self.btm_pomodoro_command)  # кнопка pomodoro
        btn_pomodoro.pack(side=tk.RIGHT, fill=tk.BOTH)

        frame_button.pack(ipadx=12, ipady=12)

        self.main_form.mainloop()

    def btm_timer_command(self):
        self.main_form.destroy()
        self.screen_timer.draw_form()

    def btm_pomodoro_command(self):
        self.main_form.destroy()
        self.screen_pomodoro.draw_form()


form_worker = FormWorker()
form_worker.draw_main_form()
