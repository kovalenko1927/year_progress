import datetime
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.title("---> 2023 YEAR PROGRESS --->")
root.geometry("400x300")


class Progress:
    def __init__(self):
        my_frame = customtkinter.CTkFrame(master=root)
        my_frame.pack(pady=20, padx=60, fill='both', expand=True)

        self.year_progress = customtkinter.CTkProgressBar(master=my_frame, height=15, width=250,
                                                          corner_radius=10, border_width=1)
        self.year_progress.pack(pady=25, padx=10)

        self.label = customtkinter.CTkLabel(master=my_frame, text="")
        self.label.pack(pady=10, padx=10)

        self.button = customtkinter.CTkButton(master=my_frame, text="Start", command=self.step)
        self.button.pack(pady=20)

    def step(self):
        x = (365 - (datetime.date(2023, 12, 31) - datetime.date.today()).days) / 3.65
        self.year_progress.set(value=x / 100)
        self.label.configure(text=f"{round(x, 2)}% of the year have already passed!\n"
                                  f"\n {datetime.date.today()}\n"
                                  f"\n{365 - (datetime.date(2023, 12, 31) - datetime.date.today()).days} / 365")


if __name__ == "__main__":
    pr = Progress()
    root.mainloop()