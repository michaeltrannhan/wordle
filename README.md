# WORDLE GAME SOLUTION

## Solution 1: Brute force

Base on the length of the word, I would be trying "a" to "z" for each character in the word. \
Eventually for like many iterations, I would be able to find the word.

### Enhancements:

I think finding the initial word that the highest possibility to be matched at the first guess really decrease the time for finding the word, but we need to find those words online.

## Solution 2: Using a dictionary for n-letters word

Here I chose a 5 letter for my guess, so I found this dictionary online on this Github Repo:
_`https://github.com/petehaha/WordleSolver/blob/main/wordle-answers-alphabetical.txt`_

## Prerequisites:
**Python, pip**
## How to run 
clone this repo, and then on terminal, run this:
```
pip install -r requirements.txt 
```
Then run:
```
python script.py
```
Please adjust the word size base on the word that you want to guess



