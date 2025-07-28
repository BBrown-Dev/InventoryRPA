#!/usr/bin/env python3

# This script processes an inventory dataset, cleans it, flags issues, writes the cleaned data,
# and sends alerts for any issues found. It also logs the process and records metrics.

import argparse, logging
import os

from dotenv import load_dotenv
from services.extract import load_inventory
from services.process import clean_and_flag
from services.update import write_clean
from services.alert import send_alerts
from metrics import Metrics


# This function sets up the logging configuration for the script.
def setup_logging():
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        filename="logs/run.log", level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )


# This function sets up the logging configuration for the script.
def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--input", default="data/inventory_raw.csv")
    p.add_argument("--cleaned", default="data/inventory_clean.csv")
    return p.parse_args()


# This is the main function that orchestrates the loading, processing, and alerting of the inventory data.
def main():
    load_dotenv()
    setup_logging()
    m = Metrics()

    args = parse_args()
    df_raw = load_inventory(args.input)
    df_clean = clean_and_flag(df_raw)
    write_clean(df_clean, args.cleaned)
    send_alerts(df_clean)

    m.record("total_items", len(df_clean))
    m.dump()


if __name__ == "__main__":
    main()
