# Text To Forms
> Google form generator using txt files.

[![License][Github-license]][License]
[![Twitter][twitter-followers]][twitter-url]

Text To Forms is a simple tool to create multi-answer Google forms from txt files using Python and Selenium library.

![Demo gif](https://media.giphy.com/media/VDTrwzq4ohqFr8mkSR/giphy.gif)

## Installation

Linux, Windows & MacOS:

In terminal:
```
git clone https://github.com/oscaragl13/text-to-forms.git
```

Download the version of [Chromedriver](https://chromedriver.chromium.org/downloads) that matches your Google Chrome browser version and move it into project's directory.
Open questions.txt inside project's directory and type your questions or copy them into the file, questions must be separated by blank spaces and they must have at least one answer. *See [questions.txt](questions.txt) for reference...*

Change directory to project's folder:
```
cd text-to-forms
```

Run program:
```
python main.py
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
