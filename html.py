import re
try:
  import expand_to_word
  import expand_to_quotes
  import expand_to_space_in_quotes
  import expand_to_xml_node
  import utils
except:
  from . import expand_to_word
  from . import expand_to_quotes
  from . import expand_to_space_in_quotes
  from . import expand_to_xml_node
  from . import utils

def expand(string, start, end):
  expand_stack = []

  expand_stack.append("word")

  result = expand_to_word.expand_to_word(string, start, end)
  if result:
    result["expand_stack"] = expand_stack
    return result

  expand_stack.append("quotes")

  result = expand_to_quotes.expand_to_quotes(string, start, end)
  if result:

    # Check if there is space in quotes
    space_in_quotes_result = expand_to_space_in_quotes.expand_to_space_in_quotes(result, string, start, end)
    if space_in_quotes_result:
      expand_stack.append("quotes_and_space")
      return space_in_quotes_result

    result["expand_stack"] = expand_stack
    return result

  expand_stack.append("xml_node")

  result = expand_to_xml_node.expand_to_xml_node(string, start, end)
  if result:
    result["expand_stack"] = expand_stack
    return result