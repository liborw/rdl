from rddsl import Register


def register_by_name(regs:list[Register], name:str):
    for reg in regs:
        if name == reg.name:
            return reg
    return None


def insert_text(filepath, section, text, stag='{{{', etag='}}}'):
    """
    Insert a text into a section of a file.

        :param filepath: Path to the file to update.
        :param section: Section identifier
        :param text: text to insert
        :param stag: start tag
        :param etag: end tag
    """

    # read the file
    with open(filepath, 'r') as f:
        lines = f.readlines()

    # find section
    l0 = -1
    l1 = -1
    for i, line in enumerate(lines):
        if section in line:
            if stag in line:
                l0 = i
            if etag in line:
                l1 = i

    if l0 != -1 and l1 != -1:
        raise Exception(f'Section {section} not found')

    out = ''.join(lines[:(l0+1)] + ['\n', text, '\n'] + lines[(l1-1):])

    # write to the file
    with open(filepath, 'w') as f:
        f.writelines(out)

