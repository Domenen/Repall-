import sentry_sdk
sentry_sdk.init(
    dsn="https://68ec370847fb448b9786211e83622fa9@o1329153.ingest.sentry.io/6591050",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=0.7
)

division_by_zero = 1 / 0