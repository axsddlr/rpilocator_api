import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.scrape import rpiLoc
from ratelimit import limits

app = FastAPI(
    title="Unofficial rpilocator API",
    description="An Unofficial REST API for [RpiLocator](https://rpilocator.com/), Made by [Andre "
                "Saddler]( "
                "https://github.com/axsddlr)",
    version="1.0.2",
    docs_url="/",
    redoc_url=None,
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# init classes
rpiloc = rpiLoc()

TWO_MINUTES = 150


@limits(calls=250, period=TWO_MINUTES)
@app.get("/pi4/{country}", tags=["News"])
def all_pi4_in_a_country(country):
    """get all pi4 in a country"""
    return rpiloc.rpi_all(country)


@limits(calls=250, period=TWO_MINUTES)
@app.get("/pi4/{country}/{gbs}", tags=["News"])
def all_pi4_in_country_with_model_via_GiB(country, gbs):
    """get all pi4 in a country with a plus model"""
    return rpiloc.rpi_model(country, gbs)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3000)
