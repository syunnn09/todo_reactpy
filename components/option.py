from reactpy import component, html

@component
def Option(value: str, selected: str = None, text: str = None):
    if text is None:
        text = value
    return html.option({ 'value': value }, text)
