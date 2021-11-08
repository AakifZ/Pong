##How To Run The Website
1. Open a new terminal
2. Install Python mysql: `python -m pip install mysql-connector-python`
3. Install flask: `pip install Flask`
4. cd into the 'leaderboard' folder: ex: `cd PONG/leaderboard`
5. Turn on DEBUG mode: `set FLASK_ENV=development` (On Windows) OR `export FLASK_ENV=development` (On Mac)
6. Choose the correct file to run the app: `set FLASK_APP=app` (On Windows) OR `export FLASK_APP=app` (On Mac)
7. Run the app: `python -m flask run` or `python3 -m flask run`