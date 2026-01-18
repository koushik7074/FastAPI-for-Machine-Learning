from fastapi import FastAPI
import logging

app = FastAPI()

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] (line %(lineno)d) - %(levelname)s - %(message)s",
    datefmt="%m-%d-%Y %H:%M:%S"
)

@app.get('/debug')
def debug_route():
    logging.info('debug endpoint hit!!!')
    return {'message': 'check logs!'}