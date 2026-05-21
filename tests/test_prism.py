import pytest
from letsplot_ggprism import (
    theme_prism,
    scale_color_prism,
    scale_colour_prism,
    scale_fill_prism,
    scale_shape_prism,
    COLOUR_PALETTES,
    FILL_PALETTES,
    SHAPE_PALETTES,
    THEME_PALETTES,
)

def test_imports():
    assert len(COLOUR_PALETTES) > 0
    assert len(FILL_PALETTES) > 0
    assert len(SHAPE_PALETTES) > 0
    assert len(THEME_PALETTES) > 0

def test_theme_prism():
    # Test default
    t = theme_prism()
    assert t is not None
    
    # Test specific palette
    t2 = theme_prism(palette="flames", base_size=16, border=True)
    assert t2 is not None

    # Test invalid palette
    with pytest.raises(ValueError) as excinfo:
        theme_prism(palette="nonexistent_palette")
    assert "nonexistent_palette" in str(excinfo.value)

def test_scale_color_prism():
    # Test default
    s = scale_color_prism()
    assert s is not None

    # Test specific palette
    s2 = scale_colour_prism(palette="flames")
    assert s2 is not None

    # Test invalid palette
    with pytest.raises(ValueError) as excinfo:
        scale_color_prism(palette="nonexistent")
    assert "nonexistent" in str(excinfo.value)

def test_scale_fill_prism():
    # Test default
    s = scale_fill_prism()
    assert s is not None

    # Test specific palette
    s2 = scale_fill_prism(palette="candy_bright")
    assert s2 is not None

    # Test invalid palette
    with pytest.raises(ValueError) as excinfo:
        scale_fill_prism(palette="nonexistent")
    assert "nonexistent" in str(excinfo.value)

def test_scale_shape_prism():
    # Test default
    s = scale_shape_prism()
    assert s is not None

    # Test specific palette
    s2 = scale_shape_prism(palette="filled")
    assert s2 is not None

    # Test invalid palette
    with pytest.raises(ValueError) as excinfo:
        scale_shape_prism(palette="nonexistent")
    assert "nonexistent" in str(excinfo.value)
