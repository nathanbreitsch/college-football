angular.module("cfbFilmRoom")
.factory("statsFilterService", [ function() {
    "use strict";
    var Quarterback = function() {
        var This = this;
        This.playerType = "quarterback";
        This.filters = This.quarterbackFilters();
    };
    var Player = function(player) {
        var This = this;
        switch (player) {
            case "quaterback":
            This.player = new Quarterback();
            This.filters = This.quarterbackFilters();
            break;
            default:
            This.player = null;
        }
    };
    var opponentLevel =    {
            filterTitle: "Oponent Level",
            filterValue: "opponentLevel",
            options: [
                {
                    title: "FBS",
                    value: "fbs"
                },
                {
                    title: "Power 5",
                    value: "power5"
                },
                {
                    title: "SEC",
                    value: "sec"
                },
                {
                    title: "Big 10",
                    value: "big10"
                },
                {
                    title: "Pac 12",
                    value: "pac12"
                },
                {
                    title: "Big 12",
                    value: "big12"
                },
                {
                    title: "ACC",
                    value: "acc"
                }
            ]
        };
        var quarters = {
            filterTitle: "Quarter",
            filterValue: "quarter",
            options: [
                {
                    title: "Q1",
                    value: "1"
                },
                {
                    title: "Q2",
                    value: "2"
                },
                {
                    title: "Q3",
                    value: "3"
                },
                {
                    title: "Q4",
                    value: "4"
                },
                {
                    title: "OT",
                    value: "ot"
                }
            ]
        };
        var downs = {
            filterTitle: "Downs",
            filterValue: "downs",
            options: [
                {
                    title: "1st",
                    value: "1"
                },
                {
                    title: "2nd",
                    value: "2"
                },
                {
                    title: "3rd",
                    value: "3"
                },
                {
                    title: "4th",
                    value: "4"
                }
            ]
        };
        var yardsToGo = {
            filterTitle: "Yeards to go",
            filterValue: "ytg",
            options: [
                {
                    title: "Goal to Go",
                    value: "gtg"
                },
                {
                    title: "1",
                    value: "1"
                },
                {
                    title: "2",
                    value: "2"
                },
                {
                    title: "3",
                    value: "3"
                },
                {
                    title: "4",
                    value: "4"
                },
                {
                    title: "5",
                    value: "5"
                },
                {
                    title: "6",
                    value: "6"
                },
                {
                    title: "7",
                    value: "7"
                },
                {
                    title: "8",
                    value: "8"
                },
                {
                    title: "9",
                    value: "9"
                },
                {
                    title: "10",
                    value: "10"
                },
                {
                    title: "11+",
                    value: "11"
                },
            ]
        };
        var yardLine = {
            filterTitle: "Yard Line",
            filterValue: "yardLine",
            options: [
                {
                    title: "Red Zone",
                    value: "redzone"
                },
                {
                    title: "Inside 5",
                    value: "inside5"
                },
                {
                    title: "Inside 10",
                    value: "inside10"
                },
                {
                    title: "Opp Half",
                    value: "opphalf"
                },
                {
                    title: "Own Half",
                    value: "ownhalf"
                },
            ]
        };
        var passingDistance = {
            filterTitle: "Passing Distance",
            filterValue: "passingDistance",
            options: [
                {
                    title: "Behind LOS",
                    value: "negative"
                },
                {
                    title: "0-9",
                    value: "s"
                },
                {
                    title: "10-19",
                    value: "m"
                },
                {
                    title: "20+",
                    value: "l"
                },
            ]
        };
        var underPressure = {
            filterTitle: "Under Pressure",
            filterValue: "underPressure",
            options: [
                {
                    title: "Pressure",
                    value: "pressure"
                },
                {
                    title: "No Pressure",
                    value: "nopressure"
                },
            ]
        };
        var pocketState = {
            filterTitle: "In/Out Pocket",
            filterValue: "pocket",
            options: [
                {
                    title: "In Pocket",
                    value: "inpocket"
                },
                {
                    title: "Out Pocket",
                    value: "outpocket"
                },
            ]
        };
        var shotgunState = {
            filterTitle: "Shotgun/Under Center",
            filterValue: "shotgun",
            options: [
                {
                    title: "Shotgun",
                    value: "shotgun"
                },
                {
                    title: "Under Center",
                    value: "undercenter"
                },
            ]
        };
        var contestedState = {
            filterTitle: "Contested Targets",
            filterValue: "contestedTargets",
            options: [
                {
                    title: "Contested",
                    value: "contested"
                },
                {
                    title: "Open",
                    value: "open"
                },
            ]
        };

    Player.prototype.quarterbackFilters = function() {
        var filters;
        filters = [opponentLevel, quarters, downs, yardsToGo, yardLine,
            passingDistance, underPressure, pocketState, shotgunState, contestedState];
        return filters;
    };
    return {
        Player: Player
    };
}]);
