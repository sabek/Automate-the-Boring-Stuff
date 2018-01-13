def printtable(table):
    colwidths = [0] * len(table)

    for x in range(len(table)):
        for y in range(len(table[x])):
            if colwidths[x] < len(table[x][y]):
                colwidths[x] = len(table[x][y])

    print(table[0][0].rjust(colwidths[0]) + " " + table[1][0].rjust(colwidths[1]) + " " + table[2][0].rjust(colwidths[2]))
    print(table[0][1].rjust(colwidths[0]) + " " + table[1][1].rjust(colwidths[1]) + " " + table[2][1].rjust(colwidths[2]))
    print(table[0][2].rjust(colwidths[0]) + " " + table[1][2].rjust(colwidths[1]) + " " + table[2][2].rjust(colwidths[2]))
    print(table[0][3].rjust(colwidths[0]) + " " + table[1][3].rjust(colwidths[1]) + " " + table[2][3].rjust(colwidths[2]))


tabledata = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printtable(tabledata)