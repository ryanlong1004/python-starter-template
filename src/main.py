import logging
from utils import get_root_dir

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
    handlers=[logging.FileHandler("archive_results.log"), logging.StreamHandler()],
)

def main():
    print(get_root_dir())

if __name__ == "__main__":
    main()