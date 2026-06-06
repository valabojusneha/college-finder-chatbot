def get_intent(text):
    text = text.lower()

    if "college" in text:
        return "college_search"
    if "rank" in text:
        return "rank_search"
    if "branch" in text:
        return "branch_search"

    return "unknown"