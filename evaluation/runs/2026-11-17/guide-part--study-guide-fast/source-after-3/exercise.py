def parse_numbers(text):
    return [int(item) for item in text.split(",")]


def summarize(values):
    return {"count": len(values), "sum": sum(values)}


def format_title(name):
    return f"Report: {name}"

