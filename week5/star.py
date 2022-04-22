import tkinter as tk


def star_print():
    try:
        n = int(en_input.get())
    except ValueError:
        lbl_print.configure(text='정수를 입력해 주십시오.')
    finally:
        en_input.delete(0, 'end')

    texts = ''

    for i in range(1, n + 1):
        for space in range(n - i, 0, -1):
            texts = texts + ' '
        for star in range(1, 2 * i):
            texts = texts + '*'
        texts = texts + '\n'

    lbl_print.configure(text=texts)


if __name__ == '__main__':
    w = tk.Tk()
    w.title('별찍기 프로그램')
    w.geometry('500x500')

    en_input = tk.Entry(w)
    btn_star = tk.Button(w, text="별찍기", command=star_print)
    lbl_print = tk.Label(w, text="별찍기 프로그램")

    en_input.pack()
    btn_star.pack()
    lbl_print.pack()

    en_input.focus()

    w.mainloop()
