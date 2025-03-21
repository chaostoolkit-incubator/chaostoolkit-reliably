# Changelog

## [Unreleased][]

[Unreleased]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.82.0...HEAD

## [0.82.0][]

[0.82.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.81.0...0.82.0

### Added

* Support passing proxy address to load test runner as an argument

### Removed

* don't upload to GH release, this isn't useful

## [0.81.0][]

[0.81.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.80.3...0.81.0

### Changed

* Read environ dict directly rather than via getenv
* bump dependencies

## [0.80.3][]

[0.80.3]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.80.2...0.80.3

* Log oha command line

## [0.80.2][]

[0.80.2]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.80.1...0.80.2

* Use a specific proxy environment variable to prevent mixing system proxy settings

## [0.80.1][]

[0.80.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.80.0...0.80.1

* Fix action version

## [0.80.0][]

[0.80.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.79.0...0.80.0

* Add proxy support to run_load_test

## [0.79.0][]

[0.79.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.78.0...0.79.0

* Bump dependencies

## [0.78.0][]

[0.78.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.77.0...0.78.0

### Changed

* Dropped Python 3.7
* Building for Python 3.12
* Bump dependencies
* Remove logzero dependency

## [0.77.0][]

[0.77.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.76.0...0.77.0

### Changed

* Adjust OpenAI calls to match new capabilities from the models

## [0.76.0][]

[0.76.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.75.0...0.76.0

### Changed

* Bump dependencies
* Cleanup GPT output for rendering

### Fixed

* Command line argument for `ruff`

## [0.75.0][]

[0.75.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.74.0...0.75.0

### Added

* The `verify_latency_percentile_from_load_test`  probeto perform a verification of a
  load test from `run_load_test`

## [0.74.0][]

[0.74.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.73.0...0.74.0

### Added

* The `run_load_test` action to perform a load test using the excellent [oha](https://github.com/hatoo/oha)

### Changed

* Bump dependencies

## [0.73.0][]

[0.73.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.72.1...0.73.0

### Added

* Execution URL to slack message if enabled

## [0.72.1][]

[0.72.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.72.0...0.72.1

### Fixed

* Iterate over all slack channels through pagination
* Exclude archived slack channels from capture

## [0.72.0][]

[0.72.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.71.1...0.72.0

### Changed

* Send execution log as we run not just at the end

## [0.71.1][]

[0.71.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.71.0...0.71.1

### Fixed

* Substitute variable for value

## [0.71.0][]

[0.71.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.70.0...0.71.0

### Added

* Setting execution state from experiment pauses so they can be manually resumed

## [0.70.0][]

[0.70.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.69.1...0.70.0

### Changed

* Setting OTLP as baggage as we don't know if we are in a span yet

## [0.69.1][]

[0.69.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.69.0...0.69.1

### Fixed

* Add missing leyword arguments

## [0.69.0][]

[0.69.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.68.8...0.69.0

### Added

* OTEL extension handler to add reliably attributes

## [0.68.8][]

[0.68.8]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.68.7...0.68.8

### Changed

* Pass experiment title to Honeycomb marker

## [0.68.7][]

[0.68.7]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.68.5...0.68.7

### Fixed

* Honeycomb API expects an integer not a float

## [0.68.5][]

[0.68.5]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.68.4...0.68.5

### Fixed

* Capture all the logs

## [0.68.4][]

[0.68.4]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.68.3...0.68.4

### Fixed

* Adding more debug statements

## [0.68.3][]

[0.68.3]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.68.2...0.68.3

### Fixed

* Adding debug to Honeycomb marker

## [0.68.2][]

[0.68.2]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.68.1...0.68.2

### Fixed

* Actually update Honeycomb marker

## [0.68.1][]

[0.68.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.68.0...0.68.1

### Fixed

* Function signatures in honeycomb vendor

## [0.68.0][]

[0.68.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.67.0...0.68.0

### Added

* Added vendor specific callbacks to perform vendor actions (such as setting
  markers for instance)

### Changed

* Bump dependencies

## [0.67.0][]

[0.67.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.66.0...0.67.0

### Changed

* Bump dependencies
* More logging in GitHub activity
* Give more time to finish locust process

## [0.66.0][]

[0.66.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.65.3...0.66.0

### Changed

* Capture any channels starting with pattern given with configuration value
  `reliably_capture_slack_channel_pattern`

## [0.65.3][]

[0.65.3]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.64.2...0.65.3

### Fixed

* Fix loop size change

## [0.65.2][]

[0.65.2]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.64.1...0.65.2

### Fixed

* Fix thread removal in slack capture

## [0.65.1][]

[0.65.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.64.0...0.65.1

### Fixed

* Fix thread removal in slack capture

## [0.64.0][]

[0.64.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.63.3...0.64.0

### Fixed

* Slack messages capture

### Changed

* Bump dependencies

## [0.63.3][]

[0.63.3]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.63.2...0.63.3

### Fixed

* Lookup control in global controls too

## [0.63.2][]

[0.63.2]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.63.1...0.63.2

### Fixed

* Fix signature call

## [0.63.1][]

[0.63.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.63.0...0.63.1

### Fixed

* Prevent circular imports

## [0.63.0][]

[0.63.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.62.1...0.63.0

### Added

* Captures from third-parties

### Changed

* Bump dependencies

## [0.62.1][]

[0.62.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.62.0...0.62.1

### Fixed

* Catch missing instrumentation case

## [0.62.0][]

[0.62.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.61.8...0.62.0

### Added

* Allowing the log to start earlier by the CLI

### Changed

* Bump dependencies

## [0.61.8][]

[0.61.8]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.61.7...0.61.8

### Added

* Loading context from trace

## [0.61.7][]

[0.61.7]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.61.6...0.61.7

### Added

* Passing fixed OLTP context to children calls

## [0.61.6][]

[0.61.6]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.61.5...0.61.6

### Fixed

* Propagate OTEL env into locust file

## [0.61.5][]

[0.61.5]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.61.4...0.61.5

### Fixed

* Package name in locust file

## [0.61.4][]

[0.61.4]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.61.3...0.61.4

### Added

* More logging around OLTP in Locust file

## [0.61.3][]

[0.61.3]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.61.2...0.61.3

### Fixed

* Initialize OLTP as early as we can

## [0.61.2][]

[0.61.2]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.61.1...0.61.2

### Fixed

* Bind to locust init event

## [0.61.1][]

[0.61.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.61.0...0.61.1

### Fixed

* Environment values can only be strings

## [0.61.0][]

[0.61.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.60.0...0.61.0

### Added

* OLTP support in the load test

## [0.60.0][]

[0.60.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.59.0...0.60.0

### Changed

* Do not trace requests made back to Reliably to avoid polluting user
  traces

## [0.59.0][]

[0.59.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.55.0...0.59.0

### Changed

* Bump dependencies

## [0.55.0][]

[0.55.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.54.2...0.55.0

### Added

* A metrics control so we register the following info:
  - time when a probe (hypothesis) changes its state
  - time when it changes back again (showing recovery)

### Changed

* Bump dependencies

## [0.54.2][]

[0.54.2]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.54.1...0.54.2

### Changed

* Bump dependencies

## [0.54.1][]

[0.54.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.54.0...0.54.1

### Changed

* Bump dependencies

## [0.54.0][]

[0.54.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.53.0...0.54.0

### Changed

* Switching to `pdm_backend` to build package
* Added `chaosreliably.activities.tls.verifiy_certificate` as a more succint
  probe
* Bump dependencies

## [0.53.0][]

[0.53.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.52.0...0.53.0

### Changed

* Read `RELIABLY_VERIFY_TLS` and `RELIABLY_USE_HTTP` from env when not set in
  the configuration block

## [0.52.0][]

[0.52.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.51.0...0.52.0

### Changed

* Ensure tolerance and probes cast to int when value was read from
  environment variables

## [0.51.0][]

[0.51.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.50.7...0.51.0

### Added

* DNS probes and tolerances
* Small backoff before talking with OpenAI

## [0.50.7][]

[0.50.7]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.50.6...0.50.7

### Added

* event to exit openai loop

## [0.50.6][]

[0.50.6]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.50.5...0.50.6

### Changed

* add logging

## [0.50.5][]

[0.50.5]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.50.4...0.50.5

### Changed

* revert tls serial to string

## [0.50.4][]

[0.50.4]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.50.3...0.50.4

### Added

* serializeing using default json when orjson barfs on large integers

## [0.50.3][]

[0.50.3]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.50.2...0.50.3

## [0.50.3][]

### Added

* logging when failing to serialize to json

[0.50.2]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.50.1...0.50.2

### Added

* Missing fields on aborted executions

## [0.50.1][]

[0.50.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.50.0...0.50.1

### Added

* Serialized TLS serial to string as int can overflow 64 bits
* Increase timeout on OpenAI when using gpt-4
* Add a bit of logging

## [0.50.0][]

[0.50.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.49.0...0.50.0

### Added

* A new probe to list GitHub workflow runs
* A new action to cancel a GitHub workflow run

## [0.49.0][]

[0.49.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.48.0...0.49.0

### Changed

* link plan to execution

## [0.48.0][]

[0.48.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.47.0...0.48.0

### Changed

* use orjson for data serialization instead of builtin json. faster and stricter

## [0.47.0][]

[0.47.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.46.1...0.47.0

### Changed

* forcing status to be `aborted` when unset at the end of the experiment
  as it likely means something went very wrong and we don't want to not have
  a status set

## [0.46.0][]

[0.46.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.45.1...0.46.0

### Changed

* re-organized so plan status is always set
* interrupt execution when it couldn't be properly initialized

## [0.45.1][]

[0.45.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.45.0...0.45.1

### Added

* log line for operation duration

## [0.45.0][]

[0.45.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.44.1...0.45.0

### Changed

* Run OpenAI calls in a thread so they can terminate as soon as possible

## [0.44.1][]

[0.44.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.44.0...0.44.1

### Changed

* Fix empty alt_names

## [0.44.0][]

[0.44.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.43.3...0.44.0

### Changed

* Allow reading from `default` values

## [0.43.3][]

[0.43.3]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.43.2...0.43.3

### Changed

* Better handling of missing safeguard URL

## [0.43.2][]

[0.43.2]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.43.1...0.43.2

### Changed

* Use dict not list for integrations

## [0.43.1][]

[0.43.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.43.0...0.43.1

### Changed

* Fix string removal operator
* Don't let runtime info collection fail the execution

## [0.43.0][]

[0.43.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.42.0...0.43.0

### Changed

* Only track name/version pairs

## [0.42.0][]

[0.42.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.41.0...0.42.0

### Changed

* Embed list of chaostoolkit extensions and versions used for an execution
* Remove suffix from assistant question once used

## [0.40.0][]

[0.40.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.39.1...0.40.0

### Changed

* Minor fixes to the assistant control

## [0.39.1][]

[0.39.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.39.0...0.39.1

### Changed

* Ensure only one `reliably` extension exists

## [0.39.0][]

[0.39.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.38.0...0.39.0

### Changed

* Embed triggered probe into journal

## [0.38.0][]

[0.38.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.37.0...0.38.0

### Changed

* Storing safeguards/prechecks results into extension

## [0.37.0][]

[0.37.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.36.0...0.37.0

### Changed

* Fixed tests

## [0.36.0][]

[0.36.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.35.0...0.36.0

### Changed

* Improved safeguards/prechecks (meaning they should now work)

## [0.35.0][]

[0.35.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.34.3...0.35.0

### Changed

* Parses safeguards/prechecks arguments from env

## [0.34.3][]

[0.34.3]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.34.2...0.34.3

### Changed

* Support falsey values

## [0.34.2][]

[0.34.2]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.34.1...0.34.2

### Changed

* Remove trailing print

## [0.34.1][]

[0.34.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.34.0...0.34.1

### Changed

* Fixed parsing of numbers in autopause

## [0.34.0][]

[0.34.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.33.0...0.34.0

### Changed

* Parse autopause values when they are passed as environment variables

## [0.33.0][]

[0.33.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.32.0...0.33.0

### Changed

* Adjusted Autopause format to be have a more deterministic structure

## [0.32.0][]

[0.32.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.31.0...0.32.0

### Added

* ChatGPT control to automatically ask questions at the end of the experiment
* Autopause control

## [0.31.0][]

[0.31.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.30.3...0.31.0

### Added

* Safeguard and prechecks controls

## [0.30.3][]

[0.30.3]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.30.2...0.30.3

### Changed

* Don't clear the list as it removes the probes from the experiment, simply
  set the variable to a new empty list

## [0.30.2][]

[0.30.2]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.30.1...0.30.2

### Changed

* Properly capture the current activities of the hypothesis after the method

## [0.30.1][]

[0.30.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.30.0...0.30.1

### Changed

* Dealing with SIGINT from locust

## [0.30.0][]

[0.30.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.29.0...0.30.0

### Changed

* Properly trapping json decoding error on locust results

## [0.29.0][]

[0.29.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.28.0...0.29.0

### Changed

* Setting `plan_id` on execution state
* Logging plan status

## [0.28.0][]

[0.28.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.27.0...0.28.0

### Changed

- Switched to [pdm](https://pdm.fming.dev/latest/) for package management
- Swapped flake8 for ruff
- Introduced bandit to capture basic security issues
- Moved away from setuptools to pyproject.toml
- Swapped flake8 for ruff as linter, much faster

## [0.27.0][]

[0.27.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.26.0...0.27.0

### Changed

* Updated Readme

## [0.26.0][]

[0.26.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.25.1...0.26.0

### Changed

* Deploy sub-dependencies for the SLO generator

## [0.25.1][]

[0.25.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.25.0...0.25.1

### Fixed

* Missing `slo-generator` dependency in `setup.cfg`

## [0.25.0][]

[0.25.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.24.0...0.25.0

### Added

* Tolerance to check SLO error budget

## [0.24.0][]

[0.24.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.23.1...0.24.0

### Added

* Probe to generate SLO values from different providers

## [0.23.1][]

[0.23.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.23.0...0.23.1

### Changed

* Fix GitHub repo name

## [0.23.0][]

[0.23.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.22.0...0.23.0

### Added

* More links in the extension extra block when a CI is detected

## [0.22.0][]

[0.22.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.21.0...0.22.0

### Added

* New tolerances for GH to check under/greater or equal
* Better support for pauses

## [0.21.0][]

[0.21.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.20.0...0.21.0

### Added

* Support for execution state: pause/resume and termination

## [0.20.0][]

[0.20.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.19.0...0.20.0

### Added

* Capture log to send to Reliably

## [0.19.0][]

[0.19.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.18.6...0.19.0

### Changed

* Use the new `running` callback to initialize the execution
* Bump to chaostoolkit-lib 1.30.0+

## [0.18.6][]

[0.18.6]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.18.5...0.18.6

### Changed

* Pass config and secrets to handler

## [0.18.5][]

[0.18.5]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.18.4...0.18.5

### Changed

* Creating execution on Reliably as soon as it starts

## [0.18.4][]

[0.18.4]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.18.3...0.18.4

### Changed 

* does not change the exit code on locust failed tests

## [0.18.3][]

[0.18.3]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.18.2...0.18.3

### Changed 

* be more tolerant on default values

## [0.18.2][]

[0.18.2]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.18.1...0.18.2

### Added 

* dependencies to setup.cfg

## [0.18.1][]

[0.18.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.18.0...0.18.1

### Added 

* exposed load probes to discovery

## [0.18.0][]

[0.18.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.17.1...0.18.0

### Added 

* probes to read and validate results from a load test generated by
  `inject_gradual_traffic_into_endpoint`

## [0.17.1][]

[0.17.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.17.0...0.17.1

### Changed

* do not fail `inject_gradual_traffic_into_endpoint` when errors were met
  by a load test

## [0.17.0][]

[0.17.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.16.0...0.17.0

### Added

* `inject_gradual_traffic_into_endpoint` action to perform some mild traffic
  against an endpoint

## [0.16.0][]

[0.16.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.15.0...0.16.0

### Added

* `pr_duration` probe to collect the duration of all, or a subset, of
  a GitHub repository's pull-requests
* `percentile_under` tolerance to compute the percentiles of a list of
  of values

## [0.15.0][]

[0.15.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.14.2...0.15.0

### Changed

* Strip path of its '/' boundaries
* Add `ratio_above` tolerance

## [0.14.2][]

[0.14.2]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.14.1...0.14.2

### Changed

* In case the repo is given as its full URL, just pick the path from it

## [0.14.1][]

[0.14.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.14.0...0.14.1

### Fixed

* Use the github token from secrets when provided but let the `GITHUB_TOKEN`
  value take precedence

## [0.14.0][]

[0.14.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.13.0...0.14.0

### Changed

* Fully removed Open Telemetry support for now as the underlying library
  doesn't play well with having many tracers enabled

## [0.13.0][]

[0.13.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.12.1...0.12.0

### Added

* GitHub probe and tolerance to compute the ratio of closed PRs over a priod of time

## [0.12.1][]

[0.12.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.12.0...0.12.1

### Changed

* Remove ujson from setup.cfg

## [0.12.0][]

[0.12.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.11.0...0.12.0

### Changed

* Remove ujson to be more portable

## [0.11.0][]

[0.11.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.10.0...0.11.0

### Changed

* Send planning status back to Reliably
* Add span attributes and tags

## [0.10.0][]

[0.10.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.9.4...0.10.0

### Added

* Probe to measure duration of a single HTTP request
* Tolerance to validate this duration is below a certain value
* Probe to capture the TLS certificate of a remote endpoint
* Tolerances to validate aspects of the certificate

## [0.9.4][]

[0.9.4]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.9.3...0.9.4

### Added

* Added extra information to journal

## [0.9.3][]

[0.9.3]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.9.2...0.9.3

### Fixed

* Fix URL to execution

## [0.9.2][]

[0.9.2]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.9.1...0.9.2

### Changed

* Removing the execution payload from the extension

## [0.9.1][]

[0.9.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.9.0...0.9.1

### Fixed

* Ensure extension is stored

## [0.9.0][]

[0.9.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.8.1...0.9.0

### Changed

* Migrate to new Reliably API
* Add execution url and payload into the journal

## [0.8.1][]

[0.8.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.8.0...0.8.1

### Changed

* Always load settings from the config file first if it exists

## [0.8.0][]

[0.8.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.7.0...0.8.0

### Changed

* Always send the experiment encoded in standard base64

## [0.7.0][]

[0.7.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.6.0...0.7.0

### Changed

* Ensure events are properly referenced

## [0.6.0][]

[0.6.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.5.0...0.6.0

### Added

* Read `RELIABLY_TOKEN`, `RELIABLY_HOST` and `RELIABLY_ORG` environment
  variables when secrets have not been provided. They are common.
* Spec element to send to Reliably: contains the experiment and the output at various points in time

### Changed

* Major rework to match how Reliably's API currently works

## [0.4.2][]

[0.4.2]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.4.1...0.4.2

### Changed

* Very minor but fix link to image so documentation could get generated

## [0.4.1][]

[0.4.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.4.0...0.4.1

### Changed

* Fixed documentation regarding control usage

## [0.4.0][]

[0.4.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.3.0...0.4.0

### Changed

* Fixed labels sent to Reliably to use alias field names
* Corrected docstring examples of control usage
* Modified output label entry for experiment events to be strings
* Change `ctk_type` label entry to be `entity-type`
* Change url to reliably to now include `/api/*` as Reliably changed routes to
services

## [0.3.0][]

[0.3.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.2.2...0.3.0

### Added

- Added `chaosreliably.controls`:
  - Added `before_experiment_control` to create an Experiment, Experiment Version,
    Experiment Run, and an Experiment Event (Start) within Reliably services.
  - Added `before_hypothesis_control` and `after_hypothesis_control` to create
    Experiment Events within Reliably services.
  - Added `before_method_control` and `after_method_control` to create Experiment
    Events within Reliably services.
  - Added `before_rollback_control` and `after_rollback_control` to create
    Experiment Events within Reliably services.
  - Added `before_activity_control` and `after_activity_control` to create
    Experiment Events within Reliably services.
  - Added `after_experiment_control` to create an Experiment Event within Reliably
    services

### Changed

- Updated `.github/workflows/build.yaml` to be in line with `chaostoolkit`
- Updated `Makefile` to be in line with `chaostoolkit`
- Add `check-pr.md` which alerts PR raisers to whether they've modified
`CHANGELOG.md` or tests.
- Ran `pyupgrade --py36-plus` on the project
- Bump up coverage in tests to cover failure cases in `__init__.py`
- Add `mypy` as a dependency and use it in linting to enforce typing

## [0.2.2][]

[0.2.2]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.2.1...0.2.2

- Updated `README.md` to correctly show where `tolerance` goes when using `slo_is_met` as a Steady State Hypothesis
- Fixed default reliably host to be `reliably.com` instead of `api.reliably.com`

## [0.2.1][]

[0.2.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.2.0...0.2.1

### Changed

- Updated `get_objective_results_by_labels` to have a default `limit` of `1`
- Add `slo_is_met` as a probe to encompass the `get_objective_results_by_labels` probe and `all_objective_results_ok` tolerance


## [0.2.0][]

[0.2.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.1.2...0.2.0

### Changed

- Fix issue where secrets were not correctly extracted from Experiment config [#1][1]
- Refactor to use new Reliably Entity Server rather than previous API
  - One probe available: `get_objective_results_by_labels`
    - For a given Objectives labels, get the Objective Results
  - One tolerance available: `all_objective_results_ok`
    - For a list of Objective Results, determine if they were all OK
- Allow for user to provide `org` as a secret/get it from `currentOrg` in their Reliably config

[1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/issues/1

## [0.1.2][]

[0.1.2]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.1.1...0.1.2

### Changed

- Use the most recent SLO report only

## [0.1.1][]

[0.1.1]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/compare/0.1.0...0.1.1

### Changed

- Add `install_requires` so that dependencies are properly installed via pip

## [0.1.0][]

[0.1.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/tree/0.1.0

### Added

-   Initial release
