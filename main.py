from flet import *
from googletrans import Translator

def main(page: Page):
    page.title = "Translator"
    page.window.width = 740
    page.window.height = 740
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    
    page.appbar = AppBar(
        bgcolor= colors.BLACK38,
        title=Text('TRANSLATOR'),
        center_title=True
    )

    image = Image(src='trans.png', width=220)  

    translator = Translator()

    def translate(e):
        if not input_text.value:
            output_stack.controls[0].spans[0].text = "Please enter some text to translate."
            output_stack.controls[1].spans[0].text = "Please enter some text to translate."
        else:
            try:
                translation = translator.translate(
                    input_text.value,
                    src=source_lang.value,
                    dest=target_lang.value
                )
                output_stack.controls[0].spans[0].text = translation.text
                output_stack.controls[1].spans[0].text = translation.text
            except Exception as ex:
                output_stack.controls[0].spans[0].text = f"An error occurred: {str(ex)}"
                output_stack.controls[1].spans[0].text = f"An error occurred: {str(ex)}"
        page.update()

    input_text = TextField(label="Enter text to translate", multiline=True)
   
    source_lang = Dropdown(
        label="Source language",
        options=[
            dropdown.Option("ar", "Arabic"),
            dropdown.Option("en", "English"),
            dropdown.Option("es", "Spanish"),
            dropdown.Option("fr", "French"),
            dropdown.Option("de", "German"),
            dropdown.Option("it", "Italian"),
        ],
        value="en"
    )
    
    target_lang = Dropdown(
        label="Target language",
        options=[
            dropdown.Option("ar", "Arabic"),
            dropdown.Option("en", "English"),
            dropdown.Option("es", "Spanish"),
            dropdown.Option("fr", "French"),
            dropdown.Option("de", "German"),
            dropdown.Option("it", "Italian"),
        ],
        value="es"
    )
    
    translate_button = ElevatedButton("Translate", on_click=translate, animate_size=38)
    
    output_stack = Stack(
        [
            Text(
                spans=[
                    TextSpan(
                        "",
                        TextStyle(
                            size=30,
                            weight=FontWeight.BOLD,
                            foreground=Paint(
                                color=colors.BLUE_700,
                                stroke_width=4,
                                stroke_join=StrokeJoin.ROUND,
                                style=PaintingStyle.STROKE,
                            ),
                        ),
                    ),
                ],
            ),
            Text(
                spans=[
                    TextSpan(
                        "",
                        TextStyle(
                            size=30,
                            weight=FontWeight.BOLD,
                            color=colors.GREY_300,
                        ),
                    ),
                ],
            ),
        ]
    )

    page.add(
        Column([
            image,
            input_text,
            Row([source_lang, target_lang]),
            translate_button,
            output_stack,
        ], 
        alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        )
    )

app(target=main)
