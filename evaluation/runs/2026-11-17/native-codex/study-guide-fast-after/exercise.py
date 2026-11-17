def parse_numbers(text):
    return [int(item) for item in text.split(",")]


def summarize(values):
    raise NotImplementedError


def format_title(name):
    return f"Report: {name}"

