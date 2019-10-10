len_indent = 99
indents = 'def many_indent():\n'

for i in range(len_indent):
    indents += '\t' * (i + 1) + 'if True:\n'

indents += '\t' * (len_indent + 1) + 'pass'

with open('indent.py', 'w') as f:
    f.write(indents)

from indent import many_indent