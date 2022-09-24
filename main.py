# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# reference https://www.cnblogs.com/poloyy/p/15312290.html
# https://fastapi.tiangolo.com/tutorial/body-fields/
# 框架比较：https://blog.csdn.net/weixin_46364913/article/details/124007850

import uvicorn

from pathlib import Path

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from baishitong.api.v1 import api_router
from baishitong.config import CONF, configure
from baishitong.db import setup as db_setup
from baishitong.log import LOG, setup as log_setup
from baishitong.types import constants


PROJECT_NAME = "BaiShiTong Server"


async def on_startup() -> None:
    configure("baishitong")
    log_setup(
        Path(CONF.default.log_dir).joinpath("baishitong", "baishitong-server.log"),
        debug=CONF.default.debug,
    )
    await db_setup()

    # Set all CORS enabled origins
    if CONF.default.cors_allow_origins:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in CONF.default.cors_allow_origins],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    LOG.debug("baishitong server start")


async def on_shutdown() -> None:
    LOG.debug("baishitong server stop")


app = FastAPI(
    title=PROJECT_NAME,
    openapi_url=f"{constants.API_PREFIX}/openapi.json",
    on_startup=[on_startup],
    on_shutdown=[on_shutdown],
)

app.include_router(api_router, prefix=constants.API_PREFIX)


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8080, reload=True, debug=True)