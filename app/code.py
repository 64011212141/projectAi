import re
import pickle
email = {1:"spam", 0:"non-spam"}
def predict_email(model,cv,text):
    text_1 = re.sub(r'[!@#$%^&*(),:;0-9,\n]',' ',text)
    text_2 = text_1.lower()
    x = cv.transform([text_2])
    lang = model.predict(x)
    return email[lang[0]]

