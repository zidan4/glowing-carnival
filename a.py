def get_http_headers(http_payload):
  try:
    # split the headers off if it is HTTP traffic
    headers_raw = http_payload[:http_payload.index("\r\n\r\n")+2]
    # break out the headers
    headers = dict(re.findall(r"(?P<name>.*?): (?P<value>.*?)\r\n", ¬
    headers_raw))
  except:
    return None
  if "Content-Type" not in headers:
    return None
  return headers
