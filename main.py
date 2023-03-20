import tkinter as tk
import tkinter.font as font


def data():
    protein = float(entry2.get()) * 1.5
    comment = tk.Label(root, text=f"<結果> \n必要なプロテイン摂取量は{protein}gです")
    comment.place(relx=0.5, rely=0.5, anchor="center")
    comment2 = tk.Label(root, text="プロテインパウダーを摂取する場合スプーン2、3杯程度です。\n必要に応じて摂取するようにしましょう。")
    comment2.place(relx=0.5, rely=0.6, anchor="center")


root = tk.Tk()
root.title("")
root.geometry("600x500")
root.resizable(False, False)

font1 = font.Font(family="Helvetica", size=20, weight="bold")
font2 = font.Font(family="Helvetica", size=10)  # 入力欄

title1 = tk.Label(root, text="プロテイン摂取量確認アプリ", font=font1)
title1.pack(side="top", padx=10, pady=10)

text = tk.Label(root, text="下記入力することで、1日に必要なプロテイン摂取量が分かります。数字のみ記入してください", font=font2)
text.pack(side="top", padx=10, pady=10)

frame1 = tk.Frame(root)
frame1.pack(pady=10)

text1 = tk.Label(frame1, text="身長", font=font2)
text1.pack(side="left", padx=10)

entry1 = tk.Entry(frame1, font=font2)
entry1.pack(side="left", padx=10)

text2 = tk.Label(frame1, text="(cm)", font=font2)
text2.pack(side="left")

frame2 = tk.Frame(root)
frame2.pack(pady=10)

text3 = tk.Label(frame2, text="体重", font=font2)
text3.pack(side="left", padx=10)

entry2 = tk.Entry(frame2, font=font2)
entry2.pack(side="left", padx=10)

text4 = tk.Label(frame2, text="(kg)", font=font2)
text4.pack(side="left")

button1 = tk.Button(root, text="測定する", command=data, font=font2)
button1.pack(side="top", pady=10)

root.mainloop()
