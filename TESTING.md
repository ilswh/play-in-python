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
|play.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/play-in-python/main/run.py) | ![screenshot](documentation/py-validation-run.png) | W291 trailing whitespace |
| stages.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/play-in-python/main/boutique-ado/settings.py) | ![screenshot](documentation/py-validation-settings.png) | E501 line too long |
| lives.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/play-in-python/main/blog/views.py) | ![screenshot](documentation/py-validation-blog-views.png) | Pass: No Errors |
| stages.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ilswh/play-in-python/main/checkout/urls.py) | ![screenshot](documentation/py-validation-checkout-urls.png) | W292 no newline at end of file |

## Browser Compatibility

- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Safari](https://support.apple.com/downloads/safari)

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | About | Contact | etc | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browser-chrome-home.png) | ![screenshot](documentation/browser-chrome-about.png) | ![screenshot](documentation/browser-chrome-contact.png) | ![screenshot](documentation/browser-chrome-etc.png) | Works as expected |
| Firefox | ![screenshot](documentation/browser-firefox-home.png) | ![screenshot](documentation/browser-firefox-about.png) | ![screenshot](documentation/browser-firefox-contact.png) | ![screenshot](documentation/browser-firefox-etc.png) | Works as expected |
| Safari | ![screenshot](documentation/browser-safari-home.png) | ![screenshot](documentation/browser-safari-about.png) | ![screenshot](documentation/browser-safari-contact.png) | ![screenshot](documentation/browser-safari-etc.png) | Minor CSS differences |

## Responsiveness

- Mobile
- Tablet
- Desktop

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Welcome | Rules | Play | etc | Notes |
| --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsive-mobile-home.png) | ![screenshot](documentation/responsive-mobile-about.png) | ![screenshot](documentation/responsive-mobile-contact.png) | ![screenshot](documentation/responsive-mobile-etc.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsive-tablet-home.png) | ![screenshot](documentation/responsive-tablet-about.png) | ![screenshot](documentation/responsive-tablet-contact.png) | ![screenshot](documentation/responsive-tablet-etc.png) | Works as expected |
| Desktop | ![screenshot](documentation/responsive-desktop-home.png) | ![screenshot](documentation/responsive-desktop-about.png) | ![screenshot](documentation/responsive-desktop-contact.png) | ![screenshot](documentation/responsive-desktop-etc.png) | Works as expected |

## Lighthouse Audit

Use this space to discuss testing the live/deployed site's Lighthouse Audit reports.
Avoid testing the local version (especially if developing in Gitpod), as this can have knock-on effects of performance.

Sample Lighthouse testing documentation:

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Welcome | ![screenshot](documentation/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse-home-desktop.png) | Some minor warnings |
| Rules | ![screenshot](documentation/lighthouse-about-mobile.png) | ![screenshot](documentation/lighthouse-about-desktop.png) | Some minor warnings |
| Play | ![screenshot](documentation/lighthouse-gallery-mobile.png) | ![screenshot](documentation/lighthouse-gallery-desktop.png) | Slow response time due to large images |
| x | x | x | repeat for any other tested pages/sizes |

## Defensive Programming

PP3 (Python-only):
- Users must enter a valid letter/word/string when prompted
- Users must choose from a specific list only

You should include any manual tests performed, and the expected results/outcome.
Each test case should be specific, objective, and step-wise replicable.


When in doubt, use the above method instead, and delete the table below.


| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Welcome | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| Game | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | |
| | Load gallery images | All images load as expected | Pass | |


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
