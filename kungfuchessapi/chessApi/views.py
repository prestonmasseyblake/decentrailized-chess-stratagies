from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from rest_framework.views import APIView 
from rest_framework.response import Response
import chess 


chessGame = chess.Board()

# helper functions 
def make_matrix(board):  # type(board) == chess.Board()
    pgn = board.epd()
    foo = []  # Final board
    pieces = pgn.split(" ", 1)[0]
    rows = pieces.split("/")
    for row in rows:
        foo2 = []  # This is the row I make
        for thing in row:
            if thing.isdigit():
                for i in range(0, int(thing)):
                    foo2.append('.')
            else:
                foo2.append(thing)
        foo.append(foo2)
    return foo
# end helper functions 


# import chess.pgn
class chessEndPoint(APIView):
    #returns the current state of the board
    def get(self, request, *args, **kwargs):
        print("gewa")
        
        text = print(chessGame)
        print(type(chessGame))
        # print(text)
        bb = make_matrix(chessGame)
        return Response(bb)

class chessPiece(APIView):
    #returns the current state of the piece and what moves it 
    def get(self, request, *args, **kwargs):
        print("gewg")
    
