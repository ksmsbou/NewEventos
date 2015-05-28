eventosModule.config(function ($routeProvider) {
    $routeProvider.when('/VPrincipalUsuario', {
                controller: 'VPrincipalUsuarioController',
                templateUrl: 'app/cu2/VPrincipalUsuario.html'
            }).when('/VEventosInscritos', {
                controller: 'VEventosInscritosController',
                templateUrl: 'app/cu2/VEventosInscritos.html'
            }).when('/VEventoInscrito', {
                controller: 'VEventoInscritoController',
                templateUrl: 'app/cu2/VEventoInscrito.html'
            }).when('/VEventosNoInscritos', {
                controller: 'VEventosNoInscritosController',
                templateUrl: 'app/cu2/VEventosNoInscritos.html'
            }).when('/VEventoNoInscrito', {
                controller: 'VEventoNoInscritoController',
                templateUrl: 'app/cu2/VEventoNoInscrito.html'
            });
});

eventosModule.controller('VPrincipalUsuarioController', 
   ['$scope', '$location', '$route', 'flash', 'cu2Service', 'cu3Service',
    function ($scope, $location, $route, flash, cu2Service, cu3Service) {
      $scope.msg = '';
      cu2Service.VPrincipalUsuario().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.AVerEventosInscritos0 = function() {
          
        cu2Service.AVerEventosInscritos().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};
      $scope.AVerEventosNoInscritos1 = function() {
          
        cu2Service.AVerEventosNoInscritos().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};
      $scope.ASalir2 = function() {
          
        cu3Service.ASalir().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};

    }]);
eventosModule.controller('VEventosInscritosController', 
   ['$scope', '$location', '$route', 'flash', 'cu2Service', 'cu3Service',
    function ($scope, $location, $route, flash, cu2Service, cu3Service) {
      $scope.msg = '';
      cu2Service.VEventosInscritos().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.AVerEventoInscrito0 = function() {
          
        cu2Service.AVerEventoInscrito().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};
      $scope.ASalir1 = function() {
          
        cu3Service.ASalir().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};

    }]);
eventosModule.controller('VEventoInscritoController', 
   ['$scope', '$location', '$route', 'flash', 'cu2Service', 'cu3Service',
    function ($scope, $location, $route, flash, cu2Service, cu3Service) {
      $scope.msg = '';
      cu2Service.VEventoInscrito().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.ACredencial0 = function() {
          
        cu2Service.ACredencial().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};
      $scope.ACertificado1 = function() {
          
        cu2Service.ACertificado().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};
      $scope.ASalir2 = function() {
          
        cu3Service.ASalir().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};

    }]);
eventosModule.controller('VEventosNoInscritosController', 
   ['$scope', '$location', '$route', 'flash', 'cu2Service', 'cu3Service',
    function ($scope, $location, $route, flash, cu2Service, cu3Service) {
      $scope.msg = '';
      cu2Service.VEventosNoInscritos().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.AVerEventoNoInscrito0 = function() {
          
        cu2Service.AVerEventoNoInscrito().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};
      $scope.ASalir1 = function() {
          
        cu3Service.ASalir().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};

    }]);
eventosModule.controller('VEventoNoInscritoController', 
   ['$scope', '$location', '$route', 'flash', 'cu2Service', 'cu3Service',
    function ($scope, $location, $route, flash, cu2Service, cu3Service) {
      $scope.msg = '';
      cu2Service.VEventoNoInscrito().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.AReservarEvento0 = function() {
          
        cu2Service.AReservarEvento().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};
      $scope.ASalir1 = function() {
          
        cu3Service.ASalir().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};

    }]);
