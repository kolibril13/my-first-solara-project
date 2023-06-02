import solara

clicks = solara.reactive(0)


@solara.component
def Page():
    color = "green"
    if clicks.value >= 2:
        color = "blue"

    def increment():
        clicks.value += 1
        print("clicks", clicks)

    label = "Not clicked yetttt" if clicks.value == 0 else f"Clicked: {clicks}"
    solara.Button(label=label, on_click=increment, color=color)
