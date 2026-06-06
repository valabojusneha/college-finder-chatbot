from ai.nlp_engine import get_intent

def get_response(user_input, df):
    intent = get_intent(user_input)

    if "cse" in user_input.lower():
        return df[df["branch"] == "CSE"].to_dict(orient="records")

    if "ece" in user_input.lower():
        return df[df["branch"] == "ECE"].to_dict(orient="records")

    return "I can help with college search by rank or branch."