from lets_plot import scale_color_manual, scale_fill_manual, scale_shape_manual
from .palettes import COLOUR_PALETTES, FILL_PALETTES, SHAPE_PALETTES

def scale_color_prism(palette="colors", **kwargs):
    """
    Discrete color scale that uses palettes mirroring the color schemes in GraphPad Prism.

    Parameters
    ----------
    palette : str, default="colors"
        Palette name. Use `list(COLOUR_PALETTES.keys())` to show all valid names.
    **kwargs
        Additional arguments passed to `scale_color_manual`.

    Returns
    -------
    FeatureSpec
        A lets-plot color scale object.
    """
    if palette not in COLOUR_PALETTES:
        raise ValueError(
            f"The color palette '{palette}' does not exist. "
            f"Valid color palette names: {list(COLOUR_PALETTES.keys())}"
        )
    return scale_color_manual(values=COLOUR_PALETTES[palette], **kwargs)

# Alias for scale_color_prism
scale_colour_prism = scale_color_prism

def scale_fill_prism(palette="colors", **kwargs):
    """
    Discrete fill scale that uses palettes mirroring the color schemes in GraphPad Prism.

    Parameters
    ----------
    palette : str, default="colors"
        Palette name. Use `list(FILL_PALETTES.keys())` to show all valid names.
    **kwargs
        Additional arguments passed to `scale_fill_manual`.

    Returns
    -------
    FeatureSpec
        A lets-plot fill scale object.
    """
    if palette not in FILL_PALETTES:
        raise ValueError(
            f"The fill palette '{palette}' does not exist. "
            f"Valid fill palette names: {list(FILL_PALETTES.keys())}"
        )
    return scale_fill_manual(values=FILL_PALETTES[palette], **kwargs)

def scale_shape_prism(palette="default", **kwargs):
    """
    Discrete shape scale that uses marker shape sequences mirroring GraphPad Prism.

    Parameters
    ----------
    palette : str, default="default"
        Palette name. One of: "default", "filled", "complete".
    **kwargs
        Additional arguments passed to `scale_shape_manual`.

    Returns
    -------
    FeatureSpec
        A lets-plot shape scale object.
    """
    if palette not in SHAPE_PALETTES:
        raise ValueError(
            f"The shape palette '{palette}' does not exist. "
            f"Valid shape palette names: {list(SHAPE_PALETTES.keys())}"
        )
    return scale_shape_manual(values=SHAPE_PALETTES[palette], **kwargs)
