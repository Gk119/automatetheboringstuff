def printTable(table):
    colWidths = [0] * len(table)

    for col in range(len(table)):
        for row in range(len(table[col])):
            if colWidths[col] < len(table[col][row]):
                colWidths[col] = len(table[col][row])

    for col in range(len(table[0])):
        for row in range(len(table)):
            print(table[row][col].rjust(colWidths[row]), end = ' ')
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)