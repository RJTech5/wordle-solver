# wordle-solver
Wordle Solver is one of the best wordle solvers currently available. Using the NY Times word list, this solver can solve wordle puzzles within three guesses 80% of the time. In addition, this solver supports any 5-letter word wordle like puzzle.

## Stats
**With wordle word list (2314 words):**
* Average Tries: 3.0099
* Within Three Tries: 79.395%

**With all five letter words (14,000 words):**
* Average Tries: 4.17
* Within Three Tries: 34.366%

## How to use
Run main.py, and type the starting word "spald" (the best wordle word when playing perfectly) into your wordle game.

Type the response by wordle into the command line by using "_" for absent or grey letters, "/" for misplaced or yellow letters, and the actual letter for correct letters. For example, a game may look like the following:

**Computer: Type "spald"**

> wordles response: ⬛⬛⬛⬛⬛

> your response: _____

**Computer: Type "tenor"**

> wordles response: ⬛🟨🟩🟨⬛

> your response: _/n/_

**Computer: Type "money"**

> wordles response: 🟩🟩🟩🟩🟩

> your response: money

**Computer: The word is "money"!**

## How it works
When using just wordle words, this script will filter words based on all the hints you provide. If multiple words are left, the script will select the word leading to the most eliminations to narrow down possibilities as fast as possible.

When using all five letter words, the program will still filter words based on hints provided but will select the next word from the remaining words based on word usage frequency. This optimizes the algorithm no matter what specific wordle game you are playing.  


