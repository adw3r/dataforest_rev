import configparser
import os
from argparse import ArgumentParser, Namespace
from pathlib import Path

from dotenv import load_dotenv

config = configparser.ConfigParser()
load_dotenv()

ROOT_FOLDER = Path(__file__).absolute().parent.parent
CONFIG_FILE = Path(ROOT_FOLDER, 'config.ini')
config.read_file(CONFIG_FILE.open())


def get_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument('--proxy_pool', default=config['general']['DEFAULT_PROXIES'], type=str)
    args = parser.parse_args()
    return args


# TARGETS_API_HOST = config['general']['TARGETS_API_HOST']
PROXIES_API_HOST = config['general']['PROXIES_API_HOST']
# LOGGING_LEVEL = config['general'].getint('LOGGING_LEVEL')

CAPMONSTER_HOST = os.environ.get('CAPMONSTER_HOST')
CAPMONSTER_KEY = os.environ.get('CAPMONSTER_KEY')

ARGS = get_args()
DEFAULT_PROXIES = ARGS.proxy_pool
