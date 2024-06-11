# wordle-solver
Wordle Solver is one of the best wordle solvers currently available. Using the NY Times word list, this solver can solve wordle puzzles within three guesses 80% of the time. In addition, this solver supports any 5-letter word wordle like puzzle.

# Stats
With wordle words (2314 words)
Average Tries: 3.0099
Within Three Tries: 79.395%

With all five letter words (14,000 words)
Average Tries: 3.69
Within Three Tries: 79.395%

# How to use
Run main.py, and type the starting word "spald" (the best wordle word when playing perfectly) into your wordle game.

Type the response by wordle into the command line by using "_" for absent or grey letters, "/" for misplaced or yellow letters, and the actual letter for correct letters. For example, a game may look like the following:

Computer: Type "spald"

your response: __/_/

Computer: Type "today"

your response: _/d/_

Computer: Type "radio"

your response: _/dio

Computer: Type "audio"

your response: Audio

Computer: The word is "audio"!

