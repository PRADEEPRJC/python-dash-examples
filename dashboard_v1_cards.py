import dash
from dash import html, dcc
import dash_mantine_components as dmc
from dash_iconify import DashIconify

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the metric cards data
metrics_data = [
    {
        "title": "New Business",
        "policies": "1,000",
        "premium": "$1,000,000",
        "icon": "material-symbols:business",
        "color": "blue"
    },
    {
        "title": "Renewals",
        "policies": "2,500", 
        "premium": "$3,250,000",
        "icon": "material-symbols:autorenew",
        "color": "green"
    },
    {
        "title": "Claims Processed",
        "policies": "450",
        "premium": "$750,000",
        "icon": "material-symbols:assignment-turned-in",
        "color": "orange"
    },
    {
        "title": "Active Policies",
        "policies": "8,750",
        "premium": "$12,500,000",
        "icon": "material-symbols:shield-check",
        "color": "teal"
    },
    {
        "title": "Cancelled Policies",
        "policies": "125",
        "premium": "$180,000",
        "icon": "material-symbols:cancel-outline",
        "color": "red"
    }
]

# Row 1: Classic Cards with Icons on Top
def create_classic_card(title, policies, premium, icon, color):
    return dmc.Card(
        children=[
            dmc.Stack(
                [
                    dmc.Center(
                        DashIconify(icon=icon, width=50, height=50, color=color)
                    ),
                    dmc.Center(
                        dmc.Text(title, size="lg", fw=600)
                    ),
                    dmc.Divider(),
                    dmc.Text(f"Policies: {policies}", size="md", ta="center"),
                    dmc.Text(f"Premium: {premium}", size="md", fw=700, c=color, ta="center")
                ],
                gap="sm"
            )
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
        p="md",
        style={"height": "180px"}
    )

# Row 2: Horizontal Layout Cards
def create_horizontal_card(title, policies, premium, icon, color):
    return dmc.Card(
        children=[
            dmc.Group(
                [
                    DashIconify(icon=icon, width=40, height=40, color=color),
                    dmc.Stack(
                        [
                            dmc.Text(title, size="sm", fw=600),
                            dmc.Text(policies, size="xl", fw=700, c=color),
                            dmc.Text(premium, size="sm")
                        ],
                        gap="xs"
                    )
                ],
                gap="md"
            )
        ],
        withBorder=True,
        shadow="md",
        radius="lg",
        p="lg",
        style={"height": "120px", "backgroundColor": "#f8f9fa"}
    )

# Row 3: Gradient Background Cards
def create_gradient_card(title, policies, premium, icon, color):
    gradients = {
        "blue": "linear-gradient(45deg, #228be6, #74c0fc)",
        "green": "linear-gradient(45deg, #51cf66, #8ce99a)",
        "orange": "linear-gradient(45deg, #ff8c00, #ffd43b)",
        "teal": "linear-gradient(45deg, #20c997, #63e6be)",
        "red": "linear-gradient(45deg, #f03e3e, #ffa8a8)"
    }
    return dmc.Card(
        children=[
            dmc.Stack(
                [
                    dmc.Group(
                        [
                            dmc.Text(title, size="lg", fw=600, c="white"),
                            DashIconify(icon=icon, width=35, height=35, color="white")
                        ],
                        justify="space-between"
                    ),
                    dmc.Text(policies, size="xxl", fw=900, c="white"),
                    dmc.Text(premium, size="md", c="white")
                ],
                gap="xs"
            )
        ],
        radius="xl",
        p="lg",
        style={
            "background": gradients[color],
            "height": "150px",
            "color": "white"
        }
    )

# Row 4: Minimal Border Cards
def create_minimal_card(title, policies, premium, icon, color):
    return dmc.Paper(
        children=[
            dmc.Stack(
                [
                    dmc.Group(
                        [
                            dmc.Text(title, size="xs", c="dimmed", tt="uppercase"),
                            DashIconify(icon=icon, width=20, height=20, color=color)
                        ],
                        justify="space-between"
                    ),
                    dmc.Text(policies, size="xl", fw=700, c=color),
                    dmc.Text(f"Premium {premium}", size="sm", c="dark")
                ],
                gap="xs"
            )
        ],
        withBorder=True,
        p="lg",
        style={"height": "130px", "borderLeft": f"4px solid {color}"}
    )

# Row 5: Badge Style Cards
def create_badge_card(title, policies, premium, icon, color):
    return dmc.Card(
        children=[
            dmc.Stack(
                [
                    dmc.Badge(title, color=color, size="lg", radius="md"),
                    dmc.Group(
                        [
                            DashIconify(icon=icon, width=45, height=45, color=color),
                            dmc.Stack(
                                [
                                    dmc.Text(policies, size="xl", fw=700),
                                    dmc.Text(premium, size="sm", c="dimmed")
                                ],
                                gap="xs"
                            )
                        ],
                        align="center"
                    )
                ],
                gap="md"
            )
        ],
        withBorder=True,
        shadow="lg",
        radius="md",
        p="md",
        style={"height": "160px"}
    )

# Row 6: Compact Cards
def create_compact_card(title, policies, premium, icon, color):
    return dmc.Paper(
        children=[
            dmc.Group(
                [
                    dmc.Stack(
                        [
                            dmc.Text(title, size="xs", fw=600),
                            dmc.Text(policies, size="lg", fw=700, c=color),
                            dmc.Text(premium, size="xs", c="dimmed")
                        ],
                        gap="xs"
                    ),
                    DashIconify(icon=icon, width=30, height=30, color=color)
                ],
                justify="space-between",
                align="center"
            )
        ],
        shadow="xs",
        p="sm",
        radius="sm",
        style={"height": "100px", "backgroundColor": "#f1f3f4"}
    )

# Row 7: Outlined Cards
def create_outlined_card(title, policies, premium, icon, color):
    return dmc.Card(
        children=[
            dmc.Stack(
                [
                    dmc.Center(dmc.Text(title, size="md", fw=600, c=color)),
                    dmc.Center(DashIconify(icon=icon, width=40, height=40, color=color)),
                    dmc.Stack(
                        [
                            dmc.Center(dmc.Text(policies, size="lg", fw=700)),
                            dmc.Center(dmc.Text(premium, size="sm", c="dimmed"))
                        ],
                        gap="xs"
                    )
                ],
                gap="sm"
            )
        ],
        style={
            "border": f"2px solid {color}",
            "height": "170px"
        },
        radius="md",
        p="md"
    )

# Row 8: Shadow Cards with Hover Effect
def create_shadow_card(title, policies, premium, icon, color):
    return dmc.Card(
        children=[
            dmc.Stack(
                [
                    dmc.Text(title, size="sm", c="dimmed", ta="center"),
                    dmc.Center(
                        dmc.Group(
                            [
                                DashIconify(icon=icon, width=35, height=35, color=color),
                                dmc.Text(policies, size="xl", fw=900, c=color)
                            ],
                            gap="sm",
                            align="center"
                        )
                    ),
                    dmc.Center(dmc.Text(premium, size="md", fw=600))
                ],
                gap="md"
            )
        ],
        shadow="xl",
        radius="lg",
        p="lg",
        style={
            "height": "140px",
            "transition": "transform 0.2s ease",
            ":hover": {"transform": "translateY(-5px)"}
        }
    )

# Row 9: Rounded Corner Cards
def create_rounded_card(title, policies, premium, icon, color):
    return dmc.Paper(
        children=[
            dmc.Stack(
                [
                    dmc.Group(
                        [
                            dmc.Text(title, size="lg", fw=600),
                            DashIconify(icon=icon, width=25, height=25, color=color)
                        ],
                        justify="space-between"
                    ),
                    dmc.Space(h="sm"),
                    dmc.Text(policies, size="xxl", fw=800, c=color),
                    dmc.Text(premium, size="md")
                ],
                gap="xs"
            )
        ],
        withBorder=True,
        p="xl",
        radius="xl",
        style={"height": "180px", "borderRadius": "25px"}
    )

# Row 10: Dashboard Style Cards
def create_dashboard_card(title, policies, premium, icon, color):
    return dmc.Card(
        children=[
            dmc.Stack(
                [
                    dmc.Group(
                        [
                            dmc.Stack(
                                [
                                    dmc.Text(title, size="xs", c="dimmed"),
                                    dmc.Text(policies, size="lg", fw=700, c=color),
                                    dmc.Text(premium, size="xs")
                                ],
                                gap="xs"
                            ),
                            dmc.Paper(
                                DashIconify(icon=icon, width=30, height=30, color="white"),
                                p="sm",
                                radius="md",
                                style={"backgroundColor": color}
                            )
                        ],
                        justify="space-between",
                        align="flex-start"
                    )
                ]
            )
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
        p="md",
        style={"height": "120px"}
    )

# Create the app layout
app.layout = dmc.MantineProvider(
    children=[
        dmc.Container(
            [
                dmc.Center(
                    dmc.Title("Business Metrics Dashboard - 10 Different Designs", order=1)
                ),
                dmc.Space(h="xl"),
                
                # Row 1: Classic Cards
                dmc.Text("Row 1: Classic Cards with Top Icons", size="lg", fw=600, c="blue"),
                dmc.Space(h="md"),
                dmc.SimpleGrid(
                    cols={"base": 1, "sm": 2, "md": 3, "lg": 5},
                    spacing="lg",
                    children=[create_classic_card(m["title"], m["policies"], m["premium"], m["icon"], m["color"]) for m in metrics_data]
                ),
                dmc.Space(h="xl"),
                
                # Row 2: Horizontal Cards
                dmc.Text("Row 2: Horizontal Layout Cards", size="lg", fw=600, c="green"),
                dmc.Space(h="md"),
                dmc.SimpleGrid(
                    cols={"base": 1, "sm": 2, "md": 3, "lg": 5},
                    spacing="lg",
                    children=[create_horizontal_card(m["title"], m["policies"], m["premium"], m["icon"], m["color"]) for m in metrics_data]
                ),
                dmc.Space(h="xl"),
                
                # Row 3: Gradient Cards
                dmc.Text("Row 3: Gradient Background Cards", size="lg", fw=600, c="orange"),
                dmc.Space(h="md"),
                dmc.SimpleGrid(
                    cols={"base": 1, "sm": 2, "md": 3, "lg": 5},
                    spacing="lg",
                    children=[create_gradient_card(m["title"], m["policies"], m["premium"], m["icon"], m["color"]) for m in metrics_data]
                ),
                dmc.Space(h="xl"),
                
                # Row 4: Minimal Cards
                dmc.Text("Row 4: Minimal Border Cards", size="lg", fw=600, c="teal"),
                dmc.Space(h="md"),
                dmc.SimpleGrid(
                    cols={"base": 1, "sm": 2, "md": 3, "lg": 5},
                    spacing="lg",
                    children=[create_minimal_card(m["title"], m["policies"], m["premium"], m["icon"], m["color"]) for m in metrics_data]
                ),
                dmc.Space(h="xl"),
                
                # Row 5: Badge Cards
                dmc.Text("Row 5: Badge Style Cards", size="lg", fw=600, c="red"),
                dmc.Space(h="md"),
                dmc.SimpleGrid(
                    cols={"base": 1, "sm": 2, "md": 3, "lg": 5},
                    spacing="lg",
                    children=[create_badge_card(m["title"], m["policies"], m["premium"], m["icon"], m["color"]) for m in metrics_data]
                ),
                dmc.Space(h="xl"),
                
                # Row 6: Compact Cards
                dmc.Text("Row 6: Compact Cards", size="lg", fw=600, c="violet"),
                dmc.Space(h="md"),
                dmc.SimpleGrid(
                    cols={"base": 1, "sm": 2, "md": 3, "lg": 5},
                    spacing="lg",
                    children=[create_compact_card(m["title"], m["policies"], m["premium"], m["icon"], m["color"]) for m in metrics_data]
                ),
                dmc.Space(h="xl"),
                
                # Row 7: Outlined Cards
                dmc.Text("Row 7: Outlined Cards", size="lg", fw=600, c="indigo"),
                dmc.Space(h="md"),
                dmc.SimpleGrid(
                    cols={"base": 1, "sm": 2, "md": 3, "lg": 5},
                    spacing="lg",
                    children=[create_outlined_card(m["title"], m["policies"], m["premium"], m["icon"], m["color"]) for m in metrics_data]
                ),
                dmc.Space(h="xl"),
                
                # Row 8: Shadow Cards
                dmc.Text("Row 8: Shadow Cards", size="lg", fw=600, c="pink"),
                dmc.Space(h="md"),
                dmc.SimpleGrid(
                    cols={"base": 1, "sm": 2, "md": 3, "lg": 5},
                    spacing="lg",
                    children=[create_shadow_card(m["title"], m["policies"], m["premium"], m["icon"], m["color"]) for m in metrics_data]
                ),
                dmc.Space(h="xl"),
                
                # Row 9: Rounded Cards
                dmc.Text("Row 9: Rounded Corner Cards", size="lg", fw=600, c="cyan"),
                dmc.Space(h="md"),
                dmc.SimpleGrid(
                    cols={"base": 1, "sm": 2, "md": 3, "lg": 5},
                    spacing="lg",
                    children=[create_rounded_card(m["title"], m["policies"], m["premium"], m["icon"], m["color"]) for m in metrics_data]
                ),
                dmc.Space(h="xl"),
                
                # Row 10: Dashboard Cards
                dmc.Text("Row 10: Dashboard Style Cards", size="lg", fw=600, c="grape"),
                dmc.Space(h="md"),
                dmc.SimpleGrid(
                    cols={"base": 1, "sm": 2, "md": 3, "lg": 5},
                    spacing="lg",
                    children=[create_dashboard_card(m["title"], m["policies"], m["premium"], m["icon"], m["color"]) for m in metrics_data]
                ),
                dmc.Space(h="xl")
            ],
            size="xl",
            p="md"
        )
    ]
)

if __name__ == "__main__":
    app.run(debug=True)