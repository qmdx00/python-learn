import tkinter as t

root = t.Tk()

cv = t.Canvas(root, bg="white")

print(root.winfo_width())
cv.create_rectangle(10, 10, 110, 110)
cv.pack()

root.mainloop()
