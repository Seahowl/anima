var dominionApp = angular.module('dominionApp', ['ui.bootstrap', 'ui.router']);

dominionApp.config(function($stateProvider, $urlRouterProvider) {
	$urlRouterProvider.otherwise('/home');
    
    $stateProvider
        
        // HOME STATES AND NESTED VIEWS ========================================
        .state('home', {
            url: '/home',
            templateUrl: './components/home/homePartial.html'
        })
        
        // ABOUT PAGE AND MULTIPLE NAMED VIEWS =================================
        .state('about', {
            url: '/about',
            templateUrl: './components/about/aboutPartial.html'      
        })

        // ABOUT PAGE AND MULTIPLE NAMED VIEWS =================================
        .state('dominion', {
            url: '/dominion',
            templateUrl: './components/dominion/dominionPartial.html'      
        })
        .state('dominion.effects', {
            url: '/effect/',
            templateUrl: './components/dominion/effectsPartial.html',
            controller: 'effectsController'
        })
        .state('dominion.effect', {
            url: '/effect/{effectId:[0-9]}',
            templateUrl: './components/dominion/effectPartial.html',
            controller: 'effectController'
        })
        .state('dominion.trees', {
            url: '/tree/',
            templateUrl: './components/dominion/treesPartial.html',
            controller: 'treesController'
        })
        .state('dominion.techniques', {
            url: '/techniques/',
            templateUrl: './components/dominion/techniquesPartial.html',
            controller: 'techniquesController'
        })
        .state('dominion.disadvantages', {
            url: '/disadvantages/',
            templateUrl: './components/dominion/disadvantagesPartial.html',
            controller: 'disadvantagesController'
        })
        .state('api', {
            // this state is blank so that it passes routing off to the django router      
        });
        
});

dominionApp.run(function($rootScope, $document){
    $rootScope.toggleHelp = function() {
        if ($document[0].getElementById("help").className == "hidehelp")
        {
            $document[0].getElementById("help").className = "showhelp";
        }
        else
        {
            $document[0].getElementById("help").className = "hidehelp";
        }
    };
});

dominionApp.controller('effectController', ['$scope', '$http', '$stateParams', '$q',
    function($scope, $http, $stateParams, $q)
    {
        getURL = "http://localhost:8000/dominion/api/effects/" + $stateParams.effectId
        $scope.jsonStuff = {}
        $http.get(getURL, {cache:true}).
        then(function(response) {
            $scope.jsonStuff = response.data
            abilityNames = ["Strength","Dexterity", "Agility", "Constitution", "Power", "Will"];
            abilityCosts = [];
            abilityCosts[0] = $scope.jsonStuff[0].fields.effect_str_cost;
            abilityCosts[1] = $scope.jsonStuff[0].fields.effect_dex_cost;
            abilityCosts[2] = $scope.jsonStuff[0].fields.effect_agi_cost;
            abilityCosts[3] = $scope.jsonStuff[0].fields.effect_con_cost;
            abilityCosts[4] = $scope.jsonStuff[0].fields.effect_pow_cost;
            abilityCosts[5] = $scope.jsonStuff[0].fields.effect_will_cost;

            $scope.primaryStat = ""
            $scope.secondaryStatList = ""

            for (i = 0; i < 6; i++) { 
                if (abilityCosts[i] == 0)
                {
                    $scope.primaryStat = abilityNames[i];
                }
                else if (abilityCosts[i] > 0)
                {
                    $scope.secondaryStatList = $scope.secondaryStatList + abilityNames[i] + " +" + abilityCosts[i] + "; "; 
                }
            }
            getLevelsURL = "http://localhost:8000/dominion/api/effects/" + $stateParams.effectId + "/levels/"
            $scope.jsonLevelsStuff = {}
            $http.get(getLevelsURL, {cache:true}).
            then(function(response) {
                $scope.jsonLevelsStuff = response.data
            }, function(response) {
                $scope.jsonLevelsStuff = 'error'
            });

            var promises = []

            getModifiersURL = "http://localhost:8000/dominion/api/effects/" + $stateParams.effectId + "/modifiers/"
            $scope.jsonModifiersStuff = {}
            $http.get(getModifiersURL, {cache:true}).
            then(function(response) {
                $scope.jsonModifiersStuff = response.data
                if (response.data.length != 0)
                {
                    for(i=0; i < response.data.length; i++)
                    {
                        getModifierLevelsURL = "http://localhost:8000/dominion/api/effects/" + $stateParams.effectId + "/modifiers/" + response.data[i].pk + "/levels/"
                        promises.push($http.get(getModifierLevelsURL, {cache:true}))
                    }
                    $q.all(promises).
                    then(function(responseInner) {
                        for(i=0; i < responseInner.length; i++)
                        {
                            $scope.jsonModifiersStuff[i].levels = responseInner[i].data
                        }
                    }, function(response) {
                        response.data[i].levels = 'error'
                    });
                }
            }, function(response) {
                $scope.jsonModifiersStuff = 'error'
            });
        }, function(response) {
            $scope.jsonStuff = 'error'
        });
    }
]);

dominionApp.controller('effectsController', 
    function($scope, $http, $stateParams)
    {
        getURL = "http://localhost:8000/dominion/api/effects/"
        $scope.jsonStuff = {}
        $http.get(getURL, {cache:true}).
        then(function(response) {
            $scope.jsonStuff = response.data
        }, function(response) {
            $scope.jsonStuff = 'error'
        });
    }
);

dominionApp.controller('treesController', 
    function($scope, $http, $stateParams)
    {
        getURL = "http://localhost:8000/dominion/api/trees/"
        $scope.jsonStuff = {}
        $http.get(getURL, {cache:true}).
        then(function(response) {
            $scope.jsonStuff = response.data
        }, function(response) {
            $scope.jsonStuff = 'error'
        });
    }
);
dominionApp.controller('techniquesController', 
    function($scope, $http, $stateParams)
    {
        getURL = "http://localhost:8000/dominion/api/techniques/"
        $scope.jsonStuff = {}
        $http.get(getURL, {cache:true}).
        then(function(response) {
            $scope.jsonStuff = response.data
        }, function(response) {
            $scope.jsonStuff = 'error'
        });
    }
);
dominionApp.controller('disadvantagesController', 
    function($scope, $http, $stateParams)
    {
        getURL = "http://localhost:8000/dominion/api/disadvantages/"
        $scope.jsonStuff = {}
        $http.get(getURL, {cache:true}).
        then(function(response) {
            $scope.jsonStuff = response.data
        }, function(response) {
            $scope.jsonStuff = 'error'
        });
    }
);



