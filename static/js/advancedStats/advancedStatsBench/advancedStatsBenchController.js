angular.module("cfbFilmRoom")
    .controller("AdvancedStatsBenchController", ["$scope", "$http", "statsFilterService",
    "statsGlossaryService", function ($scope, $http, statsFilterService, statsGlossaryService) {
        "use strict";
        var This = this;
        This._scope = $scope;
        This._quarterback = new statsFilterService.Player("quarterback");
        This._scope.glossary = new statsGlossaryService.Glossary();
        This._quarterbackFilters = This._quarterback.quarterbackFilters();
        This._scope.activeFilters = This._quarterbackFilters;
        This._scope.playerTypes = [
            {
                title: "Passing"
            },
            {
                title: "Rushing"
            },
            {
                title: "Recieving"
            },
            {
                title: "Blocking"
            },
            {
                title: "Pass-Rush & Tackling"
            },
            {
                title: "Coverage"
            }
        ];

        $http({
          method: 'GET',
          url: '/api/quarterback_stats'
        }).then(function successCallback(response) {
          console.log(response);
              This._scope.tableData = response.data.athletes;

          }, function errorCallback(response) {

        });
/*
        This._scope.tableData = [
            {
                name: "Juan Garcia",
                position: "some position",
                team: "some team",
                stat1: 1,
                stat2: 12,
                stat3: 13,
                stat4: 14,
                stat5: 15,
                stat6: 16,
                stat7: 17,
                stat8: 18,
                stat9: 19,
                stat10: 110,
                stat11: 111,
                stat12: 112,
                stat13: 113,
                stat14: 114,
                stat15: 115,
            },
            {
                name: "Steve Garcia",
                position: "some position",
                team: "some team",
                stat1: 1,
                stat2: 112,
                stat3: 113,
                stat4: 114,
                stat5: 115,
                stat6: 116,
                stat7: 117,
                stat8: 118,
                stat9: 119,
                stat10: 1110,
                stat11: 1111,
                stat12: 1112,
                stat13: 1113,
                stat14: 1114,
                stat15: 1115,
            },
            {
                name: "Marco Garcia",
                position: "some position",
                team: "some team",
                stat1: 13,
                stat2: 132,
                stat3: 133,
                stat4: 134,
                stat5: 1335,
                stat6: 163,
                stat7: 137,
                stat8: 138,
                stat9: 139,
                stat10: 4110,
                stat11: 1511,
                stat12: 1612,
                stat13: 1173,
                stat14: 19184,
                stat15: 1015,
            },
            {
                position: "some position",
                team: "some team",
                stat1: 91,
                stat2: 412,
                stat3: 173,
                stat4: 184,
                stat5: 115,
                stat6: 166,
                stat7: 127,
                stat8: 198,
                stat9: 119,
                stat10: 16610,
                stat11: 1171,
                stat12: 112,
                stat13: 1133,
                stat14: 1124,
                stat15: 11115,
            },
        ];
        */

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
        This._scope.activeKey = This._scope.tableDataHeaders[0];
        This._scope.sortDirection = 1;

        /*
            sort direction:
                 1 = number (hight to low), character (low to high)
                -1 = number (low to high), character (high to low)
        */



        This._scope.orderBy = function(key) {
            var value;
            // set sort direction
            This._scope.sortDirection = This._determineSortDirection(key);
            // keep searching for a value in the of data type key
            for (var i = 0; i < This._scope.tableData.length; i++) {
                if (This._scope.tableData[i][key]) {
                    value = This._scope.tableData[i][key];
                    break;
                }
            }
            // test the typeof data to order appropriately
            console.log(typeof value);
            if (typeof value == "string") {
                console.log("string");
                This._scope.tableData = This._alphabeticalSort(This._scope.tableData, key);
            }
            else if (typeof value == "number") {
                console.log("number");
                This._scope.tableData = This._numericalSort(This._scope.tableData, key);
            }
            else {
                console.log("not recognized type");
            }
        };

        This._determineSortDirection = function(key) {
            if (key == This._scope.activeKey) {
                return -1 * This._scope.sortDirection;
            }
            else {
                This._scope.activeKey = key;
                return 1;
            }
        };

        This._numericalSort = function(array, key) {
            function mergeSort (arr) {
                if (arr.length < 2) return arr;

                var mid = Math.floor(arr.length /2);
                var subLeft = mergeSort(arr.slice(0,mid));
                var subRight = mergeSort(arr.slice(mid));

                return merge(subLeft, subRight);
            }

            function merge (a,b) {
                var result = [];
                while (a.length >0 && b.length >0) {
                    if (This._scope.sortDirection < 0) {
                        result.push(a[0][key] < b[0][key]? a.shift() : b.shift());
                    }
                    else {
                        result.push(a[0][key] > b[0][key]? a.shift() : b.shift());
                    }
                }
                return result.concat(a.length? a : b);
            }
            return mergeSort(array);
        };

        This._alphabeticalSort = function(array, key) {
            array.sort(function(a, b) {
                console.log(b[key] !== undefined);
                var textA = a[key] !== undefined ? a[key].toUpperCase() : a[key];
                var textB = b[key] !== undefined ? b[key].toUpperCase() : b[key];
                if (This._scope.sortDirection > 0) {
                    return (textA < textB) ? -1 : (textA > textB) ? 1 : 0;
                }
                else {
                    return (textA > textB) ? -1 : (textA < textB) ? 1 : 0;
                }

            });

            return array;
        };


    }]);
