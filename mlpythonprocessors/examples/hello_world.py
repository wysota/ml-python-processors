from mountainlab_pytools.mlprocessors.core import Processor, StringParameter, BoolParameter
from mountainlab_pytools.mlprocessors.core import Input, Output, StreamInput, StreamOutput
from mountainlab_pytools.mlprocessors.registry import registry, register_processor


@register_processor(registry)
class Empty(Processor):
    """
	This processor does nothing.
    """
    pass

class HelloWorld(Processor):
    """
        This processor prints 'Hello world!'
    """
    def run(self):
        print("Hello world!")


class HelloPerson(Processor):
    """
        Processor accepts an optional 'person' parameter
        and prints 'Hello' followed by the value of the parameter
    """

    person = StringParameter(optional=True, default='stranger')

    def run(self):
        print("Hello %s!" % self.person)

class HelloPersonWithOutput(Processor):
    """
        This processor is similar to HelloPerson but is able to
        output to a file.
    """

    person = StringParameter('person name')
    output = Output(optional=True)

    def run(self):
        s = 'Hello %s!\n' % self.person

        # if output file path was given, save output to file
        if self.output:
            with open(self.output, 'w') as f:
                f.write(s)
        # otherwise print to stdout
        else:
            print(s)

colors = (
            ('red',     '\x1b[31m'),
            ('green',   '\x1b[32m'),
            ('yellow',  '\x1b[33m'),
            ('blue',    '\x1b[34m'),
            ('magenta', '\x1b[35m'),
)

class TransformProcessor(Processor):
    input = StreamInput('input file', mode = 'r')
    output = StreamOutput('output file', mode = 'w')

class Colorize(TransformProcessor):
    """
        Wraps input in ANSI color tags
    """
#    input = StreamInput('input file')
#    output = StreamOutput('output file')
    color = StringParameter('color to apply to text', choices=colors)

    reset = '\x1b[0m'

    def run(self):
        text = self.color+self.input.read()+self.reset
        self.output.write(text)

class Replace(TransformProcessor):
    """
        Replace substring 'search' with 'replace'
    """
    search = StringParameter('text to replace')
    replace = StringParameter('text to replace with (or empty to cut)', optional=True)
    g = BoolParameter('global replace', optional=True, default=False)

    def run(self):
        print("G:", self.search, self.replace, self.g)
        text = self.input.read()
        if self.g:
            text = text.replace(self.search, '' if not self.replace else self.replace)
        else:
            text = text.replace(self.search, '' if not self.replace else self.replace, 1)
        print("Result:", text)
        self.output.write(text)
