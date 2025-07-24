# FastAPI main app
from fastapi import FastAPI
app = FastAPI()
@app.get('/')
def root(): return {'message': 'Hello from CryptoQuiver API'}