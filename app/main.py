from fastapi import FastAPI
from code import predict_email
import pickle
app = FastAPI()
m = pickle.load(open('C:\projectAi\model\cls_emailspam_0.1.pkl', 'rb'))
cv = pickle.load(open('C:\projectAi\model\cv1_feature.pkl', 'rb'))
print(predict_email(m,cv , "hola esta es una clase de IA"))
@app.get("/")
def root():
    return {"message": "This is my api"}
@app.get("/api/predict{item_str}")
def read_str(item_str):
    email = predict_email(m, cv, item_str)
    return {"EmailSpam": email}