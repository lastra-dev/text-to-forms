# Text To Forms
> Google form builder using text files.

[![License][Github-license]][License]
[![Twitter][twitter-followers]][twitter-url]

Text To Forms is a simple tool to create multi-answer Google forms from txt files using Python and Selenium library.

![Demo gif](https://media.giphy.com/media/VDTrwzq4ohqFr8mkSR/giphy.gif)

## Installation

Install [Selenium][selenium-link]:
```
pip3 install selenium
```
Clone this repository:
```
git clone https://github.com/oscaragl13/text-to-forms.git
```
Change directory to project's folder:
```
cd text-to-forms
```
### Download chromedriver and move it into project's directory:
Make sure to exchange \<LATEST RELEASE\> to the number below.

[![Chromedriver version][chromedriver-latest-release]][chromedriver-download]

#### Windows:
```
curl -o chromedriver.zip https://chromedriver.storage.googleapis.com/<LATEST RELEASE>/chromedriver_win32.zip
tar -xf chromedriver.zip
del chromedriver.zip
```
#### MacOS:
```
curl -o chromedriver.zip https://chromedriver.storage.googleapis.com/<LATEST RELEASE>/chromedriver_mac64.zip
unzip chromedriver.zip
rm chromedriver.zip
xattr -d com.apple.quarantine chromedriver
```
#### Linux:
```
curl -o chromedriver.zip https://chromedriver.storage.googleapis.com/<LATEST RELEASE>/chromedriver_linux64.zip
unzip chromedriver.zip
rm chromedriver.zip
```
Open questions.txt inside project's directory and type your questions, or copy them into the file, questions must be separated by blank lines and each one must have at least one answer, you can also leave the default questions.

*See [questions.txt](questions.txt) for reference...*

Run program:
```
python3 main.py
```

## Usage example

This tool can be specially useful when you have written an exam in Word or PDF, and you need to copy it to a Google form. Imagine having to copy a hundred questions with its answers one by one.

## Screenshots
![screenshot1](https://i.imgur.com/OHEn8IL.png)

## Release History

* 1.0.0
    * Work in progress

## Meta

Oscar Lastra – [@oscaraGL16](https://twitter.com/oscaragl16) – oscar.glastra@gmail.com

<!-- LICENSE INFORMATION -->

[Github Profile][Github-url]

## Contributing

1. Fork it (<https://github.com/oscaragl13/text-to-forms/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[twitter-url]: https://twitter.com/oscaragl16
[Github-url]: https://github.com/oscaragl13/text-to-forms/
[Github-license]: https://img.shields.io/github/license/oscaragl13/text-to-forms
[License]: https://github.com/oscaragl13/text-to-forms/blob/main/LICENSE
[twitter-followers]: https://img.shields.io/twitter/follow/oscaragl16.svg?style=social&label=Follow
[chromedriver-latest-release]: https://img.shields.io/badge/dynamic/json?color=blue&label=LATEST%20RELEASE%3A&query=%24%5B%27client%27%5D%5B%27Google%20Chrome%27%5D%5B%2A%5D%5B%27version%27%5D&url=https%3A%2F%2Fvergrabber.kingu.pl%2Fvergrabber.json
[chromedriver-download]: https://chromedriver.chromium.org/downloads
[selenium-link]: https://selenium-python.readthedocs.io/installation.html
