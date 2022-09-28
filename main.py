from flask import Flask, render_template, redirect

board = [0]*9 
next = 1


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("tic.html", board  = board,next = next)

def winner(board):
    pattern = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for p in pattern:
        t= sum([board[x] for x in p])
        if t == 3:
            print(p,t)
            return 1 # X won 
        elif t == -3: 
            print(p,t)
            return -1 # O won 
    for i in board:
        if i ==0:
            return 0 # game in progress 
    return 2  # drow

@app.route("/set/<int:i>")
def set(i):
    global board, next
    board[i]=next
    next = -next
    t = winner(board)
    if t == 0 :
        return redirect("/")
    else:
        return render_template("end.html",t = t,board=board,next = next)

@app.route("/new")
def new():
    global board , next
    board = [0] * 9
    next = 1
    return redirect("/")


app.run(debug=True)
