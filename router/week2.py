from fastapi import APIRouter, status, HTTPException, Depends
from loguru import logger

from pydantic import BaseModel, Field

from enum import Enum
import time
import random
import json
from urllib.request import urlopen
import requests

router = APIRouter()

@router.get("/countdown")
async def countdown(count: int = 5):
    for countdown in range(count):
        logger.info(count - countdown)
        time.sleep(1)
    logger.info("Hey")
    return "Hey"

@router.get("/spells")
async def spells():
    spells = [
        "Riddikulus!",
        "Wingardium Leviosa!",
        "Avada Kedavra!",
        "Expecto Patronum!",
        "Nox!",
        "Lumos!",
    ]
    random_spell = spells[random.randint(0, len(spells) - 1)]
    logger.info(random_spell)
    return random_spell


class Stooge(str, Enum):
    MOE = 'Moe'
    LARRY = 'Larry'
    CURLY = 'Curly'

@router.get("/quotes")
async def quotes(stooge: Stooge):
    stooge_quote = {
      Stooge.MOE.value: "A wise guy, huh?",
      Stooge.LARRY.value: "Ow!",
      Stooge.CURLY.value: "Nyuk nyuk!",
    }.get(stooge)
    if not stooge_quote:
        logger.error("stooge_quote not found for stooge %s", stooge)
        return HTTPException(status.HTTP_404_NOT_FOUND, f"Quote not found for stooge: {stooge}")
    logger.info(stooge_quote)
    return f"{stooge.value} says {stooge_quote}"


class ArchiveInput(BaseModel):
    url: str = Field(description="Type a website URL")
    era: str = Field(description="Type a year, month, and day, like 20150613")

@router.get("/archive")
async def archive(input = Depends(ArchiveInput)):
    logger.info("Let's find an old website.")
    url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (input.url, input.era)
    response = urlopen(url)
    contents = response.read()
    text = contents.decode("utf-8")
    data = json.loads(text)
    try:
        old_site = data["archived_snapshots"]["closest"]["url"]
        logger.info("Found this copy: ", old_site)
        return old_site
    except:
        logger.warning("Sorry, no luck finding %s", input.site)
        return HTTPException(status.HTTP_404_NOT_FOUND, f"Sorry, no luck finding: {input.site}") 


@router.get("/archive2")
async def archive2(input = Depends(ArchiveInput)):
    """Same thing, but using requests library."""
    logger.info("Let's find an old website.")
    url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (input.site, input.era)
    response = requests.get(url)
    data = response.json()
    try:
        old_site = data["archived_snapshots"]["closest"]["url"]
        logger.info("Found this copy: ", old_site)
        return old_site
    except:
        logger.warning("Sorry, no luck finding %s", input.site)
        return HTTPException(status.HTTP_404_NOT_FOUND, f"Sorry, no luck finding: {input.site}") 

