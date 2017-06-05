def get_msg_with_punctuations(old, new):
    new_org_text = new
    for i in range(len(old)):
        if not str.isalpha(old[i]):
            new_org_text = new_org_text[0:i] + old[i] + new_org_text[i:]
    for i in range(len(old)):
        if str.isupper(old[i]):
            new_org_text = new_org_text[0:i] + str.upper(new_org_text[i]) + new_org_text[i + 1:]
    return new_org_text


def get_alphabetic_msg(text):
    normal = ''
    for ch in text:
        if str.isalpha(ch):
            normal += ch
    return normal