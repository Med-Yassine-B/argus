from fx_converter_lab.clients import exchangerate_client as ex_client
from fx_converter_lab.domain.convert_valid import normalize_input_string,is_valid_curr_code

def check_currency(question):
    resp = normalize_input_string(question)

    if is_valid_curr_code(resp):
        return resp
    
    return None

def get_conv_rate(resp1,resp2):
    data = ex_client.get_rates(resp1, resp2)
        
    if data is None:
        return None
        
    return {
        "rate": data["conversion_rate"],
        "from": resp1,
        "to": resp2
    }

def convert(amount,resp1,resp2):
    data = get_conv_rate(resp1,resp2)
    if data is not None:
        return amount * data["rate"], data["from"], data["to"]
    else:
        return None