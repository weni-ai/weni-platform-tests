import os
import time

import schedule


def run_tests():
    os.popen("python -m unittest --verbose").read()


def main():
    schedule.every(1).hour.do(run_tests)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
