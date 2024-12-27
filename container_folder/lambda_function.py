import sys
import numpy as np
import pandas as pd
import json

def handler(event, context):

    query_params = event.get("queryStringParameters", {})
    input = query_params.get("input", "world")

    # Return the result as JSON
    return {
        "statusCode": 200,
        "body": json.dumps({"hello": str(input), "numpy version": str(np.__version__), "pandas version": str(pd.__version__)})
    }
