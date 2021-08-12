# Pi zero ticker
Display your favourite stock price ticker on a display.


## Installation
1. Clone repository
2. Install python dependancies from `requirements.txt` with your favourite method
```bash
    pip install -r requirements.txt
```
3. Run script
```bash
    python ticker.py -d 10 -s GME 
```

## Usage
```
usage: ticker.py [-h] [--symbol SYMBOL] [--delay DELAY]

Script to display stock ticker price on a Inky pHAT display

optional arguments:
  -h, --help            show this help message and exit
  --symbol SYMBOL, -s SYMBOL
                        Ticker symbol
  --delay DELAY, -d DELAY
                        Ticker refresh interval (in sec)
```

## Tested hardware
This was designed for a Raspberry Pi zero W and a display of type [Inky pHAT 2.13" EPD](https://shop.pimoroni.com/products/inky-phat?variant=12549254938707) (black and white version)
