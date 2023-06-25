from reactpy import html
import exhtml

def create_star_svg(is_favorite):
        if is_favorite:
            return html.svg(
                {
                    'xmlns': "http://www.w3.org/2000/svg",
                    'viewBox': '-100 -100 200 200',
                    'width': '30',
                    'height': '30',
                },
                exhtml.polygon(
                    {
                        'points': '0,-100 29.39,-40.45 95.11,-30.9 47.55,15.45 58.78,80.90 0,50 -58.78,80.9 -47.55,15.45 -95.11,-30.9 -29.39,-40.45',
                        'fill': '#faf' if is_favorite else '#fff'
                    }
                )
            )
        else:
            return html.svg(
                {
                    'xmlns': "http://www.w3.org/2000/svg",
                    'viewBox': '0 0 48 48',
                    'width': '30',
                    'height': '30',
                },
                exhtml.polygon(
                    {
                        'points': '23.98 5 29.85 16.9 42.98 18.8 33.48 28.07 35.72 41.14 23.98 34.97 12.24 41.14 14.48 28.07 4.98 18.8 18.11 16.9 23.98 5',
                        'fill': 'none',
                        'stroke': '#faf',
                        'stroke-linecap': 'round',
                        'stroke-linejoin': 'round',
                        'stroke-width': '2',
                    }
                )
            )
