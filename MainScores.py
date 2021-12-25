#!/usr/bin/python3

#Scores.html located in subdirectory "templates"
# run from command line :
#python3 -m venv venv
#. venv/bin/activate
#export FLASK_APP=MainScores.py
#flask run --host=0.0.0.0
# run from PC:
#http://your_ip:5000/


from flask import Flask, render_template, flash, request , session
from wtforms import Form
#from wtforms import Form, TextField
from Utils import SCORES_FILE_NAME, clear_screen, BAD_RETURN_CODE


app = Flask(__name__)

class Scores(Form):

 @app.route('/',   methods=['GET', 'POST'])

 def score_server():


    form = Scores(request.form)

    with open(SCORES_FILE_NAME,"r") as f:
      SCORENOW=str(f.read())
      print(SCORENOW)
      f.close()
  

    htmlfile="templates/Scores.html"
    with open(htmlfile,"r") as f:
      HTML=f.read()
      f.close()
      HTML=HTML.replace('{SCORE}',SCORENOW)
    with open(htmlfile,"w") as f:
      f.write(HTML)
      f.close()
    

    return render_template('Scores.html', form=form)



          # MAIN #

if __name__ == "__main__":

 #app.run()
 app.run(host='0.0.0.0', port=5000)
