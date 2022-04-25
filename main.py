import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from starlette.requests import Request

from api.scrape import rpiLoc

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="Unofficial rpilocator API",
    description="An Unofficial REST API for [RpiLocator](https://rpilocator.com/), Made by [Andre "
                "Saddler]( "
                "https://github.com/axsddlr)",
    version="1.0.3",
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

# init limiter
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# init classes
rpiloc = rpiLoc()


@app.get("/pi4/{country}", tags=["pi4"])
@limiter.limit("100/minute")
def all_pi4_in_a_country(request: Request, country):
    """get all pi4 in a country"""
    return rpiloc.rpi_all(country)


@app.get("/v2/pi4/{region}", tags=["rss"])
@limiter.limit("1/minute")
def all_pi4_in_a_region(request: Request, region):
    """get all pi4 in a country"""
    return rpiloc.get_rss_entires(region)


@app.get("/v3/pi4/{region}", tags=["twitter"])
@limiter.limit("55/minute")
def all_pi4_in_a_region_tweets(request: Request, region):
    """get all pi4 in a country via twitter alerts"""
    return rpiloc.get_rpil_tweets(region)


@app.get("/pi4/{country}/{gbs}", tags=["pi4"])
@limiter.limit("100/minute")
def all_pi4_in_country_with_model_via_GiB(request: Request, country, gbs):
    """get all pi4 in a country with a plus model"""
    return rpiloc.rpi_model(country, gbs)


@app.get("/v2/pi4/{region}/{gbs}", tags=["rss"])
@limiter.limit("1/minute")
def all_pi4_in_region_with_model_via_GiB(request: Request, region, gbs):
    """get all pi4 in a region with a plus model"""
    return rpiloc.get_rss_model_entires(region, gbs)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3000)
