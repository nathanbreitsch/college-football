angular.module("cfbFilmRoom")
    .controller("PlayerPageController", ["$scope", "$http", "statsFilterService",
    "statsGlossaryService", function ($scope, $http, statsFilterService, statsGlossaryService) {
        "use strict";
        var This = this;
        This._scope = $scope;

        This._scope.tableDataHeaders = [
                "first_name",
                "position",
                "team",
                "stat1",
                "stat2",
                "stat3",
                "stat4",
                "stat5",
                "stat6",
                "stat7",
                "stat8",
                "stat9",
                "stat10",
                "stat11",
                "stat12",
                "stat13",
                "stat14",
                "stat15"
        ];

    }]);
