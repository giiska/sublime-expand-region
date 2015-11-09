import re
try:
  import expand_to_word
  import expand_to_quotes
  import expand_to_xml_node
  import utils
except:
  from . import expand_to_word
  from . import expand_to_quotes
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
  # print result
  if result:
    # If there is a space in the quotes string
    # TODO: should return when current selection contains a space
    quotes_string = result['string']
    m = re.compile(r'\s')
    res = m.finditer(quotes_string)
    space_start_result = result['start']
    space_end_result = result['end']
    space_break = None
    for matched_space in res:
      space_start = matched_space.start() + result['start']
      space_end = matched_space.end() + result['start']

      print '__',space_start, space_end

      if(end == space_start and start == result['start']):
        print 'space end and quote start'
        space_break = True
        break
      if(start == space_end and end == result['end']):
        print 'space start and quote end'
        space_break = True
        break
      # todo: maybe this can be simplified
      if((start == space_end and end == space_start_result) or (start == space_end_result and end == space_start_result) or (start == space_end_result and end == space_start)):
        print 'space start and space end'
        space_break = True
        break
      if(start == result['start'] and end == result['end']):
        print 'quote start and quote end'
        space_break = True
        break

      # set space_start_result
      if(space_end <= start and space_end > space_start_result):
        space_start_result = space_end

      # set space_end_result
      if(space_start > start and space_start < space_end_result and space_start >= end):
        space_end_result = space_start

    print '****', space_start_result, space_end_result
    # should not breaked
    # should not equal selection start, end
    # not the same result with quotes
    if(space_break == None and not (space_start_result == start and space_end_result == end ) and (space_start_result != result['start'] or space_end_result != result['end'])):
      expand_stack.append("quotes_and_space")
      return utils.create_return_obj(space_start_result, space_end_result, string, "quotes_and_space")

    result["expand_stack"] = expand_stack
    return result

  expand_stack.append("xml_node")

  result = expand_to_xml_node.expand_to_xml_node(string, start, end)
  if result:
    result["expand_stack"] = expand_stack
    return result