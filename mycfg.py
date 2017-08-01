c = get_config()
c.NbConvertApp.notebooks = ["Teste.ipynb"]
c.NbConvertApp.export_format = 'slides'
c.SlidesExporter.reveal_url_prefix = './reveal.js'
c.inlining_css = ''
c.SlidesExporter.reveal_theme = 'solarized'