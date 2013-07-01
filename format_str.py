#method to remove accents of a string and upping its cases, it also keep separator char such as spaces or dots
prog = re.compile('[ _\-:]+')
def to_upper_unaccent(val):
    uval = val.decode('utf-8')
    separator = prog.search(uval)
    items = [uval]
    ret = []
    if separator:
        items = prog.split(uval)
    for item in items:
        ret.append(''.join([x for x in unicodedata.normalize('NFKD',item) if unicodedata.category(x)[0] == 'L']))
    ret = separator.group(0).join(ret)
    return ret.upper()