/*
 * View model for OctoPrint-LiveLoggingViewer
 *
 * Author: Stephen Harrison
 * License: AGPLv3
 */
$(function() {
    function LiveLoggingViewerViewModel(parameters) {
        var self = this;
        self.pluginId = "liveloggingviewer";

        self.loginStateViewModel = parameters[0];
        self.settingsViewModel = parameters[1];
        self.printer = parameters[2];

        self.logMessages = ko.observableArray([]);

       self.onDataUpdaterPluginMessage = function(plugin, data) {
           if (plugin != self.pluginId) {
               return;
           }

           console.log("LOG:: logger name '" + data.name + "' level: " + data.levelname + "' file: " + data.filename + "' line: " + data.lineno+ "' message: " + data.message);
           // Insert the log at the top.
           self.logMessages.unshift(data);

           // Limit to recent x messages.
            if (self.logMessages().length >  100) {
                self.logMessages().splice(self.logMessages.length-1, 1);
            }
       };

       self.clear = function() {
           self.logMessage([]);
       };
    }

    // view model class, parameters for constructor, container to bind to
    OCTOPRINT_VIEWMODELS.push({
        construct: LiveLoggingViewerViewModel,
        additionalNames: [],
        dependencies: ["loginStateViewModel", "settingsViewModel", "printerStateViewModel"],
        optional: [],
        elements: ["#tab_plugin_liveloggingviewer"]
    });
});
