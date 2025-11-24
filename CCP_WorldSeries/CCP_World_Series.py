import os
from typing import Dict, List, Optional

# Constants
START_YEAR = 1903
END_YEAR = 2025
DATA_FILE = "WorldSeriesWinners.txt"  # File 

def load_winners(filepath: str) -> Dict[int, Optional[str]]:

    # Read WorldSeriesWinners.txt and return year -> team, or none if there was no game. 

    # Open the file
    with open(filepath, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]

    expected = END_YEAR - START_YEAR + 1
    if len(lines) != expected:
        # This is just because the file doesn't want to cooperate sometimes (?)
        print(f"Warning: expected {expected} lines but found {len(lines)} in '{DATA_FILE}'.")

    # Build year->team/None
    year_to_team: Dict[int, Optional[str]] = {}
    not_played_markers = ("not played", "no world series")
    for i, raw in enumerate(lines):
        year = START_YEAR + i
        lower = raw.lower()
        if any(marker in lower for marker in not_played_markers) or raw == "":
            year_to_team[year] = None
        else:
            year_to_team[year] = raw
    return year_to_team

def build_team_index(year_to_team: Dict[int, Optional[str]]) -> Dict[str, List[int]]:
    # Build a reverse index - team -> a sorted list of championship years. (None) for years not played
    team_to_years: Dict[str, List[int]] = {}
    for year, team in year_to_team.items():
        if team is None:
            continue
        team_to_years.setdefault(team, []).append(year)
    for years in team_to_years.values():
        years.sort()
    return team_to_years

def handle_year_query(year: int,
                      year_to_team: Dict[int, Optional[str]],
                      team_to_years: Dict[str, List[int]]) -> str:
    # Returns a exact text block for the given year

    # Out-of-range check
    if year < START_YEAR or year > END_YEAR:
        return "\nThat year is not included in the data.\n"

    winner = year_to_team.get(year)
    if winner is None:
        return f"\nThe World Series was not played in {year}.\n"

    # Winner exists
    msg_parts: List[str] = []
    msg_parts.append(f"\n{winner} won that year.\n\n")

    wins_list = team_to_years.get(winner, [])
    count = len(wins_list)

    if count == 1:
        # Winners time wooo, This is for the ones with one win and the other is for multiple wins
        msg_parts.append(f"They have won  {count} time. Their only win was in {wins_list[0]}  \n")
    else:
        msg_parts.append(f"They have won  {count} times. Here is a list of the years: \n")
        for y in wins_list:
            msg_parts.append(f"{y}  \n")
        msg_parts.append("\n")  # blank line :)

    return "".join(msg_parts)

def prompt_continue() -> bool:
    # Asks if user wants to continue or not
    ans = input("\n\tDo you want to continue? (y/n): ").strip().lower()
    return ans == "y"

def main() -> None:
    # Intro line (exact)
    print("This program displays the MLB World Series Champions.\n")

    # This is so it can run from any IDE
    filepath = os.path.join(os.path.dirname(__file__), DATA_FILE)

    try:
        year_to_team = load_winners(filepath)
    except FileNotFoundError:
        print(f"Error: could not find '{DATA_FILE}' next to this script.")
        print("Script folder:", os.path.dirname(__file__))
        return

    team_to_years = build_team_index(year_to_team)

    # Interactive loop here
    while True:
        print(f"Enter a year in the range from {START_YEAR} to {END_YEAR}")
        year_str = input(" to see which team won that year: ").strip()

        # Non-integer inputs like year not included in the data
        try:
            year = int(year_str)
        except ValueError:
            print("\nThat year is not included in the data.\n")
            if not prompt_continue():
                break
            continue

        # Print results
        print(handle_year_query(year, year_to_team, team_to_years))

        # Ask user if they want to continue 
        if not prompt_continue():
            break

if __name__ == "__main__":
    main()
