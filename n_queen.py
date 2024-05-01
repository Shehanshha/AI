from __future__ import print_function

def issafe(arr, x, y, n):
    for row in range(x):
        if arr[row][y] == 1:
            return False
    
    row = x
    col = y

    while row >= 0 and col >= 0:
        if arr[row][col] == 1:
            return False
        row -= 1
        col -= 1
    
    row, col = x, y
    while row >= 0 and col < n:
        if arr[row][col] == 1:
            return False
        row -= 1
        col += 1
    
    return True

def nQueen(arr, x, n, solutions):
    if x == n:
        temp = []
        for row in range(n):
            temp.append(arr[row][:])
        solutions.append(temp)
        return
    
    for row in range(n):
        if issafe(arr, x, row, n):
            arr[x][row] = 1
            nQueen(arr, x + 1, n, solutions)
            arr[x][row] = 0

def main():
    while True:
        n = int(input("Enter number of Queens : "))
        arr = [[0] * n for row in range(n)]
        solutions = []
        nQueen(arr, 0, n, solutions)
        
        if not solutions:
            print("No solutions found.")
        else:
            print(f"Found {len(solutions)} solutions:")
            for idx, sol in enumerate(solutions, 1):
                print(f"Arrangement {idx}:")
                for row in sol:
                    print(" ".join("Q" if cell == 1 else "." for cell in row))
                print()

if __name__ == '__main__':
    main()
