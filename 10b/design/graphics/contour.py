import cairo

# Створення контуру
width, height = 400, 400
surface = cairo.SVGSurface("output4.svg", width, height)

ctx = cairo.Context(surface)
ctx.move_to(50, 50)
ctx.line_to(100, 100)
ctx.line_to(150, 50)
ctx.line_to(50, 50)
ctx.set_source_rgb(1, 0, 0)
ctx.stroke()

ctx.show_page()
surface.finish()