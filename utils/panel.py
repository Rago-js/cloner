from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.style import Style
from rich.panel import Panel as RichPanel
import json

def Panel():
    with open("./utils/config.json", "r") as json_file:
        data = json.load(json_file)
    print(" ")
    # Define custom styles for ON and OFF
    on_style = Style(color="green", bold=True)
    off_style = Style(color="red", bold=True)

    # Create a table with 2 columns
    table = Table(title="Rago Sunucu Kopyalama", show_header=True, header_style="bold")
    table.add_column("Ayarlar", style="cyan", no_wrap=True, width=30)
    table.add_column("Durum", justify="center", width=10)

    for ayarlar, Durum in data["copy_settings"].items():
        table.add_row(ayarlar.capitalize(), Text("AÇIK" if Durum else " KAPALI", style=on_style if Durum else off_style))

    console = Console()
    console.print(table)

    # Paragraph with change logs
    paragraph = """Rago Tarafından Hazırlanmıştır."""
    console.print(RichPanel(paragraph, style="bold blue", width=47))
    
    # Version information
    version = "paylaşmayın."
    console.print(RichPanel(f"izinsiz {version}", style="bold magenta", width=47))


def Panel_Run(guild, user):
    with open("./utils/config.json", "r") as json_file:
        data = json.load(json_file)
    print(" ")
    # Define custom styles for ON and OFF
    on_style = Style(color="green", bold=True)
    off_style = Style(color="red", bold=True)

    # Create a table with 2 columns
    table = Table(title="Rago Sunucu Kopyalama", show_header=True, header_style="bold")
    table.add_column("Kopyalıyıcı aktif...", style="cyan", no_wrap=True, width=30)
    table.add_column("Durum", justify="center", width=10)

    for ayarlar, Durum in data["copy_settings"].items():
        table.add_row(ayarlar.capitalize(), Text("AÇIK" if Durum else " KAPALI", style=on_style if Durum else off_style))

    # Stick a new table in the footer
    footer = Table(show_header=False, header_style="bold", show_lines=False, width=47)
    footer.add_column(justify="center")
    footer.add_row(f"[bold magenta]Sunucu İsmi: [green]{guild}")
    footer.add_row(f"[bold magenta]Giriş Yapıldı: [green]{user}")

    console = Console()
    console.print(table)
    console.print(footer)

    # Paragraph with change logs
    paragraph = """Rago Tarafından Hazırlanmıştır."""
    console.print(RichPanel(paragraph, style="bold blue", width=47))
    
    # Version information
    version = "4.0"
    console.print(RichPanel(f"Version: {version}", style="bold magenta", width=47))
