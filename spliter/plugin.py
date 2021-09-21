from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.result import Result
from spliter.model.model import Spliter


class SpliterAction(ActionRunner):

    def __init__(self, **kwargs):
        self.spliter = Spliter(
            message=kwargs['message'],
            dot=kwargs['dot']
        )

    async def run(self, payload):
        if len(self.spliter.message)>2 and self.spliter.dot:
            print(self.spliter.dict())
            result = self.spliter.message.replace(self.spliter.dot, " ")

            return Result(port="payload", value={
                "body": result
            })
        else:
            raise ValueError("message is too short or none.")




def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='',
            className='',
            inputs=["payload"],
            outputs=['payload'],
            version='0.1',
            license="MIT",
            author="Bartosz Dobrosielski",
            init={
                "message": None,
                "dot": None,
            }

        ),
        metadata=MetaData(
            name='Spliter',
            desc='message spliter',
            type='flowNode',
            width=200,
            height=100,
            icon='',
            group=["Connectors"]
        )
    )
