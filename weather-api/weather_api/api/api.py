from typing import Optional

import fastapi
from fastapi import Depends

from weather_api.models.location import Location
from weather_api.services import openweatherservice

router = fastapi.APIRouter()

@router.get("/api/weather/{city}")
async def weather(loc: Location = Depends(), units: Optional[str] = 'metric'):
    report = await openweatherservice.get_report_async(loc.city, loc.state, loc.country, units)
    return report
