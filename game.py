import flet as ft
from database import DatabaseManager


class QuizApp:
    """Main graphical interface class for the quiz application.

    Manages the Flet UI and interaction with the existing database logic.
    """

    def __init__(self, page: ft.Page, db_manager: DatabaseManager):
        self.page = page
        self.db_manager = db_manager

        # Window / page configuration
        self.page.title = "Quiz Game"
        self.page.padding = 0
        self.page.bgcolor = "#F5F7FB"

        # Desktop window configuration
        self.page.window.icon = "../assets/icon/icon.ico"
        self.page.window.width = 560
        self.page.window.height = 720
        self.page.window.min_width = 500
        self.page.window.min_height = 650

        # Initialize UI components
        self._init_ui()

    def _init_ui(self) -> None:
        """Creates and places UI control elements on the form."""

        # ---------------------------------------------------------
        # Header
        # ---------------------------------------------------------

        header = ft.Container(
            padding=ft.Padding(left=32, right=32, top=28, bottom=22),
            content=ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        width=52,
                        height=52,
                        border_radius=14,
                        bgcolor="#E8F5E9",
                        alignment=ft.Alignment(0, 0),
                        content=ft.Icon(
                            ft.Icons.QUIZ_ROUNDED,
                            size=28,
                            color="#2E7D32",
                        ),
                    ),
                    ft.Container(
                        padding=ft.Padding(left=16),
                        content=ft.Column(
                            spacing=3,
                            controls=[
                                ft.Text(
                                    "Quiz Management",
                                    size=25,
                                    weight=ft.FontWeight.BOLD,
                                    color="#17202A",
                                ),
                                ft.Text(
                                    "Create and save quiz questions",
                                    size=13,
                                    color="#6B7280",
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )

        # ---------------------------------------------------------
        # Input fields
        # ---------------------------------------------------------

        self.quest_entry = ft.TextField(
            label="Question",
            hint_text="Enter your quiz question",
            prefix_icon=ft.Icons.HELP_OUTLINE_ROUNDED,
            width=460,
            height=58,
            text_size=14,
            border_radius=12,
            border_color="#D5D9E2",
            focused_border_color="#4CAF50",
            bgcolor="#FFFFFF",
            content_padding=ft.Padding(
                left=14,
                right=14,
                top=10,
                bottom=10,
            ),
        )

        self.answer_1_entry = ft.TextField(
            label="Answer 1",
            hint_text="Enter the first answer",
            prefix_icon=ft.Icons.LOOKS_ONE_ROUNDED,
            width=460,
            height=58,
            text_size=14,
            border_radius=12,
            border_color="#D5D9E2",
            focused_border_color="#4CAF50",
            bgcolor="#FFFFFF",
            content_padding=ft.Padding(
                left=14,
                right=14,
                top=10,
                bottom=10,
            ),
        )

        self.answer_2_entry = ft.TextField(
            label="Answer 2",
            hint_text="Enter the second answer",
            prefix_icon=ft.Icons.LOOKS_TWO_ROUNDED,
            width=460,
            height=58,
            text_size=14,
            border_radius=12,
            border_color="#D5D9E2",
            focused_border_color="#4CAF50",
            bgcolor="#FFFFFF",
            content_padding=ft.Padding(
                left=14,
                right=14,
                top=10,
                bottom=10,
            ),
        )

        self.name_user_entry = ft.TextField(
            label="Username",
            hint_text="Enter your username",
            prefix_icon=ft.Icons.PERSON_OUTLINE_ROUNDED,
            width=460,
            height=58,
            text_size=14,
            border_radius=12,
            border_color="#D5D9E2",
            focused_border_color="#4CAF50",
            bgcolor="#FFFFFF",
            content_padding=ft.Padding(
                left=14,
                right=14,
                top=10,
                bottom=10,
            ),
        )

        # ---------------------------------------------------------
        # Form card
        # ---------------------------------------------------------

        form_card = ft.Card(
            variant=ft.CardVariant.ELEVATED,
            elevation=3,
            content=ft.Container(
                width=500,
                padding=ft.Padding(
                    left=20,
                    right=20,
                    top=24,
                    bottom=24,
                ),
                bgcolor="#FFFFFF",
                border_radius=18,
                content=ft.Column(
                    spacing=16,
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Text(
                                    "Question details",
                                    size=17,
                                    weight=ft.FontWeight.BOLD,
                                    color="#17202A",
                                ),
                                ft.Container(expand=True),
                                ft.Icon(
                                    ft.Icons.EDIT_NOTE_ROUNDED,
                                    size=22,
                                    color="#7B8794",
                                ),
                            ]
                        ),
                        ft.Divider(
                            height=1,
                            color="#E8EBF0",
                        ),
                        self.quest_entry,
                        self.answer_1_entry,
                        self.answer_2_entry,
                        self.name_user_entry,
                    ],
                ),
            ),
        )

        # ---------------------------------------------------------
        # Submit button
        # ---------------------------------------------------------

        self.button_submit = ft.Button(
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=9,
                controls=[
                    ft.Icon(
                        ft.Icons.SAVE_ROUNDED,
                        size=20,
                    ),
                    ft.Text(
                        "Save Question",
                        size=15,
                        weight=ft.FontWeight.BOLD,
                    ),
                ],
            ),
            width=460,
            height=52,
            on_click=self.submit_data,
            style=ft.ButtonStyle(
                bgcolor="#4CAF50",
                color="#FFFFFF",
                elevation=2,
                shape=ft.RoundedRectangleBorder(radius=12),
                padding=ft.Padding(
                    left=20,
                    right=20,
                    top=10,
                    bottom=10,
                ),
            ),
        )

        # ---------------------------------------------------------
        # Information footer
        # ---------------------------------------------------------

        footer = ft.Container(
            width=460,
            padding=ft.Padding(top=4, bottom=12),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=7,
                controls=[
                    ft.Icon(
                        ft.Icons.INFO_OUTLINE_ROUNDED,
                        size=16,
                        color="#7B8794",
                    ),
                    ft.Text(
                        "Your question will be saved directly to the database.",
                        size=12,
                        color="#7B8794",
                    ),
                ],
            ),
        )

        # ---------------------------------------------------------
        # Main page layout
        # ---------------------------------------------------------

        main_content = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                header,
                form_card,
                ft.Container(height=18),
                self.button_submit,
                footer,
            ],
        )

        self.page.add(
            ft.SafeArea(
                expand=True,
                content=main_content,
            )
        )

    def submit_data(self, e=None) -> None:
        """Reads data from input fields and saves it via DatabaseManager."""

        # Flet uses .value instead of Tkinter's .get()
        question = self.quest_entry.value.strip()
        ans_1 = self.answer_1_entry.value.strip()
        ans_2 = self.answer_2_entry.value.strip()
        username = self.name_user_entry.value.strip()

        # Validate input data
        if not all([question, ans_1, ans_2, username]):
            self.page.show_dialog(
                ft.AlertDialog(
                    title=ft.Text(
                        "Missing information",
                        weight=ft.FontWeight.BOLD,
                    ),
                    content=ft.Text(
                        "Please fill in all form fields before saving."
                    ),
                    actions=[
                        ft.TextButton(
                            content="OK",
                            on_click=lambda e: self.page.pop_dialog(),
                        )
                    ],
                )
            )
            return

        try:
            query = """
                INSERT INTO questions (
                    question_text,
                    option_a,
                    option_b,
                    option_c,
                    option_d,
                    correct_option
                )
                VALUES (%s, %s, %s, %s, %s, %s)
            """


            params = (
                question,
                ans_1,
                ans_2,
                "none",
                "none",
                username,
            )

            self.db_manager.execute_query(query, params)

            self.page.show_dialog(
                ft.AlertDialog(
                    title=ft.Row(
                        spacing=10,
                        controls=[
                            ft.Icon(
                                ft.Icons.CHECK_CIRCLE_ROUNDED,
                                color="#4CAF50",
                                size=28,
                            ),
                            ft.Text(
                                "Success",
                                weight=ft.FontWeight.BOLD,
                            ),
                        ],
                    ),
                    content=ft.Text(
                        f"Data for user {username} successfully "
                        f"saved to database!"
                    ),
                    actions=[
                        ft.TextButton(
                            content="OK",
                            on_click=lambda e: self._close_success_dialog(),
                        )
                    ],
                )
            )

            self._clear_inputs()

        except Exception as e:
            self.page.show_dialog(
                ft.AlertDialog(
                    title=ft.Row(
                        spacing=10,
                        controls=[
                            ft.Icon(
                                ft.Icons.ERROR_OUTLINE_ROUNDED,
                                color="#D32F2F",
                                size=28,
                            ),
                            ft.Text(
                                "Database Error",
                                weight=ft.FontWeight.BOLD,
                            ),
                        ],
                    ),
                    content=ft.Text(
                        f"Failed to save data:\n{e}",
                        color="#555555",
                    ),
                    actions=[
                        ft.TextButton(
                            content="Close",
                            on_click=lambda e: self.page.pop_dialog(),
                        )
                    ],
                )
            )

    def _close_success_dialog(self) -> None:
        """Closes the success dialog."""
        self.page.pop_dialog()

    def _clear_inputs(self) -> None:
        """Clears all input fields after successful submission."""

        self.quest_entry.value = ""
        self.answer_1_entry.value = ""
        self.answer_2_entry.value = ""
        self.name_user_entry.value = ""

        self.page.update()


def main(page: ft.Page):
    """Application entry point."""

    # Initialize database manager and start the application
    db_manager = DatabaseManager()
    db_manager.create_tables()

    QuizApp(page, db_manager)


if __name__ == "__main__":
    ft.run(main)