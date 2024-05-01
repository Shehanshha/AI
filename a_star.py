g = 0
MAX_MOVES = 1000
def print_board(elements, move_name=""):
    print(f"\nDirection: {move_name}")
    for i in range(9):
        if i % 3 == 0:
            print()
        if elements[i] == -1:
            print("_", end=" ")
        else:
            print(elements[i], end=" ")
    print()
def heuristic(start, goal):
    h = 0
    for i in range(9):
        for j in range(9):
            if start[i] == goal[j] and start[i] != -1:
                h += (abs(j - i)) // 3 + (abs(j - i)) % 3
    return h
def moveleft(start, position):
 start[position], start[position - 1] = start[position - 1], start[position]
def moveright(start, position):
 start[position], start[position + 1] = start[position + 1], start[position]
def moveup(start, position):
 start[position], start[position - 3] = start[position - 3], start[position]
def movedown(start, position):
 start[position], start[position + 3] = start[position + 3], start[position]
def movetile(start, goal):
    emptyat = start.index(-1)
    row = emptyat // 3
    col = emptyat % 3
    t1, t2, t3, t4 = start[:], start[:], start[:], start[:]
    f1, f2, f3, f4 = 100, 100, 100, 100
    if col - 1 >= 0:
        moveleft(t1, emptyat)
        f1 = heuristic(t1, goal)
    if col + 1 < 3:
        moveright(t2, emptyat)
        f2 = heuristic(t2, goal)
    if row + 1 < 3:
        movedown(t3, emptyat)
        f3 = heuristic(t3, goal)
    if row - 1 >= 0:
        moveup(t4, emptyat)
        f4 = heuristic(t4, goal)
    min_heuristic = min(f1, f2, f3, f4)
    if f1 == min_heuristic:
        moveleft(start, emptyat)
        return "Left"
    elif f2 == min_heuristic:
        moveright(start, emptyat)
        return "Right"
    elif f3 == min_heuristic:
        movedown(start, emptyat)
        return "Down"
    elif f4 == min_heuristic:
        moveup(start, emptyat)
        return "Up"
def solveEight(start, goal):
    global g
    g += 1
    move_name = movetile(start, goal)
    print_board(start, move_name)
    # Calculate h(n)
    h = heuristic(start, goal)
    # Calculate f(n)
    f = g + h
    print(f"\nf(n): {f}, g(n): {g}, h(n): {h}\n")
    print("----------------------------------------------------")
    if f == g or g >= MAX_MOVES:
        print("\n\nSolved in {} moves".format(g))
        return
    solveEight(start, goal)
def main():
    global g
    start = list()
    goal = list()
    print("Enter the start state:(Enter -1 for empty):")
    for i in range(9):
        start.append(int(input()))
    print("Enter the goal state:(Enter -1 for empty):")
    for i in range(9):
        goal.append(int(input()))
    print("\nStart State:")
    print_board(start)
    print("--------------------------------------------")
    solveEight(start, goal)
    print("\nGoal State:")
    print_board(goal)
    print("\nTotal cost with the goal state: {}".format(g))
if __name__ == '__main__':
    main()