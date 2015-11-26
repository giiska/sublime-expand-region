import re
try:
  import expand_to_word
  import expand_to_quotes
  import expand_to_css_selector
  import expand_to_xml_node
  import utils
except:
  from . import expand_to_word
  from . import expand_to_quotes
  from . import expand_to_css_selector
  from . import expand_to_xml_node
  from . import utils

def expand(string, start, end):
  expand_stack = []

  expand_stack.append("word")

  result = expand_to_word.expand_to_word(string, start, end)
  if result:
    result["expand_stack"] = expand_stack
    return result

  expand_stack.append("expand_to_css_selector")

  if utils.selection_contain_linebreaks(string, start, end) == False:
    result = expand_to_css_selector.expand_to_css_selector(string, start, end)

    if result:
      result["expand_stack"] = expand_stack
      return result