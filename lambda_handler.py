import sys
import numpy
import pandas as pd
import json

def handler(event, context):

    query_params = event.get("queryStringParameters", {})
    input = float(query_params.get("input", 0))

    # Return the result as JSON
    return {
        "statusCode": 200,
        "body": json.dumps({"hello": str(input), "numpy version": str(numpy.__version__), "pandas version": str(pandas__version__)}),
    }
