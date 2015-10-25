angular.module("cfbFilmRoom")
    .directive("advStatsTable", function() {
        "use strict";
        var AdvStatsController = function($scope, $element, $window, $timeout) {
            var This = this;
            This._element = $element;
            This._timeout = $timeout;

        };
        return {
            templateUrl: "static/js/widgets/advancedStatsTable/advStatsTable.html",
            link: function(scope, element, attributes, controller) {
                console.log(scope);
                console.log(element);
                console.log(attributes);
                console.log(controller);
            },
            controller: ["$scope", "$element", "$window", "$timeout", AdvStatsController]
        };
    });
