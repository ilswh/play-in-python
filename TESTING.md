# Testing

Return back to the [README.md](README.md) file.

In this section, you need to convince the assessors that you have conducted enough testing to legitimately believe that the site works well.
Essentially, in this part, you should go over all of your project's features, and ensure that they all work as intended,
with the project providing an easy and straightforward way for the users to achieve their goals.

## Code Validation

Use the space to discuss code validation for any of your own code files (where applicable).

### Python

DO THIS:
- As an API, using the "raw" URL appended to the linter URL.
    - To find the "raw" URL, navigate to your file directly on the GitHub repo.
    - On that page, GitHub provides a button on the right called "Raw" that you can click on.
    - From that new page, copy the full URL, and paste it after the CI Python Linter URL (with a `/` separator).
    - Check the example table below for a live demo.

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
|play.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/play-in-python/main/play.py) | ![screenshot](documentation/py-validation-play.png) | W291 trailing whitespace |
| stages.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/play-in-python/main/checkout/stages.py) | ![screenshot](documentation/py-validation-checkout-urls.png) | W292 no newline at end of file |
| words.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/play-in-python/main/checkout/words.py) | ![screenshot](documentation/py-validation-checkout-words.png) | W292 no newline at end of file |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Safari](https://support.apple.com/downloads/safari)

| Browser | Welcome | Game | Play again | Notes |
| --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/chrome-welcome.png) | ![screenshot](documentation/chrome-game.png) | ![screenshot](documentation/chrome-playagain.png) | Works as expected |
| Firefox | ![screenshot](documentation/firefox-welcome.png) | ![screenshot](documentation/firefox-game.png) | ![screenshot](documentation/firefox-playagain.png) | Works as expected |
| Opera | ![screenshot](documentation/opera-welcome.png) | ![screenshot](documentation/opera-game.png) | ![screenshot](documentation/opera-playagain.png) | Works as expected |

## Responsiveness

- Mobile
- Tablet
- Desktop

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Welcome | Play | Play again | Notes |
| --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot] () | ![screenshot]() | ![screenshot]() | Works as expected |
| Tablet (DevTools) | ![screenshot] () | ![screenshot]() | ![screenshot]() | Works as expected |
| Desktop | ![screenshot] () | ![screenshot]() | ![screenshot]() | Works as expected |

## Lighthouse Audit

Use this space to discuss testing the live/deployed site's Lighthouse Audit reports.
Avoid testing the local version (especially if developing in Gitpod), as this can have knock-on effects of performance.

Sample Lighthouse testing documentation:

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

You should include any manual tests performed, and the expected results/outcome.
Each test case should be specific, objective, and step-wise replicable.

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Welcome | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| Game | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | |
| Play again | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | |

## Bugs

This section is primarily used for JavaScript and Python applications,
but feel free to use this section to document any HTML/CSS bugs you might run into.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bug03.png)

    - To fix this, I _____________________.


- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

## Unfixed Bugs

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.



There are no remaining bugs that I am aware of.
