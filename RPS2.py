import random
import tkinter as tk

# Map computer choices
computer_value = {0: "Rock", 1: "Paper", 2: "Scissor"}

def reset_game():
    b1["state"] = b2["state"] = b3["state"] = "normal"
    player_label.config(text="Player")
    comp_label.config(text="Computer")
    result_label.config(text="")

def disable_buttons():
    b1["state"] = b2["state"] = b3["state"] = "disabled"

def play(user_choice):
    comp_choice = computer_value[random.randint(0, 2)]
    player_label.config(text=user_choice)
    comp_label.config(text=comp_choice)

    if user_choice == comp_choice:
        result = "Match Draw"
    elif (user_choice, comp_choice) in [("Rock", "Scissor"), ("Paper", "Rock"), ("Scissor", "Paper")]:
        result = "You Win!"
    else:
        result = "Computer Wins!"
    result_label.config(text=result)
    disable_buttons()

# Setup GUI
root = tk.Tk()
root.title("Rock Paper Scissor Game")
root.geometry("300x300")

tk.Label(root, text="Rock Paper Scissor", font="bold 16").pack(pady=10)

frame = tk.Frame(root)
frame.pack()

player_label = tk.Label(frame, text="Player", font=12, width=8)
tk.Label(frame, text="vs", font=12).pack(side="left")
comp_label = tk.Label(frame, text="Computer", font=12, width=10)
player_label.pack(side="left")
comp_label.pack(side="left")

result_label = tk.Label(root, text="", font="bold 14", pady=10)
result_label.pack()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
b1 = tk.Button(btn_frame, text="Rock", width=8, command=lambda: play("Rock"))
b2 = tk.Button(btn_frame, text="Paper", width=8, command=lambda: play("Paper"))
b3 = tk.Button(btn_frame, text="Scissor", width=8, command=lambda: play("Scissor"))
b1.pack(side="left", padx=5)
b2.pack(side="left", padx=5)
b3.pack(side="left", padx=5)

tk.Button(root, text="Reset Game", command=reset_game, fg="red").pack(pady=10)

root.mainloop()
