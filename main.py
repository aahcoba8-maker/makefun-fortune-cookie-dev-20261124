import os

LINE = "Your future self will debug your code at 3 a.m.; leave them a comment, a test, and an apology."

def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if not os.path.isdir(out):
        out = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
