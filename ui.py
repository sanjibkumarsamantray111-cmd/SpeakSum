import customtkinter as ctk
from mic_test import listen_once

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class AICalculatorUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x600")
        self.root.title("AI Voice Calculator")
        self.root.configure(fg_color="#0f0fa8")

        self.expression = ""

        self.build_ui()

    def build_ui(self):

        # ================= LEFT MAIN AREA =================
        self.main_frame = ctk.CTkFrame(
            self.root,
            fg_color="#1414b8",
            corner_radius=0
        )
        self.main_frame.pack(side="left", fill="both", expand=True)

        # Title
        title = ctk.CTkLabel(
            self.main_frame,
            text="AI VOICE CALC ✦",
            font=("Arial", 20, "bold"),
            text_color="#cfd2ff"
        )
        title.pack(anchor="nw", padx=30, pady=30)

        # Display
        self.display_label = ctk.CTkLabel(
            self.main_frame,
            text="Say a number...",
            font=("Arial", 60, "italic"),
            text_color="#6f7cff"
        )
        self.display_label.pack(expand=True)

        # Mic Button
        self.mic_active = False

        self.mic_button = ctk.CTkButton(
            self.main_frame,
            text="🎙️❌",   # mic with slash initially
            font=("Arial", 40),
            width=180,
            height=120,
            corner_radius=60,
            fg_color="#3c3cff",
            hover_color="#5757ff",
            command=self.voice_input
        )
        self.mic_button.pack(pady=20)

        # ================= RIGHT SIDE PANEL =================
        self.side_panel = ctk.CTkFrame(
            self.root,
            width=180,
            fg_color="#1a1ad1",
            corner_radius=0
        )
        self.side_panel.pack(side="right", fill="y")

        button_data = [
            ("C", self.clear, "#ff4d4d"),
            ("÷", None, "#2e2eff"),
            ("×", None, "#2e2eff"),
            ("−", None, "#2e2eff"),
            ("=", self.calculate, "#5ea2ff"),
        ]

        for text, command, color in button_data:
            btn = ctk.CTkButton(
                self.side_panel,
                text=text,
                font=("Arial", 24, "bold"),
                width=120,
                height=90,
                corner_radius=30,
                fg_color=color,
                hover_color="#6f7cff",
                command=command
            )
            btn.pack(pady=20)

    # 🎤 MIC LOGIC CONNECTED HERE
    def voice_input(self):
        self.mic_button.configure(text="🎙️")
        self.root.update()

        new_expr = listen_once()

        self.mic_button.configure(text="🎙️❌")

        if new_expr:
            cleaned = new_expr.replace(" + ", "+")

            if self.expression:
                self.expression += "+" + cleaned
            else:
                self.expression = cleaned

            self.display_label.configure(
                text=self.expression,
                font=("Arial", 50, "bold"),
                text_color="white"
            )

    # 🟰 CALCULATION
    def calculate(self):
        try:
            result = eval(self.expression)
            self.display_label.configure(
                text=str(result),
                font=("Arial", 70, "bold"),
                text_color="#ffffff"
            )
        except:
            self.display_label.configure(text="Error")

    # 🧹 CLEAR
    def clear(self):
        self.expression = ""
        self.display_label.configure(
            text="Say a number...",
            font=("Arial", 60, "italic"),
            text_color="#6f7cff"
        )


if __name__ == "__main__":
    root = ctk.CTk()
    app = AICalculatorUI(root)
    root.mainloop()