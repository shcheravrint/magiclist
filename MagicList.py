import inspect
from dataclasses import dataclass


class MagicList(list):
    def __init__(self, cls_type):
        if not inspect.isclass(cls_type):
            raise NotImplementedError('Need to provide type')
        super().__init__()
        self._cls_type = cls_type
        #self._list = list()

    def __getitem__(self, ii):
        if ii < super().__len__():
            return super().__getitem__(ii)
        elif ii == super().__len__():
            new_el = self._cls_type()
            super().append(new_el)
            return super().__getitem__(ii)
        else:
            raise IndexError('List index out of range')

    def __setitem__(self, ii, val):
        if ii < super().__len__():
            super().__setitem__(ii, val)
        elif ii == super().__len__():
            new_el = self._cls_type()
            super().append(new_el)
        else:
            raise IndexError('List index out of range')

    # def __len__(self):
    #     """List length"""
    #     return len(self._list)

    # def __iter__(self):
    #     for elem in self._list:
    #         yield elem

    # def __repr__(self):
    #     return f"{type(self).__name__}({super().__repr__()})"


@dataclass
class Person:
    age: int = 1

# new_element_class = globals()[self._cls_type]
#             new_el = new_element_class()
#             self._list.append(new_el)
#             return new_el