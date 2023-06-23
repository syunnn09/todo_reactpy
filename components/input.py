from reactpy import component, html, hooks

from styles import center

@component
def Input(callback, value: str = ''):
    value, set_value = hooks.use_state(value)

    def on_click(e):
        if not value:
            return
        callback(value)
        set_value('')

    def on_key_down(e):
        if e['code'] == 'Enter':
            on_click(e)

    return html.div(
        { 'style': center() },
        html.input(
            {
                'type': 'text',
                'placeholder': 'タスクの追加',
                'value': value,
                'on_change': lambda e: set_value(e['target']['value']),
                'onKeyDown': on_key_down,
                'style': '''
                    width: 300px;
                    height: 20px;
                    border: 1px solid #000;
                    border-radius: 3px;
                    outline: none;
                '''
            }
        ),
        html.input(
            {
                'on_click': on_click,
                'type': 'submit',
                'value': '追加'
            }
        )
    )
