class Tag:
    pass
class HTML:
    def __init__(self, tag, klass=None):
        self.tag = tag
        self.text = ""
        self.attributes = {}

        if klass is not None:
            self.attributes["class"] = " ".join(klass)

    def __str__(self):
        attrs = []
        for attribute, value in self.attributes.items():
            attrs.append('%s="%s"' % (attribute, value))
        attrs = " ".join(attrs)
        return "<{tag} {attrs}>\n{text}\n</{tag}>".format(
            tag=self.tag, attrs=attrs, text=self.text
        )
class TopLevelTag:
    pass

# if __name__ == "__main__":
with HTML(output = "html.html") as doc:
    with TopLevelTag("head") as head:
        with Tag("title") as title:
            title.text = "hello"
            head += title
        doc += head

    with TopLevelTag("body") as body:
        with Tag("h1", klass=("main-text",)) as h1:
            h1.text = "Test"
            body += h1

        with Tag("div", klass=("container", "container-fluid"), id="lead") as div:
            with Tag("p") as paragraph:
                paragraph.text = "another test"
                div += paragraph

            with Tag("img", is_single=True, src="/icon.png") as img:
                div += img

            body += div

        doc += body