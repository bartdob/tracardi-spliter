from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData, Form, FormGroup, FormField, FormComponent
from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.result import Result

from tracardi_string_splitter.model.configuration import Configuration


def validate(config: dict) -> Configuration:
    return Configuration(**config)


class SplitterAction(ActionRunner):

    def __init__(self, **kwargs):
        self.config = validate(kwargs)

    async def run(self, payload):
        dot = self._get_dot_accessor(payload)
        string = dot[self.config.string]
        result = string.split(self.config.delimiter)
        return Result(port="payload", value={"result": result})


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='tracardi_string_splitter.plugin',
            className='SplitterAction',
            inputs=["payload"],
            outputs=['payload'],
            version='0.6.0',
            license="MIT",
            author="Bartosz Dobrosielski",
            manual="string_splitter_action",
            init={
                "string": None,
                "delimiter": '.',
            },
            form=Form(groups=[
                FormGroup(
                    fields=[
                        FormField(
                            id="string",
                            name="String to split",
                            description="Type path to string or string itself. Default source is event. Change it if"
                                        " the data is elsewhere.",
                            component=FormComponent(type="dotPath", props={"defaultSourceValue": "event"})
                        ),
                        FormField(
                            id="delimiter",
                            name="Delimiter",
                            description="Type delimiter. It will be used to split the string into list of strings.",
                            component=FormComponent(type="text", props={"label": "delimiter"})
                        )
                    ]
                ),
            ]),

        ),
        metadata=MetaData(
            name='String splitter',
            desc='It divides string into list of strings on defined delimiter.',
            type='flowNode',
            width=200,
            height=100,
            icon='splitter',
            group=["Data processing"]
        )
    )
