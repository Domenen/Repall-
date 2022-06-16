

class HTML:

    def __init__(self):
        self.output = "index.html"
        self.children = []
    
    def __iadd__(self, other):
        self.children.append(other)
        return self

    def __enter__(self):
        return self
    
    def __exit__(self, *args, **kwargs):
        if self.output is not None:
            with open(self.output, "w") as fp:
                fp.write(str(self))
        else:
            print(self)

    def __str__(self):
        html = "<html>\n"
        for child in self.children:
            html += str(child)
        html += "\n</html>"
        return html

class TopLevelTag:

    def __init__(self, tag):
        self.tag = tag
        self.children = []
    
    def __iadd__(self, other):
        self.children.append(other)
        return self

    def __enter__(self):
        return self
    
    def __exit__(self, *args, **kwargs):
        return self

    def __str__(self):
        if self.tag == "head":    
            html = "<%s>\n" % self.tag
            for child in self.children:
                html += str(child)
            html += "</%s>\n" % self.tag
        else: 
            html = "<%s>\n" % self.tag
            for child in self.children:
                html += str(child)
            html += "</%s>" % self.tag
        return html

class Tag:

    def __init__(self, tag, single = False):
        self.children = []
        self.tag = tag
        self.text = ""
        self.atr = ""
        self.single = single

    def __iadd__(self, other):
        self.children.append(other)
        return self

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        return self

    def __str__(self):
#                                                   ОДИНОЧНЫЕ ТЭГИ
        if self.single == True:
            if len(self.atr) > 0:
                html = "\n<{tag} {atr}>\n".format(tag = self.tag, atr = self.atr)
                for child in self.children:
                    html += str(child)    
            else:
                html = "\n<%s>\n" % self.tag
                for child in self.children:
                    html += str(child)
#                                                       ПАРНЫЕ ТЭГИ                                      
        else:
            if len(self.atr) > 0:                     
                html = "<{tag} {atr}>".format(tag = self.tag, atr = self.atr)
                if len(self.text) > 0:
                    html += self.text
                for child in self.children:
                    html += str(child)
                html += "</%s>\n" % self.tag
            else:
                html = "<%s>" % self.tag
                if len(self.text) > 0:
                    html += self.text
                for child in self.children:
                    html += str(child)
                html += "</%s>\n" % self.tag
        return html

def main():

    with HTML() as doc:
        with TopLevelTag("head") as head:
            with Tag("title") as title:
                title.text = "title"
                head += title
            doc += head
        
        with TopLevelTag("body") as body:
            with Tag("h1") as h1:
                h1.atr = "class='main-text'"
                h1.text = "test"
                body += h1
            with Tag("div") as div:
                div.atr = "class='container container-fluid' id='lead'"
                with Tag("img", single = True) as img:
                    img.atr = "src='/icon.png' data-image='responsive'"
                    div += img
                with Tag("p") as p:
                    p.text = "texttexttexttexttexttext"
                    div += p
                body += div
            doc += body


if __name__ == "__main__":
    main()