from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from rest_framework.views import APIView 
from rest_framework.response import Response
import chess
class chessEndPoint(APIView):
    print("gewa")
    # board = chess.Board()
    def get(self, request, *args, **kwargs):
        print("gewa")
        return Response("hello")
        