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
      $scope.VEventosInscritos0 = function() {
        $location.path('/VEventosInscritos');
      };
      $scope.VEventosNoInscritos1 = function() {
        $location.path('/VEventosNoInscritos');
      };
      $scope.ASalir3 = function() {
          
        cu3Service.ASalir().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};

    }]);
eventosModule.controller('VEventosInscritosController', 
   ['$scope', '$location', '$route', 'flash', 'ngTableParams', 'cu2Service', 'cu3Service',
    function ($scope, $location, $route, flash, ngTableParams, cu2Service, cu3Service) {
      $scope.msg = '';
      cu2Service.VEventosInscritos().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
              var AVerEventoInscrito0Data = $scope.res.data0;
              if(typeof AVerEventoInscrito0Data === 'undefined') AVerEventoInscrito0Data=[];
              $scope.tableParams0 = new ngTableParams({
                  page: 1,            // show first page
                  count: 10           // count per page
              }, {
                  total: AVerEventoInscrito0Data.length, // length of data
                  getData: function($defer, params) {
                      $defer.resolve(AVerEventoInscrito0Data.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                  }
              });            


      });
      $scope.VPrincipalUsuario1 = function() {
        $location.path('/VPrincipalUsuario');
      };
      $scope.ASalir2 = function() {
          
        cu3Service.ASalir().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};

      $scope.AVerEventoInscrito0 = function(id) {
          var tableFields = [["idEvento","id"], ["nombre","Nombre"], ["fecha","Fecha"]];
          var arg = {};
          arg[tableFields[0][1]] = ((typeof id === 'object')?JSON.stringify(id):id);
          cu2Service.AVerEventoInscrito(arg).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
      };

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
      $scope.ACredencial1 = function() {
          
        cu2Service.ACredencial().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};
      $scope.ACertificado2 = function() {
          
        cu2Service.ACertificado().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};
      $scope.VEventosInscritos3 = function() {
        $location.path('/VEventosInscritos');
      };
      $scope.ASalir4 = function() {
          
        cu3Service.ASalir().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};

    }]);
eventosModule.controller('VEventosNoInscritosController', 
   ['$scope', '$location', '$route', 'flash', 'ngTableParams', 'cu2Service', 'cu3Service',
    function ($scope, $location, $route, flash, ngTableParams, cu2Service, cu3Service) {
      $scope.msg = '';
      cu2Service.VEventosNoInscritos().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
              var AVerEventoNoInscrito0Data = $scope.res.data0;
              if(typeof AVerEventoNoInscrito0Data === 'undefined') AVerEventoNoInscrito0Data=[];
              $scope.tableParams0 = new ngTableParams({
                  page: 1,            // show first page
                  count: 10           // count per page
              }, {
                  total: AVerEventoNoInscrito0Data.length, // length of data
                  getData: function($defer, params) {
                      $defer.resolve(AVerEventoNoInscrito0Data.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                  }
              });            


      });
      $scope.VPrincipalUsuario1 = function() {
        $location.path('/VPrincipalUsuario');
      };
      $scope.ASalir2 = function() {
          
        cu3Service.ASalir().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};

      $scope.AVerEventoNoInscrito0 = function(id) {
          var tableFields = [["idEvento","id"], ["nombre","Nombre"], ["fecha","Fecha"]];
          var arg = {};
          arg[tableFields[0][1]] = ((typeof id === 'object')?JSON.stringify(id):id);
          cu2Service.AVerEventoNoInscrito(arg).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
      };

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
      $scope.AReservarEvento1 = function() {
          
        cu2Service.AReservarEvento().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};
      $scope.VEventosNoInscritos2 = function() {
        $location.path('/VEventosNoInscritos');
      };
      $scope.ASalir3 = function() {
          
        cu3Service.ASalir().then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};

    }]);
