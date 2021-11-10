from fastapi import FastAPI, Request
import sys
sys.path.insert(1, 'json_gen_docker/utils')
from utils.dummy import dummy_json,dummy_sql

app = FastAPI()


@app.get('/')
async def index(request: Request):
    return {'data': 'hello!'}


@app.get('/json')
async def json_gen(request: Request):
    json_string = request.headers.get('sql_string', None)
    if json_string == None:
        return {'data': 'invalid string'}
    json_dict = dummy_json(json_string)
    return {'data': json_dict}


@app.get('/sql')
async def sql_gen(request: Request):
    query_string = request.headers.get('sql_string', None)
    if query_string == None:
        return {'data': 'invalid string'}
    sql = dummy_sql(query_string)
    return {'data': sql}
