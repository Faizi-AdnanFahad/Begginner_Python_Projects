class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = f"<{name}>"
        self.end_tag = f"</{name}>"
        self.contents = contents

    def __str__(self):
        return f"{self.start_tag}{self.contents}{self.end_tag}"

    def display(self, file=None):
        print(self, file=file)  # OR # self.__str__


class DocType(Tag):

    def __init__(self):
        # super() referring to the Tag class
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = ''   # DOCTYPE doesn't have end tag


class Head(Tag):

    def __init__(self, title=None):
        # super() referring to the Tag class
        super().__init__('Head', '')
        if title is not None:
            # creating a title inside our <head>....</head>, which will be our contents
            self.contents = str(Tag('title', title))


class Body(Tag):

    def __init__(self):
        # super() referring to the Tag class
        super().__init__("body", '')  # body contents will be built separately
        self._body_contents_list = []  # contains all information in the body of the loop, each index can be
                                                                                # <head>...</head>, ...

    def add_tag(self, name, contents):
        # adding new tag to the body such as: <p1>...<p1> and adding all of them to the list
        new_tag = Tag(name, contents)
        self._body_contents_list.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents_list:
            self.contents += str(tag)

        # super() referring to the Tag class
        super().display(file=file)


class HtmlDoc(object):
    # *******************DIFFERENCE EXISTS HERE****************************
    # *******************Composition 54-56****************************
    def __init__(self, title=None):
        # *Composition* - Line 59-61* but not inheritance because (no super() call )
        self._doc_type = DocType()
        self._head = Head(title)
        self._body = Body()

    def add_tag(self, name, contents):
        # using extra things such as <p1>...</p1>...
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print("<html>", file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print("</html>", file=file)


if __name__ == '__main__':
    my_page = HtmlDoc()  # "Hi" will appear inside  |<head><title>"Hi"</title></head>|
    my_page.add_tag("h1", "Main Heading")  # Inside body
    my_page.add_tag("h2", "sub-heading")   # Inside body
    my_page.add_tag("p", "This is a paragraph that will appear on the page ")  # Inside body
    my_page.display()

    # Below is used for creating a file to add it inside that file, in this case, named test.html
    # with open("test.html", 'w') as test_doc:
    #     my_page.display(file=test_doc)











