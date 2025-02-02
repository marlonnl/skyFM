import argparse
import dotenv
import os

import lastfm

dotenv.load_dotenv()

LASTFM_USER = os.getenv("LASTFM_USER")

parser = argparse.ArgumentParser(
    prog="skyfm",
    description="creates a mosaic of your lastfm charts and post to your bsky account",
)

parser.add_argument(
    "username",
    type=str,
    default=LASTFM_USER,
    help="your lastfm username"
)
parser.add_argument(
    "-p",
    "--period",
    type=int,
    choices=[0, 7, 30, 90, 120, 360],
    default=7,
    help="the period in days. 0 = overall",
)
parser.add_argument(
    "-g",
    "--grid",
    type=int,
    nargs=2,
    default=[3,3],
    help="defines the size for the mosaic grid (rows, columns)"
)
parser.add_argument(
    #--no-bsky
    "-b",
    "--bsky",
    action=argparse.BooleanOptionalAction,
    help="Toggle on/off posting your mosaic to your bsky account. Posting is the default option"
)
args = parser.parse_args()
print(f"Retrieving data from {args.username}, period {args.period}, grid {args.grid}, bsky {args.bsky}")


def new_mosaic(username=args.username, period=args.period, grid=args.grid):
    """
    Controls the flux of creation of a new mosaic.
    """

    print(f"[skyfm] Iniciando criação de mosaico para o usuário {username}, no período de {period} dias com um grid {grid[0]}x{grid[1]}...")
    print("[skyfm] Requisitando dados do LastFM...")
    lastfm_data = lastfm.get_data(username, period, grid)

new_mosaic(args.username, args.period, args.grid)