def parse_numbers(text):
    return [int(part) for part in text.split(",")]


def summarize(values):
    return {"count": len(values), "sum": sum(values)}


def format_title(name):
    return f"Report: {name}"

