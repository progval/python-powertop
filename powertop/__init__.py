import csv
import tempfile
import subprocess

__all__ = ['Powertop', 'Section']

class Section:
    def __init__(self, header, rows):
        self.header = header
        self._rows = rows

    def rows(self):
        return [dict(zip(self.header, row)) for row in self._rows]
    
    def __repr__(self):
        return 'Section(header={!r}, rows={!r})'.format(self.header, self._rows)

class Powertop:
    def __init__(self, *, command=('/usr/sbin/powertop', '--quiet'), env=None):
        self.command = tuple(command)
        if env is None:
            env = {}
        env.setdefault('LANG', 'C') # https://lists.01.org/pipermail/powertop/2016-April/001876.html
        self.env = env

    def get_measures(self, *, time, iterations=1):
        output = self._run(time=time, iterations=iterations)
        return self._parse_output(output)

    def _run(self, *, time, iterations):
        return open('powertop2.csv').readlines()
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.csv') as fd:
            arguments = (
                    '--csv={}'.format(fd.name),
                    '--time={}'.format(time),
                    '--iteration={}'.format(iterations),
                    )
            subprocess.check_call(self.command + arguments, env=self.env)
            return fd.readlines()

    def _parse_output(self, lines):
        (delimiter, version) = self._detect_characteristics(lines)
        sections = self._split_sections(lines)
        d = dict(self._parse_section(section, delimiter=delimiter)
                for section in sections)
        if None in d:
            del d[None]
        return d

    def _detect_characteristics(self, lines):
        prefix = 'PowerTOP Version'
        for line in lines:
            if line.startswith(prefix):
                delimiter = line[len(prefix)]
                remainder = line[len(prefix)+1:]
                version = remainder.split(' ', 1)[0]
                assert version.startswith('v')
                return (delimiter, version)
        raise ValueError('PowerTOP version/delimiter not found (too recent/old?).')

    def _split_sections(self, lines):
        current_section = []
        sections = [current_section]
        for line in lines:
            line = line.strip()
            if set(line) == {'_'}: # all characters are _
                if current_section:
                    current_section = []
                    sections.append(current_section)
            elif line == '':
                continue
            else:
                current_section.append(line)
        return sections

    def _parse_section(self, lines, delimiter):
        name = lines[0].strip(' *')

        data = csv.reader(lines[1:], delimiter=delimiter)
        try:
            header = next(data)
        except StopIteration:
            return (None, None)
        rows = list(data)
        return (name, Section(header, rows))
