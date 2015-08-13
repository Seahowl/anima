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
        .state('dominion.tree', {
            url: '/tree/{treeId:[0-9]}',
            templateUrl: './components/dominion/treePartial.html',
            controller: 'treeController'
        })
        .state('dominion.techniques', {
            url: '/techniques/',
            templateUrl: './components/dominion/techniquesPartial.html',
            controller: 'techniquesController'
        })
        .state('dominion.technique', {
            url: '/technique/{techniqueId:[0-9]}',
            templateUrl: './components/dominion/techniquePartial.html',
            controller: 'techniqueController'
        })
        .state('dominion.disadvantages', {
            url: '/disadvantages/',
            templateUrl: './components/dominion/disadvantagesPartial.html',
            controller: 'disadvantagesController'
        })
        .state('dominion.disadvantage', {
            url: '/disadvantage/{disadvantageId:[0-9]}',
            templateUrl: './components/dominion/disadvantagePartial.html',
            controller: 'disadvantageController'
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

dominionApp.controller('effectsController', 
    function($scope, $http, $stateParams)
    {
        getURL = "http://localhost:8000/dominion/api/effects/";
        $scope.effectsJSON = {};
        $http.get(getURL, {cache:true}).
        then(function(response) {
            $scope.effectsJSON = response.data;
        }, function(response) {
            $scope.effectsJSON = 'error';
        });
    }
);

dominionApp.controller('effectController', ['$scope', '$http', '$stateParams', '$q',
    function($scope, $http, $stateParams, $q)
    {
        getURL = "http://localhost:8000/dominion/api/effects/" + $stateParams.effectId;
        $scope.effectJSON = {};
        $http.get(getURL, {cache:true}).
        then(function(response) {
            $scope.effectJSON = response.data;
            abilityNames = ["Strength","Dexterity", "Agility", "Constitution", "Power", "Will"];
            abilityCosts = [];
            abilityCosts[0] = $scope.effectJSON[0].fields.effect_str_cost;
            abilityCosts[1] = $scope.effectJSON[0].fields.effect_dex_cost;
            abilityCosts[2] = $scope.effectJSON[0].fields.effect_agi_cost;
            abilityCosts[3] = $scope.effectJSON[0].fields.effect_con_cost;
            abilityCosts[4] = $scope.effectJSON[0].fields.effect_pow_cost;
            abilityCosts[5] = $scope.effectJSON[0].fields.effect_will_cost;

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
            getLevelsURL = "http://localhost:8000/dominion/api/effects/" + $stateParams.effectId + "/levels/";
            $scope.effectLevelsJSON = {};
            $http.get(getLevelsURL, {cache:true}).
            then(function(response) {
                $scope.effectLevelsJSON = response.data;
            }, function(response) {
                $scope.effectLevelsJSON = 'error';
            });

            var promises = [];

            getModifiersURL = "http://localhost:8000/dominion/api/effects/" + $stateParams.effectId + "/modifiers/";
            $scope.effectModifiersJSON = {};
            $http.get(getModifiersURL, {cache:true}).
            then(function(response) {
                $scope.effectModifiersJSON = response.data;
                if (response.data.length != 0)
                {
                    for(i=0; i < response.data.length; i++)
                    {
                        getModifierLevelsURL = "http://localhost:8000/dominion/api/effects/" + $stateParams.effectId + "/modifiers/" + response.data[i].pk + "/levels/";
                        promises.push($http.get(getModifierLevelsURL, {cache:true}));
                    }
                    $q.all(promises).
                    then(function(responseInner) {
                        for(i=0; i < responseInner.length; i++)
                        {
                            $scope.effectModifiersJSON[i].levels = responseInner[i].data;
                        }
                    }, function(response) {
                        response.data[i].levels = 'error';
                    });
                }
            }, function(response) {
                $scope.effectModifiersJSON = 'error';
            });
        }, function(response) {
            $scope.effectJSON = 'error';
        });
    }
]);

dominionApp.controller('treesController', 
    function($scope, $http, $stateParams)
    {
        getURL = "http://localhost:8000/dominion/api/trees/";
        $scope.treesJSON = {};
        $http.get(getURL, {cache:true}).
        then(function(response) {
            $scope.treesJSON = response.data;
        }, function(response) {
            $scope.treesJSON = 'error';
        });
    }
);

dominionApp.controller('treeController', ['$scope', '$http', '$stateParams', '$q',
    function($scope, $http, $stateParams, $q)
    {
        getURL = "http://localhost:8000/dominion/api/trees/"  + $stateParams.treeId;
        $scope.treeJSON = {};
        $http.get(getURL, {cache:true}).
        then(function(response) {
            $scope.treeJSON = response.data

            var promises = [];
            if (response.data[0].fields.techniques.length != 0)
            {
                $scope.treeTechniquesJSON = []
                for(i=0; i < response.data[0].fields.techniques.length; i++)
                {
                    getTreeTechniquesURL = "http://localhost:8000/dominion/api/techniques/" + response.data[0].fields.techniques[i];
                    promises.push($http.get(getTreeTechniquesURL, {cache:true}));
                }
                $q.all(promises).
                then(function(responseInner) {
                    for(i=0; i < responseInner.length; i++)
                    {
                        $scope.treeTechniquesJSON[i] = responseInner[i].data;
                    }
                }, function(response) {
                    $scope.treeTechniquesJSON = 'error';
                });
            }
        }, function(response) {
            $scope.treeJSON = 'error';
        });
    }
]);

dominionApp.controller('techniquesController', 
    function($scope, $http, $stateParams)
    {
        getURL = "http://localhost:8000/dominion/api/techniques/";
        $scope.techniquesJSON = {};
        $http.get(getURL, {cache:true}).
        then(function(response) {
            $scope.techniquesJSON = response.data;
        }, function(response) {
            $scope.techniquesJSON = 'error';
        });
    }
);

dominionApp.controller('techniqueController', ['$scope', '$http', '$stateParams', '$q',
    function($scope, $http, $stateParams, $q)
    {
        //this function pulls out all the information for a single technique ($stateParams.techniqueId)
        getURL = "http://localhost:8000/dominion/api/techniques/"  + $stateParams.techniqueId 
        $scope.techniqueJSON = {};
        $http.get(getURL, {cache:true}).
        then(function(response) {
            $scope.techniqueJSON = response.data

            //collection objects for the 6 groups of promises we're going to fetch
            var effectPromises = [];
            var effectLevelPromises = [];
            var effectModifierPromises = [];
            var effectModifierLevelPromises = [];
            var disadvantagePromises = [];
            var disadvantageLevelPromises = [];
            if (response.data[0].fields.effects.length != 0)
            {
                //pre-initialize mostly for safety here.  Only techniqueEffects and disadvantages are actually going to make it to the scope 
                $scope.techniqueEffectsJSON = [];
                techniqueEffectLevelsJSON = [];
                techniqueEffectModifiersJSON = [];
                techniqueEffectModifiersLevelsJSON = [];
                $scope.disadvantagesJSON = [];
                disadvantageLevelsJSON = [];
                //each effect will have a level, so we combine them into one loop
                for(i=0; i < response.data[0].fields.effects.length; i++)
                {
                    getEffectsURL = "http://localhost:8000/dominion/api/effects/" + response.data[0].fields.effects[i];
                    getEffectLevelsURL = "http://localhost:8000/dominion/api/effects/" + response.data[0].fields.effects[i] + "/levels/" +  response.data[0].fields.effect_levels[i];
                    effectPromises.push($http.get(getEffectsURL, {cache:true}));
                    effectLevelPromises.push($http.get(getEffectLevelsURL, {cache:true}));
                }
                //each modifier will also have a level, but effects can have multiple modifiers, so we seperate this out
                for(i=0; i < response.data[0].fields.effect_modifiers.length; i++)
                {
                    getEffectModifiersURL = "http://localhost:8000/dominion/api/effects/" + response.data[0].fields.effects[i] + "/modifiers/" + response.data[0].fields.effect_modifiers[i];
                    getEffectModifierLevelsURL = "http://localhost:8000/dominion/api/effects/" + response.data[0].fields.effects[i] + "/modifiers/" + response.data[0].fields.effect_modifiers[i] + "/levels/" + response.data[0].fields.effects_modifier_levels[i];
                    effectModifierPromises.push($http.get(getEffectModifiersURL, {cache:true}));
                    effectModifierLevelPromises.push($http.get(getEffectModifierLevelsURL, {cache:true}));
                }
                //each disadvantage will have a level
                for(i=0; i < response.data[0].fields.disadvantages.length; i++)
                {
                    getDisadvantagesURL = "http://localhost:8000/dominion/api/disadvantages/" + response.data[0].fields.disadvantages[i] ;
                    getDisadvantageLevelsURL = "http://localhost:8000/dominion/api/disadvantages/" + response.data[0].fields.disadvantages[i] + "/levels/" + response.data[0].fields.disadvantages_levels[i];
                    disadvantagePromises.push($http.get(getDisadvantagesURL, {cache:true}));
                    disadvantageLevelPromises.push($http.get(getDisadvantageLevelsURL, {cache:true}));
                }
                /*
                Right.  This looks messy as hell, but it's pretty simple in concept.  These promises are going to evaluate 
                serially based on the order in the .then because we return the next promise group after we do all our 
                manipulation. Effects, then their levels, modifiers, then the modifier levels, then disadvantages are 
                seperate.

                To keep it grouped roughly with it's data, when we get the levels, we go through match the level to the 
                effect and then add that data to the effect object.  Same thing with modifiers and their levels, with the 
                extra step of then adding the modifiers to our $scope effects object.  Unfortunately, I couldn't think of 
                a better way to do this than the i*j cycle one I used below.
                */
                $q.all(effectPromises).
                then(function(responseInner) {
                    for(i=0; i < responseInner.length; i++)
                    {
                        $scope.techniqueEffectsJSON[i] = responseInner[i].data;
                    }
                }, function(response) {
                    $scope.techniqueEffectsJSON = 'error';
                });
                $q.all(effectLevelPromises).
                then(function(responseInner) {
                    for(i=0; i < responseInner.length; i++)
                    {
                        techniqueEffectLevelsJSON[i] = responseInner[i].data;
                    }
                    levelHoldArray = [];
                    for(i=0; i < $scope.techniqueEffectsJSON.length; i++) 
                    {
                        for(j=0; j < techniqueEffectLevelsJSON.length; j++)
                        {
                            if($scope.techniqueEffectsJSON[i][0].pk == techniqueEffectLevelsJSON[j][0].fields.effect)
                            {
                                levelHoldArray = techniqueEffectLevelsJSON[j];
                            }
                        }
                        $scope.techniqueEffectsJSON[i][0].level = levelHoldArray;
                    }    
                }, function(response) {
                    techniqueEffectLevelsJSON = 'error';
                });
                $q.all(effectModifierPromises).
                then(function(responseInner) {
                    for(i=0; i < responseInner.length; i++)
                    {
                        techniqueEffectModifiersJSON[i] = responseInner[i].data;
                    }
                }, function(response) {
                    techniqueEffectModifiersJSON = 'error';
                });
                $q.all(effectModifierLevelPromises).
                then(function(responseInner) {
                    for(i=0; i < responseInner.length; i++)
                    {
                        techniqueEffectModifiersLevelsJSON[i] = responseInner[i].data;
                    }
                    for(i=0; i < techniqueEffectModifiersJSON.length; i++) 
                    {
                        for(j=0; j < techniqueEffectModifiersLevelsJSON.length; j++)
                        {
                            if(techniqueEffectModifiersJSON[i][0].pk == techniqueEffectModifiersLevelsJSON[j][0].fields.effect_modifier)
                            {
                                techniqueEffectModifiersJSON[i][0].level = techniqueEffectModifiersLevelsJSON[j][0];
                            }
                        }
                    }
                    
                    for(i=0; i < $scope.techniqueEffectsJSON.length; i++) 
                    {
                        modifierHoldArray = [];
                        for(j=0; j < techniqueEffectModifiersJSON.length; j++)
                        {
                            if($scope.techniqueEffectsJSON[i][0].pk == techniqueEffectModifiersJSON[j][0].fields.effect)
                            {
                                modifierHoldArray.push(techniqueEffectModifiersJSON[j][0]);
                            }
                        }
                        $scope.techniqueEffectsJSON[i][0].modifiers = modifierHoldArray;
                    }   
                }, function(response) {
                    techniqueEffectModifiersJSON = 'error';
                });
                
                $q.all(disadvantagePromises).
                then(function(responseInner) {
                    for(i=0; i < responseInner.length; i++)
                    {
                        $scope.disadvantagesJSON[i] = responseInner[i].data;
                    }
                    return $q.all(disadvantageLevelPromises)
                }, function(response) {
                    $scope.treeTechniquesJSON = 'error';
                });
                $q.all(disadvantageLevelPromises).
                then(function(responseInner) {
                    for(i=0; i < responseInner.length; i++)
                    {
                        disadvantageLevelsJSON[i] = responseInner[i].data;
                    }
                    for(i=0; i < $scope.disadvantagesJSON.length; i++) 
                    {
                        for(j=0; j < disadvantageLevelsJSON.length; j++)
                        {
                            if($scope.disadvantagesJSON[i].pk == disadvantageLevelsJSON[j].disadvantage)
                            {
                                $scope.disadvantagesJSON[i][0].level = disadvantageLevelsJSON[j];
                            }
                        }
                    }
                }, function(response) {
                    $scope.disadvantagesJSON = 'error';
                });

                //after we fetch all our data, it's time for the manipulations so that we can do good display of the data.

                $scope.cost = "";
                $scope.maint = "";

                abilityNames = ["Strength","Dexterity", "Agility", "Constitution", "Power", "Will"];
                abilityCosts = [];
                abilityCosts[0] = $scope.techniqueJSON[0].fields.str_cost;
                abilityCosts[1] = $scope.techniqueJSON[0].fields.dex_cost;
                abilityCosts[2] = $scope.techniqueJSON[0].fields.agi_cost;
                abilityCosts[3] = $scope.techniqueJSON[0].fields.con_cost;
                abilityCosts[4] = $scope.techniqueJSON[0].fields.pow_cost;
                abilityCosts[5] = $scope.techniqueJSON[0].fields.will_cost;
                abilityMaints = [];
                abilityMaints[0] = $scope.techniqueJSON[0].fields.str_maint;
                abilityMaints[1] = $scope.techniqueJSON[0].fields.dex_maint;
                abilityMaints[2] = $scope.techniqueJSON[0].fields.agi_maint;
                abilityMaints[3] = $scope.techniqueJSON[0].fields.con_maint;
                abilityMaints[4] = $scope.techniqueJSON[0].fields.pow_maint;
                abilityMaints[5] = $scope.techniqueJSON[0].fields.will_maint;


                for (i = 0; i < 6; i++) { 
                    if (abilityCosts[i] > 0)
                    {
                        $scope.cost = $scope.cost + abilityNames[i] + " " + abilityCosts[i] + "; "; 
                    }
                    if (abilityCosts[i] > 0)
                    {
                        $scope.maint = $scope.maint + abilityNames[i] + " " + abilityMaints[i] + "; "; 
                    }
                }
            }
        }, function(response) {
            $scope.treeJSON = 'error';
        });
    }
]);

dominionApp.controller('disadvantagesController', 
    function($scope, $http, $stateParams)
    {
        getURL = "http://localhost:8000/dominion/api/disadvantages/";
        $scope.disadvantagesJSON = {};
        $http.get(getURL, {cache:true}).
        then(function(response) {
            $scope.disadvantagesJSON = response.data;
        }, function(response) {
            $scope.disadvantagesJSON = 'error';
        });
    }
);

dominionApp.controller('disadvantageController', ['$scope', '$http', '$stateParams', '$q',
    function($scope, $http, $stateParams, $q)
    {
        getURL = "http://localhost:8000/dominion/api/disadvantages/"  + $stateParams.disadvantageId;
        $scope.disadvantageJSON = {};
        $http.get(getURL, {cache:true}).
        then(function(response) {
            $scope.disadvantageJSON = response.data;

            getLevelsURL = "http://localhost:8000/dominion/api/disadvantages/" + $stateParams.disadvantageId + "/levels/";
            $scope.disadvantageLevelsJSON = {};
            $http.get(getLevelsURL, {cache:true}).
            then(function(response) {
                $scope.disadvantageLevelsJSON = response.data;
            }, function(response) {
                $scope.disadvantageLevelsJSON = 'error';
            });
        }, function(response) {
            $scope.disadvantageJSON = 'error';
        });
    }
]);



