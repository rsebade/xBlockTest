"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Dict, Integer
from xblock.fragment import Fragment

from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('studioinput', 'static/html'))

class StudioInputXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    count = Integer(
        default=0, scope=Scope.user_state,
        help="A simple counter, to show something happening",
    )

    content = Dict(
        default={},
        scope=Scope.settings,
        help=u"List of items"
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the StudioInputXBlock, shown to students
        when viewing courses.
        """
        context = {
            'inputs': self.content,
        }

        frag = Fragment()
        template = env.get_template("studioinput.html")
        frag.add_content(template.render(**context))
        frag.add_css(self.resource_string("static/css/studioinput.css"))
        frag.add_javascript(self.resource_string("static/js/src/studioinput.js"))
        frag.initialize_js('StudioInputXBlock')
        return frag

    def studio_view(self, context=None):
        """Create a fragment used to display the edit view in the Studio."""

        context = {
            'inputs': self.content,
        }

        frag = Fragment()
        template = env.get_template('studioinput_edit.html')
        frag.add_content(template.render(**context))
        frag.add_css(self.resource_string("static/css/studioinput_edit.css"))
        frag.add_javascript(self.resource_string("static/js/src/studioinput_edit.js"))
        frag.initialize_js('StudioInputEditXBlock')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def studio_submit(self, data, suffix=''):
        """Called when submitting the form in Studio."""
        inputs = {}

        inputlist = data.get('inputs').items()
        inputlist.reverse()
        for item in inputlist:
            key , val = item
            inputs[key] = val  

        self.content = inputs

        return {'result':'success'}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("StudioInputXBlock",
             """<studioinput/>
             """),
            ("Multiple StudioInputXBlock",
             """<vertical_demo>
                <studioinput/>
                <studioinput/>
                <studioinput/>
                </vertical_demo>
             """),
        ]
