import pandas as pd
from fastapi import FastAPI
from database import engine
from models import ModelOutputResponse


app = FastAPI()


@app.get("/")
def read_root():
    return {"Status": "Ok"}


@app.get('/report', description='Return Model predictions', response_model=ModelOutputResponse)
def get_model_predictions():
    df = pd.read_sql_query('select geo_h3_10, predictions, model_type from postamat.platform_model limit 1000',
                           con=engine)
    return df.to_json()
