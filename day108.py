"""
Day 108: Tower of Hanoi

Question:
Print the moves to solve the Tower of Hanoi for n disks.
"""

# Solution
def hanoi(n, src, dst, aux):
    if n == 0:
        return
    hanoi(n - 1, src, aux, dst)
    print(f"Move disk {n} from {src} to {dst}")
    hanoi(n - 1, aux, dst, src)

hanoi(3, "A", "C", "B")
