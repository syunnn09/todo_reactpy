from reactpy import component, html
from typing import Callable

import exhtml


@component
def Checkbox(is_checked: bool, callback: Callable, margin: str = '0', width: str = '20px', height: str = '20px', default_color: str = '#fff', default_fill_color: str = '#000'):
    if is_checked:
        default_color, default_fill_color  = default_fill_color, default_color

    def create_check_mark():
        if is_checked:
            return html.svg(
                {
                    'xmlns': 'http://www.w3.org/2000/svg',
                    'width': width,
                    'height': height,
                    'fill': default_fill_color,
                    'viewBox': '0 0 16 16'
                },
                exhtml.path(
                    {
                        'd': 'M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z'
                    }
                )
            )
        else:
            return html._()

    return html.div(
        {
            'on_click': callback,
            'style': f'''
                margin: {margin};
                width: {width};
                height: {height};
                border: 1px solid #000;
                border-radius: 3px;
                background-color: {default_color};
                transition: opacity 2s ease-in-out;
                cursor: pointer;
            '''
        },
        create_check_mark()
    )
