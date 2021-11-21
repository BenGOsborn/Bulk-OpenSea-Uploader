# Bulk OpenSea Uploader

## WARNING: DO NOT RUN CODE THAT YOU DO NOT UNDERSTAND. BE CAREFUL WHEN GIVING THIS SCRIPT ACCESS TO YOUR METAMASK WALLET. I AM NOT RESPONSIBLE FOR ANY FUNDS YOU MAY LOSE.

## Bulk uploads NFT data to [OpenSea](https://opensea.io) automatically.

### Description

A simple script which bulk uploads your NFT's to OpenSea without having to deploy your own smart contract and without having to pay any gas fees. Set this script to run overnight and wake up to find all of your NFT's uploaded with no extra effort from you. Requires access to your [Metamask](https://metamask.io) wallet to run.

### Requirements

- Python==3.8
- Pipenv==2021.5.29

### Instructions

1. Make a new `.env` file in `src` and inside of it specify your seed phrase `SEED_PHRASE=` and password `PASSWORD=`
2. Copy your NFT assets you wish to upload to `src/data/assets`, then inside of `src/data/metadata.json`, specify the metadata of each asset you wish to upload as an NFT to OpenSea. By default, the script only accepts `name` and `asset` attributes, where the `name` is the name of the NFT, and the `asset` is the name of the asset stored in `src/data/assets`
3. Set your desired network in `main.py`. If you wish to use a default network specified by Metamask, uncomment the `uploader.set_network("", 0, 1) # Use a default network provided by Metamask` line, and replace the third argument with the position of where the default network appears in the Metamask networks list.
4. Inside of `src` run `pipenv install`
5. Download the latest [Chromedriver](https://chromedriver.chromium.org/downloads) and place the binary in `src/bin`. **NOTE** that if you are on Windows you will have to change the Chromedriver executable name in `uploader.py` from `chromedriver` to `chromedriver.exe`
6. Package up your Metamask extension, then copy the resulting `.crx` file, rename it to `metamask.crx`, and place it in `src/bin`
7. Within `src`, run `pipenv run python main.py`