def camel_case(text):
    text = text.replace("-", " ").replace("_", " ") # MUST DO: text = text.replace(old, new)
    words = text.split()
    return "".join(w.capitalize() if w!= words[0] else w for w in words)

# or

def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s