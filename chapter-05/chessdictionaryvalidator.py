def isValidChessBoard(board):
    wpieces = {'wking':1 ,'wqueen':1, 'wbishop':2, 'wrook':2, 'wknight':2, 'wpawn':8}
    bpieces = {'bking':1 ,'bqueen':1, 'bbishop':2, 'brook':2, 'bknight':2, 'bpawn':8}

    pieces = {}
    
    if 'wking' not in board.values():
        return False
    
    if 'bking' not in board.values():
        return False

    for piece in board.values():
        pieces.setdefault(piece,0)
        pieces[piece] = pieces[piece] + 1
    
    if pieces['wking'] != 1 or pieces['bking'] != 1:
        return False

    for piece in wpieces.keys():
        if piece in pieces.keys():
            if pieces[piece] > wpieces[piece]:
                return False

    for piece in bpieces.keys():
        if piece in pieces.keys():
            if pieces[piece] > bpieces[piece]:
                return False
    
    wcount = 0
    bcount = 0

    for piece in wpieces.keys():
        if piece in pieces.keys():
            wcount += pieces[piece]

    for piece in bpieces.keys():
        if piece in pieces.keys():
            bcount += pieces[piece]
        
    if wcount > 16 or bcount > 16:
        return False

    positions = []
    for n in ['1','2','3','4','5','6','7','8']:
        for a in ['a','b','c','d','e','f','g','h']:
            positions.append(n + a)
    
    for pos in board.keys():
        if pos not in positions:
            return False

    print(pieces)
    return True


board1 = {'1a':'wking', '2c':'wpawn', '3c':'wpawn', '4a':'bking'}
print(isValidChessBoard(board1))
