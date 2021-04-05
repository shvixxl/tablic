"""Command constructions"""

import operator

from app.helpers.chat import commands


CONSTRUCTIONS = [
    (r'^(.+?)\s+\?\s+(.+?)\s+:\s+(.+)$', commands.ternary),
    (r'^(.+?)\s+if\s+(.+?)\s+else\s+(.+)$', commands.readable_ternary),

    (r'^(.+?)\s+&\s+(.+)$', operator.and_),
    (r'^(.+?)\s+&&\s+(.+)$', operator.and_),
    (r'^(.+?)\s+and\s+(.+)$', operator.and_),
    (r'^(.+?)\s+\|\s+(.+)$', operator.or_),
    (r'^(.+?)\s+\|\|\s+(.+)$', operator.or_),
    (r'^(.+?)\s+or\s+(.+)$', operator.or_),

    (r'^(.+?)\s+>\s+(.+)$', operator.gt),
    (r'^(.+?)\s+>=\s+(.+)$', operator.ge),
    (r'^(.+?)\s+<\s+(.+)$', operator.lt),
    (r'^(.+?)\s+<=\s+(.+)$', operator.le),
    (r'^(.+?)\s+=\s+(.+)$', operator.eq),
    (r'^(.+?)\s+==\s+(.+)$', operator.eq),
    (r'^(.+?)\s+!=\s+(.+)$', operator.floordiv),

    (r'^(.+?)\s+\+\s+(.+)$', operator.add),
    (r'^(.+?)\s+-\s+(.+)$', operator.sub),
    (r'^(.+?)\s+\*\*\s+(.+)$', operator.pow),
    (r'^(.+?)\s+\*\s+(.+)$', operator.mul),
    (r'^(.+?)\s+//\s+(.+)$', operator.floordiv),
    (r'^(.+?)\s+/\s+(.+)$', operator.truediv),
    (r'^(.+?)\s+%\s+(.+)$', operator.mod),

    (r'^-\s*(.+)$', operator.neg),

    (r'^random\s+(.+?)\s+(.+)$', commands.random),
    (r'^rand\s+(.+?)\s+(.+)$', commands.random),
    (r'^r\s+(.+?)\s+(.+)$', commands.random),

    (r'^roll\s+(.+?)\s+(.+)$', commands.roll_n),
    (r'^(.+?)d(.+)$', commands.roll_n),

    (r'^roll\s+(.+)$', commands.roll),
    (r'^r\s*(.+)$', commands.roll),
    (r'^d(.+)$', commands.roll),

    (r'coin', commands.coin),
    (r'c', commands.coin),
]
