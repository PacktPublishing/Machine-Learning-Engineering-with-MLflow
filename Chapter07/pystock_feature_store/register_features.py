# This is an example feature definition file

from google.protobuf.duration_pb2 import Duration

from feast import Entity, Feature, FeatureView, ValueType
from feast.data_source import FileSource
from feast.data_format import ParquetFormat

# Read data from parquet files. Parquet is convenient for local development mode. For
# production, you can use your favorite DWH, such as BigQuery. See Feast documentation
# for more info.
token_features = FileSource(
    path="./data/features.parquet",
    event_timestamp_column="create_date",
    created_timestamp_column="event_date",
)

driver = Entity(name="token", value_type=ValueType.STRING, description="token id",)

hourly_view_features_token = FeatureView(
    name="token_hourly_features",
    entities=["token"],
    ttl=Duration(seconds=3600 * 1),
    features=[
        Feature(name="prev_1days", dtype=ValueType.INT64),
        Feature(name="prev_2days", dtype=ValueType.INT64),
        Feature(name="prev_3days", dtype=ValueType.INT64),
        Feature(name="prev_4days", dtype=ValueType.INT64),
        Feature(name="prev_5days", dtype=ValueType.INT64),
        Feature(name="prev_6days", dtype=ValueType.INT64),
        Feature(name="prev_7days", dtype=ValueType.INT64),
        Feature(name="prev_8days", dtype=ValueType.INT64),
        Feature(name="prev_9days", dtype=ValueType.INT64),
        Feature(name="prev_10days", dtype=ValueType.INT64),
        Feature(name="prev_11days", dtype=ValueType.INT64),
        Feature(name="prev_12days", dtype=ValueType.INT64),
        Feature(name="prev_13days", dtype=ValueType.INT64)
    ],
    online=True,
    input=token_features,
    tags={},
)
