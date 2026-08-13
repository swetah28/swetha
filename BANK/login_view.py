# login_view.py - Nexus Bank 2026 | Login Screen

import tkinter as tk
import customtkinter as ctk
from styles import COLORS, FONTS, PAD, RADIUS

class LoginView(ctk.CTkFrame):
    def __init__(self, parent, on_login_success):
        super().__init__(parent, fg_color=COLORS["bg_dark"])
        self.on_login_success = on_login_success
        self._build()

    def _build(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # ── Center card ──────────────────────────────────────────────────────
        card = ctk.CTkFrame(
            self,
            fg_color=COLORS["bg_card"],
            corner_radius=RADIUS["xxl"],
            border_width=1,
            border_color=COLORS["border_light"],
            width=420,
        )
        card.grid(row=0, column=0, padx=40, pady=40, sticky="nsew")
        card.grid_propagate(False)
        card.columnconfigure(0, weight=1)

        # ── Logo / Bank name ─────────────────────────────────────────────────
        logo_frame = ctk.CTkFrame(card, fg_color=COLORS["transparent"])
        logo_frame.grid(row=0, column=0, pady=(36, 0), padx=40, sticky="ew")
        logo_frame.columnconfigure(0, weight=1)

        ctk.CTkLabel(
            logo_frame,
            text="🏦",
            font=("Segoe UI Emoji", 48),
            text_color=COLORS["primary"],
        ).grid(row=0, column=0)

        ctk.CTkLabel(
            logo_frame,
            text="N E X U S   B A N K",
            font=("Segoe UI", 22, "bold"),
            text_color=COLORS["text_primary"],
        ).grid(row=1, column=0, pady=(6, 0))

        ctk.CTkLabel(
            logo_frame,
            text="Secure · Smart · Modern",
            font=FONTS["small"],
            text_color=COLORS["text_secondary"],
        ).grid(row=2, column=0, pady=(2, 0))

        # ── Divider ───────────────────────────────────────────────────────────
        ctk.CTkFrame(
            card, height=1, fg_color=COLORS["border"], corner_radius=0
        ).grid(row=1, column=0, sticky="ew", padx=40, pady=24)

        # ── Form ──────────────────────────────────────────────────────────────
        form = ctk.CTkFrame(card, fg_color=COLORS["transparent"])
        form.grid(row=2, column=0, padx=40, sticky="ew")
        form.columnconfigure(0, weight=1)

        # Role selector
        ctk.CTkLabel(
            form, text="LOGIN AS",
            font=("Segoe UI", 10, "bold"),
            text_color=COLORS["text_muted"],
        ).grid(row=0, column=0, sticky="w", pady=(0, 6))

        self.role_var = tk.StringVar(value="Customer")
        role_seg = ctk.CTkSegmentedButton(
            form,
            values=["Customer", "Admin"],
            variable=self.role_var,
            font=FONTS["body_bold"],
            fg_color=COLORS["bg_surface"],
            selected_color=COLORS["primary"],
            selected_hover_color=COLORS["primary_dark"],
            unselected_color=COLORS["bg_surface"],
            unselected_hover_color=COLORS["bg_hover"],
            text_color=COLORS["text_primary"],
            corner_radius=RADIUS["lg"],
            height=38,
        )
        role_seg.grid(row=1, column=0, sticky="ew", pady=(0, 20))

        # Account number
        ctk.CTkLabel(
            form, text="ACCOUNT NUMBER",
            font=("Segoe UI", 10, "bold"),
            text_color=COLORS["text_muted"],
        ).grid(row=2, column=0, sticky="w", pady=(0, 6))

        self.acc_entry = ctk.CTkEntry(
            form,
            placeholder_text="e.g. ADMIN001 or ACCxxxxxxx",
            height=44,
            font=FONTS["body"],
            fg_color=COLORS["bg_surface"],
            border_color=COLORS["border"],
            text_color=COLORS["text_primary"],
            placeholder_text_color=COLORS["text_muted"],
            corner_radius=RADIUS["md"],
        )
        self.acc_entry.grid(row=3, column=0, sticky="ew", pady=(0, 16))

        # PIN
        ctk.CTkLabel(
            form, text="PIN",
            font=("Segoe UI", 10, "bold"),
            text_color=COLORS["text_muted"],
        ).grid(row=4, column=0, sticky="w", pady=(0, 6))

        self.pin_entry = ctk.CTkEntry(
            form,
            placeholder_text="Enter your 4-digit PIN",
            show="●",
            height=44,
            font=FONTS["body"],
            fg_color=COLORS["bg_surface"],
            border_color=COLORS["border"],
            text_color=COLORS["text_primary"],
            placeholder_text_color=COLORS["text_muted"],
            corner_radius=RADIUS["md"],
        )
        self.pin_entry.grid(row=5, column=0, sticky="ew", pady=(0, 8))

        # Show/hide PIN toggle
        self.show_pin = tk.BooleanVar(value=False)
        ctk.CTkCheckBox(
            form,
            text="Show PIN",
            variable=self.show_pin,
            command=self._toggle_pin,
            font=FONTS["small"],
            text_color=COLORS["text_secondary"],
            fg_color=COLORS["primary"],
            hover_color=COLORS["primary_dark"],
            border_color=COLORS["border_light"],
            corner_radius=RADIUS["sm"],
        ).grid(row=6, column=0, sticky="w", pady=(0, 20))

        # Login button
        self.login_btn = ctk.CTkButton(
            form,
            text="  Sign In  →",
            font=("Segoe UI", 14, "bold"),
            height=48,
            corner_radius=RADIUS["lg"],
            fg_color=COLORS["primary"],
            hover_color=COLORS["primary_dark"],
            text_color=COLORS["white"],
            command=self._attempt_login,
        )
        self.login_btn.grid(row=7, column=0, sticky="ew", pady=(0, 4))

        # Status / error label
        self.status_lbl = ctk.CTkLabel(
            form, text="",
            font=FONTS["small"],
            text_color=COLORS["danger"],
            wraplength=340,
        )
        self.status_lbl.grid(row=8, column=0, pady=(6, 0))

        # ── Footer hint ───────────────────────────────────────────────────────
        ctk.CTkLabel(
            card,
            text="Default Admin → ADMIN001 | PIN: 1234",
            font=FONTS["tiny"],
            text_color=COLORS["text_muted"],
        ).grid(row=3, column=0, pady=(16, 28))

        # Enter key binding
        self.pin_entry.bind("<Return>", lambda e: self._attempt_login())
        self.acc_entry.bind("<Return>", lambda e: self.pin_entry.focus())

    def _toggle_pin(self):
        self.pin_entry.configure(show="" if self.show_pin.get() else "●")

    def _attempt_login(self):
        import database as db
        acc = self.acc_entry.get().strip()
        pin = self.pin_entry.get().strip()
        role = self.role_var.get().lower()

        if not acc or not pin:
            self._set_status("⚠  Please enter Account Number and PIN.", COLORS["warning"])
            return

        self.login_btn.configure(text="Verifying…", state="disabled")
        self.after(400, lambda: self._verify(acc, pin, role))

    def _verify(self, acc, pin, role):
        import database as db
        user = db.authenticate(acc, pin)
        self.login_btn.configure(text="  Sign In  →", state="normal")

        if user is None:
            self._set_status("✗  Invalid account number or PIN.", COLORS["danger"])
            self._shake()
            return

        if user["role"] != role:
            self._set_status(
                f"✗  This account is not a {role.title()} account.", COLORS["danger"]
            )
            self._shake()
            return

        self._set_status("✓  Authenticated!", COLORS["accent"])
        self.after(300, lambda: self.on_login_success(user))

    def _set_status(self, msg, color):
        self.status_lbl.configure(text=msg, text_color=color)

    def _shake(self):
        """Horizontal shake animation on the card."""
        card = self.winfo_children()[0]
        orig_x = card.winfo_x()
        offsets = [8, -8, 6, -6, 4, -4, 0]
        def step(i=0):
            if i < len(offsets):
                card.place(x=orig_x + offsets[i])
                self.after(40, lambda: step(i + 1))
        step()

    def clear(self):
        self.acc_entry.delete(0, "end")
        self.pin_entry.delete(0, "end")
        self._set_status("", COLORS["danger"])
