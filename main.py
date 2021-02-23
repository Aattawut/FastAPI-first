from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def helloworld():
    return 'Hello World FastAPI'


@app.get("/bmi")
def bmi(weight: float, height: float):
    '''
    คำนวณค่าดัชนีมวลกาย (bmi) จาก น้ำหนัก(kg)/ส่วนสูง(m)**2"
    '''
    bmi = weight/(height/100)**2
    return str(bmi)
