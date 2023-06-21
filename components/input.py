from reactpy import component, html

from styles import center

@component
def Input():
    return html.div(
        { 'style': center() },
        html.input(
            {
                'type': 'text',
                'placeholder': 'タスクの追加',
                'style': '''
                    width: 300px;
                    height: 20px;
                    border: 1px solid #000;
                    border-radius: 3px;
                    outline: none;
                '''
            }
        )
    )
