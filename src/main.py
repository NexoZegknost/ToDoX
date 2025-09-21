from flet import *
import server.function as func


def main(page: Page):

    page.title = "TodoX"
    page.bgcolor = "white"
    page.fonts = {
        "header": "font/Montserrat_Alternates/MontserratAlternates-ExtraBold.ttf",
        "content": "font/Montserrat/static/Montserrat-Medium.ttf",
    }
    page.theme = Theme(font_family="content")

    # Components
    newTaskBox = TextField(label="Content", color="black")
    newTaskBoxTitle = TextField(label="Title", color="black")
    taskArea = Column([])

    # Load content
    createdTasks = func.loadTask()
    for record in createdTasks:
        taskArea.controls.append(
            Row(
                controls=[
                    Checkbox(
                        check_color="white",
                        label_style=TextStyle(
                            color="black",
                        ),
                        active_color="black",
                        shape=RoundedRectangleBorder(radius=4),
                        on_change=lambda e: doneTask(e, record["id"]),
                    ),
                    Column(
                        controls=[
                            Text(
                                value=record["title"],
                                font_family="header",
                                size=20,
                                color="black",
                            ),
                            Text(
                                value=record["content"],
                                color="black",
                            ),
                        ]
                    ),
                ],
            )
        )

    # Functions
    def doneTask(e, index):

        print(index)
        # cache = func.removeTask(int(index))
        # if len(cache) == 0:
        #     pass
        page.update()

    def newTask(e):
        if newTaskBox.value.strip() != "" and newTaskBoxTitle.value.strip() != "":
            index = func.createTask(newTaskBoxTitle.value, newTaskBox.value)
            taskArea.controls.append(
                Row(
                    controls=[
                        Checkbox(
                            check_color="white",
                            label_style=TextStyle(
                                color="black",
                            ),
                            active_color="black",
                            shape=RoundedRectangleBorder(radius=4),
                            on_change=lambda e: doneTask(e, index),
                        ),
                        Column(
                            controls=[
                                Text(
                                    value=newTaskBoxTitle.value,
                                    font_family="header",
                                    size=20,
                                    color="black",
                                ),
                                Text(
                                    value=newTaskBox.value,
                                    color="black",
                                ),
                            ]
                        ),
                    ],
                )
            )
            newTaskBox.value = ""
            newTaskBoxTitle.value = ""
            page.update()

    page.add(
        newTaskBoxTitle,
        newTaskBox,
        FilledButton(
            text="Create",
            bgcolor="black",
            color="white",
            icon=Icons.CREATE_SHARP,
            width=100,
            on_click=newTask,
        ),
        Text(value="Created tasks", size=30, color="black", font_family="header"),
        taskArea,
    )


app(target=main, assets_dir="assets")
