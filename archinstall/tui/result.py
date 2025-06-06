from dataclasses import dataclass
from enum import Enum, auto
from typing import Any

from .menu_item import MenuItem


class ResultType(Enum):
	Selection = auto()
	Skip = auto()
	Reset = auto()


@dataclass
class Result:
	type_: ResultType
	_item: MenuItem | list[MenuItem] | str | None

	def has_item(self) -> bool:
		return self._item is not None

	def get_value(self) -> Any:
		return self.item().get_value()

	def get_values(self) -> list[Any]:
		return [i.get_value() for i in self.items()]

	def item(self) -> MenuItem:
		assert self._item is not None and isinstance(self._item, MenuItem)
		return self._item

	def items(self) -> list[MenuItem]:
		assert self._item is not None and isinstance(self._item, list)
		return self._item

	def text(self) -> str:
		assert self._item is not None and isinstance(self._item, str)
		return self._item
