FROM python:3.8-slim-bullseye

WORKDIR /training/devops
RUN python3 -m venv venv
RUN . venv/bin/activate

# Install dependencies:
COPY requirements.txt ./
COPY MainScores.py ./
COPY Utils.py ./
COPY scores.txt ./
COPY templates/Scores.html ./templates/Scores.html

RUN pip3 install -r requirements.txt

CMD [ "python3", "./MainScores.py" , "runserver", "0.0.0.0:5000"]
