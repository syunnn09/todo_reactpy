from reactpy import component, html


def Head():
    return (
        html.style(
            '''
                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }
            '''
        )
    )