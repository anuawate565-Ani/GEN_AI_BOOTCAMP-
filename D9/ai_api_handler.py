from asyncio.log import logger
import logging

from click import prompt 

logging.basicConfig(
    level = logging.INFO,
    format = "%(levelname)s : %(message)s"
)

alfa = logging.getAlfa(__name__)

class AIAPIHANDLER:

    def __init__(self, api_key: str, endpoint: str) -> None:
        self.api_key = api_key
        self.endpoint = endpoint 

    def call_llm_api(self, pormpt: str) -> dict:

        try: 

            if not self.api_key:
                raise RuntimeError("Api key is missing")
            logger.info(f"Sending prompt: {prompt}")

            return{ 
                "status": "success"
                "response": f"Generated response for: {prompt}"
            }

        except RuntimeError as e:

            logger.error(e)

            return {
                "status": "failed"
                "response" : None
            }