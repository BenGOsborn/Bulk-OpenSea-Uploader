# Bulk OpenSea Uploader

## WARNING: DO NOT RUN CODE THAT YOU DO NOT UNDERSTAND. BE CAREFUL WHEN GIVING THIS SCRIPT ACCESS TO YOUR CRYPTO WALLET. I AM NOT RESPONSIBLE FOR ANY FUNDS YOU MAY LOSE.

## Bulk uploads NFT data to OpenSea.

### Description

A simple script which bulk uploads your NFT's to OpenSea without having to deploy your own smart contract and without having to pay any gas fees.

### Requirements

- Python==3.8
- Pipenv==2021.5.29

### Instructions

1. Make a new `.env` file in `src` and inside of it specify your seed phrase `SEED_PHRASE=` and password `PASSWORD=`
2. Copy your NFT assets you wish to upload to `data/images`, then inside of `data/metadata.json`, specify the metadata of each asset you wish to upload as an NFT to OpenSea. By default, the script only accepts `name` and `image` attributes, where the `name` is the name of the NFT, and the `image` is the name of the asset stored in the 