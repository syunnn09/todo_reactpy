from reactpy import component, html, hooks

from styles import center

@component
def Input(callback):
    value, set_value = hooks.use_state('')

    def on_click(e):
        if not value:
            return
        callback(value)

    return html.div(
        { 'style': center() },
        html.input(
            {
                'type': 'text',
                'placeholder': 'タスクの追加',
                'value': value,
                'on_change': lambda e: set_value(e['target']['value']),
                'onKeyDown': lambda e: print(e),
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
