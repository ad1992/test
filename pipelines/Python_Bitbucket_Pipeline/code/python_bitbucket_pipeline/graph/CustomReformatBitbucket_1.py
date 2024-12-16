from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from python_bitbucket_pipeline.config.ConfigStore import *
from python_bitbucket_pipeline.udfs.UDFs import *

def CustomReformatBitbucket_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    from typing import Optional, List, Dict
    from dataclasses import dataclass, field
    from abc import ABC
    
    from pyspark.sql.column import Column
    from pyspark.sql.functions import col
    from dataclasses import dataclass
    from typing import Optional, List, Dict
    from pyspark.sql.column import Column as sparkColumn


    @dataclass(frozen = True)
    class SColumn:
        expression: Optional[Column] = None

        @staticmethod
        def getSColumn(column: str):
            return SColumn(col(column))

        def column(self) -> sparkColumn:
            return self.expression

        def columnName(self) -> str:
            return self.expression._jc.toString()


    @dataclass(frozen = True)
    class SColumnExpression:
        target: str
        expression: SColumn
        description: str
        _row_id: Optional[str] = None

        @staticmethod
        def remove_backticks(s):
            if s.startswith("`") and s.endswith("`"):
                return s[1:- 1]
            else:
                return s

        @staticmethod
        def getColumnExpression(column: str):
            return SColumnExpression(column, SColumn.getSColumn(col(column)), "")

        @staticmethod
        def getColumnsFromColumnExpressionList(columnExpressions: list):
            columnList = []

            for expression in columnExpressions:
                columnList.append(expression.expression)

            return columnList

        def column(self) -> Column:

            if (self.expression.columnName() == SColumnExpression.remove_backticks(self.target)):
                return self.expression.expression

            return self.expression.expression.alias(self.target)


    @dataclass(frozen = True)
    class ReformatProperties():
        columnsSelector: List[str] = field(default_factory = list)
        expressions: List[SColumnExpression] = field(default_factory = list)
        activeTab: str = "expressions"
        importLanguage: str = "${$.workflow.metainfo.frontEndLanguage}"
        importString: str = ""

    props = ReformatProperties(  #skiptraversal
        columnsSelector = [], 
        expressions = [], 
        activeTab = "expressions", 
        importLanguage = "${$.workflow.metainfo.frontEndLanguage}", 
        importString = ""
    )
    in0 = in0

    if len(props.expressions) > 0:
        selectColumns = map(lambda x: x.column(), props.expressions)

        return in0.select(*selectColumns)
    else:
        return in0
