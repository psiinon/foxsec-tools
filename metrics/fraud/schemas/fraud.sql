CREATE EXTERNAL TABLE IF NOT EXISTS fraud (
  `category` STRING,
  `day` STRING,
  `field` STRING,
  `startts` INT,
  `value` INT
)
ROW FORMAT  serde 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://foxsec-metrics/fraud/fraud_json3';
