-- Check vs yesterday as we dont know if the query will run before the data is generated
SELECT count(*) as count FROM foxsec_metrics.aws_route53_diffs WHERE day = cast((CURRENT_DATE - interval '1' day) as varchar)