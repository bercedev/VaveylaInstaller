from json import loads
from rich.prompt import Prompt
from . import logo, console, bilgi

def importlang ():
    console.clear()
    logo()
    bilgi("\n\[1] Türkçe\n\[2] Azərbaycanca\n\[3] English")
    Dil = Prompt.ask("[bold yellow]Bir dil seçin / Please select a language[/]", choices=["1", "2", "3"], default="1")

    if Dil == "1":
        COUNTRY = "Turkey"
        LANGUAGE = "TR"
        TZ = "Europe/Istanbul"
    elif Dil == "2":
        COUNTRY = "Azerbaijan"
        LANGUAGE = "AZ"
        TZ = "Asia/Baku"
    elif Dil == "3":
        COUNTRY = "United Kingdom"
        LANGUAGE = "EN"
        TZ = "Europe/London"

    return COUNTRY, LANGUAGE, TZ

COUNTRY, LANGUAGE, TZ = importlang()
LANG = loads(open(f"./vaveylainstaller/language/{LANGUAGE}.wjson", "r").read())["STRINGS"]
