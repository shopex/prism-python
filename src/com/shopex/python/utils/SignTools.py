# __author__ = 'daixinyu'
# coding=utf8


def mix_header_params(headers):
    query = ""
    for key, value in headers.iteritems():
        if (key == "Authorization" or key.startswith("X-Api-")):
            query += key + "=" + value + "&"
    if len(query) > 0:
        return query[0:len(query) - 1]
    return ""


def mix_request_params(params):
    if params == "":
        return ""
    query = ""
    for key, value in params.iteritems():
        if (key != "" and "sign" != (key)):
            query += key + "=" + str(value) + "&"
    if len(query) > 0:
        return query[0:len(query) - 1]
    return ""

