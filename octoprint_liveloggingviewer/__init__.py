# coding=utf-8
from __future__ import absolute_import

import logging
import logging.handlers

import octoprint.plugin
from .LiveLoggingHandler import LiveLoggingHandler

class LiveloggingviewerPlugin(octoprint.plugin.StartupPlugin,
                              octoprint.plugin.SettingsPlugin,
                              octoprint.plugin.AssetPlugin,
                              octoprint.plugin.TemplatePlugin):

	def initialize(self):
		self._logger.setLevel(logging.DEBUG)
		self._logger.info("Live Logging Viewer Plugin [%s] initialized..." % self._identifier)

	# Startup complete we can not get to the settings.
	def on_after_startup(self):
		self._logger.info("Live Logging Viewer - Atteching Lggging Handler")

		if self._settings.get(['enabled']):
			handler = LiveLoggingHandler()
			handler._plugin_manager = self._plugin_manager

			level = self._settings.get(['level'])
			# TODO: This needs to be configurable.
			handler.setLevel(level)

			logName = self._settings.get(['logName'])
			self._logger.info("Using log name: '{0}' at level {1}".format(logName, level))
			logger = logging.getLogger(logName)
			logger.addHandler(handler)
			self._logger.info("Live Logging Viewer Attached for log: '{0}'".format(logName))

	##~~ SettingsPlugin mixin

	def get_settings_defaults(self):
		return dict(
			logName="",
			enabled=True,
			level="INFO"
		)

	def get_template_configs(self):
		return [
			# dict(type="navbar", custom_bindings=False),
			dict(type="settings", custom_bindings=False),
			dict(type="tab", name="Log Viewer")
		]

	##~~ AssetPlugin mixin

	def get_assets(self):
		# Define your plugin's asset files to automatically include in the
		# core UI here.
		return dict(
			js=["js/liveloggingviewer.js"],
			css=["css/liveloggingviewer.css"],
			less=["less/liveloggingviewer.less"]
		)

	##~~ Softwareupdate hook

	def get_update_information(self):
		# Define the configuration for your plugin to use with the Software Update
		# Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
		# for details.
		return dict(
			liveloggingviewer=dict(
				displayName="Live Logging Viewer",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="Tinamous",
				repo="OctoPrint-LiveLoggingViewer",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/Tinamous/OctoPrint-LiveLoggingViewer/archive/{target_version}.zip"
			)
		)


# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "Live Logging Viewer"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = LiveloggingviewerPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

