import re
import sys
import sublime

try:
  import utils
except:
  from . import utils

# If there is a space in the quotes string, expand to space first
def expand_to_css_selector(string, start, end):

  view = sublime.Window.active_view(sublime.active_window())
  line_start = view.line(view.sel()[0]).begin()
  cur_line = view.substr(view.line(view.sel()[0]))
  # TODO: Optimize search first none space pos
  # print('aaaaa', cur_line)
  # print('aaaaa',len(cur_line))
  has_seletor = re.compile(r'\s*[\.\#]{1}([^\s].*[^\s])*\s*[\{|,]')
  matched = has_seletor.match(cur_line)
  # print('bbbbb', matched)
  if matched:
    print('cccccc', matched.groups(1))
    # Retrieve the groups(1)'s start and end.
    newStartIndex = matched.start(1) + line_start
    newEndIndex = matched.end(1) + line_start

    # if is not equal current selection
    if (not (start == newStartIndex and end == newEndIndex)):
      print(newStartIndex, newEndIndex)
      return utils.create_return_obj(newStartIndex, newEndIndex, string, "css_selector")