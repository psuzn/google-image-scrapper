# google-image-scrapper
> Similar image scrapper from google reverse image search using selenium 

The idea is you'll give a link to a image and this script will search similar image to the image on that link using google reverse image search and downloads for you.
## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [Maintainers](#maintainers)
- [Contribute](#contribute)
- [License](#license)

## Install
clone the repo to your machine
```
$ git clone https://github.com/psuzn/google-image-scrapper.git
```
Move into ```google-image-scrapper``` directory
```
$ cd google-image-scrapper
```
Then install require modules

```
$ sudo pip install -r requirements.txt
```

## Usage
The ```scrapper.py``` reads the ```images.txt``` for the info about the images to search from.

Basic structure of ```images.txt``` is 
```
folder-name no-of-images-to-download Link-for-a-sample-image
```
Example: 
```images.txt```
```
led 100 https://probots.co.in/images/large/8mmWhiteLED_01_LRG.jpg
resistor 50 https://media.rs-online.com/t_large/R0131772-01.jpg
```
i.e.

- From first line : 100 similar images to the image on the link will be downloaded into ```dowmload/led``` directory.

- From second line : 50 similar images to the image on the link will be downloaded into 
```download/resistor``` directory 

Note:
 - only one space between the each section in ```images.txt```.
 - All the images will be downloaded inside ```download/``` directory.
 - I found that if you  were logged in to google then it will give better results so script will promot for gmail and password (though you can skip by just hitting enter).
## Maintainers

[@psuzn](https://github.com/psuzn)

## Contribute

Feel free to dive in! [Open an issue](https://github.com/psuzn/google-image-scrapper) or submit PRs.

## License

MIT © 2018 psuzn
