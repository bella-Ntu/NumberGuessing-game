import random
import tkinter as tk
from tkinter import messagebox

def guess_game():
    root = tk.Tk()
    root.title('Number Guessing Game')
    root.geometry('420x300')

    lower = 1
    upper = 100
    secret = random.randint(lower,upper)
    attempts_left = 7

    instruction = tk.Label(root, text=f'Guess the number between {lower} and {upper}',
             font=('Arial', 12, 'bold'))
    instruction.pack(pady=15)
    
    entry = tk.Entry(root, font=('Arial', 18), width=8, justify='center')
    entry.pack(pady=10)

    status = tk.Label(root, text='', font=('Arial', 12))
    status.pack(pady=10)

    attempts_label = tk.Label(root, text=f'Attempts left: {attempts_left}',
                              font=('Arial', 11))
    attempts_label.pack(pady=5)

    def update_display():
        instruction.config(text=f'Guess the number between {lower} and {upper}')
        root.title(f'Guess Number (1 - {upper})')

    def make_guess():
        nonlocal attempts_left, secret

        try:
            guess = int(entry.get())
        except ValueError:
            messagebox.showerror('Invalid', 'Please enter a whole number!')
            entry.delete(0, tk.END)
            return

        attempts_left -= 1
        attempts_label.config(text=f'Attempts left: {attempts_left}')

        if guess < secret:
            status.config(text='Too Low!', fg='blue')
        elif guess > secret:
            status.config(text='Too High!', fg='red')
        else:
            messagebox.showinfo('🎉🎉Congragulations!',
                                f'You got it right in {7- attempts_left} attempts!🎉🎉')

            play_again()
            return

        entry.delete(0, tk.END)

        if attempts_left <= 0:
            messagebox.showinfo('Game Over 🕹️', f'The number was {secret}')
            play_again()

    def play_again():
        nonlocal secret, upper, attempts_left

        if messagebox.askyesno('Play Again?', 'Do you want to play another round?'):
            upper += 50
            secret = random.randint(lower, upper)
            attempts_left = 7
            attempts_label.config(text=f'Attemptsleft: {attempts_left}')
            status.config(text='')
            update_display()
            entry.delete(0, tk.END)
            entry.focus()
        else:
            messagebox.showinfo('Thanks for playing! See you next time👋')   
            root.destroy()

    tk.Button(root, text='Guess', font=('Arial', 12), width=12,
              command=make_guess).pack(pady=12)
    tk.Button(root, text='Qut', font=('Arial', 10),
              command=root.destroy).pack()
    
    update_display()
    entry.focus()

    root.mainloop()

if __name__ == "__main__":
    guess_game()                                 

        
                                                        #ALITUHA SHABELLA   25/BSE/BU/R/0016