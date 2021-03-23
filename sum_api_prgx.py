#!/usr/bin/env python

from sum_inout import SumModel
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

app = FastAPI(title="PRGX SUM API",
              description="Here's our API to handle basic sum of two digits", version="1.0")



@app.post("/api/sum/", summary="Sum X and Y",
          description="Allows the addition of two certain digits given by User")
async def sum_input(sum_in: SumModel):
    """
    Retrieves the addition of two certain digits given by User request body
        :param sum_in: Class that represent the correct structure for post request body

        :return: JSONResponse of the addition of digits otherwise the given error response
    """
    x = sum_in.x
    y = sum_in.y
    sum_out = x + y

    return JSONResponse({"sum": sum_out})


if __name__ == "__main__":
    uvicorn.run("sum_api_prgx:app", host="127.0.0.1", port=5000, log_level="info")
