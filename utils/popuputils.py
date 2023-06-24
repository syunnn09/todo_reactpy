from reactpy import component, html

from styles import center

@component
def Button(word: str, callback, color: str = '#000', background_color: str = '#fff'):
    return html.button(
        {
            'on_click': callback,
            'style': f'''
                min-width: 100px;
                min-height: 32px;
                padding: 5px 1rem;
                border: 1px solid #000;
                color: {color};
                background-color: {background_color};
                cursor: pointer;
            '''
        },
        word
    )


@component
def PopupYesNo(comment, ok_callback, no_callback, ok_word='OK', no_word='キャンセル'):
    return html.div(
        {
            'on_click': no_callback,
            'style': '''
                position: fixed;
                z-index: 999;
                background-color: #000;
                opacity: 0.7;
                width: 100%;
                height: 100vh;
                top: 0;
                bottom: 0;
            '''
        },
        html.div(
            {
                'style': '''
                    min-width: 380px;
                    height: 130px;
                    background-color: #fff;
                    border-radius: 6px;
                    position: fixed;
                    top: 50%;
                    left: 50%;
                    z-index: 9999;
                    transform: translate(-50%, -50%);
                '''
            },
            html.div(
                {
                    'style': '''
                        height: 100%;
                        padding: 10px 0;
                        display: flex;
                        justify-content: space-around;
                        align-items: center;
                        flex-direction: column;
                    '''
                },
                html.p(
                    { 'style': 'padding: 0 1rem; font-size: 20px; text-align: center;' }, comment
                ),
                html.div(
                    { 'style': center() + 'gap: 1rem;' },
                    Button(ok_word, lambda e: ok_callback(e), color='#fff', background_color='#f00'),
                    Button(no_word, lambda e: no_callback(e))
                )
            )
        )
    )
