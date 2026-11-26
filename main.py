import os

# The entry: a one-line resignation letter (Caesar, updated for the office).
ENTRY = "I came, I saw, I cleared my browser history."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
