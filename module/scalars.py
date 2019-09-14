
from tartiflette import Scalar
from bson import ObjectId
from typing import Union
from tartiflette.language.ast.base import Node
from tartiflette.constants import UNDEFINED_VALUE


JsonScalar = Scalar("Json")
@JsonScalar
class JsonClass:
    @staticmethod
    def coerce_input(val):
        return val

    @staticmethod
    def coerce_output(val):
        return val

    def parse_literal(self, ast: "Node") -> Union[str, "UNDEFINED_VALUE"]:
        return self.coerce_input(ast.value)
