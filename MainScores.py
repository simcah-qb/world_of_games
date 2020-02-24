import Score


def score_server():
    html = None
    try:
        score = Score.read_score_from_file()
        html = f"<html><head><title>Scores Game</title></head><body><h1>The score is " \
            f"<div id=\"score\">{score}</div></h1></body></html>"
    except BaseException as e:
        html = f"<html><head><title>Scores Game</title></head><body><body><h1>" \
            f"<div id=\"score\" style=\"color:red\">{e}</div></h1></body></html>"
    return html