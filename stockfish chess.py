from stockfishpy.stockfishpy import *
STOCKFISH_PATH='G:\Downloads\stockfish-10-win (1)\stockfish-10-win\Windows\stockfish_10_x64_popcnt.exe'
chessEngine = Engine(STOCKFISH_PATH, param={'Threads': 4,
                                            'Ponder': 'true'},depth=12)
'''
print (chessEngine.uci())
print (chessEngine.isready())
chessEngine.ucinewgame()
chessEngine.setposition('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR b KQkq - 0 1')
move = chessEngine.bestmove()
print (move['bestmove'])
move = chessEngine.bestmove()
print (move['bestmove'])
move = chessEngine.bestmove()
print (move['bestmove'])
'''

for i in range(50):
    fen=input('fen=')
    chessEngine.setposition(fen)
    move = chessEngine.bestmove()
    print (move['bestmove'])
