from .type import Type


class Reference(Type):

    accept_types = type
    type = "object"

    def __init__(self, reference: object):
        super().__init__()
        self.reference = reference

        try:
            self.extra_validators.append(reference.schema)
        except AttributeError:
            raise ValueError("Passed reference is not valid reference object")

    def to_doc(self) -> dict:
        doc = self._get_base_doc()
        # todo: add reference mapping here
        return doc
