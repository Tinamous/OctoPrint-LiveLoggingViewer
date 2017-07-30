# OctoPrint-LiveLoggingViewer

View OctoPrint log messages as they happen in a OctoPrint tab.

Useful for plugin development to help view log messages as they happen rather than downloading the log file or tailing them through an ssh connection.

Does not show historic log messages and shows only the most recent 100 messages (latest at the top).

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/Tinamous/OctoPrint-LiveLoggingViewer/archive/master.zip

## Configuration

You can set the minimum log level to watch and the log name to filter for a specific plugin.

Leave Log Name blank for all logs.
