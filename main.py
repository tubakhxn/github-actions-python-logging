import logging

logging.basicConfig(
    filename='app.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    logging.info("Script started.")
    try:
        x = 10 / 0
    except ZeroDivisionError as e:
        logging.error(f"Error occurred: {e}")
        raise

if __name__ == "__main__":
    main()
