# Scales Guide

`letsplot-ggprism` provides manual discrete mapping scales that match GraphPad Prism's exact palettes for colors, fills, and shapes.

---

## Color and Fill Scales

To color your points, lines, or box border elements:
```python
scale_color_prism(palette="colors", **kwargs)
scale_colour_prism(palette="colors", **kwargs)
```

To fill your bars, boxplots, or area elements:
```python
scale_fill_prism(palette="colors", **kwargs)
```

### Parameters

* **`palette`** (`str`, default `"colors"`): Name of the palette to use. See the [Palettes Gallery](palettes.md) for all available names.
* **`**kwargs`**: All additional parameters are forwarded directly to Lets-Plot's underlying manual mapping scales (`scale_color_manual` / `scale_fill_manual`), such as `name`, `labels`, `breaks`, `limits`, etc.

### Example

```python
ggplot(df, aes(x="x", y="y", fill="category")) + \
    geom_bar(stat="identity") + \
    scale_fill_prism(palette="candy_bright") + \
    theme_prism()
```

---

## Shape Scales

To map data categories to GraphPad Prism point shapes:
```python
scale_shape_prism(palette="default", **kwargs)
```

### Parameters

* **`palette`** (`str`, default `"default"`): One of:
    * `"default"`: standard Prism shapes (solid circles, squares, triangles, diamonds, plus, cross).
    * `"filled"`: filled shapes matching ggplot2 shape codes `21` to `25` (circle, square, up-triangle, down-triangle, diamond).
    * `"complete"`: combines all standard and filled shapes.
* **`**kwargs`**: All additional parameters are forwarded to Lets-Plot's `scale_shape_manual`.

### Example

```python
ggplot(df, aes(x="x", y="y", shape="group")) + \
    geom_point(size=4) + \
    scale_shape_prism(palette="filled") + \
    theme_prism()
```
