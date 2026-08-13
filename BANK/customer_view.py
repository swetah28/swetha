# customer_view.py - Nexus Bank 2026 | Customer Dashboard

import tkinter as tk
import customtkinter as ctk
from styles import COLORS, FONTS, PAD, RADIUS
import database as db
from datetime import datetime

class CustomerView(ctk.CTkFrame):
    def __init__(self, parent, user: dict, on_logout):
        super().__init__(parent, fg_color=COLORS["bg_dark"])
        self.user = user
        self.on_logout = on_logout
        self._build()
        self.refresh_data()

    def _build(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # ── Header Bar ───────────────────────────────────────────────────────
        hb = ctk.CTkFrame(self, fg_color=COLORS["bg_card"],
                          height=72, corner_radius=0)
        hb.grid(row=0, column=0, sticky="ew")
        hb.columnconfigure(1, weight=1)
        hb.grid_propagate(False)

        ctk.CTkLabel(hb, text="🏦", font=("Segoe UI Emoji", 32),
                     text_color=COLORS["primary"]).grid(row=0, column=0, padx=(24, 8), pady=16)

        greeting = ctk.CTkFrame(hb, fg_color=COLORS["transparent"])
        greeting.grid(row=0, column=1, sticky="w")
        ctk.CTkLabel(greeting, text=f"Welcome back,",
                     font=FONTS["small"], text_color=COLORS["text_secondary"]).grid(
            row=0, column=0, sticky="w", pady=(0, 0))
        ctk.CTkLabel(greeting, text=self.user["name"],
                     font=FONTS["heading"], text_color=COLORS["text_primary"]).grid(
            row=1, column=0, sticky="w", pady=0)

        # Logout & Settings btn container
        rc = ctk.CTkFrame(hb, fg_color=COLORS["transparent"])
        rc.grid(row=0, column=2, padx=24, sticky="e")
        ctk.CTkLabel(rc, text=self.user["acc_no"], font=FONTS["mono"],
                     text_color=COLORS["primary_light"]).pack(side="left", padx=16)
        ctk.CTkButton(rc, text="⏻ Logout", width=90, height=36,
                      font=FONTS["body_bold"], corner_radius=RADIUS["md"],
                      fg_color=COLORS["danger"], hover_color=COLORS["danger_dark"],
                      text_color=COLORS["white"], command=self.on_logout).pack(side="left")

        # ── Main Content Area ────────────────────────────────────────────────
        mc = ctk.CTkFrame(self, fg_color=COLORS["bg_dark"])
        mc.grid(row=1, column=0, sticky="nsew", padx=24, pady=24)
        mc.columnconfigure(0, weight=6)  # Left column (Balance + Actions)
        mc.columnconfigure(1, weight=4)  # Right column (History)
        mc.rowconfigure(0, weight=1)

        # ── Left Column (Balance & Actions) ──
        left_col = ctk.CTkFrame(mc, fg_color=COLORS["transparent"])
        left_col.grid(row=0, column=0, sticky="nsew", padx=(0, 12))
        left_col.columnconfigure(0, weight=1)
        # 1. Balance Card
        self.bal_card = ctk.CTkFrame(
            left_col, fg_color=COLORS["bg_card"], corner_radius=RADIUS["xl"],
            border_width=1, border_color=COLORS["border"])
        self.bal_card.grid(row=0, column=0, sticky="ew", pady=(0, 24))
        self.bal_card.columnconfigure(0, weight=1)

        ctk.CTkLabel(self.bal_card, text="Available Balance",
                     font=FONTS["body"], text_color=COLORS["text_secondary"]).grid(
            row=0, column=0, padx=32, pady=(24, 0), sticky="w")
        self.lbl_balance = ctk.CTkLabel(
            self.bal_card, text=f"₹{self.user['balance']:,.2f}",
            font=("Segoe UI", 48, "bold"), text_color=COLORS["white"])
        self.lbl_balance.grid(row=1, column=0, padx=32, pady=(0, 24), sticky="w")

        # 2. Action Area (Tabs for Deposit / Withdraw / PIN)
        self.action_card = ctk.CTkFrame(
            left_col, fg_color=COLORS["bg_card"], corner_radius=RADIUS["xl"],
            border_width=1, border_color=COLORS["border"])
        self.action_card.grid(row=1, column=0, sticky="nsew")
        self.action_card.columnconfigure((0, 1), weight=1)
        self.action_card.rowconfigure(1, weight=1)

        self.tab = ctk.CTkSegmentedButton(
            self.action_card,
            values=["Deposit", "Withdraw", "Change PIN"],
            font=FONTS["body_bold"],
            fg_color=COLORS["bg_surface"],
            selected_color=COLORS["primary"],
            selected_hover_color=COLORS["primary_dark"],
            unselected_color=COLORS["bg_surface"],
            unselected_hover_color=COLORS["bg_hover"],
            text_color=COLORS["text_primary"],
            height=40,
            command=self._switch_tab
        )
        self.tab.grid(row=0, column=0, columnspan=2, sticky="ew", padx=24, pady=(24, 16))

        self.tab_frames = {}
        self._build_deposit_tab()
        self._build_withdraw_tab()
        self._build_pin_tab()

        self.tab.set("Deposit")
        self._switch_tab("Deposit")

        # ── Right Column (Transaction History) ──
        right_col = ctk.CTkFrame(
            mc, fg_color=COLORS["bg_card"], corner_radius=RADIUS["xl"],
            border_width=1, border_color=COLORS["border"])
        right_col.grid(row=0, column=1, sticky="nsew", padx=(12, 0))
        right_col.columnconfigure(0, weight=1)
        right_col.rowconfigure(1, weight=1)

        ctk.CTkLabel(right_col, text="Recent Transactions", font=FONTS["heading"],
                     text_color=COLORS["text_primary"]).grid(
            row=0, column=0, padx=24, pady=(24, 16), sticky="w")

        self.hist_scroll = ctk.CTkScrollableFrame(
            right_col, fg_color=COLORS["transparent"], corner_radius=0)
        self.hist_scroll.grid(row=1, column=0, sticky="nsew", padx=12, pady=(0, 24))
        self.hist_scroll.columnconfigure(0, weight=1)

    # ── Action Tabs ──────────────────────────────────────────────────────────
    def _switch_tab(self, name):
        for f in self.tab_frames.values():
            f.grid_remove()
        self.tab_frames[name].grid(row=1, column=0, columnspan=2, sticky="nsew", padx=24, pady=(0, 24))

    def _build_deposit_tab(self):
        f = ctk.CTkFrame(self.action_card, fg_color=COLORS["transparent"])
        f.columnconfigure(0, weight=1)
        self.tab_frames["Deposit"] = f

        ctk.CTkLabel(f, text="Amount to Deposit (₹)", font=FONTS["body_bold"],
                     text_color=COLORS["text_secondary"], anchor="w").grid(row=0, column=0, sticky="w", pady=(0, 8))
        self.d_amt = ctk.CTkEntry(f, height=48, font=("Segoe UI", 20),
                                  fg_color=COLORS["bg_surface"], border_color=COLORS["border"],
                                  text_color=COLORS["text_primary"], corner_radius=RADIUS["md"])
        self.d_amt.grid(row=1, column=0, sticky="ew", pady=(0, 24))

        self.d_stat = ctk.CTkLabel(f, text="", font=FONTS["small"], text_color=COLORS["accent"])
        self.d_stat.grid(row=2, column=0, pady=(0, 8))

        ctk.CTkButton(f, text="Confirm Deposit", font=FONTS["body_bold"], height=48,
                      corner_radius=RADIUS["lg"],
                      fg_color=COLORS["accent"], hover_color=COLORS["accent_dark"],
                      text_color=COLORS["white"], command=self._do_deposit).grid(row=3, column=0, sticky="ew")

    def _build_withdraw_tab(self):
        f = ctk.CTkFrame(self.action_card, fg_color=COLORS["transparent"])
        f.columnconfigure(0, weight=1)
        self.tab_frames["Withdraw"] = f

        ctk.CTkLabel(f, text="Amount to Withdraw (₹)", font=FONTS["body_bold"],
                     text_color=COLORS["text_secondary"], anchor="w").grid(row=0, column=0, sticky="w", pady=(0, 8))
        self.w_amt = ctk.CTkEntry(f, height=48, font=("Segoe UI", 20),
                                  fg_color=COLORS["bg_surface"], border_color=COLORS["border"],
                                  text_color=COLORS["text_primary"], corner_radius=RADIUS["md"])
        self.w_amt.grid(row=1, column=0, sticky="ew", pady=(0, 24))

        self.w_stat = ctk.CTkLabel(f, text="", font=FONTS["small"], text_color=COLORS["danger"])
        self.w_stat.grid(row=2, column=0, pady=(0, 8))

        ctk.CTkButton(f, text="Confirm Withdraw", font=FONTS["body_bold"], height=48,
                      corner_radius=RADIUS["lg"],
                      fg_color=COLORS["warning_dark"], hover_color=COLORS["warning"],
                      text_color=COLORS["white"], command=self._do_withdraw).grid(row=3, column=0, sticky="ew")

    def _build_pin_tab(self):
        f = ctk.CTkFrame(self.action_card, fg_color=COLORS["transparent"])
        f.columnconfigure(1, weight=1)
        self.tab_frames["Change PIN"] = f

        def ent(r, t):
            ctk.CTkLabel(f, text=t, font=FONTS["body_bold"], text_color=COLORS["text_secondary"],
                         anchor="w").grid(row=r, column=0, sticky="w", pady=(0, 12), padx=(0, 16))
            e = ctk.CTkEntry(f, show="●", height=40, font=FONTS["body"],
                             fg_color=COLORS["bg_surface"], border_color=COLORS["border"],
                             text_color=COLORS["text_primary"], corner_radius=RADIUS["md"])
            e.grid(row=r, column=1, sticky="ew", pady=(0, 12))
            return e

        self.p_curr = ent(0, "Current PIN")
        self.p_new  = ent(1, "New PIN")
        self.p_conf = ent(2, "Confirm PIN")

        self.p_stat = ctk.CTkLabel(f, text="", font=FONTS["small"], text_color=COLORS["accent"])
        self.p_stat.grid(row=3, column=0, columnspan=2, pady=(8, 8))

        ctk.CTkButton(f, text="Update PIN", font=FONTS["body_bold"], height=44,
                      corner_radius=RADIUS["lg"],
                      fg_color=COLORS["primary"], hover_color=COLORS["primary_dark"],
                      text_color=COLORS["white"], command=self._do_pin_change).grid(row=4, column=0, columnspan=2, sticky="ew")

    # ── Action Logic ─────────────────────────────────────────────────────────
    def _do_deposit(self):
        try:
            amt = float(self.d_amt.get().strip())
            self.user = db.deposit(self.user["acc_no"], amt, "Online Deposit")
            self.d_stat.configure(text=f"✓ Deposited ₹{amt:,.2f} successfully.", text_color=COLORS["accent"])
            self.d_amt.delete(0, "end")
            self.refresh_data()
        except ValueError as e:
            self.d_stat.configure(text=f"✗ {e}", text_color=COLORS["danger"])

    def _do_withdraw(self):
        try:
            amt = float(self.w_amt.get().strip())
            self.user = db.withdraw(self.user["acc_no"], amt, "Online Withdrawal")
            self.w_stat.configure(text=f"✓ Withdrawn ₹{amt:,.2f} successfully.", text_color=COLORS["accent"])
            self.w_amt.delete(0, "end")
            self.refresh_data()
        except ValueError as e:
            self.w_stat.configure(text=f"✗ {e}", text_color=COLORS["danger"])

    def _do_pin_change(self):
        curr = self.p_curr.get().strip()
        n1 = self.p_new.get().strip()
        n2 = self.p_conf.get().strip()

        if not curr or not n1 or not n2:
            return self.p_stat.configure(text="⚠ All fields are required.", text_color=COLORS["warning"])
        if n1 != n2:
            return self.p_stat.configure(text="✗ New PINs do not match.", text_color=COLORS["danger"])
        if len(n1) != 4 or not n1.isdigit():
            return self.p_stat.configure(text="✗ PIN must be 4 digits.", text_color=COLORS["danger"])

        try:
            db.change_pin(self.user["acc_no"], curr, n1)
            self.p_stat.configure(text="✓ PIN successfully updated.", text_color=COLORS["accent"])
            for e in [self.p_curr, self.p_new, self.p_conf]: e.delete(0, "end")
        except ValueError as e:
            self.p_stat.configure(text=f"✗ {e}", text_color=COLORS["danger"])

    # ── Data Refresh ─────────────────────────────────────────────────────────
    def refresh_data(self):
        # Fresh user data handles external admin edits
        upd = db.get_user(self.user["acc_no"])
        if upd:
            self.user = upd
            self.lbl_balance.configure(text=f"₹{self.user['balance']:,.2f}")

        # Rebuild history
        for w in self.hist_scroll.winfo_children():
            w.destroy()

        txs = db.get_transactions(self.user["acc_no"])
        if not txs:
            ctk.CTkLabel(self.hist_scroll, text="No transactions found.",
                         font=FONTS["body"], text_color=COLORS["text_muted"]).pack(pady=40)
            return

        for t in txs:
            frame = ctk.CTkFrame(self.hist_scroll, fg_color=COLORS["bg_surface"],
                                 corner_radius=RADIUS["md"])
            frame.pack(fill="x", padx=12, pady=6)
            frame.columnconfigure(1, weight=1)

            is_cr = (t["type"] == "CREDIT")
            icon  = "↓" if is_cr else "↑"
            color = COLORS["accent"] if is_cr else COLORS["warning"]

            # Icon circle
            ic = ctk.CTkFrame(frame, width=40, height=40, corner_radius=20,
                              fg_color=color if is_cr else COLORS["danger_dark"])
            ic.grid(row=0, column=0, rowspan=2, padx=12, pady=12)
            ic.pack_propagate(False)
            ctk.CTkLabel(ic, text=icon, font=("Segoe UI", 18, "bold"),
                         text_color=COLORS["white"]).pack(expand=True)

            # Details
            dt = datetime.strptime(t["timestamp"], "%Y-%m-%d %H:%M:%S")
            ctk.CTkLabel(frame, text=t["description"], font=FONTS["body_bold"],
                         text_color=COLORS["text_primary"], anchor="w").grid(
                row=0, column=1, sticky="w", padx=8, pady=(12, 0))
            ctk.CTkLabel(frame, text=dt.strftime("%d %b %Y, %H:%M"), font=FONTS["tiny"],
                         text_color=COLORS["text_secondary"], anchor="w").grid(
                row=1, column=1, sticky="w", padx=8, pady=(0, 12))

            # Amount & Balance
            sign = "+" if is_cr else "-"
            amt_color = COLORS["accent"] if is_cr else COLORS["text_primary"]
            ctk.CTkLabel(frame, text=f"{sign} ₹{t['amount']:,.2f}",
                         font=FONTS["subhead"], text_color=amt_color, anchor="e").grid(
                row=0, column=2, sticky="e", padx=16, pady=(12, 0))
            ctk.CTkLabel(frame, text=f"Bal: ₹{t['balance_after']:,.2f}",
                         font=FONTS["tiny"], text_color=COLORS["text_muted"], anchor="e").grid(
                row=1, column=2, sticky="e", padx=16, pady=(0, 12))
