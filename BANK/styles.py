# styles.py - Nexus Bank 2026 Design System

# ─── Color Palette ─────────────────────────────────────────────────────────────
COLORS = {
    # Backgrounds
    "bg_deep":       "#0A0E1A",   # Deepest background
    "bg_dark":       "#0F1628",   # Main window background
    "bg_card":       "#161D35",   # Card / panel background
    "bg_surface":    "#1E2847",   # Elevated surface (sidebars, inputs)
    "bg_hover":      "#252F52",   # Hover state

    # Primary – Electric Blue
    "primary":       "#4F8EF7",
    "primary_light": "#7AABFF",
    "primary_dark":  "#2E6BD6",

    # Accent – Emerald Green (credits / success)
    "accent":        "#2ECC71",
    "accent_dark":   "#27AE60",

    # Danger – Crimson (debits / error)
    "danger":        "#E74C3C",
    "danger_dark":   "#C0392B",

    # Warning – Amber
    "warning":       "#F39C12",
    "warning_dark":  "#D68910",

    # Text
    "text_primary":  "#E8EBF4",
    "text_secondary":"#8B95B4",
    "text_muted":    "#4A5275",

    # Borders / Dividers
    "border":        "#252F52",
    "border_light":  "#3D4D7A",

    # Gold – for admin badge
    "gold":          "#F1C40F",
    "gold_dark":     "#D4AC0D",

    # White / transparent helpers
    "white":         "#FFFFFF",
    "transparent":   "transparent",
}

# ─── Fonts ──────────────────────────────────────────────────────────────────────
FONTS = {
    "display":   ("Segoe UI", 28, "bold"),
    "heading":   ("Segoe UI", 20, "bold"),
    "subhead":   ("Segoe UI", 16, "bold"),
    "body_bold": ("Segoe UI", 13, "bold"),
    "body":      ("Segoe UI", 13),
    "small":     ("Segoe UI", 11),
    "tiny":      ("Segoe UI", 10),
    "mono":      ("Consolas", 12),
}

# ─── Radius / Padding ───────────────────────────────────────────────────────────
RADIUS = {
    "sm":  4,
    "md":  8,
    "lg":  12,
    "xl":  18,
    "xxl": 24,
}

PAD = {
    "xs":  4,
    "sm":  8,
    "md":  16,
    "lg":  24,
    "xl":  32,
}
