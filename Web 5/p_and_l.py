import argparse

DAYS_IN = {"day": 1,
           "month": 30,
           "year": 360}

parser = argparse.ArgumentParser()
parser.add_argument("--per-day", type=float, required=False, default=0)
parser.add_argument("--per-week", type=float, required=False, default=0)
parser.add_argument("--per-month", type=float, required=False, default=0)
parser.add_argument("--per-year", type=float, required=False, default=0)
parser.add_argument("--get-by", choices=("day", "month", "year"), required=False, default="day")

args = parser.parse_args()

per_day = args.per_day
per_week = args.per_week
per_month = args.per_month
per_year = args.per_year
get_by = args.get_by

per_day = per_day + per_week / 7 + per_month / 30 + per_year / 360

print(int(per_day * DAYS_IN[get_by]))
