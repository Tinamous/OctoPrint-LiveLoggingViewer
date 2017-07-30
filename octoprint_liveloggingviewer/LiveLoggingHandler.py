import logging

# Log handler that pushes log messages via the plugin manager to the browser as events.
class LiveLoggingHandler(logging.Handler):
	def emit(self, record):
		log_entry = self.format(record)
		value = dict(
			name=record.name,
			message=record.msg,
			filename=record.filename,
			lineno=record.lineno,
			levelname=record.levelname,
			levelno=record.levelno
		)
		self._plugin_manager.send_plugin_message("liveloggingviewer", value)
		return True