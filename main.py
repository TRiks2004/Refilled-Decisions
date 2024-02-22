import dearpygui.dearpygui as dpg

import dearpygui.demo as demo 


def on_mouse_move(sender, app_data):
    # x = app_data[1][0]
    # y = app_data[1][1]
    # print(f"Mouse position: x={x}, y={y}")
    ...

def on_text_changed(sender, app_data):

    print(dpg.get_item_configuration(sender))

    print(dpg.get_item_type(sender))
    print(dpg.get_item_slot(sender))
    # cursor_pos = dpg.get_item_info(sender)["cursor_pos"]
    # print(f"Cursor position in Input Text: {cursor_pos}")
    ...

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.handler_registry():
    dpg.add_mouse_move_handler(callback=on_mouse_move)

with dpg.window(label="Example Window", width=dpg.get_viewport_height(), height=dpg.get_viewport_height()):
    dpg.add_text("Containers can be nested for advanced layout options")
    with dpg.child_window(width=500, height=320):
        
       
        with dpg.group(horizontal=False, tag="group_1"):
            dpg.add_button(label="Header 1", width=75, height=75)
            dpg.add_button(label="Header 2", width=75, height=75)
            dpg.add_button(label="Header 3", width=75, height=75)
        

        dpg.add_button(
            label="Header 3", parent= "group_1",
            width=75, height=75)



    

dpg.show_item_registry()

demo.show_demo()

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()