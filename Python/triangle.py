from tkinter import *
from R2Graph import *
from geom import *

def main():
    rootWindow = Tk()
    rootWindow.title("Triangle")
    rootWindow.geometry("800x600")

    drawArea = Canvas(
        rootWindow, 
        width = 800 - 8*2, 
        height = 600 - 24 - 8*2,
        bg = "white"
    )
    drawArea.place(anchor="nw", x = 8, y = 8 + 24);

    points = []

    def clear():
        points.clear()
        drawArea.delete("all");

    def drawTriangle():
        drawArea.create_line(
            points[0].x, points[0].y,
            points[1].x, points[1].y,
            points[2].x, points[2].y,
            points[0].x, points[0].y,
            fill="blue", width=2
        )
        (center, radius) = incircle(
            points[0], points[1], points[2]
        )
        drawArea.create_oval(
            center.x-radius, center.y-radius,
            center.x+radius, center.y+radius,
            fill="", outline="darkGreen"
        )

    def click(e):
        if len(points) == 3:
            clear()
        # points.append((e.x, e.y))
        points.append(R2Point(e.x, e.y))
        drawArea.create_line(
            e.x-8, e.y, e.x+8, e.y, fill="red", width=3
        )
        drawArea.create_line(
            e.x, e.y-8, e.x, e.y+8, fill="red", width=3
        )
        if len(points) == 3:
            drawTriangle()

    drawArea.bind(
        "<Button-1>", click
    )

    clearButton = Button(
        text="Clear", width=40, height=16, command=clear
    )
    clearButton.place(
        anchor="nw", x=8, y=8, height=24, width=48
    )

    rootWindow.mainloop()

if __name__ == "__main__":
    main()
