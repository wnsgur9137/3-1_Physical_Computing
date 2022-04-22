import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

file = './text/file_io_test.txt'


fp = open(file, 'w')

fp = open('./text/file_io_test.txt', 'r')
lines = fp.readlines() # 파일을 1행 단위의 리스트 원소로 리턴
# print(lines)
for line in lines:
    # print(line.rstrip('\n'))
    # print(line.strip('\n'))
    print(line[0:-1])
# for line in fp:
#     print(line, end='')


fp_dir = './text/'

def file_write():
    try:
        fp = open(fp_dir+et_file_name.get().strip(), 'w')
        print(et_file_content.get(), file=fp)
        messagebox.showinfo('쓰기', '{0}파일 쓰기가 완료되었습니다.'.format(et_file_name.get()))
    except:
        print('write 에러')
    finally:
        fp.close()

def file_read():
    fp = open(fp_dir + et_file_name.get().strip(), 'r')
    lines = fp.readlines()
    line_list = []
    for line in lines:
        print(line)
        line_list.append(line)

    print('line_list : ', end='')
    print(line_list)
    print(type(line_list))
    lbl_finally.configure(text='{0}'.format(line_list[:]))
    try:
        pass
    except:
        print('read 에러')
    finally:
        fp.close()


def file_a():
    try:
        fp = open(et_file_name.get().strip(), 'a')
    except:
        print('read 에러')
    finally:
        fp.close()


if __name__ == '__main__':
    win = tk.Tk()
    win.title('파일 입출력 GUI')

    lbl_file_name = tk.Label(win, text='파일 이름 : ')
    et_file_name = tk.Entry(win)
    lbl_file_content = tk.Label(win, text='내용 : ')
    et_file_content = tk.Entry(win)
    btn_file_write = tk.Button(win, text='파일 쓰기', command=file_write)
    btn_file_read = tk.Button(win, text='파일 읽기', command=file_read)
    btn_file_a = tk.Button(win, text='파일 이어쓰기', command=file_a)
    lbl_finally = tk.Label(win)

    lbl_file_name.grid(row=0, column=0)
    et_file_name.grid(row=0, column=1, columnspan=2)

    lbl_file_content.grid(row=1, column=0)
    et_file_content.grid(row=1, column=1, columnspan=2)

    btn_file_write.grid(row=2, column=0)
    btn_file_read.grid(row=2, column=1)
    btn_file_a.grid(row=2, column=2)

    lbl_finally.grid(row=3, column=0, columnspan=4)

    win.mainloop()