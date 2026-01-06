import flet as ft

color_scheme = ft.Theme(
    color_scheme=ft.ColorScheme(
        primary="#000000",  # 主色：黑色
        on_primary="#FFFFFF",  # 主色上的文字：白色
        primary_container="#FFFFFF",  # 主容器色：白色
        on_primary_container="#000000",  # 主容器上的文字：黑色
        secondary="#222222",  # 次要色：深灰
        on_secondary="#FFFFFF",  # 次要色上的文字：白色
        secondary_container="#FFFFFF",  # 次容器色：白色
        on_secondary_container="#000000",  # 次容器上的文字：黑色
        tertiary="#000000",  # 第三色：黑色
        on_tertiary="#FFFFFF",  # 第三色上的文字：白色
        error="#000000",  # 错误色：黑色
        on_error="#FFFFFF",  # 错误色上的文字：白色
        surface="#FFFFFF",  # 卡片等控件背景：白色
        on_surface="#000000",  # 表面上的文字：黑色
        outline="#222222",  # 边框：深灰
        outline_variant="#FFFFFF",  # 较浅边框：白色
        shadow="#222222",  # 阴影：深灰
        scrim="#000000",  # 遮罩：黑色
        inverse_surface="#000000",  # 反色：黑色
        on_inverse_surface="#FFFFFF",  # 反色上的文字：白色
        inverse_primary="#FFFFFF",  # 反色主色：白色
        surface_tint="#FFFFFF",  # 表面高亮：白色
        primary_fixed="#000000",
        secondary_fixed="#222222",
        tertiary_fixed="#000000",
        primary_fixed_dim="#222222",
        secondary_fixed_dim="#000000",
        tertiary_fixed_dim="#222222",
        surface_bright="#FFFFFF",
        surface_container="#FFFFFF",
        surface_container_high="#FFFFFF",
        surface_container_highest="#FFFFFF",
        surface_container_low="#FFFFFF",
        surface_container_lowest="#FFFFFF",
        surface_dim="#222222",
    ),
)


class InkIconButton(ft.Container):
    def __init__(self, **kwargs):
        super().__init__(ink=False, **kwargs)  # 关闭水波纹动画


class Pagination(ft.Container):
    def __init__(self, value="1/12", on_prev=None, on_next=None, **kwargs):
        super().__init__(
            bgcolor="#FFFFFF",
            padding=ft.Padding.all(0),
            border_radius=15,
            border=ft.Border.all(1, "#222222"),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                # 间隔为0
                spacing=0,
                controls=[
                    InkIconButton(
                        content=ft.Icon(ft.Icons.CHEVRON_LEFT, color="#000000"),
                        on_click=on_prev,
                        # border=ft.Border(0, 0, 1, 0),
                        # border_radius=ft.BorderRadius(
                        #     top_left=15, bottom_left=15, top_right=0, bottom_right=0
                        # ),
                        padding=ft.Padding(6, 2, 2, 2),
                    ),
                    ft.Container(
                        content=ft.Text(
                            value,
                            color="#000000",
                            size=14,
                        ),
                        padding=ft.Padding(6, 2, 6, 2),
                        border=ft.Border(
                            left=ft.BorderSide(1, "#222222"),
                            # top=ft.BorderSide(0, "#FFFFFF"),
                            right=ft.BorderSide(1, "#222222"),
                            # bottom=ft.BorderSide(1, "#222222"),
                        ),
                    ),
                    InkIconButton(
                        content=ft.Icon(ft.Icons.CHEVRON_RIGHT, color="#000000"),
                        on_click=on_next,
                        padding=ft.Padding(2, 4, 6, 4),
                    ),
                ],
            ),
        )


def main(page: ft.Page):
    page.title = "E-Ink Counter"
    page.bgcolor = "#FFFFFF"  # 白色背景
    page.theme = ft.Theme(
        color_scheme=color_scheme,
        visual_density=ft.VisualDensity.COMPACT,  # 紧凑布局
        use_material3=False,  # 关闭Material3特效
    )
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text("顶部内容"),
                    border=ft.Border(bottom=ft.BorderSide(1, "#222222")),
                    padding=ft.Padding.all(0),
                    width=float("inf"),
                ),
                ft.Container(
                    content=ft.Text("主要内容"),
                    expand=True,
                    width=float("inf"),
                    bgcolor="#AAE468",
                    padding=ft.Padding.all(0),
                ),
                ft.Row(
                    controls=[
                        ft.Container(expand=True),  # 弹簧
                        Pagination(
                            value="1/12",
                            on_prev=lambda e: print("Previous page"),
                            on_next=lambda e: print("Next page"),
                        ),
                    ],
                ),
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # 顶部和底部分开
        )
    )


ft.run(main)
