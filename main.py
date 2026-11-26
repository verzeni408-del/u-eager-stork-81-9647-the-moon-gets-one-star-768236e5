"""Write the competition entry to /output/entry.txt (stdlib only)."""

import os

ENTRY = "One star. The Moon turned my husband into a werewolf. He ate the neighbor's cat. No refund."
# 91 chars, limit 120. One-star review about the Moon itself:
# human harmed (husband turned werewolf, neighbor's cat eaten) + dark twist.

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
