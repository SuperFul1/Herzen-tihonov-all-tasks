from tkinter import *
import tkinter as tk
from tkinter import Menu
from tkinter.ttk import Radiobutton
import math
from math import pi


class Task(tk.Tk):

    def __init__(self):
        super().__init__()
        self.wm_title("Computational mathematics")
        self.geometry('600x600')

        self.task_name = ''
        self.calc_type = 0 # Тип вычислений
        self.left_limit_x = 0
        self.right_limit_x = 0
        self.lower_limit_y = 0
        self.upper_limit_y = 0
        self.var_number = 1 # Количество переменных в подинтегральной функции
        self.step_number_x = 0 # Количество разбиений с постоянным шагом
        self.step_number_y = 0 # Количество разбиений с постоянным шагом
        self.accuracy = 0 # Точность вычислений
        self.function_str = ''
        self.function_str2 = ''
        self.function_str3 = ''
        self.var_x = 'var_x'
        self.var_y = 'var_y'
        self.var_z = 'var_z'
        self.var_t = 'var_t'

        self.calc_type_d1 = 0
        self.y_0 = 0
        self.z_0 = 0
        self.x_0 = 0
        self.t_0 = 0

        self.calc_type_e_f = 0

        self.temp_widgets = []

        self.create_widgets()

    def remove_temp_widgets(self):
        for wd in self.temp_widgets:
            wd.pack_forget()
        self.temp_widgets.clear()

    def set_function_str(self):
        def clicked():
            st = txt.get()
            try:
                self.function_str = st
                self.var_number = 1
                self.calc_function_x(1)
                print(self.function_str)
                text.configure(text=f'Function saved successfully')
                self.remove_temp_widgets()
            except:
                self.function_str = ""
                text.configure(text = f'Error when entering formula. \n{start_text}')

        self.remove_temp_widgets()
        start_text = f"Enter the formula for the function in python code format.\nThe variable name must be '{self.var_x}'"
        text = Label(self, text=start_text)
        text.pack(side=tk.TOP)
        txt = Entry(self, width=50)
        txt.insert(0, self.function_str)
        txt.pack(side=tk.TOP)
        btn = Button(self, text="Submit", command=clicked)
        btn.pack(side=tk.TOP)
        self.temp_widgets.append(text)
        self.temp_widgets.append(txt)
        self.temp_widgets.append(btn)

    def set_function_str_two_params(self):
        def clicked():
            st = txt.get()
            try:
                self.function_str = st
                self.var_number = 2
                self.calc_function_xy(1, 1)
                print(self.function_str)
                text.configure(text=f'Function saved successfully')
                self.remove_temp_widgets()
            except:
                self.function_str = ""
                text.configure(text = f'Error when entering formula. \n{start_text}')

        self.remove_temp_widgets()
        start_text = f"Enter the formula for the function in python code format.\nThe variable name must be " \
                     f"'{self.var_x} и {self.var_y} '"
        text = Label(self, text=start_text)
        text.pack(side=tk.TOP)
        txt = Entry(self, width=50)
        txt.insert(0, self.function_str)
        txt.pack(side=tk.TOP)
        btn = Button(self, text="Submit", command=clicked)
        btn.pack(side=tk.TOP)
        self.temp_widgets.append(text)
        self.temp_widgets.append(txt)
        self.temp_widgets.append(btn)

    def set_function_str_d1(self):
        def clicked():
            st = txt.get()
            try:
                self.function_str = st
                self.var_number = 2
                self.calc_function_xy(1, 1)
                print(self.function_str)
                text.configure(text=f'Function saved successfully')
                self.remove_temp_widgets()
            except:
                self.function_str = ""
                text.configure(text = f'Error when entering formula. \n{start_text}')

        self.remove_temp_widgets()
        start_text = f"Derivative is equal\n (no need to indicate the derivative itself)\n" \
                     f"Variable names must be " \
                     f"'{self.var_x} и {self.var_y} '"
        text = Label(self, text=start_text)
        text.pack(side=tk.TOP)
        txt = Entry(self, width=50)
        txt.insert(0, self.function_str)
        txt.pack(side=tk.TOP)
        btn = Button(self, text="Submit", command=clicked)
        btn.pack(side=tk.TOP)
        self.temp_widgets.append(text)
        self.temp_widgets.append(txt)
        self.temp_widgets.append(btn)

    def set_function_str_2d(self):
        def clicked():
            st = txt.get()
            try:
                self.function_str = st
                self.var_number = 3
                self.calc_function_xyz(1, 1, 1)
                print(self.function_str)
                text.configure(text=f'Function saved successfully')
                self.remove_temp_widgets()
            except:
                self.function_str = ""
                text.configure(text = f'Error when entering formula. \n{start_text}')

        self.remove_temp_widgets()
        start_text = f"derivative is equal\n (no need to indicate the derivative itself)\n" \
                     f"Variable names must be " \
                     f"'{self.var_x} & {self.var_y} & {self.var_z} (as a derivative)'"
        text = Label(self, text=start_text)
        text.pack(side=tk.TOP)
        txt = Entry(self, width=50)
        txt.insert(0, self.function_str)
        txt.pack(side=tk.TOP)
        btn = Button(self, text="Submit", command=clicked)
        btn.pack(side=tk.TOP)
        self.temp_widgets.append(text)
        self.temp_widgets.append(txt)
        self.temp_widgets.append(btn)

    def set_function_str_system_d(self):
        def clicked():
            st = txt.get()
            st2 = txt2.get()
            st3 = txt3.get()
            try:
                self.function_str = st
                self.function_str2 = st2
                self.function_str3 = st3
                self.var_number = 4
                self.calc_function_xyzt(st, 1, 1, 1, 1)
                self.calc_function_xyzt(st2, 1, 1, 1, 1)
                self.calc_function_xyzt(st3, 1, 1, 1, 1)
                print(self.function_str)
                text.configure(text=f'Functions successfully saved')
                self.remove_temp_widgets()
            except:
                self.function_str = ""
                self.function_str2 = ""
                self.function_str3 = ""
                text.configure(text=f'Error when entering formulas. \n{start_text}')

        self.remove_temp_widgets()
        start_text = f"Enter three differential equations\n" \
                     f"Variable names must be " \
                     f"{self.var_x}, {self.var_y}, {self.var_z}\n" \
                     f"The name of the variable with respect to which the derivative is taken," \
                     f"must be {self.var_t}."
        text = Label(self, text=start_text)
        text.pack(side=tk.TOP)
        txt = Entry(self, width=50)
        txt.insert(0, self.function_str)
        txt.pack(side=tk.TOP)
        txt2 = Entry(self, width=50)
        txt2.insert(0, self.function_str2)
        txt2.pack(side=tk.TOP)
        txt3 = Entry(self, width=50)
        txt3.insert(0, self.function_str3)
        txt3.pack(side=tk.TOP)
        btn = Button(self, text="Submit", command=clicked)
        btn.pack(side=tk.TOP)
        self.temp_widgets.append(text)
        self.temp_widgets.append(txt)
        self.temp_widgets.append(txt2)
        self.temp_widgets.append(txt3)
        self.temp_widgets.append(btn)

    def left_rectangle_const_step(self):
        h = (self.right_limit_x - self.left_limit_x) / self.step_number_x
        x = self.left_limit_x
        y = 0
        while x <= (self.right_limit_x - h):
            y += self.calc_function_x(x)
            x += h
        res = y * h
        return res

    def right_rectangle_const_step(self):
        h = (self.right_limit_x - self.left_limit_x) / self.step_number_x
        x = self.left_limit_x + h
        y = 0
        while x <= self.right_limit_x:
            y += self.calc_function_x(x)
            x += h
        res = y * h
        return res

    def trapeze_const_step(self):
        h = (self.right_limit_x - self.left_limit_x) / self.step_number_x
        x = self.left_limit_x + h
        y0 = self.calc_function_x(self.left_limit_x)
        y_max = self.calc_function_x(self.right_limit_x)
        summa = 0
        while x <= (self.right_limit_x - h):
            summa += self.calc_function_x(x)
            x += h
        res = h * (((y0 + y_max)/2) + summa)
        return res

    def parabola_const_step(self):
        h = (self.right_limit_x - self.left_limit_x) / (2 * self.step_number_x)
        x = self.left_limit_x + h
        y0 = self.calc_function_x(self.left_limit_x)
        y_max = self.calc_function_x(self.right_limit_x)
        s1 = 0
        while x <= (self.right_limit_x - h):
            s1 += self.calc_function_x(x)
            x += 2 * h
        s2 = 0
        x = self.left_limit_x + 2 * h
        while x <= (self.right_limit_x - 2 * h):
            s2 += self.calc_function_x(x)
            x += 2 * h
        y = (h/3) * (y0 + 4 * s1 + 2 * s2 + y_max)
        return y

    # calculate functions with variable step

    def first_algorithm_with_variable_step(self):
        h = (self.right_limit_x - self.left_limit_x) / self.step_number_x
        integral = 0
        r = self.accuracy + 1
        while r > self.accuracy:
            s2 = 0
            x = self.left_limit_x
            while x <= (self.right_limit_x - h):
                s2 += self.calc_function_x(x)
                x += h
            i2n = h * s2
            r = abs(i2n - integral)
            integral = i2n
            h = h / 2
        return integral, h

    def second_algorithm_with_variable_step(self):
        h_d = (self.right_limit_x - self.left_limit_x)/self.step_number_x
        h_v = h_d
        h_s = 0
        integral = 0
        sum1 = 0
        while True:
            x = self.left_limit_x + h_s
            while True:
                sum1 += self.calc_function_x(x)
                x += h_v
                if x > self.right_limit_x - h_d: break
            i2n = h_d * sum1
            r = abs (i2n - integral)
            integral = i2n
            h_v = h_d
            h_d /=2
            h_s = h_d
            if r <= self.accuracy: break
        return integral, h_v

    def multiple_integral(self):
        hx = (self.right_limit_x - self.left_limit_x)/self.step_number_x
        hy = (self.upper_limit_y - self.lower_limit_y)/self.step_number_y
        sx = 0
        x = self.left_limit_x
        while x <= (self.right_limit_x - hx):
            sy = 0
            y = self.lower_limit_y
            while y <= (self.upper_limit_y - hy):
                sy += self.calc_function_xy(x, y)
                y += hy
            iy = hy * sy
            sx += iy
            x += hx
        ix = hx * sx
        return ix

    def eiler_d1(self):
        h = (self.right_limit_x - self.left_limit_x) / self.step_number_x
        y = self.y_0
        x = self.left_limit_x
        res = [[x, y]]
        print(f'first: {res}\n')
        i = 1
        while x <= self.right_limit_x - h:
            y += h * self.calc_function_xy(x, y)
            x += h
            res.append([x, y])
            print(res[i])
            i += 1
        return res

    def runge_kutta_d1(self):
        h = (self.right_limit_x - self.left_limit_x) / self.step_number_x
        y = self.y_0
        x = self.left_limit_x
        res = [[x, y]]
        print(f'first: {res}\n')
        i = 1
        while x <= self.right_limit_x - h:
            k_1 = h * self.calc_function_xy(x, y)
            k_2 = h * self.calc_function_xy(x + h / 2, y + k_1 / 2)
            k_3 = h * self.calc_function_xy(x + h / 2, y + k_2 / 2)
            k_4 = h * self.calc_function_xy(x + h, y + k_3)
            y += (k_1 + 2 * (k_2 + k_3) + k_4) / 6
            x += h
            res.append([x, y])
            print(res[i])
            i += 1
        return res

    def diff_Second(self):
        h = (self.right_limit_x - self.left_limit_x) / self.step_number_x
        x = self.left_limit_x
        y = self.y_0
        z = self.z_0
        res = [[x, y]]
        print(f'first: {res}\n')
        i = 1
        while x <= self.right_limit_x - h:
            x += h
            y1 = y + h * z
            z1 = z + h * self.calc_function_xyz(x, y, z)
            y = y1
            z = z1
            res.append([x, y])
            print(res[i])
            i += 1
        return res

    def diff_System(self): # new
        h = (self.right_limit_x - self.left_limit_x) / self.step_number_x
        t = self.left_limit_x
        x = self.x_0
        y = self.y_0
        z = self.z_0
        res = [[t, x, y, z]]
        print(f'first: {res}\n')
        i = 1
        while t <= self.right_limit_x - h:
            t += h
            x += h * self.calc_function_xyzt(self.function_str, x, y, z, t)
            y += h * self.calc_function_xyzt(self.function_str2, x, y, z, t)
            z += h * self.calc_function_xyzt(self.function_str3, x, y, z, t)
            res.append([t, x, y, z])
            i += 1
        return res

    def middle_nu(self):
        a = self.left_limit_x
        b = self.right_limit_x
        while (b-a) > self.accuracy:
            x0 = (a + b) / 2
            something = self.calc_function_x(x0)*self.calc_function_x(a)
            if something < 0:
                b = x0
            else:
                a = x0
        return x0

    def chorde_nu(self):
        a = self.left_limit_x
        b = self.right_limit_x
        xn = a
        x0 = a - (b - a) * self.calc_function_x(a) / (self.calc_function_x(b) - self.calc_function_x(a))
        while abs(x0 - xn) > self.accuracy:
            something = self.calc_function_x(x0) * self.calc_function_x(a)
            if something < 0:
                b = x0
            else:
                a = x0
            xn = x0
            x0 = a - (b - a) * self.calc_function_x(a) / (self.calc_function_x(b) - self.calc_function_x(a))
        return x0

    def newton_nu(self):
        a = self.left_limit_x
        b = self.right_limit_x
        h = 0.001
        xn = b
        x0 = a
        while True:
            xn = x0 - self.calc_function_x(x0)*2*h/\
                 (self.calc_function_x(x0 + h)-self.calc_function_x(x0 - h))
            if abs(x0-xn) < self.accuracy:
                break
            x0 = xn
        return xn

    def e_in_x_row(self):
        x = self.x_0
        eps = self.accuracy
        u = 1
        res = 1
        k = 1
        while abs(u) > eps:
            m = x/k
            u *= m
            res += u
            k += 1
        return res

    def cos_x_row(self):
        x = self.x_0
        eps = self.accuracy
        u = 1
        res = 1
        k = 1
        while abs(u) > eps:
            m = (-1)*x*x/(2*k*(2*k-1))
            u *= m
            res += u
            k += 1
        return res

    def sin_x_row(self):
        x = self.x_0
        eps = self.accuracy
        u = x
        res = x
        k = 1
        while abs(u) > eps:
            m = (-1)*x*x/(2*k*(2*k+1))
            u *= m
            res += u
            k += 1
        return res

    def e_in_x_ch(self):
        x = self.x_0
        eps = self.accuracy
        a = [1, 0.5000063, 0.1666674, 0.0416350,
             0.0083298, 0.0014393]
        c = 0.99999998
        p = 1
        for k in range(len(a)):
            p *= x
            u = p*a[k]
            c += u
            if abs(u) <= eps:
                break
        return c

    def sin_in_x_ch(self):
        x = self.x_0
        eps = self.accuracy
        a = [1.0000000002, -0.1666666589, 0.008333075,
             -0.000198107, 0.000002608]
        p = x
        c = a[0]*x
        for k in range(1, len(a)):
            print(c, '\n')
            print(p)
            p *= x**2
            u = p*a[k]
            c += u
            if abs(u) <= eps:
                break
        return c

    def calc_function_x(self, x):
        f = self.function_str.replace(self.var_x, str(x))
        return eval(f)

    def calc_function_xy(self, x, y):
        f = self.function_str.replace(self.var_x, str(x)).replace(self.var_y, str(y))
        return eval(f)

    def calc_function_xyz(self, x, y, z):
        f = self.function_str.replace(self.var_x, str(x)).replace(self.var_y,
                                                                  str(y)).replace(self.var_z, str(z))
        return eval(f)

    def calc_function_xyzt(self, f_str, x=0, y=0, z=0, t=0):
        f = f_str.replace(self.var_x, str(x)).\
            replace(self.var_y, str(y)).\
            replace(self.var_z, str(z)).\
            replace(self.var_t, str(t))
        return eval(f)

    def get_digit_value_by_type(self, limit_type):
        if limit_type == 1:
            return self.left_limit_x
        elif limit_type == 2:
            return self.right_limit_x
        elif limit_type == 3:
            return self.lower_limit_y
        elif limit_type == 4:
            return self.upper_limit_y
        elif limit_type == 5:
            return self.step_number_x
        elif limit_type == 6:
            return self.step_number_y
        elif limit_type == 7:
            return self.accuracy
        elif limit_type == 8:
            return self.y_0
        elif limit_type == 9:
            return self.z_0
        elif limit_type == 10:
            return self.x_0
        elif limit_type == 11:
            return self.t_0

    def set_digit_value_by_type(self, limit_type, value):
        if limit_type == 1:
            self.left_limit_x = value
        elif limit_type == 2:
            self.right_limit_x = value
        elif limit_type == 3:
            self.lower_limit_y = value
        elif limit_type == 4:
            self.upper_limit_y = value
        elif limit_type == 5:
            self.step_number_x = value
        elif limit_type == 6:
            self.step_number_y = value
        elif limit_type == 7:
            self.accuracy = value
        elif limit_type == 8:
            self.y_0 = value
        elif limit_type == 9:
            self.z_0 = value
        elif limit_type == 10:
            self.x_0 = value
        elif limit_type == 11:
            self.t_0 = value

    def set_float_parameter(self, label_text, limit_type):
        def clicked():
            st = eval(txt.get())
            try:
                s = float(st)
                self.set_digit_value_by_type(limit_type, s)
                self.remove_temp_widgets()
            except:
                self.function_str = ""
                text.configure(text = f'Input error. \n{start_text}')

        self.remove_temp_widgets()
        start_text = f"{label_text}"
        text = Label(self, text=start_text)
        text.pack(side=tk.TOP)
        txt = Entry(self, width=10)
        txt.insert(0, str(self.get_digit_value_by_type(limit_type)))
        txt.pack(side=tk.TOP)
        btn = Button(self, text="Submit", command=clicked)
        btn.pack(side=tk.TOP)
        self.temp_widgets.append(text)
        self.temp_widgets.append(txt)
        self.temp_widgets.append(btn)

    def set_left_limit_x(self):
        self.set_float_parameter("Left limit", 1)

    def set_right_limit_x(self):
        self.set_float_parameter("Right limit", 2)

    def set_lower_limit_y(self):
        self.set_float_parameter("Lower limit on y", 3)

    def set_upper_limit_y(self):
        self.set_float_parameter("Upper limit on y", 4)

    def set_step_number_x(self):
        self.set_float_parameter("Number of splits", 5)

    def set_step_number_y(self):
        self.set_float_parameter("Number of splits on y", 6)

    def set_accuracy(self):
        self.set_float_parameter("Accuracy", 7)

    def set_y_0(self):
        self.set_float_parameter("Value", 8)

    def set_z_0(self):
        self.set_float_parameter("Value", 9)

    def set_x_0(self):
        self.set_float_parameter("Value", 10)

    def set_t_0(self):
        self.set_float_parameter("Value", 11)

    def calculation(self):
        res = ''
        if self.var_number == 1:
            if self.calc_type == 1:
                res = self.left_rectangle_const_step()
            elif self.calc_type == 2:
                res = self.right_rectangle_const_step()
            elif self.calc_type == 3:
                res = self.trapeze_const_step()
            elif self.calc_type == 4:
                res = self.parabola_const_step()
            elif self.calc_type == 5:
                res = self.first_algorithm_with_variable_step()
            elif self.calc_type == 6:
                res = self.second_algorithm_with_variable_step()
            elif self.calc_type == 7:
                res = self.middle_nu()
            elif self.calc_type == 8:
                res = self.chorde_nu()
            elif self.calc_type == 9:
                res = self.newton_nu()
        if self.var_number == 2:
            if self.calc_type_d1 == 1:
                res = self.eiler_d1()
            elif self.calc_type_d1 == 2:
                res = self.runge_kutta_d1()
            else:
                res = self.multiple_integral()
        if self.var_number == 3:
            res = self.diff_Second()
        if self.var_number == 4:
            res = self.diff_System()
        if self.var_number == 5:
            if self.calc_type_e_f == 1:
                res = self.e_in_x_row()
            if self.calc_type_e_f == 2:
                res = self.cos_x_row()
            if self.calc_type_e_f == 3:
                res = self.sin_x_row()
            if self.calc_type_e_f == 4:
                res = self.e_in_x_ch()
            if self.calc_type_e_f == 5:
                res = self.sin_in_x_ch()

        self.remove_temp_widgets()
        if type(res) == tuple:
            text = Label(self, text=f'Result: {res[0]}\nh = {res[1]}')
        elif type(res) == list:
            s = 'Result:\n'
            for r in res:
                if len(r) == 2:
                    s = s + f'[{round(r[0],3)} ; {round(r[1],3)}]\n'
                elif len(r) == 4:
                    s = s + f'[{round(r[0], 3)} ; {round(r[1], 3)} ; {round(r[2], 3)} ; {round(r[3], 3)}]\n'
            text = Label(self, text=s)
        else:
            text = Label(self, text=f'Result: {res}')
        text.pack(side=tk.TOP)
        self.temp_widgets.append(text)

    def set_calculation_type(self):
        def clicked():
            res = selected.get()
            print(res)
            self.calc_type = res

        self.remove_temp_widgets()
        selected = IntVar(value=self.calc_type)
        text1 = Label(self, text="Select the method for calculating the integral:")
        text4 = Label(self, text="")
        text5 = Label(self, text="")
        text2 = Label(self, text="Constant step methods")
        text3 = Label(self, text="Variable step methods")

        text1.pack(side=tk.TOP)
        text4.pack(side=tk.TOP)
        text2.pack(side=tk.TOP)

        rad1 = Radiobutton(self, text='Left rectangle method', value=1, variable=selected)
        rad2 = Radiobutton(self, text='Right rectangle method', value=2, variable=selected)
        rad3 = Radiobutton(self, text='Trapezoid method', value=3, variable=selected)
        rad4 = Radiobutton(self, text='Parabola method', value=4, variable=selected)
        rad1.pack(side=tk.TOP)
        rad2.pack(side=tk.TOP)
        rad3.pack(side=tk.TOP)
        rad4.pack(side=tk.TOP)
        text5.pack(side=tk.TOP)
        text3.pack(side=tk.TOP)
        rad5 = Radiobutton(self, text='First algorithm', value=5, variable=selected)
        rad6 = Radiobutton(self, text='Second algorithm', value=6, variable=selected)
        rad5.pack(side=tk.TOP)
        rad6.pack(side=tk.TOP)
        btn = Button(self, text="Submit", command=clicked)
        btn.pack(side=tk.TOP)

        self.temp_widgets.append(text1)
        self.temp_widgets.append(text2)
        self.temp_widgets.append(text3)
        self.temp_widgets.append(text4)
        self.temp_widgets.append(text5)
        self.temp_widgets.append(rad1)
        self.temp_widgets.append(rad2)
        self.temp_widgets.append(rad3)
        self.temp_widgets.append(rad4)
        self.temp_widgets.append(rad5)
        self.temp_widgets.append(rad6)
        self.temp_widgets.append(btn)

    def set_calculation_type_d1(self):
        def clicked():
            res = selected.get()
            print(res)
            self.calc_type_d1 = res
        self.remove_temp_widgets()
        selected = IntVar(value=self.calc_type_d1)
        text1 = Label(self, text="Select differential equation calculation method:")
        text1.pack(side=tk.TOP)
        rad1 = Radiobutton(self, text='Euler method', value=1, variable=selected)
        rad1.pack(side=tk.TOP)
        rad2 = Radiobutton(self, text='Runge-Kutta method', value=2, variable=selected)
        rad2.pack(side=tk.TOP)
        btn = Button(self, text="Submit", command=clicked)
        btn.pack(side=tk.TOP)

        self.temp_widgets.append(text1)
        self.temp_widgets.append(rad1)
        self.temp_widgets.append(rad2)
        self.temp_widgets.append(btn)

    def set_calculation_type_nu(self):
        def clicked():
            res = selected.get()
            print(res)
            self.calc_type = res

        self.remove_temp_widgets()
        selected = IntVar(value=self.calc_type)

        rad1 = Radiobutton(self, text='Midline method', value=7, variable=selected)
        rad2 = Radiobutton(self, text='Chord method', value=8, variable=selected)
        rad3 = Radiobutton(self, text='Newton\'s method', value=9, variable=selected)
        rad1.pack(side=tk.TOP)
        rad2.pack(side=tk.TOP)
        rad3.pack(side=tk.TOP)
        btn = Button(self, text="Submit", command=clicked)
        btn.pack(side=tk.TOP)

        self.temp_widgets.append(rad1)
        self.temp_widgets.append(rad2)
        self.temp_widgets.append(rad3)
        self.temp_widgets.append(btn)

    def set_calculation_type_e_f(self):
        def clicked():
            res = selected.get()
            print(res)
            self.calc_type_e_f = res

        self.remove_temp_widgets()
        self.var_number = 5
        selected = IntVar(value=self.calc_type_e_f)
        text1 = Label(self, text="Select the method and the desired function:")
        text4 = Label(self, text="")
        text5 = Label(self, text="")
        text2 = Label(self, text="Series expansion")
        text3 = Label(self, text="Chebyshev method")

        text1.pack(side=tk.TOP)
        text4.pack(side=tk.TOP)
        text2.pack(side=tk.TOP)

        rad1 = Radiobutton(self, text='e^x', value=1, variable=selected)
        rad2 = Radiobutton(self, text='cos(x)', value=2, variable=selected)
        rad3 = Radiobutton(self, text='sin(x)', value=3, variable=selected)
        rad1.pack(side=tk.TOP)
        rad2.pack(side=tk.TOP)
        rad3.pack(side=tk.TOP)
        text5.pack(side=tk.TOP)
        text3.pack(side=tk.TOP)
        rad5 = Radiobutton(self, text='e^x', value=4, variable=selected)
        rad5.pack(side=tk.TOP)
        rad6 = Radiobutton(self, text='sin(x)', value=5, variable=selected)
        rad6.pack(side=tk.TOP)
        btn = Button(self, text="Submit", command=clicked)
        btn.pack(side=tk.TOP)

        self.temp_widgets.append(text1)
        self.temp_widgets.append(text2)
        self.temp_widgets.append(text3)
        self.temp_widgets.append(text4)
        self.temp_widgets.append(text5)
        self.temp_widgets.append(rad1)
        self.temp_widgets.append(rad2)
        self.temp_widgets.append(rad3)
        self.temp_widgets.append(rad5)
        self.temp_widgets.append(rad6)
        self.temp_widgets.append(btn)

    def show_credits(self):
        credit = Toplevel()
        credit.geometry("750x200")
        credit.title("Credits")
        Label(credit, text="The work was carried out by Yurkov E.S., Filonenko N.M., Tikhonov A.S. \n IVT-1, 2nd year, \n The Herzen University", font=('18')).place(x=60, y=60)

    def create_widgets(self):
        menu = Menu(self)
        calc_item1 = Menu(menu)
        calc_item1.add_command(label='Subintegral function', command=self.set_function_str)
        calc_item1.add_separator()
        calc_item1.add_command(label='Integration method', command=self.set_calculation_type)
        calc_item1.add_separator()
        calc_item1.add_command(label='Left border', command=self.set_left_limit_x)
        calc_item1.add_separator()
        calc_item1.add_command(label='Right border', command=self.set_right_limit_x)
        calc_item1.add_separator()
        calc_item1.add_command(label='Calculation accuracy', command=self.set_accuracy)
        calc_item1.add_separator()
        calc_item1.add_command(label='Number of splits', command=self.set_step_number_x)
        calc_item1.add_separator()
        calc_item1.add_command(label='Calculate', command=self.calculation)
        menu.add_cascade(label='Simple integral', menu=calc_item1)

        calc_item2 = Menu(menu)
        calc_item2.add_command(label='Subintegral function', command=self.set_function_str_two_params)
        calc_item2.add_separator()
        calc_item2.add_command(label='Left border on x', command=self.set_left_limit_x)
        calc_item2.add_separator()
        calc_item2.add_command(label='Right border on x', command=self.set_right_limit_x)
        calc_item2.add_separator()
        calc_item2.add_command(label='Lower border on y', command=self.set_lower_limit_y)
        calc_item2.add_separator()
        calc_item2.add_command(label='Upper border on y', command=self.set_upper_limit_y)
        calc_item2.add_separator()
        calc_item2.add_command(label='Number of splits on x', command=self.set_step_number_x)
        calc_item2.add_separator()
        calc_item2.add_command(label='Number of splits on y', command=self.set_step_number_y)
        calc_item2.add_separator()
        calc_item2.add_command(label='Calculate', command=self.calculation)
        menu.add_cascade(label='Double integral', menu=calc_item2)

        calc_item3 = Menu(menu)
        calc_item3.add_command(label='Function', command=self.set_function_str_d1)
        calc_item3.add_separator()
        calc_item3.add_command(label='Solution method', command=self.set_calculation_type_d1)
        calc_item3.add_separator()
        calc_item3.add_command(label='Initial value y', command=self.set_y_0)
        calc_item3.add_separator()
        calc_item3.add_command(label='Left border on x', command=self.set_left_limit_x)
        calc_item3.add_separator()
        calc_item3.add_command(label='Right border on x', command=self.set_right_limit_x)
        calc_item3.add_separator()
        calc_item3.add_command(label='Number of splits', command=self.set_step_number_x)
        calc_item3.add_separator()
        calc_item3.add_command(label='Calculate', command=self.calculation)
        calc_item3.add_separator()
        menu.add_cascade(label='Differential equations', menu=calc_item3)

        calc_item4 = Menu(menu)
        calc_item4.add_command(label='Function', command=self.set_function_str_2d)
        calc_item4.add_separator()
        calc_item4.add_command(label='Initial value y(x0)', command=self.set_y_0)
        calc_item4.add_separator()
        calc_item4.add_command(label='The value of the first derivative of x0', command=self.set_z_0)
        calc_item4.add_separator()
        calc_item4.add_command(label='Left border on x (or x0)', command=self.set_left_limit_x)
        calc_item4.add_separator()
        calc_item4.add_command(label='Right border on x', command=self.set_right_limit_x)
        calc_item4.add_separator()
        calc_item4.add_command(label='Number of splits', command=self.set_step_number_x)
        calc_item4.add_separator()
        calc_item4.add_command(label='Calculate', command=self.calculation)
        calc_item4.add_separator()
        menu.add_cascade(label='Differential equations of 2nd order', menu=calc_item4)

        calc_item5 = Menu(menu)
        calc_item5.add_command(label='Function', command=self.set_function_str_system_d)
        calc_item5.add_separator()
        calc_item5.add_command(label='Initial value x(t0)', command=self.set_x_0)
        calc_item5.add_separator()
        calc_item5.add_command(label='Initial value y(t0)', command=self.set_y_0)
        calc_item5.add_separator()
        calc_item5.add_command(label='Initial value z(t0)', command=self.set_z_0)
        calc_item5.add_separator()
        calc_item5.add_command(label='Left value border t (or t0)', command=self.set_left_limit_x)
        calc_item5.add_separator()
        calc_item5.add_command(label='Right value border t', command=self.set_right_limit_x)
        calc_item5.add_separator()
        calc_item5.add_command(label='Number of splits', command=self.set_step_number_x)
        calc_item5.add_separator()
        calc_item5.add_command(label='Calculate', command=self.calculation)
        calc_item5.add_separator()
        menu.add_cascade(label='System of differential equations', menu=calc_item5)

        calc_item6 = Menu(menu)
        calc_item6.add_command(label='Equation', command=self.set_function_str)
        calc_item6.add_separator()
        calc_item6.add_command(label='Calculation method', command=self.set_calculation_type_nu)
        calc_item6.add_separator()
        calc_item6.add_command(label='Left border', command=self.set_left_limit_x)
        calc_item6.add_separator()
        calc_item6.add_command(label='Right border', command=self.set_right_limit_x)
        calc_item6.add_separator()
        calc_item6.add_command(label='Calculation accuracy', command=self.set_accuracy)
        calc_item6.add_separator()
        calc_item6.add_command(label='Calculate', command=self.calculation)
        menu.add_cascade(label='Solving nonlinear equations', menu=calc_item6)

        calc_item7 = Menu(menu)
        calc_item7.add_command(label='Calculation method', command=self.set_calculation_type_e_f)
        calc_item7.add_separator()
        calc_item7.add_command(label='Initial value x', command=self.set_x_0)
        calc_item7.add_separator()
        calc_item7.add_command(label='Calculation accuracy', command=self.set_accuracy)
        calc_item7.add_separator()
        calc_item7.add_command(label='Calculate', command=self.calculation)
        menu.add_cascade(label='Computing elementary functions', menu=calc_item7)

        menu.add_command(label='Credits', command=self.show_credits)

        self.config(menu=menu)


if __name__ == '__main__':
    app = Task()
    app.mainloop()