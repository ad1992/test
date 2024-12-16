from prophecy.cb.server.base.ComponentBuilderBase import *
from pyspark.sql import *
from pyspark.sql.functions import *

from prophecy.cb.server.base import WorkflowContext
from prophecy.cb.server.base.datatypes import SInt, SString
from prophecy.cb.ui.uispec import *


class CustomReformatBitbucket(ComponentSpec):
    name: str = "CustomReformatBitbucket"
    category: str = "NewBitbucketCategory"

    def optimizeCode(self) -> bool:
        # Return whether code optimization is enabled for this component
        return True

    @dataclass(frozen=True)
    class CustomReformatBitbucketProperties(ComponentProperties):
        # properties for the component with default values
        my_property: SString = SString("default value of my property")

    def dialog(self) -> Dialog:
        # Define the UI dialog structure for the component
        return Dialog("CustomReformatBitbucket")

    def validate(self, context: WorkflowContext, component: Component[CustomReformatBitbucketProperties]) -> List[Diagnostic]:
        # Validate the component's state
        return []

    def onChange(self, context: WorkflowContext, oldState: Component[CustomReformatBitbucketProperties], newState: Component[CustomReformatBitbucketProperties]) -> Component[
    CustomReformatBitbucketProperties]:
        # Handle changes in the component's state and return the new state
        return newState


    class CustomReformatBitbucketCode(ComponentCode):
        def __init__(self, newProps):
            self.props: CustomReformatBitbucket.CustomReformatBitbucketProperties = newProps

        def apply(self, spark: SparkSession, in0: DataFrame) -> DataFrame:
            # This method contains logic used to generate the spark code from the given inputs.
            return in0
