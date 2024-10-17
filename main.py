from tkinter import *
import pygame

pygame.mixer.init()

MAIN_BACKGROUND = "#E7E7E7"
MAIN_TITLE_COLOR = "#485696"
SUBTITLE_COLOR = "#E8871E"
BUTTON_BACKGROUND_COLOR = "#F24C00"

fading_colors = [
    "#E7E7E7",  # Background color (fully faded)
    "#D5E0DF",  # 10% opacity
    "#C3D9D7",  # 20% opacity
    "#B1D2CF",  # 30% opacity
    "#9FCBC7",  # 40% opacity
    "#8DC4BF",  # 50% opacity
    "#7BBDB7",  # 60% opacity
    "#69B6AF",  # 70% opacity
    "#57AFA7",  # 80% opacity
    "#45A89F",  # 90% opacity
    "#1B998B",  # Full text color (not faded)
]

DEFAULT_TIME = 12  # sec


class GUI:
    def __init__(self):

        self.root = Tk()
        self.root.title("Text Disappearing App")  # Sets the window title
        self.root.geometry("1000x600")  # Sets the window size (width x height)
        self.root.configure(bg=MAIN_BACKGROUND)  # Sets the window background color

        # Add an empty frame to simulate top padding
        self.top_padding = Frame(self.root, height=150, background=MAIN_BACKGROUND)

        self.label = Label(self.root,
                           text="",
                           bg=MAIN_BACKGROUND, fg=MAIN_TITLE_COLOR,
                           font=("Poppins", 25, "bold"),
                           pady=15)

        self.sub_label = Label(self.root,
                               text="Every second counts – type continuously to hold on to your words before\n they "
                                    "fade into nothingness!",
                               bg=MAIN_BACKGROUND, fg=SUBTITLE_COLOR,
                               font=("Poppins", 12))

        self.start_button = Button(self.root,
                                   text="Start Typing",
                                   font=("Poppins", 12),
                                   pady=12, padx=40,
                                   bg=BUTTON_BACKGROUND_COLOR, fg="white",
                                   bd=0,
                                   command=self.start)

        self.text_area = Text(self.root,
                              height=20, width=70,
                              bg=MAIN_BACKGROUND,
                              bd=0,
                              font=("Poppins", 14))
        self.text_area.focus_set()

        self.timer = DEFAULT_TIME  # time after which the text disappear
        self.home()

    def reset_timer(self, event):
        # if a user typed then the timer is reset
        self.text_area.configure(fg=fading_colors[-1])
        self.timer = DEFAULT_TIME

    def decrement(self):
        self.timer -= 1
        self.text_area.configure(fg=fading_colors[self.timer - 1])

        if self.timer == 1:
            self.play_sound()
            self.text_area.configure(fg="#ffc8dd")
            self.text_area.delete('1.0', END)
        else:
            self.root.after(1000, self.decrement)

    def start(self):
        self.top_padding.pack_forget()
        self.sub_label.pack_forget()
        self.start_button.pack_forget()

        self.label.configure(text="Keep Typing or Watch It Disappear!",
                             font=("Poppins", 22, "bold"),
                             pady=50)

        self.text_area.pack()

        self.decrement()

    def home(self):
        self.label.pack_forget()

        self.top_padding.pack()

        self.label.configure(text="Stay in Motion, or Your Text Disappears!", pady=15)
        self.label.pack()

        self.text_area.pack_forget()

        self.sub_label.pack()

        self.start_button.pack(pady=30)

    def play_sound(self):
        try:
            pygame.mixer.music.load('sound/sound effect.mp3')
        except pygame.error:
            pass
        else:
            pygame.mixer.music.play()
        self.root.after(300, self.home)


gui = GUI()
gui.root.bind("<KeyPress>", gui.reset_timer)
gui.root.mainloop()
