
from utilities.models import get_dynamic_model


def add_comment(
        user_id: int,
        type: str,
        type_id: int,
        comment: str
):
    model = get_dynamic_model(type, type_id)



