import cairo

# Create a new surface
width, height = 400, 400
surface = cairo.SVGSurface("output4.svg", width, height)

# Create a new context
ctx = cairo.Context(surface)

# Set the line width and color
ctx.set_line_width(5)
ctx.set_source_rgb(255, 0, 0)

# Draw a rectangle
ctx.rectangle(50, 50, 300, 300)
ctx.stroke()

# Draw a line
ctx.set_source_rgba(0, 255, 0, 0.5)
ctx.move_to(50, 50)
ctx.line_to(350, 350)
ctx.stroke()

# Draw some text
ctx.set_source_rgba(0, 0, 255, 0.5)
ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
ctx.set_font_size(40)
ctx.move_to(50, 200)
ctx.show_text("Hello, Pycairo!")

# Finish and save the surface
ctx.show_page()
surface.finish()
