from rich.console import Console
from rich.table import Table
import calendar

console = Console()

year = 2026
month = 1

cal = calendar.monthcalendar(year, month)

table = Table(title="🗓 January 2026", show_lines=True)

for day in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
    table.add_column(day, justify="center")

for week in cal:
    table.add_row(*[str(d) if d != 0 else "" for d in week])

console.print(table)