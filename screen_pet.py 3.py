from tkinter import HIDDEN, NORMAL,Tk, Canvas
root=Tk()

c=Canvas(root, width=800, height=800)
c.configure(bg='dark blue',highlightthickness=0)

c.body_color = 'Sky Blue1'
body = c.create_oval(70, 40, 730, 700, outline=c.body_color, fill=c.body_color)
ear_left = c.create_polygon(150, 160, 150, 20, 330, 140, outline=c.body_color, fill=c.body_color)
ear_right = c.create_polygon(510, 90, 650, 20, 640, 140, outline=c.body_color, \
fill=c.body_color)
foot_left = c.create_oval(130, 640, 290, 720, outline=c.body_color, fill= c.body_color)
foot_right = c.create_oval(500, 640, 660, 720, outline=c.body_color, fill=c.body_color)
eye_left = c.create_oval(260, 220, 320, 340, outline='black', fill='white')
pupil_left = c.create_oval(280, 290, 300, 310, outline='black', fill='black')
eye_right = c.create_oval(460, 220, 520, 340, outline='black', fill='white')
pupil_right = c.create_oval(480, 290, 500, 310,outline='black', fill='black')
mouth_normal = c.create_line(340, 500, 400, 544, 460, 500, smooth=1, width=2,state=NORMAL)
c.pack()
root.mainloop()

def toggle_eyes():
    current_color = c.itemcget(eye_left, 'fill')
    new_color = c.body_color if current_color == 'white' else 'white'
    current_state = c.itemcget(pupil_left, 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(pupil_right, state=new_state)
    c.itemconfigure(eye_left, fill=new_color)
    c.itemconfigure(eye_right, fill=new_color)

def blink():    
        toggle_eyes()
        root.after(250, toggle_eyes)
        root.after(3000, blink)
root=Tk()

mouth_normal = c.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2, state=NORMAL)

mouth_happy = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN)
mouth_sad = c.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2, state=HIDDEN)
cheek_left = c.create_oval(70, 180, 120, 230, outline='pink', fill='pink', state=HIDDEN)
cheek_right = c.creat_oval9(280, 180, 330, 230,  outline='pink', fill='pink', state=HIDDEN)

c.pack()

root.after(1000, blink)
def show_happy(event):
    if (20 <= event.x <= 350) and (20 <= event.y <= 350):
        c.itemconfigure(cheek_left, state=NORMAL)
        c.itemconfigure(cheek_right, state=NORMAL)
        c.itemconfigure(mouth_happy,state=NORMAL)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_sad, state=HIDDEN)
    return
def hide_happy(event):
    c.itemconfigure(cheek_left, state=HIDDEN)
    c.itemconfigure(cheek_right, state=HIDDEN)
    c.itemconfigure(mouth_happy, state=HIDDEN)
    c.itemconfigure(mouth_normal, state=NORMAL)
    c.itemconfigure(mouth_sad, state=HIDDEN)
    return
c.bind('<Motion>', show_happy)
c.bind('<Leave>', hide_happy)
root.mainloop()
                    



                        
root.mainloop()
