def predict_rank(marks):
    if marks >= 90:
        return "1 - 5000"
    elif marks >= 80:
        return "5000 - 15000"
    elif marks >= 70:
        return "15000 - 30000"
    else:
        return "30000+"