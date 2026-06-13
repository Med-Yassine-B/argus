from argus.clients import exchangerate_client as ex_client
from argus.domain.validation import normalize_input_string, is_valid_curr_code


# This function has to be moved to dmoain
def check_currency(question: str) -> str | None:
    resp = normalize_input_string(question)

    if is_valid_curr_code(resp):
        return resp

    return None


def get_conv_rate(resp1: str, resp2: str) -> float | None:
    data = ex_client.get_rates(resp1, resp2)

    if data is None:
        return None

    return float(data["conversion_rate"])


def convert(amount: float, resp1: str, resp2: str) -> float | None:
    data = get_conv_rate(resp1, resp2)
    if data is not None:
        return amount * data
    else:
        return None
