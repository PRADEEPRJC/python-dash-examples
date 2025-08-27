import dash
from dash import html, dcc, callback, Input, Output
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import random

# Initialize the Dash app
app = dash.Dash(__name__)

# Define comprehensive metrics data with both type 1 (dual values) and type 2 (single value)
all_metrics = [
    # Type 1 metrics (dual values)
    {"name": "New Business", "count": "1,247", "premium": "$2,850,000", "icon": "material-symbols:business", "color": "blue", "type": 1},
    {"name": "Renewals", "count": "3,156", "premium": "$5,750,000", "icon": "material-symbols:autorenew", "color": "green", "type": 1},
    {"name": "Claims Processed", "count": "892", "premium": "$1,340,000", "icon": "material-symbols:assignment-turned-in", "color": "orange", "type": 1},
    {"name": "Active Policies", "count": "12,438", "premium": "$18,925,000", "icon": "material-symbols:shield-check", "color": "teal", "type": 1},
    {"name": "Cancelled Policies", "count": "234", "premium": "$425,000", "icon": "material-symbols:cancel-outline", "color": "red", "type": 1},
    {"name": "Pending Applications", "count": "567", "premium": "$975,000", "icon": "material-symbols:pending-actions", "color": "yellow", "type": 1},
    {"name": "Lapsed Policies", "count": "145", "premium": "$298,000", "icon": "material-symbols:schedule", "color": "gray", "type": 1},
    {"name": "Reinstated Policies", "count": "89", "premium": "$167,000", "icon": "material-symbols:restore", "color": "cyan", "type": 1},
    
    # Type 2 metrics (single value)
    {"name": "Customer Satisfaction", "value": "94.5%", "icon": "material-symbols:sentiment-satisfied", "color": "green", "type": 2},
    {"name": "Agent Performance", "value": "87.2%", "icon": "material-symbols:trending-up", "color": "blue", "type": 2},
    {"name": "Claim Settlement Ratio", "value": "92.8%", "icon": "material-symbols:check-circle", "color": "teal", "type": 2},
    {"name": "Revenue Growth", "value": "+15.3%", "icon": "material-symbols:growth", "color": "green", "type": 2},
    {"name": "Market Share", "value": "23.7%", "icon": "material-symbols:pie-chart", "color": "purple", "type": 2},
    {"name": "Processing Time", "value": "2.4 days", "icon": "material-symbols:timer", "color": "orange", "type": 2},
    {"name": "Digital Adoption", "value": "78.5%", "icon": "material-symbols:smartphone", "color": "indigo", "type": 2},
    {"name": "Risk Score", "value": "Low", "icon": "material-symbols:security", "color": "green", "type": 2},
]

# Generate random metrics for each tab
def generate_tab_metrics():
    tabs_data = []
    for i in range(10):
        num_metrics = random.randint(4, 10)
        tab_metrics = random.sample(all_metrics, num_metrics)
        tabs_data.append(tab_metrics)
    return tabs_data

tab_metrics_data = generate_tab_metrics()

# Tab 1: Sleek Gradient Cards
def create_sleek_card(metric):
    if metric["type"] == 1:
        return dmc.Card(
            children=[
                dmc.Stack([
                    dmc.Group([
                        dmc.ThemeIcon(
                            DashIconify(icon=metric["icon"], width=20),
                            size="lg",
                            variant="light",
                            color=metric["color"]
                        ),
                        dmc.Text(metric["name"], size="sm", fw=600, c="white")
                    ], justify="space-between"),
                    dmc.Space(h="md"),
                    dmc.Group([
                        dmc.Stack([
                            dmc.Text("Policies", size="xs", c="rgba(255,255,255,0.8)"),
                            dmc.Text(metric["count"], size="xl", fw=700, c="white")
                        ], gap="xs"),
                        dmc.Stack([
                            dmc.Text("Premium", size="xs", c="rgba(255,255,255,0.8)"),
                            dmc.Text(metric["premium"], size="lg", fw=600, c="white")
                        ], gap="xs")
                    ], justify="space-between")
                ], gap="sm")
            ],
            p="lg",
            radius="xl",
            style={
                "background": f"linear-gradient(135deg, {metric['color']} 0%, rgba(0,0,0,0.2) 100%)",
                "height": "140px",
                "border": "none"
            }
        )
    else:
        return dmc.Card(
            children=[
                dmc.Stack([
                    dmc.Group([
                        dmc.ThemeIcon(
                            DashIconify(icon=metric["icon"], width=20),
                            size="lg",
                            variant="light",
                            color="white"
                        ),
                        dmc.Text(metric["name"], size="sm", fw=600, c="white")
                    ], justify="space-between"),
                    dmc.Center([
                        dmc.Text(metric["value"], size="xxl", fw=900, c="white")
                    ])
                ], gap="md")
            ],
            p="lg",
            radius="xl",
            style={
                "background": f"linear-gradient(135deg, {metric['color']} 0%, rgba(0,0,0,0.2) 100%)",
                "height": "140px",
                "border": "none"
            }
        )

# Tab 2: Glass Morphism Cards
def create_glass_card(metric):
    if metric["type"] == 1:
        return dmc.Paper(
            children=[
                dmc.Stack([
                    dmc.Group([
                        dmc.Avatar(
                            DashIconify(icon=metric["icon"], width=24, color=metric["color"]),
                            size="md",
                            radius="xl",
                            style={"backgroundColor": "rgba(255,255,255,0.2)"}
                        ),
                        dmc.Text(metric["name"], size="md", fw=600)
                    ]),
                    dmc.Divider(variant="dashed", opacity=0.3),
                    dmc.SimpleGrid([
                        dmc.Stack([
                            dmc.Text(metric["count"], size="xl", fw=700, c=metric["color"]),
                            dmc.Text("Total Policies", size="xs", c="dimmed")
                        ], gap="xs", align="center"),
                        dmc.Stack([
                            dmc.Text(metric["premium"], size="lg", fw=600, c=metric["color"]),
                            dmc.Text("Total Premium", size="xs", c="dimmed")
                        ], gap="xs", align="center")
                    ], cols=2)
                ], gap="sm")
            ],
            p="lg",
            radius="lg",
            style={
                "background": "rgba(255, 255, 255, 0.1)",
                "backdropFilter": "blur(10px)",
                "border": "1px solid rgba(255, 255, 255, 0.2)",
                "height": "160px"
            }
        )
    else:
        return dmc.Paper(
            children=[
                dmc.Stack([
                    dmc.Group([
                        dmc.Avatar(
                            DashIconify(icon=metric["icon"], width=24, color=metric["color"]),
                            size="md",
                            radius="xl",
                            style={"backgroundColor": "rgba(255,255,255,0.2)"}
                        ),
                        dmc.Text(metric["name"], size="md", fw=600)
                    ]),
                    dmc.Center([
                        dmc.Text(metric["value"], size="xxl", fw=900, c=metric["color"])
                    ])
                ], gap="md")
            ],
            p="lg",
            radius="lg",
            style={
                "background": "rgba(255, 255, 255, 0.1)",
                "backdropFilter": "blur(10px)",
                "border": "1px solid rgba(255, 255, 255, 0.2)",
                "height": "160px"
            }
        )

# Tab 3: Neumorphism Cards
def create_neuro_card(metric):
    if metric["type"] == 1:
        return dmc.Paper(
            children=[
                dmc.Stack([
                    dmc.Center([
                        dmc.ThemeIcon(
                            DashIconify(icon=metric["icon"], width=28),
                            size="xl",
                            variant="light",
                            color=metric["color"]
                        )
                    ]),
                    dmc.Center([
                        dmc.Text(metric["name"], size="md", fw=600, ta="center")
                    ]),
                    dmc.SimpleGrid([
                        dmc.Center([
                            dmc.Stack([
                                dmc.Text(metric["count"], size="lg", fw=700, c=metric["color"], ta="center"),
                                dmc.Text("Policies", size="xs", c="dimmed", ta="center")
                            ], gap="xs")
                        ]),
                        dmc.Center([
                            dmc.Stack([
                                dmc.Text(metric["premium"], size="sm", fw=600, c=metric["color"], ta="center"),
                                dmc.Text("Premium", size="xs", c="dimmed", ta="center")
                            ], gap="xs")
                        ])
                    ], cols=2)
                ], gap="sm")
            ],
            p="lg",
            radius="xl",
            style={
                "backgroundColor": "#f0f0f0",
                "boxShadow": "8px 8px 16px #d1d1d1, -8px -8px 16px #ffffff",
                "border": "none",
                "height": "180px"
            }
        )
    else:
        return dmc.Paper(
            children=[
                dmc.Stack([
                    dmc.Center([
                        dmc.ThemeIcon(
                            DashIconify(icon=metric["icon"], width=32),
                            size="xl",
                            variant="light",
                            color=metric["color"]
                        )
                    ]),
                    dmc.Center([
                        dmc.Text(metric["name"], size="md", fw=600, ta="center")
                    ]),
                    dmc.Center([
                        dmc.Text(metric["value"], size="xxl", fw=900, c=metric["color"])
                    ])
                ], gap="md")
            ],
            p="lg",
            radius="xl",
            style={
                "backgroundColor": "#f0f0f0",
                "boxShadow": "8px 8px 16px #d1d1d1, -8px -8px 16px #ffffff",
                "border": "none",
                "height": "180px"
            }
        )

# Tab 4: Minimal Line Cards
def create_minimal_card(metric):
    if metric["type"] == 1:
        return dmc.Paper(
            children=[
                dmc.Stack([
                    dmc.Group([
                        dmc.Text(metric["name"], size="sm", c="dimmed", tt="uppercase", fw=600),
                        DashIconify(icon=metric["icon"], width=20, color=metric["color"])
                    ], justify="space-between"),
                    dmc.Group([
                        dmc.Stack([
                            dmc.Text(metric["count"], size="xl", fw=700, c=metric["color"]),
                            dmc.Text("Policies", size="xs", c="dimmed")
                        ], gap="xs"),
                        dmc.Stack([
                            dmc.Text(metric["premium"], size="lg", fw=600, c="dark"),
                            dmc.Text("Premium", size="xs", c="dimmed")
                        ], gap="xs")
                    ], justify="space-between", align="flex-end")
                ], gap="lg")
            ],
            p="lg",
            style={
                "borderLeft": f"4px solid {metric['color']}",
                "backgroundColor": "white",
                "height": "120px"
            },
            withBorder=True
        )
    else:
        return dmc.Paper(
            children=[
                dmc.Stack([
                    dmc.Group([
                        dmc.Text(metric["name"], size="sm", c="dimmed", tt="uppercase", fw=600),
                        DashIconify(icon=metric["icon"], width=20, color=metric["color"])
                    ], justify="space-between"),
                    dmc.Center([
                        dmc.Text(metric["value"], size="xxl", fw=900, c=metric["color"])
                    ])
                ], gap="lg")
            ],
            p="lg",
            style={
                "borderLeft": f"4px solid {metric['color']}",
                "backgroundColor": "white",
                "height": "120px"
            },
            withBorder=True
        )

# Tab 5: Floating Cards
def create_floating_card(metric):
    if metric["type"] == 1:
        return dmc.Card(
            children=[
                dmc.Stack([
                    dmc.Group([
                        dmc.Badge(metric["name"], color=metric["color"], variant="light", size="lg"),
                        dmc.ActionIcon(
                            DashIconify(icon=metric["icon"], width=20),
                            variant="light",
                            color=metric["color"],
                            size="lg"
                        )
                    ], justify="space-between"),
                    dmc.Grid([
                        dmc.GridCol([
                            dmc.Stack([
                                dmc.Text(metric["count"], size="xl", fw=700, c=metric["color"]),
                                dmc.Text("Total Policies", size="xs", c="dimmed")
                            ], gap="xs")
                        ], span=6),
                        dmc.GridCol([
                            dmc.Stack([
                                dmc.Text(metric["premium"], size="lg", fw=600),
                                dmc.Text("Premium Value", size="xs", c="dimmed")
                            ], gap="xs")
                        ], span=6)
                    ])
                ], gap="md")
            ],
            shadow="xl",
            radius="lg",
            p="lg",
            style={
                "height": "140px",
                "transform": "translateY(0px)",
                "transition": "all 0.3s ease"
            }
        )
    else:
        return dmc.Card(
            children=[
                dmc.Stack([
                    dmc.Group([
                        dmc.Badge(metric["name"], color=metric["color"], variant="light", size="lg"),
                        dmc.ActionIcon(
                            DashIconify(icon=metric["icon"], width=20),
                            variant="light",
                            color=metric["color"],
                            size="lg"
                        )
                    ], justify="space-between"),
                    dmc.Center([
                        dmc.Text(metric["value"], size="xxl", fw=900, c=metric["color"])
                    ])
                ], gap="lg")
            ],
            shadow="xl",
            radius="lg",
            p="lg",
            style={
                "height": "140px",
                "transform": "translateY(0px)",
                "transition": "all 0.3s ease"
            }
        )

# Tab 6: Split Design Cards
def create_split_card(metric):
    if metric["type"] == 1:
        return dmc.Paper(
            children=[
                dmc.Group([
                    dmc.Stack([
                        dmc.ThemeIcon(
                            DashIconify(icon=metric["icon"], width=24),
                            size="xl",
                            color=metric["color"]
                        ),
                        dmc.Text(metric["name"], size="sm", fw=600, c="white")
                    ], gap="sm", align="center"),
                    dmc.Paper([
                        dmc.Stack([
                            dmc.SimpleGrid([
                                dmc.Stack([
                                    dmc.Text(metric["count"], size="lg", fw=700),
                                    dmc.Text("Policies", size="xs", c="dimmed")
                                ], gap="xs", align="center"),
                                dmc.Stack([
                                    dmc.Text(metric["premium"], size="md", fw=600),
                                    dmc.Text("Premium", size="xs", c="dimmed")
                                ], gap="xs", align="center")
                            ], cols=2)
                        ])
                    ], p="md", style={"backgroundColor": "white", "borderRadius": "8px"})
                ], align="center", gap="md")
            ],
            p="md",
            radius="lg",
            style={
                "background": f"linear-gradient(90deg, {metric['color']} 40%, white 40%)",
                "height": "120px"
            }
        )
    else:
        return dmc.Paper(
            children=[
                dmc.Group([
                    dmc.Stack([
                        dmc.ThemeIcon(
                            DashIconify(icon=metric["icon"], width=24),
                            size="xl",
                            color="white"
                        ),
                        dmc.Text(metric["name"], size="sm", fw=600, c="white")
                    ], gap="sm", align="center"),
                    dmc.Paper([
                        dmc.Center([
                            dmc.Text(metric["value"], size="xl", fw=900, c=metric["color"])
                        ])
                    ], p="md", style={"backgroundColor": "white", "borderRadius": "8px", "minWidth": "120px"})
                ], align="center", gap="md")
            ],
            p="md",
            radius="lg",
            style={
                "background": f"linear-gradient(90deg, {metric['color']} 40%, white 40%)",
                "height": "120px"
            }
        )

# Tab 7: Outlined Hover Cards
def create_outlined_card(metric):
    if metric["type"] == 1:
        return dmc.Paper(
            children=[
                dmc.Stack([
                    dmc.Group([
                        dmc.Text(metric["name"], size="md", fw=600, c=metric["color"]),
                        dmc.ThemeIcon(
                            DashIconify(icon=metric["icon"], width=20),
                            variant="outline",
                            color=metric["color"]
                        )
                    ], justify="space-between"),
                    dmc.Divider(color=metric["color"]),
                    dmc.Group([
                        dmc.Stack([
                            dmc.Text(metric["count"], size="xl", fw=700),
                            dmc.Text("Policies", size="sm", c="dimmed")
                        ], gap="xs", align="center"),
                        dmc.Stack([
                            dmc.Text(metric["premium"], size="lg", fw=600),
                            dmc.Text("Premium", size="sm", c="dimmed")
                        ], gap="xs", align="center")
                    ], justify="space-around")
                ], gap="md")
            ],
            p="lg",
            radius="md",
            style={
                "border": f"2px solid {metric['color']}",
                "height": "150px",
                "transition": "all 0.3s ease",
            },
            className="hover-card"
        )
    else:
        return dmc.Paper(
            children=[
                dmc.Stack([
                    dmc.Group([
                        dmc.Text(metric["name"], size="md", fw=600, c=metric["color"]),
                        dmc.ThemeIcon(
                            DashIconify(icon=metric["icon"], width=20),
                            variant="outline",
                            color=metric["color"]
                        )
                    ], justify="space-between"),
                    dmc.Divider(color=metric["color"]),
                    dmc.Center([
                        dmc.Text(metric["value"], size="xxl", fw=900, c=metric["color"])
                    ])
                ], gap="md")
            ],
            p="lg",
            radius="md",
            style={
                "border": f"2px solid {metric['color']}",
                "height": "150px",
                "transition": "all 0.3s ease",
            },
            className="hover-card"
        )

# Tab 8: Compact Dashboard Cards
def create_compact_card(metric):
    if metric["type"] == 1:
        return dmc.Card(
            children=[
                dmc.Stack([
                    dmc.Group([
                        dmc.Stack([
                            dmc.Text(metric["name"], size="xs", c="dimmed", tt="uppercase"),
                            dmc.Text(metric["count"], size="lg", fw=700, c=metric["color"])
                        ], gap="xs"),
                        dmc.Avatar(
                            DashIconify(icon=metric["icon"], width=18),
                            color=metric["color"],
                            variant="light",
                            size="md"
                        )
                    ], justify="space-between", align="flex-start"),
                    dmc.Text(metric["premium"], size="sm", fw=600, c="dark")
                ], gap="sm")
            ],
            withBorder=True,
            p="md",
            radius="sm",
            style={"height": "100px", "backgroundColor": "#fafafa"}
        )
    else:
        return dmc.Card(
            children=[
                dmc.Group([
                    dmc.Stack([
                        dmc.Text(metric["name"], size="xs", c="dimmed", tt="uppercase"),
                        dmc.Text(metric["value"], size="xl", fw=700, c=metric["color"])
                    ], gap="xs"),
                    dmc.Avatar(
                        DashIconify(icon=metric["icon"], width=18),
                        color=metric["color"],
                        variant="light",
                        size="md"
                    )
                ], justify="space-between", align="center")
            ],
            withBorder=True,
            p="md",
            radius="sm",
            style={"height": "100px", "backgroundColor": "#fafafa"}
        )

# Tab 9: Layered Cards
def create_layered_card(metric):
    if metric["type"] == 1:
        return dmc.Stack([
            dmc.Paper(
                children=[
                    dmc.Group([
                        dmc.Text(metric["name"], size="md", fw=600),
                        DashIconify(icon=metric["icon"], width=24, color=metric["color"])
                    ], justify="space-between")
                ],
                p="md",
                radius="lg",
                style={
                    "backgroundColor": metric["color"],
                    "color": "white",
                    "marginBottom": "-10px",
                    "zIndex": 2,
                    "position": "relative"
                }
            ),
            dmc.Paper(
                children=[
                    dmc.Stack([
                        dmc.Space(h="lg"),
                        dmc.SimpleGrid([
                            dmc.Stack([
                                dmc.Text(metric["count"], size="xl", fw=700, ta="center"),
                                dmc.Text("Total Policies", size="xs", c="dimmed", ta="center")
                            ], gap="xs"),
                            dmc.Stack([
                                dmc.Text(metric["premium"], size="lg", fw=600, ta="center"),
                                dmc.Text("Premium Value", size="xs", c="dimmed", ta="center")
                            ], gap="xs")
                        ], cols=2)
                    ], gap="sm")
                ],
                p="lg",
                pt="xl",
                radius="lg",
                withBorder=True,
                style={"backgroundColor": "white", "height": "120px"}
            )
        ], gap=0)
    else:
        return dmc.Stack([
            dmc.Paper(
                children=[
                    dmc.Group([
                        dmc.Text(metric["name"], size="md", fw=600),
                        DashIconify(icon=metric["icon"], width=24, color="white")
                    ], justify="space-between")
                ],
                p="md",
                radius="lg",
                style={
                    "backgroundColor": metric["color"],
                    "color": "white",
                    "marginBottom": "-10px",
                    "zIndex": 2,
                    "position": "relative"
                }
            ),
            dmc.Paper(
                children=[
                    dmc.Stack([
                        dmc.Space(h="lg"),
                        dmc.Center([
                            dmc.Text(metric["value"], size="xxl", fw=900, c=metric["color"])
                        ])
                    ], gap="sm")
                ],
                p="lg",
                pt="xl",
                radius="lg",
                withBorder=True,
                style={"backgroundColor": "white", "height": "120px"}
            )
        ], gap=0)

# Tab 10: Advanced Interactive Cards
def create_advanced_card(metric):
    if metric["type"] == 1:
        return dmc.Paper(
            children=[
                dmc.Stack([
                    dmc.Group([
                        dmc.Avatar(
                            DashIconify(icon=metric["icon"], width=20),
                            size="lg",
                            radius="xl",
                            color=metric["color"],
                            variant="filled"
                        ),
                        dmc.Stack([
                            dmc.Text(metric["name"], size="sm", fw=600),
                            dmc.Progress(value=75, color=metric["color"], size="xs")
                        ], gap="xs")
                    ], gap="md"),
                    dmc.Grid([
                        dmc.GridCol([
                            dmc.Paper([
                                dmc.Stack([
                                    dmc.Text(metric["count"], size="lg", fw=700, c=metric["color"], ta="center"),
                                    dmc.Text("Policies", size="xs", c="dimmed", ta="center")
                                ], gap="xs")
                            ], p="sm", radius="md", style={"backgroundColor": "#f8f9fa"})
                        ], span=6),
                        dmc.GridCol([
                            dmc.Paper([
                                dmc.Stack([
                                    dmc.Text(metric["premium"], size="md", fw=600, c=metric["color"], ta="center"),
                                    dmc.Text("Premium", size="xs", c="dimmed", ta="center")
                                ], gap="xs")
                            ], p="sm", radius="md", style={"backgroundColor": "#f8f9fa"})
                        ], span=6)
                    ])
                ], gap="md")
            ],
            p="lg",
            radius="xl",
            withBorder=True,
            shadow="md",
            style={"height": "160px", "transition": "all 0.3s ease"}
        )
    else:
        return dmc.Paper(
            children=[
                dmc.Stack([
                    dmc.Group([
                        dmc.Avatar(
                            DashIconify(icon=metric["icon"], width=20),
                            size="lg",
                            radius="xl",
                            color=metric["color"],
                            variant="filled"
                        ),
                        dmc.Stack([
                            dmc.Text(metric["name"], size="sm", fw=600),
                            dmc.Progress(value=85, color=metric["color"], size="xs")
                        ], gap="xs")
                    ], gap="md"),
                    dmc.Center([
                        dmc.Text(metric["value"], size="xxl", fw=900, c=metric["color"])
                    ])
                ], gap="lg")
            ],
            p="lg",
            radius="xl",
            withBorder=True,
            shadow="md",
            style={"height": "160px", "transition": "all 0.3s ease"}
        )

# Define card creation functions for each tab
card_creators = [
    create_sleek_card,
    create_glass_card,
    create_neuro_card,
    create_minimal_card,
    create_floating_card,
    create_split_card,
    create_outlined_card,
    create_compact_card,
    create_layered_card,
    create_advanced_card
]

tab_names = [
    "Sleek Gradients",
    "Glass Morphism",
    "Neumorphism",
    "Minimal Lines",
    "Floating Cards",
    "Split Design",
    "Outlined Hover",
    "Compact Dashboard",
    "Layered Cards",
    "Advanced Interactive"
]

def calculate_grid_cols(num_metrics):
    if num_metrics <= 4:
        return {"base": 1, "sm": 2, "md": 2, "lg": 4}
    elif num_metrics <= 6:
        return {"base": 1, "sm": 2, "md": 3, "lg": 3}
    elif num_metrics <= 8:
        return {"base": 1, "sm": 2, "md": 3, "lg": 4}
    else:
        return {"base": 1, "sm": 2, "md": 3, "lg": 5}

# Create tab content
def create_tab_content(tab_index):
    metrics = tab_metrics_data[tab_index]
    card_creator = card_creators[tab_index]
    cols = calculate_grid_cols(len(metrics))
    
    return dmc.Container([
        dmc.Stack([
            dmc.Title(f"{tab_names[tab_index]} - {len(metrics)} Metrics", order=3, ta="center"),
            dmc.Text(f"Showcasing {len(metrics)} business metrics with {tab_names[tab_index].lower()} design", 
                    size="md", c="dimmed", ta="center"),
            dmc.Space(h="lg"),
            dmc.SimpleGrid(
                cols=cols,
                spacing="lg",
                children=[card_creator(metric) for metric in metrics]
            )
        ], gap="xl")
    ], size="xl", p="md")

# Create the app layout
app.layout = dmc.MantineProvider(
    children=[
        dmc.Container([
            dmc.Stack([
                dmc.Center([
                    dmc.Title("Enhanced Business Metrics Dashboard", order=1, c="blue")
                ]),
                dmc.Center([
                    dmc.Text("10 Unique Design Styles • Dynamic Layouts • Type 1 & Type 2 Metrics", 
                            size="lg", c="dimmed")
                ]),
                dmc.Space(h="xl"),
                
                # Custom CSS for hover effects
                #html.Style({
                #    "dangerouslySetInnerHTML": {
                #        "__html": """
                #            .hover-card:hover {
                #                transform: translateY(-5px) !important;
                #                box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04) !important;
                #            }
                #            
                #            .mantine-Tabs-tab[data-active] {
                #                background: linear-gradient(45deg, #228be6, #74c0fc) !important;
                #                color: white !important;
                #            }
                #            
                #            .floating-card:hover {
                #                transform: translateY(-10px) !important;
                #                box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25) !important;
                #            }
                #        """
                #    }
                #}),
                
                dmc.Tabs([
                    dmc.TabsList([
                        dmc.TabsTab(tab_names[i], value=f"tab-{i}")
                        for i in range(10)
                    ], grow=True, variant="outline"),
                    
                    *[dmc.TabsPanel(
                        create_tab_content(i),
                        value=f"tab-{i}"
                    ) for i in range(10)]
                    
                ], value="tab-0", orientation="horizontal", variant="outline"),
                
                dmc.Space(h="xl"),
                dmc.Divider(),
                dmc.Space(h="md"),
                
                # Footer with metrics summary
                dmc.Group([
                    dmc.Paper([
                        dmc.Stack([
                            dmc.Text("Dashboard Summary", size="sm", fw=600, c="blue"),
                            dmc.Text(f"Total Metrics: {sum(len(tab_data) for tab_data in tab_metrics_data)}", size="xs"),
                            dmc.Text(f"Design Variations: {len(tab_names)}", size="xs"),
                            dmc.Text("Responsive Grid Layouts", size="xs")
                        ], gap="xs")
                    ], p="md", withBorder=True, radius="md"),
                    
                    dmc.Paper([
                        dmc.Stack([
                            dmc.Text("Metric Types", size="sm", fw=600, c="green"),
                            dmc.Text("Type 1: Dual Values (Policies + Premium)", size="xs"),
                            dmc.Text("Type 2: Single Values (Percentages/Text)", size="xs"),
                            dmc.Text("Dynamic Content Generation", size="xs")
                        ], gap="xs")
                    ], p="md", withBorder=True, radius="md"),
                    
                    dmc.Paper([
                        dmc.Stack([
                            dmc.Text("Features", size="sm", fw=600, c="orange"),
                            dmc.Text("• Responsive Design", size="xs"),
                            dmc.Text("• Interactive Elements", size="xs"),
                            dmc.Text("• Modern Aesthetics", size="xs"),
                            dmc.Text("• Optimized Layouts", size="xs")
                        ], gap="xs")
                    ], p="md", withBorder=True, radius="md")
                ], justify="space-around", align="flex-start")
                
            ], gap="md")
        ], size="xl", p="md")
    ]
)

if __name__ == "__main__":
    app.run(debug=True)