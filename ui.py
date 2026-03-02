import customtkinter as ctk
import threading
from mic_test import listen_once
import re
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class AICalculatorUI:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x650")
        self.root.title("AI Voice Calculator")

        # Store spoken numbers
        self.numbers = []

        # Main frame
        self.main_frame = ctk.CTkFrame(root, fg_color="#8E8CD8")
        self.main_frame.pack(fill="both", expand=True)

        # Title
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="VOICE CALC ✨",
            font=("Arial", 24, "bold")
        )
        self.title_label.place(x=40, y=30)

        # Display
        self.display_label = ctk.CTkLabel(
            self.main_frame,
            text="Say numbers...",
            font=("Arial", 50, "italic")
        )
        self.display_label.place(relx=0.5, rely=0.35, anchor="center")

        # Mic Button
        self.mic_button = ctk.CTkButton(
            self.main_frame,
            text="🎤",
            width=200,
            height=80,
            corner_radius=40,
            font=("Arial", 28),
            command=self.start_listening
        )
        self.mic_button.place(relx=0.5, rely=0.75, anchor="center")

        # Buttons
        self.create_buttons()

    # =========================
    # THREADING
    # =========================

    def start_listening(self):
        thread = threading.Thread(target=self.listen)
        thread.daemon = True
        thread.start()

    def listen(self):
        try:
            text = listen_once()
            if text:
                self.root.after(0, lambda: self.process_text(text))
        except:
            self.root.after(0, lambda: self.display_label.configure(text="Error"))

    # =========================
    # PROCESS SPOKEN TEXT
    # =========================

    def process_text(self, text):
        try:
            numbers_found = re.findall(r"\d+", text)
            
            if not numbers_found:
                self.display_label.configure(text="Invalid")
                return

            for num in numbers_found:
                self.numbers.append(float(num))


            # Show numbers on screen
            display_text = " + ".join(str(int(n)) for n in self.numbers)
            self.display_label.configure(text=display_text)

        except Exception as e:
            print("DEBUG ERROR:", e)
            self.display_label.configure(text="Invalid")

    # =========================
    # BUTTONS
    # =========================

    def create_buttons(self):

        buttons = ["C","-", "÷", "="]
        y_positions = [150, 250, 350, 450]

        for btn_text, y in zip(buttons, y_positions):

            btn = ctk.CTkButton(
                self.main_frame,
                text=btn_text,
                width=120,
                height=70,
                corner_radius=30,
                font=("Arial", 24),
                command=lambda t=btn_text: self.button_clicked(t)
            )

            btn.place(x=950, y=y)

    # =========================
    # BUTTON LOGIC
    # =========================

    def button_clicked(self, text):

        if text == "C":
            self.numbers = []
            self.display_label.configure(text="Say numbers...")
            return

        if text == "=":
            if not self.numbers:
                return

            total = sum(self.numbers)
            self.display_label.configure(text=str(total))

            # Reset for next calculation
            self.numbers = [total]


# =========================
# RUN APP
# =========================

if __name__ == "__main__":
    root = ctk.CTk()
    app = AICalculatorUI(root)
    root.mainloop()