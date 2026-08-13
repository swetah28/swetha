# admin_view.py - Nexus Bank 2026 | Admin Dashboard

import tkinter as tk
import customtkinter as ctk
from styles import COLORS, FONTS, PAD, RADIUS
import database as db
from datetime import datetime


# ─── Reusable Card widget ────────────────────────────────────────────────────────
class StatCard(ctk.CTkFrame):
    def __init__(self, parent, icon, label, value, accent):
        super().__init__(
            parent,
            fg_color=COLORS["bg_card"],
            corner_radius=RADIUS["lg"],
            border_width=1,
            border_color=COLORS["border"],
        )
        self.columnconfigure(0, weight=1)
        ctk.CTkLabel(self, text=icon, font=("Segoe UI Emoji", 28)).grid(
            row=0, column=0, pady=(18, 4))
        self.val_lbl = ctk.CTkLabel(
            self, text=value, font=("Segoe UI", 22, "bold"), text_color=accent)
        self.val_lbl.grid(row=1, column=0)
        ctk.CTkLabel(self, text=label, font=FONTS["small"],
                     text_color=COLORS["text_secondary"]).grid(
            row=2, column=0, pady=(2, 16))

    def update_value(self, v): self.val_lbl.configure(text=v)


# ─── Main Admin Dashboard ────────────────────────────────────────────────────────
class AdminView(ctk.CTkFrame):
    def __init__(self, parent, user: dict, on_logout):
        super().__init__(parent, fg_color=COLORS["bg_dark"])
        self.user = user
        self.on_logout = on_logout
        self._build()
        self.refresh_stats()

    # ── Layout skeleton ──────────────────────────────────────────────────────
    def _build(self):
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self._build_sidebar()
        self._build_main_area()

    # ── Sidebar ──────────────────────────────────────────────────────────────
    def _build_sidebar(self):
        sb = ctk.CTkFrame(
            self, fg_color=COLORS["bg_card"], width=220,
            corner_radius=0, border_width=0)
        sb.grid(row=0, column=0, sticky="nsew")
        sb.grid_propagate(False)
        sb.columnconfigure(0, weight=1)

        # Brand
        ctk.CTkLabel(sb, text="🏦", font=("Segoe UI Emoji", 36),
                     text_color=COLORS["primary"]).grid(
            row=0, column=0, pady=(30, 0))
        ctk.CTkLabel(sb, text="NEXUS BANK", font=("Segoe UI", 14, "bold"),
                     text_color=COLORS["text_primary"]).grid(row=1, column=0)
        ctk.CTkLabel(sb, text="Admin Portal", font=FONTS["small"],
                     text_color=COLORS["gold"]).grid(row=2, column=0, pady=(2, 24))

        # Divider
        ctk.CTkFrame(sb, height=1, fg_color=COLORS["border"],
                     corner_radius=0).grid(row=3, column=0, sticky="ew", padx=20)

        # Navigation buttons
        pages = [
            ("📊", "Dashboard",        self.show_dashboard),
            ("➕", "Create Account",   self.show_create),
            ("👥", "All Accounts",     self.show_accounts),
            ("💳", "Credit / Debit",   self.show_transfer),
            ("📄", "Audit Log",        self.show_audit),
        ]
        self.nav_btns = {}
        for i, (icon, label, cmd) in enumerate(pages):
            btn = ctk.CTkButton(
                sb, text=f" {icon}  {label}",
                font=FONTS["body"],
                anchor="w",
                height=44,
                corner_radius=RADIUS["md"],
                fg_color=COLORS["transparent"],
                hover_color=COLORS["bg_hover"],
                text_color=COLORS["text_primary"],
                command=cmd,
            )
            btn.grid(row=4 + i, column=0, sticky="ew", padx=12, pady=3)
            self.nav_btns[label] = btn

        # Admin info panel
        info = ctk.CTkFrame(sb, fg_color=COLORS["bg_surface"],
                            corner_radius=RADIUS["md"])
        info.grid(row=20, column=0, sticky="ew", padx=12, pady=(0, 12))
        info.columnconfigure(0, weight=1)
        ctk.CTkLabel(info, text="👤 " + self.user["name"], font=FONTS["body_bold"],
                     text_color=COLORS["text_primary"], anchor="w").grid(
            row=0, column=0, padx=12, pady=(10, 2), sticky="w")
        ctk.CTkLabel(info, text=self.user["acc_no"], font=FONTS["tiny"],
                     text_color=COLORS["text_muted"], anchor="w").grid(
            row=1, column=0, padx=12, sticky="w")
        ctk.CTkButton(info, text="⏻  Logout", font=FONTS["small"],
                      height=34, corner_radius=RADIUS["md"],
                      fg_color=COLORS["danger"], hover_color=COLORS["danger_dark"],
                      text_color=COLORS["white"],
                      command=self.on_logout).grid(
            row=2, column=0, sticky="ew", padx=12, pady=10)
        # push info to bottom
        sb.rowconfigure(19, weight=1)

    # ── Main content area  ───────────────────────────────────────────────────
    def _build_main_area(self):
        self.content = ctk.CTkFrame(self, fg_color=COLORS["bg_dark"])
        self.content.grid(row=0, column=1, sticky="nsew")
        self.content.columnconfigure(0, weight=1)
        self.content.rowconfigure(1, weight=1)

        # Header bar
        header = ctk.CTkFrame(self.content, fg_color=COLORS["bg_card"],
                              height=60, corner_radius=0)
        header.grid(row=0, column=0, sticky="ew")
        header.columnconfigure(1, weight=1)
        header.grid_propagate(False)

        self.page_title = ctk.CTkLabel(
            header, text="Dashboard", font=FONTS["heading"],
            text_color=COLORS["text_primary"])
        self.page_title.grid(row=0, column=0, padx=24, pady=16, sticky="w")

        self.header_time = ctk.CTkLabel(
            header, text="", font=FONTS["small"],
            text_color=COLORS["text_muted"])
        self.header_time.grid(row=0, column=1, padx=24, sticky="e")
        self._tick()

        # Content swap frame
        self.swap = ctk.CTkFrame(self.content, fg_color=COLORS["bg_dark"])
        self.swap.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
        self.swap.columnconfigure(0, weight=1)
        self.swap.rowconfigure(0, weight=1)

        # Build all sub-pages
        self._pages = {}
        self._build_dashboard_page()
        self._build_create_page()
        self._build_accounts_page()
        self._build_transfer_page()
        self._build_audit_page()

        self.show_dashboard()

    # ── Clock tick ───────────────────────────────────────────────────────────
    def _tick(self):
        self.header_time.configure(
            text=datetime.now().strftime("🕐  %d %b %Y  |  %H:%M:%S"))
        self.after(1000, self._tick)

    # ── Page switcher ─────────────────────────────────────────────────────────
    def _show_page(self, name):
        for p in self._pages.values():
            p.grid_remove()
        self._pages[name].grid(row=0, column=0, sticky="nsew")
        self.page_title.configure(text=name)
        for label, btn in self.nav_btns.items():
            btn.configure(
                fg_color=COLORS["primary"] if label == name or
                (name == "Dashboard" and label == "Dashboard") else COLORS["transparent"],
                text_color=COLORS["white"] if label == name else COLORS["text_primary"],
            )

    def show_dashboard(self):  self._show_page("Dashboard")
    def show_create(self):
        self._show_page("Create Account")
    def show_accounts(self): self.refresh_accounts(); self._show_page("All Accounts")
    def show_transfer(self): self._show_page("Credit / Debit")
    def show_audit(self):    self.refresh_audit();    self._show_page("Audit Log")

    # ═══════════════════════════════════════════════════════════════════════════
    # PAGE: Dashboard
    # ═══════════════════════════════════════════════════════════════════════════
    def _build_dashboard_page(self):
        p = ctk.CTkScrollableFrame(
            self.swap, fg_color=COLORS["bg_dark"], corner_radius=0)
        self._pages["Dashboard"] = p
        p.columnconfigure((0, 1, 2, 3), weight=1)

        # Stat cards
        self.sc_users = StatCard(p, "👥", "Total Accounts", "0",
                                 COLORS["primary"])
        self.sc_users.grid(row=0, column=0, padx=12, pady=12, sticky="nsew")

        self.sc_bal = StatCard(p, "💰", "Total Deposits", "₹0.00",
                               COLORS["accent"])
        self.sc_bal.grid(row=0, column=1, padx=12, pady=12, sticky="nsew")

        self.sc_tx = StatCard(p, "🔄", "Transactions Today", "0",
                              COLORS["warning"])
        self.sc_tx.grid(row=0, column=2, padx=12, pady=12, sticky="nsew")

        self.sc_cust = StatCard(p, "🧾", "Customers", "0",
                                COLORS["primary_light"])
        self.sc_cust.grid(row=0, column=3, padx=12, pady=12, sticky="nsew")

        # Recent Transactions table
        ctk.CTkLabel(p, text="Recent Transactions",
                     font=FONTS["subhead"], text_color=COLORS["text_primary"]).grid(
            row=1, column=0, columnspan=4, sticky="w", padx=16, pady=(20, 8))

        self.dash_tx_frame = ctk.CTkFrame(
            p, fg_color=COLORS["bg_card"], corner_radius=RADIUS["lg"],
            border_width=1, border_color=COLORS["border"])
        self.dash_tx_frame.grid(row=2, column=0, columnspan=4,
                                sticky="nsew", padx=12, pady=(0, 16))
        self.dash_tx_frame.columnconfigure(0, weight=1)

    def refresh_stats(self):
        users   = db.get_all_users()
        custs   = [u for u in users if u["role"] == "customer"]
        total_b = sum(u["balance"] for u in custs)
        txs     = db.get_transactions()
        today   = datetime.now().strftime("%Y-%m-%d")
        today_t = [t for t in txs if t["timestamp"].startswith(today)]

        self.sc_users.update_value(str(len(users)))
        self.sc_bal.update_value(f"₹{total_b:,.2f}")
        self.sc_tx.update_value(str(len(today_t)))
        self.sc_cust.update_value(str(len(custs)))

        # Rebuild recent tx
        for w in self.dash_tx_frame.winfo_children():
            w.destroy()
        headers = ["Timestamp", "Account", "Type", "Amount", "Balance After"]
        for c, h in enumerate(headers):
            ctk.CTkLabel(
                self.dash_tx_frame, text=h,
                font=FONTS["body_bold"], text_color=COLORS["text_secondary"],
                anchor="w",
            ).grid(row=0, column=c, padx=16, pady=8, sticky="w")
        self.dash_tx_frame.columnconfigure(list(range(5)), weight=1)
        recent = txs[:12]
        if not recent:
            ctk.CTkLabel(
                self.dash_tx_frame, text="No transactions yet.",
                font=FONTS["body"], text_color=COLORS["text_muted"]
            ).grid(row=1, column=0, columnspan=5, pady=16)
        for r, t in enumerate(recent, 1):
            color = COLORS["accent"] if t["type"] == "CREDIT" else COLORS["danger"]
            vals = [t["timestamp"], t["acc_no"], t["type"],
                    f"₹{t['amount']:,.2f}", f"₹{t['balance_after']:,.2f}"]
            for c, v in enumerate(vals):
                ctk.CTkLabel(
                    self.dash_tx_frame, text=v, font=FONTS["small"],
                    text_color=color if c == 2 else COLORS["text_primary"],
                    anchor="w",
                ).grid(row=r, column=c, padx=16, pady=5, sticky="w")

    # ═══════════════════════════════════════════════════════════════════════════
    # PAGE: Create Account
    # ═══════════════════════════════════════════════════════════════════════════
    def _build_create_page(self):
        p = ctk.CTkScrollableFrame(
            self.swap, fg_color=COLORS["bg_dark"], corner_radius=0)
        self._pages["Create Account"] = p
        p.columnconfigure(0, weight=1)

        card = ctk.CTkFrame(p, fg_color=COLORS["bg_card"],
                            corner_radius=RADIUS["xl"],
                            border_width=1, border_color=COLORS["border_light"])
        card.grid(row=0, column=0, padx=80, pady=30, sticky="ew")
        card.columnconfigure(0, weight=1)

        ctk.CTkLabel(card, text="➕  Create New Account",
                     font=FONTS["heading"], text_color=COLORS["text_primary"]).grid(
            row=0, column=0, pady=(28, 4), padx=32, sticky="w")
        ctk.CTkLabel(card, text="Fill in the details below to open a new bank account.",
                     font=FONTS["small"], text_color=COLORS["text_secondary"]).grid(
            row=1, column=0, padx=32, sticky="w", pady=(0, 20))

        fields_frame = ctk.CTkFrame(card, fg_color=COLORS["transparent"])
        fields_frame.grid(row=2, column=0, padx=32, sticky="ew", pady=(0, 12))
        fields_frame.columnconfigure(1, weight=1)

        def lbl(row, text):
            ctk.CTkLabel(fields_frame, text=text, font=FONTS["body_bold"],
                         text_color=COLORS["text_secondary"], anchor="w").grid(
                row=row, column=0, padx=(0, 16), pady=8, sticky="w")

        def entry(row, **kw):
            e = ctk.CTkEntry(fields_frame, height=42, font=FONTS["body"],
                             fg_color=COLORS["bg_surface"],
                             border_color=COLORS["border"],
                             text_color=COLORS["text_primary"],
                             placeholder_text_color=COLORS["text_muted"],
                             corner_radius=RADIUS["md"], **kw)
            e.grid(row=row, column=1, sticky="ew", pady=8)
            return e

        lbl(0, "Full Name")
        self._c_name = entry(0, placeholder_text="e.g. Swetha Devi")

        lbl(1, "Account Type")
        self._c_role = ctk.CTkOptionMenu(
            fields_frame, values=["Customer", "Admin"],
            font=FONTS["body"], fg_color=COLORS["bg_surface"],
            button_color=COLORS["primary"], button_hover_color=COLORS["primary_dark"],
            text_color=COLORS["text_primary"], corner_radius=RADIUS["md"], height=42)
        self._c_role.grid(row=1, column=1, sticky="ew", pady=8)

        lbl(2, "Initial Deposit (₹)")
        self._c_deposit = entry(2, placeholder_text="e.g. 5000.00")

        lbl(3, "PIN (4 digits)")
        self._c_pin = entry(3, placeholder_text="4-digit PIN", show="●")

        lbl(4, "Confirm PIN")
        self._c_pin2 = entry(4, placeholder_text="Re-enter PIN", show="●")

        ctk.CTkButton(
            card, text="  Create Account  ✓",
            font=FONTS["body_bold"], height=48,
            corner_radius=RADIUS["lg"],
            fg_color=COLORS["accent"], hover_color=COLORS["accent_dark"],
            text_color=COLORS["white"],
            command=self._do_create,
        ).grid(row=3, column=0, padx=32, sticky="ew", pady=(8, 8))

        self._c_status = ctk.CTkLabel(card, text="", font=FONTS["small"],
                                      text_color=COLORS["accent"], wraplength=480)
        self._c_status.grid(row=4, column=0, pady=(0, 20))

    def _do_create(self):
        name    = self._c_name.get().strip()
        role    = self._c_role.get().lower()
        dep_str = self._c_deposit.get().strip()
        pin     = self._c_pin.get().strip()
        pin2    = self._c_pin2.get().strip()

        if not name:
            return self._c_status.configure(
                text="⚠  Name is required.", text_color=COLORS["warning"])
        if pin != pin2:
            return self._c_status.configure(
                text="✗  PINs do not match.", text_color=COLORS["danger"])
        if len(pin) != 4 or not pin.isdigit():
            return self._c_status.configure(
                text="✗  PIN must be exactly 4 digits.", text_color=COLORS["danger"])
        try:
            dep = float(dep_str) if dep_str else 0.0
            if dep < 0:
                raise ValueError
        except ValueError:
            return self._c_status.configure(
                text="✗  Invalid deposit amount.", text_color=COLORS["danger"])

        new_user = db.create_account(name, pin, role, dep)
        self._c_status.configure(
            text=f"✓  Account created!\n"
                 f"   Account No: {new_user['acc_no']}\n"
                 f"   Name: {new_user['name']}  |  Opening Balance: ₹{new_user['balance']:,.2f}",
            text_color=COLORS["accent"])

        # Clear fields
        for w in [self._c_name, self._c_deposit, self._c_pin, self._c_pin2]:
            w.delete(0, "end")
        self.refresh_stats()

    # ═══════════════════════════════════════════════════════════════════════════
    # PAGE: All Accounts
    # ═══════════════════════════════════════════════════════════════════════════
    def _build_accounts_page(self):
        p = ctk.CTkFrame(self.swap, fg_color=COLORS["bg_dark"])
        p.columnconfigure(0, weight=1)
        p.rowconfigure(1, weight=1)
        self._pages["All Accounts"] = p

        # Filter bar
        fb = ctk.CTkFrame(p, fg_color=COLORS["transparent"])
        fb.grid(row=0, column=0, sticky="ew", padx=16, pady=12)
        self._acc_search = ctk.CTkEntry(
            fb, placeholder_text="🔍  Search by name or account…",
            width=300, height=40, font=FONTS["body"],
            fg_color=COLORS["bg_surface"], border_color=COLORS["border"],
            text_color=COLORS["text_primary"],
            placeholder_text_color=COLORS["text_muted"],
            corner_radius=RADIUS["md"])
        self._acc_search.pack(side="left", padx=(0, 8))
        self._acc_search.bind("<KeyRelease>", lambda e: self.refresh_accounts())
        ctk.CTkButton(fb, text="⟳ Refresh", width=90, height=40,
                      font=FONTS["small"],
                      fg_color=COLORS["bg_surface"], hover_color=COLORS["bg_hover"],
                      text_color=COLORS["text_primary"], corner_radius=RADIUS["md"],
                      command=self.refresh_accounts).pack(side="left")

        # Table
        self._acct_table = ctk.CTkScrollableFrame(
            p, fg_color=COLORS["bg_card"],
            corner_radius=RADIUS["lg"],
            border_width=1, border_color=COLORS["border"])
        self._acct_table.grid(row=1, column=0, sticky="nsew", padx=16, pady=(0, 16))
        self._acct_table.columnconfigure(list(range(5)), weight=1)

    def refresh_accounts(self):
        for w in self._acct_table.winfo_children():
            w.destroy()
        query = self._acc_search.get().lower() if hasattr(self, "_acc_search") else ""
        headers = ["Account No", "Name", "Role", "Balance", "Actions"]
        for c, h in enumerate(headers):
            ctk.CTkLabel(self._acct_table, text=h, font=FONTS["body_bold"],
                         text_color=COLORS["text_secondary"], anchor="w").grid(
                row=0, column=c, padx=16, pady=10, sticky="w")

        users = db.get_all_users()
        if query:
            users = [u for u in users
                     if query in u["name"].lower() or query in u["acc_no"].lower()]
        if not users:
            ctk.CTkLabel(self._acct_table, text="No accounts found.",
                         font=FONTS["body"], text_color=COLORS["text_muted"]).grid(
                row=1, column=0, columnspan=5, pady=20)
            return

        for r, u in enumerate(users, 1):
            bg = COLORS["bg_surface"] if r % 2 == 0 else COLORS["transparent"]
            role_color = COLORS["gold"] if u["role"] == "admin" else COLORS["primary_light"]
            vals = [u["acc_no"], u["name"], u["role"].title(),
                    f"₹{u['balance']:,.2f}"]
            for c, v in enumerate(vals):
                ctk.CTkLabel(self._acct_table, text=v, font=FONTS["small"],
                             text_color=role_color if c == 2 else COLORS["text_primary"],
                             anchor="w").grid(
                    row=r, column=c, padx=16, pady=6, sticky="w")
            # Delete button
            acc_no = u["acc_no"]
            ctk.CTkButton(
                self._acct_table, text="🗑 Delete", width=80, height=30,
                font=FONTS["tiny"],
                fg_color=COLORS["danger"], hover_color=COLORS["danger_dark"],
                text_color=COLORS["white"], corner_radius=RADIUS["sm"],
                command=lambda a=acc_no: self._delete_account(a),
            ).grid(row=r, column=4, padx=16, pady=6)

    def _delete_account(self, acc_no):
        if acc_no == "ADMIN001":
            return
        db.delete_account(acc_no)
        self.refresh_accounts()
        self.refresh_stats()

    # ═══════════════════════════════════════════════════════════════════════════
    # PAGE: Credit / Debit
    # ═══════════════════════════════════════════════════════════════════════════
    def _build_transfer_page(self):
        p = ctk.CTkScrollableFrame(
            self.swap, fg_color=COLORS["bg_dark"], corner_radius=0)
        self._pages["Credit / Debit"] = p
        p.columnconfigure((0, 1), weight=1)

        def make_panel(col, title, icon, btn_color, btn_hover, action):
            card = ctk.CTkFrame(
                p, fg_color=COLORS["bg_card"],
                corner_radius=RADIUS["xl"],
                border_width=1, border_color=COLORS["border_light"])
            card.grid(row=0, column=col, padx=12, pady=24, sticky="nsew")
            card.columnconfigure(0, weight=1)

            ctk.CTkLabel(card, text=f"{icon}  {title}",
                         font=FONTS["heading"],
                         text_color=COLORS["text_primary"]).grid(
                row=0, column=0, padx=24, pady=(24, 12), sticky="w")

            def lbl(r, t):
                ctk.CTkLabel(card, text=t, font=FONTS["body_bold"],
                             text_color=COLORS["text_secondary"],
                             anchor="w").grid(row=r, column=0, padx=24,
                                              pady=(8, 2), sticky="w")

            def ent(r, **kw):
                e = ctk.CTkEntry(card, height=42, font=FONTS["body"],
                                 fg_color=COLORS["bg_surface"],
                                 border_color=COLORS["border"],
                                 text_color=COLORS["text_primary"],
                                 placeholder_text_color=COLORS["text_muted"],
                                 corner_radius=RADIUS["md"], **kw)
                e.grid(row=r, column=0, padx=24, sticky="ew", pady=(0, 4))
                return e

            lbl(1, "Account Number")
            acc_e = ent(2, placeholder_text="Target account number")
            lbl(3, "Amount (₹)")
            amt_e = ent(4, placeholder_text="Enter amount")
            lbl(5, "Description")
            desc_e = ent(6, placeholder_text="Optional note")

            stat = ctk.CTkLabel(card, text="", font=FONTS["small"],
                                text_color=btn_color, wraplength=360)
            stat.grid(row=8, column=0, pady=(4, 0))

            ctk.CTkButton(
                card, text=f"  {icon}  Confirm {title}",
                font=FONTS["body_bold"], height=48,
                corner_radius=RADIUS["lg"],
                fg_color=btn_color, hover_color=btn_hover,
                text_color=COLORS["white"],
                command=lambda: action(acc_e, amt_e, desc_e, stat),
            ).grid(row=7, column=0, padx=24, sticky="ew", pady=(12, 4))

            return card

        make_panel(0, "Credit Account", "💚",
                   COLORS["accent"], COLORS["accent_dark"],
                   self._do_credit)
        make_panel(1, "Debit Account", "🔴",
                   COLORS["danger"], COLORS["danger_dark"],
                   self._do_debit)

    def _do_credit(self, acc_e, amt_e, desc_e, stat):
        self._execute_transfer(
            acc_e, amt_e, desc_e, stat, db.admin_credit,
            COLORS["accent"], "💚  Credited")

    def _do_debit(self, acc_e, amt_e, desc_e, stat):
        self._execute_transfer(
            acc_e, amt_e, desc_e, stat, db.admin_debit,
            COLORS["danger"], "🔴  Debited")

    def _execute_transfer(self, acc_e, amt_e, desc_e, stat, fn, color, verb):
        acc  = acc_e.get().strip().upper()
        desc = desc_e.get().strip() or "Admin transaction"
        try:
            amt = float(amt_e.get().strip())
        except ValueError:
            stat.configure(text="✗  Enter a valid amount.", text_color=COLORS["danger"])
            return
        try:
            updated = fn(acc, amt, desc)
            stat.configure(
                text=f"{verb} ₹{amt:,.2f}\n"
                     f"New balance for {updated['name']}: ₹{updated['balance']:,.2f}",
                text_color=color)
            acc_e.delete(0, "end")
            amt_e.delete(0, "end")
            desc_e.delete(0, "end")
            self.refresh_stats()
        except ValueError as e:
            stat.configure(text=f"✗  {e}", text_color=COLORS["danger"])

    # ═══════════════════════════════════════════════════════════════════════════
    # PAGE: Audit Log
    # ═══════════════════════════════════════════════════════════════════════════
    def _build_audit_page(self):
        p = ctk.CTkFrame(self.swap, fg_color=COLORS["bg_dark"])
        p.columnconfigure(0, weight=1)
        p.rowconfigure(1, weight=1)
        self._pages["Audit Log"] = p

        fb = ctk.CTkFrame(p, fg_color=COLORS["transparent"])
        fb.grid(row=0, column=0, sticky="ew", padx=16, pady=12)
        self._audit_search = ctk.CTkEntry(
            fb, placeholder_text="🔍  Filter by account or type…",
            width=320, height=40, font=FONTS["body"],
            fg_color=COLORS["bg_surface"], border_color=COLORS["border"],
            text_color=COLORS["text_primary"],
            placeholder_text_color=COLORS["text_muted"],
            corner_radius=RADIUS["md"])
        self._audit_search.pack(side="left", padx=(0, 8))
        self._audit_search.bind("<KeyRelease>", lambda e: self.refresh_audit())
        ctk.CTkButton(fb, text="⟳ Refresh", width=90, height=40,
                      font=FONTS["small"], fg_color=COLORS["bg_surface"],
                      hover_color=COLORS["bg_hover"],
                      text_color=COLORS["text_primary"],
                      corner_radius=RADIUS["md"],
                      command=self.refresh_audit).pack(side="left")

        self._audit_table = ctk.CTkScrollableFrame(
            p, fg_color=COLORS["bg_card"],
            corner_radius=RADIUS["lg"],
            border_width=1, border_color=COLORS["border"])
        self._audit_table.grid(row=1, column=0, sticky="nsew", padx=16, pady=(0, 16))
        self._audit_table.columnconfigure(list(range(6)), weight=1)

    def refresh_audit(self):
        for w in self._audit_table.winfo_children():
            w.destroy()
        query = self._audit_search.get().lower() if hasattr(self, "_audit_search") else ""
        headers = ["Timestamp", "Account", "Type", "Amount", "Description", "Balance After"]

        for c, h in enumerate(headers):
            ctk.CTkLabel(self._audit_table, text=h, font=FONTS["body_bold"],
                         text_color=COLORS["text_secondary"], anchor="w").grid(
                row=0, column=c, padx=14, pady=10, sticky="w")

        txs = db.get_transactions()
        if query:
            txs = [t for t in txs
                   if query in t["acc_no"].lower() or query in t["type"].lower()
                   or query in t["description"].lower()]
        if not txs:
            ctk.CTkLabel(self._audit_table, text="No transactions found.",
                         font=FONTS["body"],
                         text_color=COLORS["text_muted"]).grid(
                row=1, column=0, columnspan=6, pady=20)
            return
        for r, t in enumerate(txs, 1):
            color = COLORS["accent"] if t["type"] == "CREDIT" else COLORS["danger"]
            vals = [t["timestamp"], t["acc_no"], t["type"],
                    f"₹{t['amount']:,.2f}", t["description"],
                    f"₹{t['balance_after']:,.2f}"]
            for c, v in enumerate(vals):
                ctk.CTkLabel(
                    self._audit_table, text=v, font=FONTS["tiny"],
                    text_color=color if c == 2 else COLORS["text_primary"],
                    anchor="w").grid(row=r, column=c, padx=14, pady=4, sticky="w")
