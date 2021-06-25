row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")
position = [int(x) for x in str(position)]
column_pos = position[0]-1
row_pos = position[1]-1

x = "x"

print(column_pos, row_pos)

map[row_pos][column_pos] = 'X'

print(f"{row1}\n{row2}\n{row3}")
