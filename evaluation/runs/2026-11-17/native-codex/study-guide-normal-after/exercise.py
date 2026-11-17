def parse_numbers(text):
    return [int(part) for part in text.split(",")]


def summarize(values):
    raise NotImplementedError


def format_title(name):
    return f"Report: {name}"

