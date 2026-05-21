# letsplot-ggprism

A GraphPad Prism theme and palette package for Python's [Lets-Plot](https://lets-plot.org/) library.

This package is a port of the popular R package [ggprism](https://github.com/csdaw/ggprism) by csdaw, making it easy to replicate the visual aesthetic of GraphPad Prism graphs using python's `lets-plot`.

---

## Installation

You can install `letsplot-ggprism` directly from GitHub using `pip` or `uv`:

=== "pip"
    ```bash
    pip install git+https://github.com/xpf10/-letsplot-ggprism.git
    ```

=== "uv"
    ```bash
    uv add git+https://github.com/xpf10/-letsplot-ggprism.git
    ```

---

## Quickstart

Here is a quick example of how to style a plot using `letsplot-ggprism`:

```python
from lets_plot import *
from letsplot_ggprism import theme_prism, scale_color_prism, scale_shape_prism

LetsPlot.setup_html()

# Sample data
data = {
    "x": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    "y": [2, 3.5, 4, 4.5, 5, 1.5, 3, 3.8, 4.2, 4.8],
    "group": ["A", "A", "A", "A", "A", "B", "B", "B", "B", "B"]
}

# Construct plot
plot = (
    ggplot(data, aes(x="x", y="y", color="group", shape="group"))
    + geom_point(size=4)
    + geom_line(size=1)
    + scale_color_prism(palette="flames")
    + scale_shape_prism(palette="default")
    + theme_prism(palette="flames", base_size=12, border=True)
    + ggtitle("GraphPad Prism Style Plot in Lets-Plot")
)

# Render or save
ggsave(plot, "my_prism_plot.html")
```

---

## Features

* **`theme_prism()`**: Easy-to-use Lets-Plot theme that mirrors GraphPad Prism style (thick axes, bold text, custom font styling, and optional panel borders).
* **`scale_color_prism()` / `scale_fill_prism()`**: Discrete color/fill scales using all 20+ Prism-specific palettes (e.g. `colors`, `flames`, `candy_bright`, `evergreen`, `prism_light`, etc.).
* **`scale_shape_prism()`**: Point shape scales based on the Prism shape palettes (`default`, `filled`, `complete`).

---

## Visual Gallery

Here is what these themes and color scales look like:

### 1. Default Colors (No Border)
![Default Colors](images/colors_sample.png)

### 2. Flames Theme & Scale (With Border)
![Flames](images/flames_sample.png)

### 3. Prism Dark Theme & Scale (No Border)
![Prism Dark](images/prism_dark_sample.png)

