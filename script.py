## Solution 1:
# Brute force:
# Base on the length of the word, I would be trying "a" to "z" for each character in the word.
# Eventually for like many iterations, I would be able to find the word.

# Solution 2:
# I would be using the dictionary to find the word.
# Since I could only find 5 letter words dictionary only, so the problem would be solved in word of 5 letters

# Solution 1:

import requests
import string
import logging
import time


def solve_daily_wordle(api_url, word_size=5):
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

    def get_feedback(guess):
        try:
            response = requests.get(
                f"{api_url}/daily",
                params={"guess": guess, "size": word_size},
                timeout=10,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.SSLError as e:
            logging.error(f"SSL Error: {e}. Try using 'verify=False' if necessary.")
            raise
        except requests.exceptions.ConnectionError as e:
            logging.error(
                f"Connection Error: {e}. Ensure the API endpoint is correct and reachable."
            )
            raise
        except requests.exceptions.Timeout:
            logging.error(
                "Request timed out. Check your network connection or increase the timeout duration."
            )
            raise
        except requests.exceptions.RequestException as e:
            logging.error(f"API request failed: {e}")
            raise

    # Start with an initial guess (e.g., 'aaaaa')
    # Start with a random guess from the dictionary
    with open("words.txt") as f:
        words = f.readlines()
    guess = words[0].strip()
    alphabet = string.ascii_lowercase

    # Initialize variables for tracking confirmed positions and candidates
    confirmed_positions = [None] * word_size  # Correct letters in correct positions
    possible_letters = [
        set(alphabet) for _ in range(word_size)
    ]  # Possible letters for each slot

    while True:
        logging.info(f"Guessing: {guess}")
        time.sleep(2)
        feedback = get_feedback(guess)

        # Process feedback
        for i, result in enumerate(feedback):
            if result["result"] == "correct":
                confirmed_positions[i] = guess[i]
                possible_letters[i] = {guess[i]}
            elif result["result"] == "absent":
                for pos in range(word_size):
                    if guess[i] in possible_letters[pos]:
                        possible_letters[pos].discard(guess[i])
            elif result["result"] == "present":
                possible_letters[i].discard(guess[i])

        # Check if the word is solved
        if all(confirmed_positions):
            solved_word = "".join(confirmed_positions)
            logging.info(f"Word solved: {solved_word}")
            return solved_word

        # Generate the next guess
        try:
            guess = "".join(
                (
                    confirmed_positions[i]
                    if confirmed_positions[i]
                    else next(iter(possible_letters[i]))
                )
                for i in range(word_size)
            )
        except StopIteration:
            logging.error("Ran out of possible letters to guess.")
            raise ValueError("No valid guesses remain.")


# Example usage
if __name__ == "__main__":
    api_url = "https://wordle.votee.dev:8000"  # Replace with the correct API URL
    try:
        solve_daily_wordle(api_url)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
