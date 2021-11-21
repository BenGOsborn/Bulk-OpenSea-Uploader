import os
import dotenv
from uploader import Uploader
import json

def main():
    # Initialize env variables
    dotenv.load_dotenv()
    seed_phrase = os.getenv("SEED_PHRASE")
    password = os.getenv("PASSWORD")

    # Initialize
    uploader = Uploader()
    uploader.connect_metamask(seed_phrase, password)

    # Connect to the specified network - ENTER THE APPROPRIATE NETWORK
    # uploader.add_network("", 0, 1) # Default network provided by Metamask
    NETWORK_RPC = "https://rpc-mumbai.maticvigil.com/"
    CHAIN_ID = 80001
    uploader.add_network(NETWORK_RPC, CHAIN_ID) # Custom network to add to Metamask
    uploader.open_metamask()

    # Connect to OpenSea
    uploader.connect_opensea(True)
    COLLECTION_URL = "https://testnets.opensea.io/collection/big-test-4"
    uploader.set_collection_url(COLLECTION_URL)

    # Upload NFT data in 'metadata.json' to OpenSea - MODIFY THE UPLOAD FUNCTION AND THE METADATA TO CONTAIN ANY ADDITIONAL METADATA
    metadata = json.load(open(os.path.join(os.getcwd(), "data", "manifest.json")))
    first_upload = True
    for i, data in enumerate(metadata):
        try:
            uploader.upload(os.path.join(os.getcwd(), "data", "images", data["image"]), data["name"])
            if first_upload:
                uploader.sign_transaction()
                first_upload = False 
        except Exception as e:
            print(f"Failed to upload NFT {i} '{data['name']}' for reason '{e}'.")

    # Close
    uploader.close()

# Run main if this file is run directly
if __name__ == "__main__":
    main()