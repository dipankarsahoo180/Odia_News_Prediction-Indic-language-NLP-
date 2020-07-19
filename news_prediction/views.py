import joblib
from django.shortcuts import render, redirect

model = joblib.load("news_prediction/odia_nlp_model_final.pkl")


# Create your views here.
def index(request):
    # global result1
    if request.method == "POST":
        data = request.POST.get('odia_text')
        result1 = "The model predicts this text \n      "+data+" \n      as "
        result2 = str(list(model.predict([data])))[2:-2] + " news"

    else:
        result1 = "Enter text to predict (Only for Odia language) "
        result2= ''
    return render(request, 'index.html', {'result1': result1,"result2":result2})
