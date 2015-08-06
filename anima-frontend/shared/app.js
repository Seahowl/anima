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

        .state('api', {
            // this state is blank so that it passes routing off to the django router      
        });
        
});