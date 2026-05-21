# Themes Guide

The primary function for styling your plots in the GraphPad Prism aesthetic is `theme_prism()`.

## Function Signature

```python
def theme_prism(
    palette="black_and_white",
    base_size=14,
    base_family="sans",
    base_fontface="bold",
    border=False
)
```

---

## Parameters

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `palette` | `str` | `"black_and_white"` | The color palette scheme to use for theme elements (like axes, text, backgrounds). |
| `base_size` | `int` or `float` | `14` | The base font size for the plot in points. |
| `base_family` | `str` | `"sans"` | Font family for text elements (e.g. `"sans"`, `"serif"`, `"mono"`). |
| `base_fontface` | `str` | `"bold"` | Base font style face. One of: `"plain"`, `"bold"`, `"italic"`, `"bold_italic"`. |
| `border` | `bool` | `False` | Whether to draw a complete border rectangle around the panel instead of just the x/y axes. |

---

## Examples

### 1. Default Prism Style
```python
p + theme_prism()
```
This applies the standard black and white Prism look with bold text and simple left/bottom axes.

### 2. Custom Font Size and Border
```python
p + theme_prism(base_size=12, border=True)
```
This shrinks the text to size 12 and draws a complete rectangular border outline around the plot panel.

### 3. Styled Palette (e.g. Flames)
```python
p + theme_prism(palette="flames")
```
This styles the axis lines and plot titles with the flame palette color scheme.
