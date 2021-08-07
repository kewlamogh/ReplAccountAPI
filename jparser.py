def jparse(json):
  j = str(json)
  j = j.replace("null", "None")
  j = j.replace("false", "False")
  j = j.replace("true", "True")
  j = j.replace("\n", "")
  return eval(j)