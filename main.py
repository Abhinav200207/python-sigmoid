import SurroundedRegions

def main():
    board = [["X", "X", "X", "X"],
             ["X", "O", "O", "X"],
             ["X", "X", "O", "X"],
             ["X", "O", "X", "X"]]

    print("Original board:")
    for row in board:
        print(*row)

    solution = SurroundedRegions.Solution()
    solution.solve(board)

    print("\nBoard after capturing surrounded regions:")
    for row in board:
        print(*row)


if __name__ == "__main__":
    main()