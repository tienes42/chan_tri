from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.health import router as health_router

app = FastAPI(title='HỌC ĐỂ LÀM GÌ API', version='0.1.0')
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
app.include_router(health_router, prefix='/api')

@app.get('/')
def root():
    return {'name':'HỌC ĐỂ LÀM GÌ','status':'running','docs':'/docs'}
