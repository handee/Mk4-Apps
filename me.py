"""My first app"""

___name___         = "My app"
___license___      = "MIT"
___dependencies___ = ["ugfx_helper"]

import ugfx_helper, ugfx

ugfx_helper.init()
ugfx.clear()

ugfx.text(5, 5, "Hello World", ugfx.RED)
ugfx.fill_circle(100, 100, 30, ugfx.GREEN)
ugfx.fill_circle(200, 100, 30, ugfx.GREEN)
ugfx.area(80, 150, 140, 20, ugfx.GREEN)
ugfx.area(120, 170, 60, 20, ugfx.GREEN)

while Buttons.is_pressed(Buttons.BTN_Menu):
    sleep.wfi() # This means sleep for a short while

ugfx.clear()
app.restart_to_default()
