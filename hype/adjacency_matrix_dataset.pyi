
# Typing introduced in Python version 3.9
# Check https://docs.python.org/3/library/typing.html

# Here used to create a tuple


import torch
from typing import Tuple

class AdjacencyDataset:
    def iter(self): ...

    def __iter__(self): ...

    def avg_queue_size(self) -> float: ...  # This is a 'type alias' . Specifies the return type is float [ refer https://docs.python.org/3/library/typing.html and https://www.python.org/dev/peps/pep-0484/ ]

    def __len__(self) -> int: ...

    def queue_misses(self) -> int: ...

    def next(self) -> Tuple[torch.Tensor, torch.Tensor]: ...

    def __next__(self) -> Tuple[torch.Tensor, torch.Tensor]: ...
