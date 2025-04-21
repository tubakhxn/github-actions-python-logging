import logging

logging.basicConfig(level=logging.INFO)

def main():
    logging.info("Script started.")
    #error
    x = 10 / 0

if __name__ == "__main__":
    main()
