class Indexer:
    """Allocate & arrange indices.
    """
    def __init__(self, len:int=0, indices:list=None) -> None:
        """Initialize.

        Args:
            len (int, optional): number of items. Defaults to 0.
            indices (list, optional): a list of unused indices. Defaults to None.
        """
        if indices is None:
            indices = list()
        self.len, self.indices = len, indices

    def allocate(self) -> int:
        """Allocate an index.

        Returns:
            int: an index.
        """
        self.len += 1
        if len(self.indices) == 0:
            return self.len - 1
        else:
            return self.indices.pop()
    
    def free(self, idx: int) -> None:
        """Delete an index.

        Args:
            idx (int): an index to be deleted.
        """
        self.len -= 1
        self.indices.append(idx)
        self.indices.sort(reverse=True)
    
    def __str__(self) -> str:
        """Debug

        Returns:
            str: [description]
        """
        return f'{self.len} {self.indices}'