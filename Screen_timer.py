import tkinter as tk
import time


class ScreenTimer:
    flag_drop, root_t, lbl_info, flag_stop, time_format, timer_label

    __var = None
    def __int__(self, var1):
        self.var1 = var1

    def btm_pomodoro_command(self):  # вызываем через функцию, чтобы избежать циклов вызовов
        from Screen_pomodoro import pomodoro_window
        root_t.destroy()
        pomodoro_window()

    def end(self):
        global timer_label
        return timer_label.configure(text="00:00")

    def timer(self, value):  # основная функция
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
            if remaining_time < 0:  # не даем уйти счетчику в минус
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

    def stop_to_go(self):  # остановка времени
        global time_format, timer_label
        timer_label.configure(text=time_format)
        # mins, secs = time_format.split(':') подумать, как сделать перезапуск с последним значением
        # mins = int(mins)
        # secs = int(secs)
        # value = mins + (secs / 60)
        # btn_start = tk.Button(command=lambda: timer(value, timer_label))

    def btm_drop_command(self):  # функция смены флага сброса времени
        global flag_drop
        flag_drop = True

    def btm_stop_command(self):  # функция смены флага остановки времени
        global flag_stop
        flag_stop = True


