from typing import (List, Tuple)

DOCUMENT_TYPES: List[Tuple[str, str]] = [
    ('Презентация', 'Презентация'),
    ('Презентация без контактов', 'Презентация без контактов'),
    ('Цены', 'Цены'),
    ('Документы', 'Документы'),
    ('Прочее', 'Прочее'),
]


VIEW_FROM_WINDOWS: List[Tuple[str, str]] = [
    ('На улицу', 'На улицу'),
    ('Во двор', 'Во двор')
]

NAME_TYPE_ROOMS: List[Tuple[str, str]] = [
    ('студия', 'студия'),
    ('с 1-ой спальней', 'с 1-ой спальней'),
    ('с 2-мя спальнями', 'с 2-мя спальнями'),
    ('с 3-мя спальнями', 'с 3-мя спальнями'),
    ('с 4-ой спальней', 'с 4-ой спальней')
]

__all__ = (
    'DOCUMENT_TYPES',
    'VIEW_FROM_WINDOWS',
    'NAME_TYPE_ROOMS',
)
