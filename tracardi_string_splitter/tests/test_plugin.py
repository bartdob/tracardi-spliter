from tracardi_plugin_sdk.service.plugin_runner import run_plugin
from tracardi_string_splitter.plugin import SplitterAction

init = dict(
    string='dev,sopp,dev',
    delimiter=',',
)

payload = {}

result = run_plugin(SplitterAction, init, payload)
print(result)