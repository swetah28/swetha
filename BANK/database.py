# database.py - Nexus Bank 2026 | File-based Storage Engine

import os
import uuid
import hashlib
from datetime import datetime

# ─── File Paths ─────────────────────────────────────────────────────────────────
BASE_DIR        = os.path.dirname(os.path.abspath(__file__))
USERS_FILE      = os.path.join(BASE_DIR, "data", "users.txt")
TRANS_FILE      = os.path.join(BASE_DIR, "data", "transactions.txt")

# ─── Schema ─────────────────────────────────────────────────────────────────────
# users.txt       → acc_no | pin_hash | name | role | balance
# transactions.txt→ timestamp | acc_no | type | amount | description | balance_after

SEP = "|"

# ────────────────────────────────────────────────────────────────────────────────
def _ensure_files():
    """Create data directory and seed admin if files don't exist."""
    os.makedirs(os.path.join(BASE_DIR, "data"), exist_ok=True)
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            # Default admin account: acc=ADMIN001, pin=1234
            f.write(
                f"ADMIN001{SEP}{_hash('1234')}{SEP}System Administrator"
                f"{SEP}admin{SEP}0.00\n"
            )
    if not os.path.exists(TRANS_FILE):
        open(TRANS_FILE, "w", encoding="utf-8").close()

def _hash(pin: str) -> str:
    return hashlib.sha256(pin.encode()).hexdigest()

def _gen_acc() -> str:
    """Generate a unique 10-digit account number."""
    return "ACC" + str(uuid.uuid4().int)[:7].upper()

# ─── User CRUD ──────────────────────────────────────────────────────────────────
def _read_users() -> list[dict]:
    _ensure_files()
    users = []
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(SEP)
            if len(parts) == 5:
                users.append({
                    "acc_no":   parts[0],
                    "pin_hash": parts[1],
                    "name":     parts[2],
                    "role":     parts[3],
                    "balance":  float(parts[4]),
                })
    return users

def _write_users(users: list[dict]):
    _ensure_files()
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        for u in users:
            f.write(
                f"{u['acc_no']}{SEP}{u['pin_hash']}{SEP}{u['name']}"
                f"{SEP}{u['role']}{SEP}{u['balance']:.2f}\n"
            )

# ─── Transaction Log ────────────────────────────────────────────────────────────
def _log_transaction(acc_no: str, ttype: str, amount: float,
                     desc: str, balance_after: float):
    _ensure_files()
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(TRANS_FILE, "a", encoding="utf-8") as f:
        f.write(f"{ts}{SEP}{acc_no}{SEP}{ttype}{SEP}{amount:.2f}"
                f"{SEP}{desc}{SEP}{balance_after:.2f}\n")

def get_transactions(acc_no: str = None) -> list[dict]:
    """Return all transactions, optionally filtered by account."""
    _ensure_files()
    records = []
    with open(TRANS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(SEP)
            if len(parts) == 6:
                rec = {
                    "timestamp":     parts[0],
                    "acc_no":        parts[1],
                    "type":          parts[2],
                    "amount":        float(parts[3]),
                    "description":   parts[4],
                    "balance_after": float(parts[5]),
                }
                if acc_no is None or rec["acc_no"] == acc_no:
                    records.append(rec)
    return list(reversed(records))   # newest first

# ─── Public API ─────────────────────────────────────────────────────────────────

def authenticate(acc_no: str, pin: str) -> dict | None:
    """Return user dict on success, None on failure."""
    for u in _read_users():
        if u["acc_no"] == acc_no.upper() and u["pin_hash"] == _hash(pin):
            return u
    return None

def create_account(name: str, pin: str, role: str = "customer",
                   initial_deposit: float = 0.0) -> dict:
    """Create a new account and return the new user dict."""
    users = _read_users()
    # Ensure unique acc number
    existing_acc = {u["acc_no"] for u in users}
    acc_no = _gen_acc()
    while acc_no in existing_acc:
        acc_no = _gen_acc()

    new_user = {
        "acc_no":   acc_no,
        "pin_hash": _hash(pin),
        "name":     name,
        "role":     role,
        "balance":  initial_deposit,
    }
    users.append(new_user)
    _write_users(users)

    if initial_deposit > 0:
        _log_transaction(acc_no, "CREDIT", initial_deposit,
                         "Initial Deposit", initial_deposit)
    return new_user

def get_user(acc_no: str) -> dict | None:
    for u in _read_users():
        if u["acc_no"] == acc_no.upper():
            return u
    return None

def get_all_users() -> list[dict]:
    return _read_users()

def get_all_customers() -> list[dict]:
    return [u for u in _read_users() if u["role"] == "customer"]

def deposit(acc_no: str, amount: float, desc: str = "Deposit") -> dict:
    """Credit amount to account. Returns updated user dict."""
    if amount <= 0:
        raise ValueError("Amount must be positive.")
    users = _read_users()
    for u in users:
        if u["acc_no"] == acc_no.upper():
            u["balance"] = round(u["balance"] + amount, 2)
            _write_users(users)
            _log_transaction(acc_no, "CREDIT", amount, desc, u["balance"])
            return u
    raise ValueError(f"Account {acc_no} not found.")

def withdraw(acc_no: str, amount: float, desc: str = "Withdrawal") -> dict:
    """Debit amount from account. Returns updated user dict."""
    if amount <= 0:
        raise ValueError("Amount must be positive.")
    users = _read_users()
    for u in users:
        if u["acc_no"] == acc_no.upper():
            if u["balance"] < amount:
                raise ValueError("Insufficient balance.")
            u["balance"] = round(u["balance"] - amount, 2)
            _write_users(users)
            _log_transaction(acc_no, "DEBIT", amount, desc, u["balance"])
            return u
    raise ValueError(f"Account {acc_no} not found.")

def change_pin(acc_no: str, old_pin: str, new_pin: str) -> bool:
    """Change PIN. Returns True on success."""
    users = _read_users()
    for u in users:
        if u["acc_no"] == acc_no.upper():
            if u["pin_hash"] != _hash(old_pin):
                raise ValueError("Current PIN is incorrect.")
            u["pin_hash"] = _hash(new_pin)
            _write_users(users)
            return True
    raise ValueError(f"Account {acc_no} not found.")

def delete_account(acc_no: str) -> bool:
    """Delete an account. Returns True if deleted."""
    users = _read_users()
    original = len(users)
    users = [u for u in users if u["acc_no"] != acc_no.upper()]
    if len(users) == original:
        return False
    _write_users(users)
    return True

def admin_credit(acc_no: str, amount: float, desc: str = "Admin Credit") -> dict:
    """Admin-only: forcibly credit any account."""
    return deposit(acc_no, amount, desc)

def admin_debit(acc_no: str, amount: float, desc: str = "Admin Debit") -> dict:
    """Admin-only: forcibly debit any account."""
    return withdraw(acc_no, amount, desc)

# ─── Bootstrap ──────────────────────────────────────────────────────────────────
_ensure_files()
