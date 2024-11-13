import re as reg

# NOTE: Marked as 7 Kyu

def printer_errors(s: str) -> str:
    replaced_s = reg.sub(r"[^a-mA-M]", "x", s)
    count_x = replaced_s.count("x")

    return f"{count_x}/{len(s)}"

if __name__ == "__main__":
    pass