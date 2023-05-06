# MkDocs Material template page

Templates and Snippets for MKDocs

# Heading 1

## Heading 2

### Heading 3

This is some example text, just some words to see what's up with this documentation system, even some sp&cia/ chåräctérs @nd 0th3r ødîti€s!

The document can also contain some **bold** text, or some _italic_ text or some ~~strikethrough~~ text, or some super^script^ or some sub~script~ or some ==highlighted== text.

Additionally, block-quotes can be inserted:

> This is a blockquote containing some nonsence
>
> The blockquote can also contain multiple lines

Lists can also be generated, there are two types, Ordered Lists and Unordered lists

1. This is the first list item
2. Another item on the ordered list
   1. Nested ordered list
   2. another nested item
3. Third item in the list
   - unordered nested list
   - inside an ordered list

- This is the first unordered item
- The second item
  - Nested unordered lists
  - Another nested item
- The third unordered item
  1. Ordered lists inside of unordered lists
  2. And another ordered item

Next, we might want to add some code to the document. Adding some `inline code` is pretty easy. Alternatively, we can also make a typeless code-block:

```
  function codeblock(String content) {
    return content.html;
  }

  String text = "This is some test content";
  codeblock(text);
```

If we want our codeblock to be styled according to a certain coding language, with line highlighting:

``` py hl_lines="2 3"
text = "This is some test content"

def codeBlock(content):
  html = content.html
  return html

codeBlock(text)
```

Or another coding language, with title:

``` js title="codeBlock.js"
let text = "This is some test content"

function code_block(content) => {
  return content.html
}

code_block(text)
```

More information can be found in the [Code reference].

[Code reference]: https://squidfunk.github.io/mkdocs-material/reference/code-blocks/

We can divide some content using a horizontal rule:

---

(External) content can be [linked] to websites or other [pages] of the website.

[linked]: https://google.com
[pages]: second_page.md

Images and ![other graphics] get added in a similar way.

[other graphics]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Even some tooltip information can be displayed"

If a citation is needed, footnotes[^1] and other citations can be added.

[^1]: second_page.md

Call-outs can include side stories and other less important or extra content. More info can be found in the [Admonitions reference].

[Admonitions reference]: https://squidfunk.github.io/mkdocs-material/reference/admonitions/

!!! note

  This is a admonitium or call-out with the note style, this should be displayed as such.

These call-outs can also be made collapsible:

??? info

  This is a collapsed information call-out.

We can also expand this collapsible call-out normally:

???+ warning

  This is a collapsible warning call-out that is expanded by default.

Mathematical equations can be added using the MathJax extension. More information can be found in the [MathJax reference] and the [LaTex math reference].

Formulas like $y(x)=2a*bx$ can be added inline. Alternatively, mathematical equations can be added as a code block:

$$
  f = \sum^{i=0}_{n}x_i*n_i+b^{i+1} \\
  \frac{1}{2}*\sqrt(22a+16b^5)
$$

[MathJax reference]: https://squidfunk.github.io/mkdocs-material/reference/mathjax
[LaTex math reference]: https://en.wikibooks.org/wiki/LaTeX/Mathematics