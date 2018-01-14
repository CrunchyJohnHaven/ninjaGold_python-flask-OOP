# Assignment: Ninja Gold
# Create a simple game to test your understanding of flask, and implement the functionality below.

# For this assignment, you're going to create a mini-game that helps a ninja make some money! When you
#  start the game, your ninja should have 0 gold. The ninja can go to different places (farm, cave, 
#  house, casino) and earn different amounts of gold. In the case of a casino, your ninja can earn or 
#  LOSE up to 50 golds. Your job is to create a web app that allows this ninja to earn gold and to display past activities 
#  of this ninja.

from flask import Flask, session, request, redirect, render_template 
app = Flask(__name__)
import random
app.secret_key = "NinjaStealth"
@app.route('/')
def home():
    if 'gold' not in session:
        session['gold'] = 0
    if 'play' not in session:
        session['play'] = ''
    info = {}
    info['gold'] = session['gold']
    info['play'] = session['play']
    return render_template('gold.html', info=info)
@app.route('/process', methods=['post'])
def play():
    play = request.form['play']
    print play
    if play == 'farm':
        rand = random.randrange(0,5)
        message = "<div class=won>You have made" + " " + str(rand) + " " + "ninja gold</div>"
    elif play == 'cave':
        rand = random.randrange(-500,500)
        if rand >= 0:
            result = "won"
        else:
            result = "lost"
        message = "<div class=won>You have" + " " + result + " " + str(rand) + " " + "ninja gold</div>"
    elif play == 'casino':
        rand = random.randrange(-50,51)
        if rand >= 0:
            result = "won"
        else:
            result = "lost"
        message = "<div class=won>You have" + " " + result + " " + str(rand) + " " + "ninja gold</div>"
    
    log = session['play']
    log = log + message
    session['play'] = log
    log = session['gold']
    session['gold'] += rand
    return redirect('/')

@app.route('/reset', methods=['post'])
def submit():
    session['gold'] = 0
    session['play'] = ''
    return redirect('/')

app.run(debug=True)

        

# Farm - win five gold "You won ___ gold selling ninja corn!"
# Cave - win 500 or lose 500 "You won ___ gold in a ninja cave battle!"
# Casino - Earn or lose up to 50 gold "You have" ____ 