import logging

logging.basicConfig(level=logging.INFO)

def main():
    try:
        x = 10 / 0
    except ZeroDivisionError as e:
        logging.error("Division by zero occurred", exc_info=True)

if __name__ == "__main__":
    main()
