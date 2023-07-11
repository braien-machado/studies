# Using sprites

It's possible to gather multiple svg files into a single one. You encapsulate the svg tags with an outer svg tag, change the inner svg tags with `symbol` and add an `id` custom attribute and the attribute `xmlns="https://www.w3.org/2000/svg"` to each of them. An example would be:
```
sprites.svg

<svg>
  <symbol id="svg1" xmlns="https://www.w3.org/2000/svg" {...rest of svg attributes}>
    <path {...svg path attributes}>
  </symbol>
  <symbol id="svg2" xmlns="https://www.w3.org/2000/svg" {...rest of svg attributes}>
    <path {...svg path attributes}>
  </symbol>
</svg>
```
Then, you may use the SVGs wherever you need them with:
```
<svg>
  <use href={`path/to/sprites.svg#${svg_id}`} />
</svg>
```

This solution will reduce the number of requests for content when loading the page, reducing the *First Contentful Paint* and the *Speed Index* performance metrics.

> Tip: Using sprites, you may reduce the dependencies removing icon libraries if they give access to the svg files.
