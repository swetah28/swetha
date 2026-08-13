# main.py - Nexus Bank 2026 | Application Entry Point

import customtkinter as ctk
from styles import COLORS, FONTS
from login_view import LoginView
from admin_view import AdminView
from customer_view import CustomerView

# Configure core settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")  # fallback

class NexusBankApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Setup Window
        self.title("Nexus Bank - Admin & Customer Portal (2026)")
        self.geometry("1100x700")
        self.minsize(900, 600)
        self.configure(fg_color=COLORS["bg_deep"])

        # Create main container
        self.container = ctk.CTkFrame(self, fg_color=COLORS["transparent"])
        self.container.pack(fill="both", expand=True)

        self.current_view = None
        self.logged_in_user = None

        self.show_login()

    def _clear_container(self):
        if self.current_view is not None:
            self.current_view.destroy()

    def show_login(self):
        self._clear_container()
        self.logged_in_user = None
        self.current_view = LoginView(self.container, self.handle_login_success)
        self.current_view.pack(fill="both", expand=True)

    def handle_login_success(self, user: dict):
        self.logged_in_user = user
        self._clear_container()

        if user["role"] == "admin":
            self.current_view = AdminView(self.container, user, self.show_login)
        else:
            self.current_view = CustomerView(self.container, user, self.show_login)

        self.current_view.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = NexusBankApp()
    app.mainloop()
