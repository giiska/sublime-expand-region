import re

try:
  import utils
except:
  from . import utils

# If there is a space in the quotes string, expand to space first
def expand_to_space_in_quotes(result, string, start, end):
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
    print(space_start, space_end)

    if(end == space_start and start == result['start']):
      print('space end and quote start')
      space_break = True
      break
    if(start == space_end and end == result['end']):
      print('space start and quote end')
      space_break = True
      break
    # todo: maybe this can be simplified
    if((start == space_end and end == space_start_result) or (start == space_end_result and end == space_start_result) or (start == space_end_result and end == space_start)):
      print('space start and space end')
      space_break = True
      break
    if(start == result['start'] and end == result['end']):
      print('quote start and quote end')
      space_break = True
      break

    # set space_start_result
    if(space_end <= start and space_end > space_start_result):
      space_start_result = space_end

    # set space_end_result
    if(space_start > start and space_start < space_end_result and space_start >= end):
      space_end_result = space_start

  # should not breaked
  # should not equal selection start, end
  # not the same result with quotes
  if(space_break == None and not (space_start_result == start and space_end_result == end ) and (space_start_result != result['start'] or space_end_result != result['end'])):
    return utils.create_return_obj(space_start_result, space_end_result, string, "quotes_and_space")
  else:
    return False