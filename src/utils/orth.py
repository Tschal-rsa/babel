import os
import re

class Orth:
    """Orthography helper.

    Usage:
        orth('se\\\~norita') -> 'señorita';
        orth('drei{ss}ig') -> 'dreißig';
        For more rules see ./orth/command.txt
    More information: https://tex.stackexchange.com/tags/accents/info
    """
    def __init__(self) -> None:
        """Initialize via files in ./orth
        """
        path = os.path.dirname(__file__)
        # self.cmd -> cmd
        self.lib, self.cmd, self.combine = dict(), dict(), dict()
        with open(os.path.join(path, 'orth/command.txt'), 'r', encoding='utf-8') as f:
            data = f.readlines()
            for item in data:
                tup = item.split()
                self.cmd[tup[0]] = tup[1]
        for key, value in self.cmd.items():
            self.lib[key] = dict()
            with open(os.path.join(path, f'orth/{value}.txt'), 'r', encoding='utf-8') as f:
                data = f.readlines()
                for item in data:
                    tup = item.split()
                    self.lib[key][tup[0]] = tup[1]
        with open(os.path.join(path, 'orth/combination.txt'), 'r', encoding='utf-8') as f:
            data = f.readlines()
            for item in data:
                tup = item.split()
                self.combine[tup[0]] = tup[1]
    
    def _repl(self, matched: re.Match) -> str:
        pat = matched.group(1)
        return self.combine[pat] if pat in self.combine.keys() else pat
    
    def tran(self, raw: str) -> str:
        """Transform the raw string.

        Args:
            raw (str): raw string.

        Returns:
            str: output string.
        """
        # handle {}
        raw = re.sub(r'{(\w+)}', self._repl, raw)
        # handle \
        raw_list = raw.split('\\')
        output = [raw_list[0]]
        for s in raw_list[1:]:
            if len(s) > 1:
                try:
                    output.append(self.lib[s[0]][s[1]] + s[2:])
                except KeyError:
                    output.append(s[1:])
        return ''.join(output)
    
    def __call__(self, *args, **kwds):
        return self.tran(*args, **kwds)
    
    def __str__(self) -> str:
        """Debug

        Returns:
            str: [description]
        """
        return str(self.lib)

if __name__ == '__main__':
    orth = Orth()
    print(orth)
    while True:
        raw = input('> ')
        print(orth(raw))