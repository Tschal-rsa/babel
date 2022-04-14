import json
from utils.indexer import Indexer

class POS:
    """Part of Speech class
    """
    def __init__(self, idx: int, nam: str, abbr: str, info='', **kwargs) -> None:
        """Initialize.

        Args:
            idx (int): index of POS
            nam (str): name of POS
            abbr (str): abbreviation of POS
            info (str): long term definition. Defaults to ''.
        """
        self.idx, self.nam, self.abbr, self.info = idx, nam, abbr, info
    
    def pack(self) -> dict:
        """Pack POS into a dictionary.

        Returns:
            dict: output dict
        """
        return {
            'idx': self.idx,
            'nam': self.nam,
            'abbr': self.abbr,
            'info': self.info
        }

class Word:
    """Word class
    """
    def __init__(self, idx: int, con: str, nat: str, pos: int, ipa='', info='', **kwargs) -> None:
        """Initialize.

        Args:
            idx (int): index of word
            con (str): word in your conlang
            nat (str): word in your natlang (English, etc.)
            pos (int): word's part of speech (index)
            ipa (str, optional): pronunciation. Defaults to ''.
            info (str, optional): long form definition. Defaults to ''.
        """
        self.idx, self.con, self.nat, self.pos, self.ipa, self.info = idx, con, nat, pos, ipa, info
    
    def pack(self) -> dict:
        """Pack the word into a dictionary.

        Returns:
            dict: output dict
        """
        return {
            'idx': self.idx,
            'con': self.con,
            'nat': self.nat,
            'pos': self.pos,
            'ipa': self.ipa,
            'info': self.info
        }

# Unused
# def binary_search(seq, lo: int, hi: int, func) -> int:
#     """Binary search

#     Args:
#         seq: Sequence
#         lo (int): low
#         hi (int): high
#         func (function): func(item) == True when target < item
    
#     Returns:
#         int: arg max{ret <= target}
#     """
#     while (hi - lo > 0):
#         mi = (lo + hi) // 2
#         if func(seq[mi]):
#             hi = mi
#         else:
#             lo = mi + 1
#     return lo - 1

class Lexicon:
    """Lexicon class

    A Babel project should be like this:
        {
            "word": [
                {
                    "idx": 0,
                    "con": "alago",
                    "nat": "dawn",
                    "pos": 0,
                    "ipa": "",
                    "info": ""
                },
                {
                    ...
                }
            ],
            "word_indexer": [
                0,
                1,
                2
            ]
            "pos": [
                {
                    "idx": 0,
                    "nam": "noun",
                    "abbr": "n",
                    "info": ""
                },
                {
                    ...
                }
            ],
            "pos_indexer": [
                0,
                1,
                2
            ]
            ...
        }
    """
    def __init__(self, path='') -> None:
        """Initialize.

        Args:
            path (str, optional): path of Babel project. Defaults to ''.
        """
        if path:
            data = json.load(open(path, 'r', encoding='utf-8'))
            self.word_list = [Word(**item) for item in data['word']]
            self.word_indexer = Indexer(len(self.word_list), data['word_indexer'])
            self.pos_list = [POS(**item) for item in data['pos']]
            self.pos_indexer = Indexer(len(self.pos_list), data['pos_indexer'])
        else:
            self.word_list, self.pos_list = list(), list()
            self.word_indexer, self.pos_indexer = Indexer(), Indexer()
    
    def pack(self) -> dict:
        """Pack lexicon into a dictionary

        Returns:
            dict: output dict
        """
        return {
            'word': [item.pack() for item in self.word_list],
            'word_indexer': self.word_indexer.indices,
            'pos': [item.pack() for item in self.pos_list],
            'pos_indexer': self.pos_indexer.indices
        }
    
    def packWordItem(self, rank: int) -> dict:
        """Pack a word for WordItem

        Args:
            rank (int): word's rank in wordlist, can be -1

        Returns:
            dict: WordItem initializer
        """
        word = self.word_list[rank]
        return {
            'con': word.con,
            'rank': rank if rank >= 0 else rank + len(self.word_list),
            'idx': word.idx
        }
    
    def wordlist(self) -> list:
        """Pack a wordlist

        Returns:
            list[dict]: wordlist
        """
        return [self.packWordItem(i) for i in range(len(self.word_list))]
        # return [word.con for word in self.word_list]
    
    def POSlist(self) -> list:
        return [dict(nam=self.pos_list[i].nam, rank=i) for i in range(len(self.pos_list))]
    
    def word_at(self, rank: int, simple=False) -> dict:
        """Pack a word for MainWindow to render

        Args:
            rank (int): word's rank in wordlist
            simple (bool): ?

        Returns:
            dict: output dict
        """
        word = self.word_list[rank]
        return {
            'con': word.con,
            'nat': word.nat,
            'pos': self.find_pos(word.pos, abbr=simple),
            'ipa': word.ipa if simple else f'/{word.ipa}/',
            'info': word.info
        }
    
    def POS_at(self, rank: int) -> dict:
        POS = self.pos_list[rank]
        return {
            'nam': POS.nam,
            'abbr': POS.abbr,
            'info': POS.info
        }
    
    def find_pos_abbr(self, abbr: str) -> int:
        """Find part of speech by its abbreviation

        Args:
            abbr (str): Abbreviation of POS

        Returns:
            int: Index of POS, -1 when failed
        """
        for pos in self.pos_list:
            if abbr == pos.abbr:
                return pos.idx
        return -1
    
    def find_pos(self, idx: int, abbr=False) -> str:
        """Find part of speech by its index

        Args:
            idx (int): index of POS
            abbr (bool): Defaults to False.

        Returns:
            str: either name or abbreviation of POS
        """
        for pos in self.pos_list:
            if idx == pos.idx:
                return pos.abbr if abbr else pos.nam
        return 'undefined'
    
    def add_word(self, con: str, nat: str, pos: str, ipa: str, info: str) -> dict:
        """Add a word.

        Args:
            con (str): conlang word
            nat (str): natlang word
            pos (str): word's part of speech
            ipa (str): pronunciation of the word
            info (str): definition of the word

        Returns:
            dict: contains information of the word, None if failed
        """
        idx = self.find_pos_abbr(pos)
        # if idx < 0:
        #     return None
        self.word_list.append(Word(self.word_indexer.allocate(), con, nat, idx, ipa, info))
        return self.packWordItem(-1)
    
    def modify_word(self, rank: int, con: str, nat: str, pos: str, ipa: str, info: str) -> dict:
        pos_idx = self.find_pos_abbr(pos)
        word_idx = self.word_list[rank].idx
        self.word_list[rank] = Word(word_idx, con, nat, pos_idx, ipa, info)
        return self.packWordItem(rank)
    
    def remove_word(self, rank: int) -> None:
        self.word_indexer.free(self.word_list[rank].idx)
        self.word_list.pop(rank)
    
    def add_POS(self, nam: str, abbr: str, info: str) -> dict:
        self.pos_list.append(POS(self.pos_indexer.allocate(), nam, abbr, info))
        return dict(nam=nam, rank=len(self.pos_list)-1)
    
    def save(self, path: str) -> None:
        """Save current lexicon.

        Args:
            path (str): Save path
        """
        json.dump(self.pack(), open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=4)