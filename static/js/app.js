// Declare app level module which depends on filters, and services
angular.module("cfbFilmRoom", ["ngResource", "ngRoute", "ui.bootstrap", "ui.date", "ngAnimate", "ngAria", "ngMaterial"])
    .config(function($mdThemingProvider) {
        "use strict";
        // Extend the red theme with a few different colors
        var neonRedMap = $mdThemingProvider.extendPalette("red", {
            "500": "#121212"
        });
        // Register the new color palette map with the name <code>neonRed</code>
        $mdThemingProvider.definePalette("neonRed", neonRedMap);
        // Use that theme for the primary intentions
        $mdThemingProvider.theme("default")
            .primaryPalette("neonRed");
    })
    .config(["$routeProvider", function($routeProvider) {
        $routeProvider
            .when("/", {
                templateUrl: "static/views/home/home.html",
                controller: "HomeController"
            })
            .when("/advancedStatsBench", {
                templateUrl: "static/views/advancedStats/advancedStatsBench/advancedStatsBench.html",
                controller: "AdvancedStatsBenchController"
            })
            .otherwise({
                redirectTo: "/"
            });
    }]);
