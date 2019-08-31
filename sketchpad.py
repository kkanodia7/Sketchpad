# Created by Kushal Kanodia on Jan 3, 2017

from tkinter import Tk, Canvas
from random import randint

root = Tk()
canvas = Canvas(root, width=640, height=480)
canvas.pack()

tool = 1
color = "black"
points = []


def click(event):
    global tool, color, points
    if event.x <= 80:
        points = []
        if event.y < 80:
            tool = 1
        elif event.y < 160:
            tool = 2
        elif event.y < 240:
            tool = 3
        elif event.y < 320:
            tool = 4
        elif event.y < 400:
            tool = 5
        elif event.y < 440:
            if event.x < 40:
                color = "black"
            else:
                color = "red"
        else:
            if event.x < 40:
                color = "green"
            else:
                color = "blue"

    else:
        if tool == 1 or tool == 3:
            points.append(event.x)
            points.append(event.y)
        elif tool == 2:
            points.append(event.x)
            points.append(event.y)
            if len(points) >= 4:
                canvas.create_line(points, fill=color)


def drag(event):
    global tool, color, points
    if event.x > 80:
        if tool == 4:
            points.append(event.x)
            points.append(event.y)
            if len(points) >= 4:
                canvas.create_line(points, fill=color)
        if tool == 5:
            for r in range(50):
                rpixelx = randint(event.x - 20, event.x + 20)
                rpixely = randint(event.y - 20, event.y + 20)
                if (rpixelx - event.x) ** 2 + (rpixely - event.y) ** 2 <= 20 ** 2:
                    canvas.create_line(rpixelx, rpixely, rpixelx + 1, rpixely + 1, fill=color)


def release(event):
    global tool, color, points
    if event.x > 80:
        if tool == 1:
            points.append(event.x)
            points.append(event.y)
            canvas.create_line(points, fill=color)
            points = []
        elif tool == 3:
            points.append(event.x)
            points.append(event.y)
            canvas.create_rectangle(points, fill=color)
            points = []
        elif tool == 4 or tool == 5:
            points = []


def clear(event):
    canvas.delete("all")
    canvas.create_line(80, 0, 80, 480)
    canvas.create_line(0, 80, 80, 80)
    canvas.create_line(0, 160, 80, 160)
    canvas.create_line(0, 240, 80, 240)
    canvas.create_line(0, 320, 80, 320)

    canvas.create_line(15, 65, 65, 15)
    canvas.create_line(15, 145, 45, 95, 65, 120)
    canvas.create_rectangle(15, 185, 65, 215)

    canvas.create_line(40, 270, 40, 290)
    canvas.create_line(30, 280, 50, 280)
    canvas.create_line(35, 275, 45, 285)
    canvas.create_line(35, 285, 45, 275)

    for r in range(300):
        rpixelx = randint(40 - 20, 40 + 20)
        rpixely = randint(360 - 20, 360 + 20)
        if (rpixelx - 40) ** 2 + (rpixely - 360) ** 2 <= 20 ** 2:
            canvas.create_line(rpixelx, rpixely, rpixelx + 1, rpixely + 1, fill="black")

    canvas.create_rectangle(0, 400, 40, 440, fill="black")
    canvas.create_rectangle(40, 400, 80, 440, fill="red")
    canvas.create_rectangle(0, 440, 40, 480, fill="green")
    canvas.create_rectangle(40, 440, 80, 480, fill="blue")


clear(0)
root.bind("c", clear)
root.bind("<Button-1>", click)
root.bind("<B1-Motion>", drag)
root.bind("<ButtonRelease-1>", release)
root.mainloop()


# Potential Future Improvements:
#   - Indicate which tool is selected
#   - Indicate which color is selected
#   - Add more tools to use
#   - Add more colors to use
#   - Show preview of lines / rectangles before placing them
#   - Have spray-can continuously add more dots, even while cursor is still
#   - Stop spray-can from adding pixels to the side bar
#   - Add option to save / screen-shot image
#   - Fix all issues that occur when resizing the screen
