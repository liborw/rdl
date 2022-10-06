import re

section_start = re.compile(r"^.*GENERATED_START: (?P<sname>\S*).*$")
section_end = re.compile(r"^.*GENERATED_END.*$")

class Output(object):

    def __init__(self,
                 filepath:str,
                 section_start:re.Pattern = section_start,
                 section_end:re.Pattern = section_end,
                 ):

        self.filepath : str = filepath
        self._sections : dict[str, tuple[int, int]] = dict()
        self._lines : list[str] = []
        self._section_start = section_start
        self._section_end = section_end

        # read file
        with open(filepath, 'r') as f:
            self._lines = f.readlines()

        self._scan_sections()

    def _scan_sections(self):
        # find sections
        section : tuple[str, int]|None = None
        for i, line in enumerate(self._lines):
            if section is None:
                # no open section, looging for start
                match = self._section_start.match(line)
                if match:
                    section = (match['sname'], i)
            else:
                # looking for end
                if self._section_end.match(line):
                    self._sections[section[0]] = (section[1], i)
                    section = None

        # check for open section
        if section is not None:
            raise Exception(f"Section {section[0]} is not closed!")

    def list_sections(self) -> list[str]:
        """List section in a file"""

        return list(self._sections.keys())

    def replace_section(self, name:str, text:str):
        """Replace section with given text"""

        section = self._sections[name]
        lines = text.split('\n')

        # replace line inside the section
        self._lines = self._lines[:section[0]+1] + lines + self._lines[section[1]:]

        # rescan sections as the number of lines might change
        self._scan_sections()

    def write(self, filepath:str|None = None):
        "Write output to a file"""

        if filepath is None:
            filepath = self.filepath

        with open(self.filepath, 'w') as f:
            f.writelines(self._lines)

