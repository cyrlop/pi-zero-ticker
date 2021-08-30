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
usage: ticker.py [-h] [--symbol SYMBOL] [--mode {simple,graph}]
                 [--delay DELAY] [--graph_range GRAPH_RANGE]
                 [--graph_int {1d,1wk,1mo,1m}] [--hflip] [--vflip]

Script to display stock ticker price on a Inky pHAT display

optional arguments:
  -h, --help            show this help message and exit
  --symbol SYMBOL, -s SYMBOL
                        Ticker symbol
  --mode {simple,graph}, -m {simple,graph}
                        Display mode
  --delay DELAY, -d DELAY
                        Ticker refresh interval (in sec)
  --graph_range GRAPH_RANGE, -r GRAPH_RANGE
                        Graph x range (nb ticks depending on interval)
  --graph_int {1d,1wk,1mo,1m}, -i {1d,1wk,1mo,1m}
                        Interval: '1d', '1wk', '1mo', or '1m' for daily,
                        weekly, monthly, or minute data
  --hflip               Horizontally flip display
  --vflip               Vertically flip display
```

## Tested hardware
This was designed for a Raspberry Pi zero W and a display of type [Inky pHAT 2.13" EPD](https://shop.pimoroni.com/products/inky-phat?variant=12549254938707) (black and white version)

## Full installation guide

This guide assumes you use the hardware from the "Tested hardware" section and might differ if you use other things.

1. Plug screen on GPIO headers

2. Install OS on SD card (I used Raspberry OS 32-bit Lite)
    - For headless set-up, enable `ssh` and Wi-Fi following [these steps](https://www.raspberrypi.org/documentation/computers/configuration.html#setting-up-a-headless-raspberry-pi).


3. Enable SPI
    - Add this line to `/boot/config.txt` and reboot:
    ```
    dtparam=spi=on
    ```

4. Update system and install required libraries
    ```bash
    sudo apt update
    sudo apt dist-upgrade
    sudo apt install git python3-pip libatlas-base-dev libopenjp2-7 libtiff5
    ```
5. Get the code following the steps from the "Installation" section

6. Create a service to run script at startup:
    - Copy the service file from `misc/ticker.service` to `/lib/systemd/system/ticker.service`
    - Give proper permission:
    ```
    sudo chmod 644 /lib/systemd/system/ticker.service
    ```
    - Enable service and reboot
    ```
    sudo systemctl daemon-reload
    sudo systemctl enable ticker.service
    sudo reboot
    ```
    - Troubleshoot with `sudo journalctl -u ticker`
