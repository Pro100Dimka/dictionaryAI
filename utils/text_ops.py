def replace_quotes(text: str) -> str:
    result = []
    open_quote = True
    for ch in text:
        if ch == '"':
            result.append('«' if open_quote else '»')
            open_quote = not open_quote
        else:
            result.append(ch)
    return ''.join(result)


def match_case(src: str, tgt: str) -> str:
    if not src or not tgt:
        return tgt
    if src[0].islower():
        return tgt[0].lower() + tgt[1:]
    return tgt
