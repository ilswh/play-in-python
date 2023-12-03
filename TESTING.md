# Testing

Return back to the [README.md](README.md) file.

In this section, you need to convince the assessors that you have conducted enough testing to legitimately believe that the site works well.
Essentially, in this part, you should go over all of your project's features, and ensure that they all work as intended,
with the project providing an easy and straightforward way for the users to achieve their goals.

## Code Validation

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot |
| --- | --- | --- |
|play.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/play-in-python/main/play.py) | ![screenshot](documentation/py-validation-play.png) |
| stages.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/play-in-python/main/checkout/stages.py) | ![screenshot](documentation/py-validation-stages.png) |
| primary_emotions.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/play-in-python/main/primary_emotions.py) | ![screenshot](documentation/py-validation-primary_emotions.png) |
| happy_emotions.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/play-in-python/main/happy_emotions.py) | ![screenshot](documentation/py-validation-happy_emotions.png) |
| sad_emotions.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/play-in-python/main/sad_emotions.py) | ![screenshot](documentation/py-validation-sad_emotions.png) |

## Browser Compatibility

I've tested my deployed project on following browsers to check for compatibility issues.

- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Opera](https://www.opera.com/download)

| Browser | Welcome | Game | Play again | Notes |
| --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/chrome-welcome.png) | ![screenshot](documentation/chrome-game.png) | ![screenshot](documentation/chrome-playagain.png) | Works as expected |
| Firefox | ![screenshot](documentation/firefox-welcome.png) | ![screenshot](documentation/firefox-game.png) | ![screenshot](documentation/firefox-playagain.png) | Works as expected |
| Opera | ![screenshot](documentation/opera-welcome.png) | ![screenshot](documentation/opera-game.png) | ![screenshot](documentation/opera-playagain.png) | Works as expected |

## Responsiveness

I've tested my deployed project on the following devices to check for responsiveness issues.

- Mobile
- Tablet
- Desktop

| Device | Welcome | Game | Play again | Notes |
| --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot] () | ![screenshot]() | ![screenshot]() | Works as expected |
| Tablet (DevTools) | ![screenshot] () | ![screenshot]() | ![screenshot]() | Works as expected |
| Desktop | ![screenshot](documentation/chrome-welcome.png) | ![screenshot](documentation/chrome-game.png) | ![screenshot](documentation/chrome-playagain.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Welcome | ![screenshot] () | ![screenshot]() | ![screenshot]() | Works as expected |
| Play | ![screenshot] () | ![screenshot]() | ![screenshot]() | Works as expected |
| Play again | ![screenshot] () | ![screenshot]() | ![screenshot]() | Works as expected |

## Defensive Programming

PP3 (Python-only):
- Users must enter a valid letter/word/string when prompted
- Users must choose from a specific list only


| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Welcome | | | | | |
| | Feature is expected to go to choose the correct category when the user has entered a number between 1 and 3 | Tested the feature writing a number | The feature behaved as expected and chose a category within the game | Test concluded and passed | ![screenshot](documentation/feature01.png) |
| Game | | | | | |
| | Feature is expected to do add the guessed letter in correct places when user guess right | Tested the feature by typing the one of the right letters | The feature behaved as expected and places the letter in the right place | Test concluded and passed | ![screenshot](documentation/feature02.png) |
| | Feature is expected to add pieces of the hangman when the player guesses wrong letter | Tested the feature by guessing the wrong letter | The feature behaved as expected and added pieces of the hangman | Test concluded and passed | ![screenshot](documentation/feature03.png) |
| | Feature is expected to add pieces of the hangman when the player guesses an invalid character such as a number | Tested the feature by guessing a number | The feature behaved as and wrote, invalid guess | Test concluded and passed | ![screenshot](documentation/feature04.png) |
| | Feature is expected to add pieces of the hangman when the player guesses an invalid character such as a special character | Tested the feature by guessing a "?" | The feature behaved as and wrote, invalid guess | Test concluded and passed | ![screenshot](documentation/feature05.png) |
| Play again | | | | | |
| | When the game is over, feature is expected to ask the player if they want to play again | Tested the feature by finishing a round of hangman | The feature behaved as expected, and gave me the option to play again after finishing a round | Test concluded and passed | ![screenshot](documentation/feature06.png) |
| | Feature is expected to take player to categories again after choosing yes | Tested the feature by enter y | The feature behaved as expected and gave me the option to choose a category after selecting yes | Test concluded and passed | ![screenshot](documentation/feature07.png) |
| | Feature is expected to take player to say "thanks for playing" again after choosing no | Tested the feature by entering no | The feature behaved as expected and said "thanks for playing" after typing n | Test concluded and passed | ![screenshot](documentation/feature08.png) |

## Bugs

- After adding new categories and typing them in global category, the game wouldn't open.

    ![screenshot](documentation/bug03.png)

    - To fix this, I removed the underline and added named it by category instead of filename.


- Line to long.

    ![screenshot](documentation/bug04.png)

    - To fix this, I cut line in to two lines.

- Trailing whitespace.

    ![screenshot](documentation/bug04.png)

    - To fix this, I deleted whitespace.

## Unfixed Bugs

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.



There are no remaining bugs that I am aware of.
