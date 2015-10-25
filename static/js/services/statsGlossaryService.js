angular.module("cfbFilmRoom")
.factory("statsGlossaryService", [ function() {
    "use strict";
    var Glossary = function() {
        var This = this;
        This.termsList = This.getTermsList();

    };

    var ayAtt = {
        abbrev: "AY/Att",
        title: "Air Yards per Attempt",
        def: "The average distance the ball travels through the air per pass "+
        "attempt CTgt – Contested target. Any time the receiver had to compete with a defensive "+
        " back for the ball. CRec – Contested targets which still resulted in a completed pass."
    };

    var CTgt = {
        abbrev: "CTgt",
        title: "Contested Target",
        def: "Any time the receiver had to compete with a defensive back for the ball."
    };

    var CRec = {
        abbrev: "CRec",
        title: "Contested Recieved",
        def: "Contested targets which still resulted in a completed pass"
    };

    var Db = {
        abbrev: "Db",
        title: "Dropbacks",
        def: "Total number of times a QB drops back to pass"
    };

    var Dp = {
        abbrev: "Dp",
        title: "Dropped Passes",
        def: "Number of dropped passes by receivers."
    };

    var Fm = {
        abbrev: "Fm",
        title: "Fumble"
    };

    var Ht = {
        abbrev: "Ht",
        title: "Hit",
        def: "A hit on the QB"
    };

    var Hur = {
        abbrev: "Hur",
        title: "Hurry",
        def: "When the QB was forced from the pocket, or forced to rush/alter his throw by a defender."
    };

    var MT = {
        abbrev: "MT",
        title: "Missed Tackle",
        def: "Missed tackle (or missed tackles forced for offensive players)."
    };

    var PB = {
        abbrev: "PB Snaps",
        title: "Pass Block Snaps",
        def: ""
    };

    var PBPer = {
        abbrev: "PB %",
        title: "Pass Block Percentage",
        def: "Total percentage of pass block snaps on which" +
        "the blocker did not allow a sack, hit or hurry."
    };

    var Pres = {
        abbrev: "Pres",
        title: "Pressures",
        def: "Number of times QB was pressured"
    };

    var Stuff = {
        abbrev: "Stuff",
        title: "Stuff",
        def: "Any play resulting a zero or negative yards."
    };

    var TA = {
        abbrev: "TA",
        title: "Thrown Away",
        def: "Number of balls thrown away by QB."
    };

    var TackPer = {
        abbrev: "Tack %",
        title: "Tackle Percentage",
        def: "Calculated as tackles divided by tackles + missed tackles)"
    };

    var YACRBs = {
        abbrev: "YAC (RBs)",
        title: "Tackle Percentage",
        def: "Defined as yards gained after significant" +
        " contact which took some level of strength and/or agility to avoid."+
        " Does not include yards after the first minor or incidental contact."
    };

    var YACWRs = {
        abbrev: "YAC (WRs)",
        title: "Yards After Catch",
        def: ""
    };


    Glossary.prototype.getTermsList = function() {
        var terms;
        terms = [ayAtt, CTgt, CRec, Db, Dp, Fm, Ht, Hur, MT, PB, PBPer,
        Pres, Stuff, TA, TackPer, YACRBs, YACWRs];
        return terms;
    };
    return {
        Glossary: Glossary
    };
}]);
