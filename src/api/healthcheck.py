""" Service Status Endpoint"""

from http import HTTPStatus

from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["Healthcheck"])


@router.get("/healthcheck", status_code=HTTPStatus.OK)
def health_check():
    """returns the service status"""
    return HTTPStatus.OK


@router.get("/status_code/{status_code}")
async def get_status_code_for_testing(status_code: int):
    """
    Returns a response according to the input status code
    """
    if status_code == 200:
        return {"message": "OK"}
    elif status_code == 404:
        raise HTTPException(status_code=404, detail="Not Found")
    elif status_code == 500:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    else:
        raise HTTPException(status_code=400, detail="Invalid status code")
