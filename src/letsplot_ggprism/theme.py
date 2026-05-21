from lets_plot import theme, element_line, element_rect, element_text, element_blank
from .palettes import THEME_PALETTES

def theme_prism(
    palette="black_and_white",
    base_size=14,
    base_family="sans",
    base_fontface="bold",
    border=False
):
    """
    A collection of themes that mirror the color schemes available in GraphPad Prism.

    Parameters
    ----------
    palette : str, default="black_and_white"
        Palette name. Use `list(THEME_PALETTES.keys())` to show all valid names.
    base_size : int or float, default=14
        Base font size, in points.
    base_family : str, default="sans"
        Base font family.
    base_fontface : str, default="bold"
        Base font face. One of: "plain", "bold", "italic", "bold_italic".
    border : bool, default=False
        Should a border be drawn around the plot?
    
    Returns
    -------
    FeatureSpec
        A lets-plot theme object.
    """
    if palette not in THEME_PALETTES:
        raise ValueError(
            f"The palette '{palette}' does not exist. "
            f"Valid palette names: {list(THEME_PALETTES.keys())}"
        )
    
    colours = THEME_PALETTES[palette]
    
    base_line_size = base_size / 14.0
    base_rect_size = base_size / 14.0
    
    # Border vs line options
    if border:
        panel_border = element_rect(fill=None, color=colours.get("axisColor", "#000000"), size=base_rect_size)
        axis_line = element_blank()
    else:
        panel_border = element_blank()
        axis_line = element_line(color=colours.get("axisColor", "#000000"), size=base_line_size)

    # Panel background
    if palette == "office":
        panel_background = element_rect(fill=colours.get("plottingAreaColor", "#FFFFFF"), color=None)
    else:
        panel_background = element_blank()

    t = theme(
        # Base lines and rects defaults
        line=element_line(color=colours.get("axisColor", "#000000"), size=base_line_size),
        rect=element_rect(color=colours.get("axisColor", "#000000"), size=base_rect_size, fill="white"),
        text=element_text(
            family=base_family,
            face=base_fontface,
            color=colours.get("graphTitleColor", "#000000"),
            size=base_size
        ),
        
        # Axis lines and ticks
        axis_line=axis_line,
        axis_line_x=None,
        axis_line_y=None,
        axis_text=element_text(color=colours.get("axisLabelColor", "#000000"), size=base_size * 0.95),
        axis_title=element_text(color=colours.get("axisTitleColor", "#000000")),
        
        # Legend settings
        legend_background=element_blank(),
        legend_key=element_blank(),
        legend_title=element_blank(),
        legend_text=element_text(size=base_size * 0.8, face="plain"),
        
        # Grid settings
        panel_background=panel_background,
        panel_border=panel_border,
        panel_grid=element_blank(),
        panel_grid_major=element_blank(),
        panel_grid_minor=element_blank(),
        
        # Strip settings
        strip_background=element_blank(),
        strip_text=element_text(color=colours.get("axisTitleColor", "#000000"), size=base_size * 0.8),
        
        # Plot background and titles
        plot_background=element_rect(fill=colours.get("pageBackgroundColor", "#FFFFFF"), color=None),
        plot_title=element_text(size=base_size * 1.2, face=base_fontface),
        plot_subtitle=element_text(size=base_size, face=base_fontface),
        plot_caption=element_text(size=base_size * 0.8, face="plain")
    )
    
    return t
