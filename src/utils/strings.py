import json
from typing import Any
from typing import List


class Strings:

    @staticmethod
    def string_list(elements_list: List[Any], separator: str = ",") -> str:
        if elements_list is None:
            return "None"
        return separator.join(str(i) for i in elements_list)

    @staticmethod
    def _default_serialize_json(o):
        """
        Use like this: logging.debug(f"print this object: {json.dumps(myobject, indent=4, sort_keys=True, default=default_serialize_func)}")
        """
        if hasattr(o, '__dict__'):
            return o.__dict__
        return f"<could not serialize {o.__class__}>"

    @staticmethod
    def object_to_json(o: Any) -> str:
        return json.dumps(o, indent=4, sort_keys=True, default=Strings._default_serialize_json)
