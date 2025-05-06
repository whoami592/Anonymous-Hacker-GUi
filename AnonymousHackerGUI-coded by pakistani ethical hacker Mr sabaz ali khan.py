import tkinter as tk
from tkinter import ttk, messagebox
import time
import threading
import random
from PIL import Image, ImageTk
import os

class AnonymousHackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Anonymous Hacker Super Computer - By Sabaz Ali Khan")
        self.root.geometry("1000x600")
        self.root.configure(bg="#0a0a0a")
        self.root.resizable(False, False)

        # Header
        self.header = tk.Label(
            root,
            text="ANONYMOUS HACKER SUPER COMPUTER",
            font=("Courier", 24, "bold"),
            fg="#00ff00",
            bg="#0a0a0a",
            pady=10
        )
        self.header.pack()

        # Attribution
        self.credit = tk.Label(
            root,
            text="Coded by Pakistani Ethical Hacker: Mr. Sabaz Ali Khan",
            font=("Courier", 12),
            fg="#00ff00",
            bg="#0a0a0a"
        )
        self.credit.pack()

        # Main frame
        self.main_frame = tk.Frame(root, bg="#0a0a0a")
        self.main_frame.pack(pady=20, fill="both", expand=True)

        # Terminal display
        self.terminal = tk.Text(
            self.main_frame,
            height=15,
            width=80,
            font=("Courier", 12),
            fg="#00ff00",
            bg="#1a1a1a",
            bd=2,
            relief="solid"
        )
        self.terminal.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        self.terminal.insert(tk.END, "Initializing Anonymous Hacker Super Computer...\n")
        self.terminal.config(state="disabled")

        # Button frame
        self.button_frame = tk.Frame(self.main_frame, bg="#0a0a0a")
        self.button_frame.grid(row=1, column=0, columnspan=2, pady=10)

        # Buttons
        self.scan_btn = tk.Button(
            self.button_frame,
            text="Scan Network",
            command=self.simulate_scan,
            font=("Courier", 12, "bold"),
            fg="#00ff00",
            bg="#1a1a1a",
            activebackground="#00ff00",
            activeforeground="#0a0a0a",
            width=15
        )
        self.scan_btn.grid(row=0, column=0, padx=5)

        self.hack_btn = tk.Button(
            self.button_frame,
            text="Simulate Hack",
            command=self.simulate_hack,
            font=("Courier", 12, "bold"),
            fg="#00ff00",
            bg="#1a1a1a",
            activebackground="#00ff00",
            activeforeground="#0a0a0a",
            width=15
        )
        self.hack_btn.grid(row=0, column=1, padx=5)

        self.status_btn = tk.Button(
            self.button_frame,
            text="System Status",
            command=self.show_status,
            font=("Courier", 12, "bold"),
            fg="#00ff00",
            bg="#1a1a1a",
            activebackground="#00ff00",
            activeforeground="#0a0a0a",
            width=15
        )
        self.status_btn.grid(row=0, column=2, padx=5)

        # Progress bar
        self.progress = ttk.Progressbar(
            self.main_frame,
            length=400,
            mode="determinate",
            style="green.Horizontal.TProgressbar"
        )
        self.progress.grid(row=2, column=0, columnspan=2, pady=10)

        # Style for progress bar
        style = ttk.Style()
        style.theme_use("default")
        style.configure(
            "green.Horizontal.TProgressbar",
            troughcolor="#1a1a1a",
            background="#00ff00",
            bordercolor="#00ff00"
        )

        # Animation thread
        self.running = True
        self.animation_thread = threading.Thread(target=self.animate_terminal)
        self.animation_thread.daemon = True
        self.animation_thread.start()

    def type_effect(self, text):
        self.terminal.config(state="normal")
        for char in text:
            self.terminal.insert(tk.END, char)
            self.terminal.see(tk.END)
            self.root.update()
            time.sleep(0.03)
        self.terminal.insert(tk.END, "\n")
        self.terminal.config(state="disabled")

    def animate_terminal(self):
        while self.running:
            self.terminal.config(state="normal")
            self.terminal.insert(tk.END, ".")
            self.terminal.see(tk.END)
            self.terminal.config(state="disabled")
            self.root.update()
            time.sleep(0.5)

    def simulate_scan(self):
        threading.Thread(target=self._scan_network, daemon=True).start()

    def _scan_network(self):
        self.terminal.config(state="normal")
        self.terminal.delete(1.0, tk.END)
        self.terminal.config(state="disabled")
        self.type_effect("Initiating Network Scan...")
        for i in range(101):
            self.progress["value"] = i
            self.root.update()
            time.sleep(0.05)
        self.type_effect("Scan Complete. Found 192.168.1.0/24")
        self.type_effect("Devices: 10 | Vulnerabilities: 3")
        messagebox.showinfo("Scan Complete", "Network scan completed successfully!")

    def simulate_hack(self):
        threading.Thread(target=self._hack_simulation, daemon=True).start()

    def _hack_simulation(self):
        self.terminal.config(state="normal")
        self.terminal.delete(1.0, tk.END)
        self.terminal.config(state="disabled")
        self.type_effect("Starting Hack Simulation...")
        for i in range(101):
            self.progress["value"] = i
            self.root.update()
            time.sleep(0.03)
        self.type_effect("Accessing target system...")
        self.type_effect("Bypassing firewall... Done")
        self.type_effect("Simulation Complete. No actual systems harmed.")
        messagebox.showinfo("Hack Simulation", "Simulation completed successfully!")

    def show_status(self):
        self.terminal.config(state="normal")
        self.terminal.delete(1.0, tk.END)
        self.terminal.config(state="disabled")
        self.type_effect("System Status Report:")
        self.type_effect(f"CPU Usage: {random.randint(10, 90)}%")
        self.type_effect(f"Memory Usage: {random.randint(20, 80)}%")
        self.type_effect("Network: Online")
        self.type_effect("All systems operational.")

    def destroy(self):
        self.running = False
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AnonymousHackerGUI(root)
    root.mainloop()